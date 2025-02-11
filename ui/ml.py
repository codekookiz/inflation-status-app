import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
from prophet import Prophet
from datetime import datetime

# 스타일 적용
st.markdown(
    """
    <style>
        .big-font { font-size:30px !important; font-weight: bold; text-align: center; }
        .sub-header { font-size:22px !important; font-weight: bold; }
        .info-box { background-color: #f0f2f6; padding: 15px; border-radius: 10px; }
        .button { font-size:18px; font-weight: bold; color: white; background-color: #ff4b4b; padding: 10px 20px; border-radius: 5px; }
    </style>
    """,
    unsafe_allow_html=True,
)

def run_ml():

    st.text('')
    st.text('')

    # 제목 정리
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            🍚 식료품 물가 예측하기
        </h2>
        <p style="font-size: 24px; text-align: center; color: ##4C82C2;">
            <b>머신 러닝 (ML)<b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 큰 제목
    st.markdown('<p style="font-size: 24px; font-weight: bold; color: #333; font-family: Arial, sans-serif;">🎞️ ML 기반 특정 미래 시점의 물가 예측</p>', unsafe_allow_html=True)

    # 정보 박스 스타일
    st.markdown('<p style="font-size: 16px; color: #555; font-family: Arial, sans-serif; background-color: #f0f0f0; padding: 15px; border-radius: 8px; box-shadow: 0px 2px 10px rgba(0,0,0,0.1);">미래 시점과 품목을 입력하시면, 예상 가격을 알려드립니다.</p>', unsafe_allow_html=True)
    st.text('')

    if st.button('❓ 물가 예측 예시') :
        col1, col2 = st.columns(2)
        with col1 :
            st.image('image/result_a.png')
        with col2 :
            st.image('image/result_b.png')

    # 하위 제목
    st.markdown('<p style="font-size: 22px; font-weight: bold; color: #333; font-family: Arial, sans-serif; border-bottom: 3px solid #4CAF50; padding-bottom: 10px;">📌 정보 입력</p>', unsafe_allow_html=True)
    st.text('')

    # 카테고리별 세부 옵션을 딕셔너리로 정의
    step1_options = {
        "빵 및 곡물": ["선택 없음", "쌀", "현미", "찹쌀", "보리쌀", "콩", "땅콩", "혼식곡", "밀가루", "국수", "라면", "당면", "두부", "시리얼", "부침가루",
                   "케이크", "빵", "떡", "파스타면"],
        "육류": ["선택 없음", "국산쇠고기", "수입쇠고기", "돼지고기", "닭고기", "소시지", "햄및베이컨", "기타육류가공품"],
        "어류 및 수산": ["선택 없음", "갈치", "명태", "조기", "고등어", "오징어", "게", "굴", "조개", "전복", "새우", "마른멸치", "마른오징어", "낙지",
                    "오징어채", "북어채", "어묵", "맛살", "수산물통조림", "젓갈"],
        "우유 치즈 및 계란": ["선택 없음", "우유", "분유", "치즈", "발효유", "달걀"],
        "식용유지": ["선택 없음", "참기름", "식용유"],
        "과일": ["선택 없음", "사과", "배", "복숭아", "포도", "밤", "감", "귤", "오렌지", "참외", "수박", "딸기", "바나나", "키위", "블루베리", "망고",
               "체리", "아보카도", "파인애플", "아몬드", "과일가공품"],
        "채소 및 해조": ["선택 없음", "배추", "상추", "시금치", "양배추", "미나리", "깻잎", "부추", "무", "열무", "당근", "감자", "고구마", "도라지",
                     "콩나물", "버섯", "오이", "풋고추", "호박", "가지", "토마토", "파", "양파", "마늘", "브로콜리", "고사리", "파프리카", "단무지",
                     "김", "맛김", "미역"],
        "과자 빙과류 및 당류": ["선택 없음", "초콜릿", "사탕", "껌", "아이스크림", "비스킷", "스낵과자", "파이", "설탕", "잼", "꿀", "물엿"],
        "기타 식료품": ["선택 없음", "고춧가루", "참깨", "생강", "소금", "간장", "된장", "양념소스", "고추장", "카레", "식초", "드레싱", "혼합조미료", "스프",
                   "이유식", "김치", "밑반찬", "냉동식품", "즉석식품", "편의점도시락", "삼각김밥"],
        "커피 차 및 코코아": ["선택 없음", "커피", "차"],
        "생수, 청량음료 및 주스": ["선택 없음", "주스", "두유", "생수", "기능성음료", "탄산음료", "기타음료"],
        "주류": ["선택 없음", "소주", "과실주", "맥주", "막걸리", "양주", "약주"],
        "외식": ["선택 없음", "김치찌개백반", "된장찌개백반", "비빔밥", "설렁탕", "갈비탕", "삼계탕", "해물찜", "해장국", "불고기", "쇠고기(외식)",
               "돼지갈비(외식)", "삼겹살(외식)", "오리고기(외식)", "냉면", "칼국수", "죽(외식)", "생선초밥", "생선회(외식)", "자장면", "짬뽕", "탕수육",
               "볶음밥", "돈가스", "스테이크", "스파게티", "라면(외식)", "김밥", "떡볶이", "치킨", "햄버거", "피자", "쌀국수", "커피(외식)",
               "기타음료(외식)", "소주(외식)", "맥주(외식)", "막걸리(외식)", "구내식당식사비", "도시락"]
    }

    # 세션 상태 초기화
    if "step1_selected" not in st.session_state:
        st.session_state["step1_selected"] = False
    if "step2_options" not in st.session_state:
        st.session_state["step2_options"] = []    

    col1, col2 = st.columns(2)
    with col1 : 
        category = st.selectbox("🍽️ 식료품 유형을 선택하세요.", [""] + list(step1_options.keys()), key="step1")
        st.session_state["step2_options"] = step1_options.get(category, [])
        st.session_state["step1_selected"] = bool(st.session_state["step2_options"])
    with col2 :
        item = st.selectbox("🥄 세부 유형을 선택하세요.", st.session_state["step2_options"], key="step2")

    curr_price = st.number_input('💵 현재 상품/서비스 가격 (원)', value=10000)

    col3, col4 = st.columns(2)
    with col3 : 
        yearlist = list(range(2025, 2028))
        year = st.selectbox("연도를 선택하세요:", yearlist, index=yearlist.index(2025))
    with col4 :
        monthlist = list(range(1, 13))
        month = st.selectbox("월을 선택하세요:", monthlist, index=monthlist.index(2))
    
    if st.button('📊 수익 예측', disabled=not item):
        df = pd.read_csv('data/price_level_index.csv')
        if item is '선택 없음' :
            df_1 = df[['계정항목', category]]
        else :
            df_1 = df[['계정항목', item]]

        df_1.columns = ['ds', 'y']

        model = Prophet()
        model.fit(df_1)
        future = model.make_future_dataframe(periods=36, freq='M')
        forecast = model.predict(future)
        
        if month == 1 or month == 3 or month ==5 or month == 7 or month == 8 or month == 10 or month == 12 :
            new_date = f'{year}-{month}-31'
        elif month == 2 :
            new_date = f'{year}-{month}-28'
        else :
            new_date = f'{year}-{month}-30'

        pred_date = datetime.strptime(new_date, '%Y-%m-%d')

        if pred_date > datetime.today() :
            inflation_index = (forecast.loc[forecast['ds'] == new_date, 'trend'].values[0]  / df_1.iloc[df_1.index.max(), 1])
            pred_price = int(curr_price * inflation_index)

            if pred_price >= 0:
                new_pred_price = format(pred_price, ',')
                if item is '선택 없음' :
                    st.subheader(f'📈 {year}년 {month}월 {category}의 예상 평균 가격: **{new_pred_price} 원**')
                else :
                    st.subheader(f'📈 {year}년 {month}월 {item}의 예상 가격: **{new_pred_price} 원**')

                time.sleep(1)
        else:
            st.error('❌ 이미 지난 날짜이거나, 예측이 불가능한 데이터입니다.')
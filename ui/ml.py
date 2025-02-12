import streamlit as st
import joblib
import numpy as np
import pandas as pd
import time
from prophet import Prophet
from datetime import datetime
import matplotlib.pyplot as plt

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
        "빵 및 곡물": ["-", "쌀", "현미", "찹쌀", "보리쌀", "콩", "땅콩", "혼식곡", "밀가루", "국수", "라면", "당면", "두부", "시리얼", "부침가루",
                   "케이크", "빵", "떡", "파스타면", "기타"],
        "육류": ["-", "국산쇠고기", "수입쇠고기", "돼지고기", "닭고기", "소시지", "햄및베이컨", "기타육류가공품", "기타"],
        "어류 및 수산": ["-", "갈치", "명태", "조기", "고등어", "오징어", "게", "굴", "조개", "전복", "새우", "마른멸치", "마른오징어", "낙지",
                    "오징어채", "북어채", "어묵", "맛살", "수산물통조림", "젓갈", "기타"],
        "우유, 치즈 및 계란": ["-", "우유", "분유", "치즈", "발효유", "달걀", "기타"],
        "식용유지": ["-", "참기름", "식용유", "기타"],
        "과일": ["-", "사과", "배", "복숭아", "포도", "밤", "감", "귤", "오렌지", "참외", "수박", "딸기", "바나나", "키위", "블루베리", "망고",
               "체리", "아보카도", "파인애플", "아몬드", "과일가공품", "기타"],
        "채소 및 해조": ["-", "배추", "상추", "시금치", "양배추", "미나리", "깻잎", "부추", "무", "열무", "당근", "감자", "고구마", "도라지",
                     "콩나물", "버섯", "오이", "풋고추", "호박", "가지", "토마토", "파", "양파", "마늘", "브로콜리", "고사리", "파프리카", "단무지",
                     "김", "맛김", "미역", "기타"],
        "과자, 빙과류 및 당류": ["-", "초콜릿", "사탕", "껌", "아이스크림", "비스킷", "스낵과자", "파이", "설탕", "잼", "꿀", "물엿", "기타"],
        "기타 식료품": ["-", "고춧가루", "참깨", "생강", "소금", "간장", "된장", "양념소스", "고추장", "카레", "식초", "드레싱", "혼합조미료", "스프",
                   "이유식", "김치", "밑반찬", "냉동식품", "즉석식품", "편의점도시락", "삼각김밥", "기타"],
        "커피, 차 및 코코아": ["-", "커피", "차", "기타"],
        "생수, 청량음료, 과일주스 및 채소주스": ["-", "주스", "두유", "생수", "기능성음료", "탄산음료", "기타음료"],
        "주류": ["-", "소주", "과실주", "맥주", "막걸리", "양주", "약주", "기타"],
        "외식": ["-", "김치찌개백반", "된장찌개백반", "비빔밥", "설렁탕", "갈비탕", "삼계탕", "해물찜", "해장국", "불고기", "쇠고기(외식)",
               "돼지갈비(외식)", "삼겹살(외식)", "오리고기(외식)", "냉면", "칼국수", "죽(외식)", "생선초밥", "생선회(외식)", "자장면", "짬뽕", "탕수육",
               "볶음밥", "돈가스", "스테이크", "스파게티", "라면(외식)", "김밥", "떡볶이", "치킨", "햄버거", "피자", "쌀국수", "커피(외식)",
               "기타음료(외식)", "소주(외식)", "맥주(외식)", "막걸리(외식)", "구내식당식사비", "도시락", "기타"]
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

    curr_price = st.number_input('💵 2025년 1월 기준 식품/서비스 가격 (원)', value=10000)

    col3, col4 = st.columns(2)
    with col3 : 
        yearlist = list(range(2025, 2031))
        year = st.selectbox("연도를 선택하세요:", yearlist, index=yearlist.index(2025))
    with col4 :
        monthlist = list(range(1, 13))
        month = st.selectbox("월을 선택하세요:", monthlist, index=monthlist.index(2))
    
    if st.button('📊 가격 예측', disabled=not item):
        df = pd.read_csv('data/price_level_index.csv')
        if item == "-" or item == '기타':
            new_item = category
            if new_item == '외식' :
                new_item = '음식 서비스'
        else :
            new_item = item
        df_1 = df[['계정항목', new_item]]

        df_1.columns = ['ds', 'y']

        model = Prophet()
        model.fit(df_1)
        future = model.make_future_dataframe(periods=72, freq='M')
        forecast = model.predict(future)
        
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12 :
            new_date = f'{year}-{month}-31'
        elif month == 2 :
            new_date = f'{year}-{month}-28'
        else :
            new_date = f'{year}-{month}-30'

        pred_date = datetime.strptime(new_date, '%Y-%m-%d')

        

        ## 차트 만들어서, 물가 동향 보여주자. (범위를 선택 날짜까지로 할 수 있으면 좋을 듯?)

        if pred_date > datetime.today() :
            std_price = df_1.iloc[df_1.index.max(), 1]
            then_price = forecast.loc[forecast['ds'] == new_date, 'yhat'].values[0]
            inflation_index = (then_price / std_price)
            pred_price = int((curr_price * inflation_index).round(-1))

            if pred_price >= 0: 
                st.markdown('<h2>📌 예측 결과</h2>', unsafe_allow_html=True)
                
                if new_item == '기타' :
                    new_item = f'기타 {category}'
                if new_item == '음식 서비스' :
                    new_item = '외식'

                fig, ax = plt.subplots(figsize=(12, 5))
                ax.plot(forecast['ds'], forecast['yhat'] / std_price * curr_price, label='가격 동향', color='blue')
                ax.axvline(datetime.today(), color='red', linestyle='dashed', label='오늘 날짜')
                ax.scatter(pred_date, then_price / std_price * curr_price, color='black', s=30, label='예측 가격', zorder=3)
                ax.set_title(f'{new_item} 가격 예측', fontsize=16)
                ax.set_xlabel('날짜')
                ax.set_ylabel('예상 가격')
                ax.legend()
                ax.grid(True)
                st.pyplot(fig)

                new_pred_price = format(pred_price, ',')
                st.markdown(
                    f"""
                    <h4 style="text-align: center;">📈 {year}년 {month}월 {new_item}의 예상 평균 가격은 {new_pred_price} 원입니다.</h4>
                    """,
                    unsafe_allow_html=True
                )

                st.text('')
                
                fig1 = model.plot_components(forecast)
                
                fig2, ax = plt.subplots(figsize=(10, 4))  # 새로운 Figure와 Axes 생성
                original_ax = fig1.axes[0]  # 첫 번째 차트
                for line in original_ax.get_lines():
                    ax.plot(line.get_xdata(), line.get_ydata(), label=line.get_label(), color=line.get_color())
                ax.set_title("가격 트렌드 변화 (Trend)", fontsize=14)
                ax.set_ylabel("예측 값", fontsize=12)
                ax.set_xlabel("날짜", fontsize=12)
                ax.legend()
                st.pyplot(fig2)
                
                if forecast.iloc[-1]['yhat'] > std_price :
                    st.write(f"""
                    - 2030년까지 **{new_item}의 가격이 현재보다 약 {int((forecast.iloc[-1]['yhat'] / std_price - 1) * 100)}% 상승**할 것으로 예상됩니다.
                    """)
                elif forecast.iloc[-1]['yhat'] == std_price :
                    st.write(f"""
                    - 2030년까지 {new_item} **가격이 현 수준을 유지할 것으로 예상**됩니다.
                    """)
                else :
                    st.write(f"""
                    - 2030년까지 **{new_item}의 가격이 현재보다 약 {int((forecast.iloc[-1]['yhat'] / std_price - 1) * 100)}% 하락**할 것으로 예상됩니다.
                    """)
                st.text('')


                fig3, ax = plt.subplots(figsize=(10, 4))  # 새로운 Figure와 Axes 생성
                original_ax = fig1.axes[1]  # 두 번째 차트
                for line in original_ax.get_lines():
                    ax.plot(line.get_xdata(), line.get_ydata(), label=line.get_label(), color=line.get_color())
                ax.set_title("주차별 경향성 (Weekly Seasonality)", fontsize=14)
                ax.set_ylabel("예측 값", fontsize=12)
                ax.set_xlabel("주차", fontsize=12)
                ax.legend()
                st.pyplot(fig3)
                st.write("""
                - 각 식료품 품목에 따라 **주차별 수익의 변동성**이 다르게 나타납니다.
                - 이 데이터는 연간 주기성을 가지고 있으며, **특정 주차 혹은 달에 수익이 높아지거나 낮아지는 경향**을 보입니다.
                - 이러한 경향성을 통해, **특정 시기에 수익이 높아지거나 낮아질 것을 예상**할 수 있습니다.
                """)

                st.markdown("---")



        else:
            st.error('❌ 이미 지난 날짜이거나, 예측이 불가능한 데이터입니다.')
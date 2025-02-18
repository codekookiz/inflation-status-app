import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import platform
import os
from matplotlib import rc
from datetime import datetime

@st.cache_data
def fontRegistered():
    font_dirs = [os.getcwd()]
    font_files = fm.findSystemFonts(fontpaths=font_dirs)
    for font_file in font_files:
        fm.fontManager.addfont(font_file)
    fm._load_fontmanager(try_read_cache=False)

plt.rcParams['axes.unicode_minus'] = False
system_os = platform.system()
if system_os == "Darwin":  # macOS
    font_path = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
elif system_os == "Windows":  # Windows
    font_path = "C:/Windows/Fonts/malgun.ttf"
else:  # Linux
    rc('font', family='NanumGothic')

def run_eda():
    fontRegistered()
    plt.rc('font', family='NanumGothic')

    st.text('')
    st.text('')

    # 제목
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            📊 과거 물가는 어땠나요?
        </h2>
        <p style="font-size: 24px; text-align: center; color: ##4C82C2;">
            <b>탐색적 데이터 분석 (EDA)<b>
        </p>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 데이터 불러오기
    st.info("📌 **기본 데이터** (price_level_index.csv) : 불필요 컬럼 삭제 및 식료품 데이터만 추출")
    df = pd.read_csv("data/price_level_index.csv", index_col=0)
    
    # 데이터프레임 출력
    st.dataframe(df, use_container_width=True)
    st.info("""
        None으로 출력되는 데이터의 경우 해당 시점에 데이터가 존재하지 않는 것입니다.
    """)

    st.markdown("---")

    # 기본 통계 데이터 버튼
    if st.button("📈 기본 통계 데이터 보기"):
        st.dataframe(df.describe())

        st.info("""
                * count : 전체 데이터 수
                * mean : 평균값
                * std : 표준편차
                * min : 최솟값
                * 25% : 최솟값으로부터 1/4 지점의 값
                * 50% : 중앙값
                * 75% : 최솟값으로부터 3/4 지점의 값
                * max : 최댓값
                """)

    st.markdown("---")

    # 최대/최소 데이터 확인
    st.info("📌 **최대/최소 데이터 확인하기**")

    menu2 = df.columns.tolist()
    selected_column = st.selectbox("📌 비교할 컬럼 선택", menu2)

    # 최댓값 데이터
    st.markdown("✅ **최댓값 데이터** : 물가가 가장 높았던 시기")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), selected_column])

    # 최솟값 데이터
    st.markdown("✅ **최솟값 데이터** : 물가가 가장 낮았던 시기")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), selected_column])

    st.markdown("---")

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

    if "step1_selected" not in st.session_state:
        st.session_state["step1_selected"] = False
    if "step2_options" not in st.session_state:
        st.session_state["step2_options"] = [] 

    st.info('💰 현재의 식품 구매 가격과 돌아가고 싶은 시점을 입력할 경우, 당시 가격을 확인할 수 있습니다. **(2025년 1월 기준)**')
    col1, col2 = st.columns(2)
    with col1 :
        category = st.selectbox("🍽️ 식료품 유형을 선택하세요.", list(step1_options.keys()), key="step1_eda")
        st.session_state["step2_options"] = step1_options.get(category, [])
        st.session_state["step1_selected"] = bool(st.session_state["step2_options"])
        price = st.number_input('💵 2025년 1월 기준, 얼마에 구매하셨나요?', value=10000, step=1000)
    with col2 :
        item = st.selectbox("🥄 세부 유형을 선택하세요.", st.session_state["step2_options"], key="step2_eda")
        yearlist = list(range(2014, 2025))
        year = st.selectbox("확인하고 싶은 연도를 선택하세요:", yearlist, index=yearlist.index(2020))
    st.text('')

    st.info("""
        None으로 출력되는 데이터의 경우\n\n
        해당 컬럼의 좌측에 위치한 더 큰 범주의 컬럼(빵 및 곡물, 과일 등)으로 가격 확인이 가능합니다.
    """)

    if item == "-" or item == '기타':
        new_item = category
        if new_item == '외식' :
            new_item = '음식 서비스'
    else :
        new_item = item

    min_date = f'{year}-01-01'
    max_date = f'{year}-12-01'

    df_new = df.loc[(df.index >= min_date) & (df.index <= max_date), :]

    df_new = (df_new * price / 100).round(-1)

    df_trans = df_new[[new_item]].transpose()
    
    st.dataframe(df_trans)

    st.markdown("---")
    df_eda = pd.read_csv("data/price_level_index.csv", index_col=0)
    df_eda.index = pd.to_datetime(df_eda.index, errors="coerce")
    df_eda = df_eda.apply(pd.to_numeric, errors="coerce")

    st.subheader("📊 기본 식재료 vs 가공식품 및 외식 물가 상승 비교")
    food_items = ["빵 및 곡물", "육류", "어류 및 수산", "우유, 치즈 및 계란", "식용유지", "과일", "채소 및 해조", "기타 식료품"]
    processed_items = ["과자, 빙과류 및 당류", "커피, 차 및 코코아", "생수, 청량음료, 과일주스 및 채소주스", "주류", "음식 서비스"]
    df_eda["기본 식재료 평균"] = df_eda[food_items].mean(axis=1)
    df_eda["가공식품 및 외식 평균"] = df_eda[processed_items].mean(axis=1)
    fig1, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_eda.index, df_eda["기본 식재료 평균"], label="기본 식재료", color="blue", linewidth=2)
    ax.plot(df_eda.index, df_eda["가공식품 및 외식 평균"], label="가공식품", color="red", linewidth=2)
    ax.set_xlabel("연도", fontsize=12)
    ax.set_ylabel("평균 물가 지수", fontsize=12)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(fig1)

    st.write("""
    - 기본 식재료와 가공식품의 물가 지수를 비교한 결과, **기본 식재료의 물가 상승률이 가공식품보다 높게 나타났습니다.**
    - 2020년 이전까지는 대체적으로 가공식품의 물가 상승률이 높게 나타났으나, 2020년 이후부터는 기본 식재료의 물가 상승률이 더 높게 나타났습니다.
        - **2020년 코로나19의 영향으로 인한 물가 변동**이 이러한 결과를 가져온 것으로 분석됩니다.
             - 코로나19로 인해 **농수산물의 물류 및 유통망이 제한**되었고, 이와 더불어 **외식이 제한**되면서 기본 식재료의 공급은 줄고 수요는 급증하여
             이와 같은 경향성이 발생한 것이라고 볼 수 있습니다.
    """)

    st.markdown("---")

    st.subheader("🔥 2024년 물가 상승률 Top 5")
    df_last_year = df_eda[df_eda.index >= df_eda.index.max() - pd.DateOffset(years=1)]
    price_changes = (df_last_year.iloc[-1] - df_last_year.iloc[0]) / df_last_year.iloc[0] * 100
    top_5 = price_changes.nlargest(5)
    fig2, ax = plt.subplots()
    bars = sb.barplot(y=top_5.index, x=top_5.values, ax=ax, palette="Reds_r")
    for bar, value in zip(bars.patches, top_5.values):
        ax.text(bar.get_x() + bar.get_width() - 1,  # X 좌표 (막대 끝 - 살짝 왼쪽)
        bar.get_y() + bar.get_height() / 2,  # Y 좌표 (막대 중앙)
        f"{value:.1f}%",  # 표시할 텍스트
        va='center', ha='right', fontsize=10, color='white', fontweight='bold')  # 정렬 및 스타일
    ax.set_xlabel("상승률 (%)")
    ax.set_ylabel("항목")
    st.pyplot(fig2)
 
    st.write("""
    - 2024년 기준 **물가 상승률이 가장 높은 Top 5**는 다음과 같습니다. : **무, 당근, 배추, 양배추, 보리쌀**
    - 이러한 현상의 원인은 크게 3가지로 볼 수 있습니다.
        - **이상기후로 인한 작황 부진** : 고온 현상과 작황 부진이 주요 채소의 생육에 부정적인 영향을 미쳤습니다.
        - **재배 면적 감소** : 여름철 배추와 무의 재배 면적이 감소하면서 생산량이 감소해 가격 상승을 초래했습니다.
        - **수확 시기 지연 및 저장 물량 부족** : 기상 악화로 인해 일부 채소의 수확 시기가 지연되었고, 이는 시장 공급에 차질을 빚어 가격 상승을 유발했습니다.
    """)

    st.markdown("---")

    st.subheader("📅 월별 평균 물가 변동률 히트맵")
    df_eda = df_eda.rename(columns= {"음식 서비스":"외식"})
    df_eda["연도"] = df_eda.index.year
    df_eda["월"] = df_eda.index.month
    df_eda_categorized = df_eda.loc[:, ["빵 및 곡물", "육류", "어류 및 수산", "우유, 치즈 및 계란", "식용유지", "과일", "채소 및 해조",
                                        "과자, 빙과류 및 당류", "기타 식료품", "커피, 차 및 코코아", "생수, 청량음료, 과일주스 및 채소주스",
                                        "주류", "외식", "연도", "월"]]
    monthly_avg = df_eda_categorized.groupby(["연도", "월"]).mean()
    fig3, ax = plt.subplots(figsize=(10, 6))
    sb.heatmap(monthly_avg.T, cmap="seismic", center=100, linewidths=0.5, ax=ax, robust=True)
    st.pyplot(fig3)

    st.write("""
    - **월별 평균 물가 변동률 히트맵**을 통해 **식품 및 서비스의 계절적 변동**을 확인할 수 있습니다.
        - **빵 및 곡물, 육류, 어류 및 수산** 등은 **겨울철**에 물가가 상승하는 경향을 보이며, **과일, 채소 및 해조**는 **여름철**에 상승하는 경향을 보입니다.
             - 빵 및 곡물, 육류, 어류 및 수산의 경우 **곡류 및 육류의 수입 비용 증가, 수온 하락으로 인한 어획량 감소** 등이 원인으로 작용했습니다.
             - 과일, 채소 및 해조의 경우 **이상 기후로 인한 생산량 감소, 야외 활동 증가로 인한 소비 증가** 등이 원인으로 작용했습니다.
        - **주류, 외식**은 **연말**에 물가가 상승하는 경향을 보이며, **음료류**는 **여름철**에 상승하는 경향을 보입니다.
             - 이는 **모임 자리가 많아지는 연말**에 외식 및 주류 소비가 증가하는 경향과, **여름철 더위**로 인한 음료류 소비 증가를 반영한 것으로 분석됩니다.
    - 식용 유지의 가격이 최근 약 2년 동안 급격히 상승하는 경향을 보였습니다.
        - 이는 **우크라이나 전쟁, 이상기후로 인한 생산량 감소, 바이오 연료 산업 성장, 주요 생산국의 수출 제한** 등이 원인으로 작용했습니다.
    - 과일, 채소 및 해조류의 가격은 지난 10년 동안 큰 폭으로 요동치는 모습을 보였습니다.
        - 이러한 현상은 **이상기후로 인한 작황 불안정, 수입 과일의 환율 및 무역 정책 영향, 노동력 부족 및 인건비 상승, 유통 구조 변화, 해조류 생산량 변동** 등이 원인으로 작용했습니다.
    """)

    st.markdown("---")
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
    st.markdown("✅ **최댓값 데이터**")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].max(), selected_column])

    # 최솟값 데이터
    st.markdown("✅ **최솟값 데이터**")
    st.dataframe(df.loc[df[selected_column] == df[selected_column].min(), selected_column])

    st.markdown("---")

    # 연도별 평균 수익 시각화
    st.info('💰 현재의 식품/서비스 가격과 과거 시점을 입력하실 경우, 당시의 가격을 확인하실 수 있습니다. **(2025년 1월 기준)**')
    price = st.number_input('💵 2025년 1월 가격 (원)', value=10000, step=1000)
    col1, col2 = st.columns(2)
    with col1 : 
        yearlist = list(range(2014, 2025))
        year = st.selectbox("연도를 선택하세요:", yearlist, index=yearlist.index(2020))
    with col2 :
        monthlist = list(range(1, 13))
        month = st.selectbox("월을 선택하세요:", monthlist, index=monthlist.index(10))
    st.text('')

    st.info("""
        None으로 출력되는 데이터의 경우 해당 시점에 데이터가 없는 것으로,\n\n 
        해당 컬럼의 좌측에 위치한 더 큰 범주의 컬럼(빵 및 곡물, 과일 등)으로 가격 확인이 가능합니다.
    """)

    if month < 10 :
        new_date = f'{year}-0{month}-01'
    else :
        new_date = f'{year}-{month}-01'
    df_new = df.loc[df.index == new_date, :]

    df_new = (df_new * price / 100).round(-1)
    
    st.dataframe(df_new)

    st.markdown("---")

    df_eda = pd.read_csv("data/price_level_index.csv", index_col=0)
    df_eda.index = pd.to_datetime(df_eda.index, errors="coerce")
    df_eda = df_eda.apply(pd.to_numeric, errors="coerce")

    st.subheader("📊 기본 식재료 vs 가공식품 물가 상승 비교")
    food_items = ["빵 및 곡물", "육류", "어류 및 수산", "우유, 치즈 및 계란", "식용유지", "과일", "채소 및 해조", "기타 식료품"]
    processed_items = ["과자, 빙과류 및 당류", "커피, 차 및 코코아", "생수, 청량음료, 과일주스 및 채소주스", "주류", "음식 서비스"]
    df_eda["기본 식재료 평균"] = df_eda[food_items].mean(axis=1)
    df_eda["가공식품 평균"] = df_eda[processed_items].mean(axis=1)
    fig1, ax = plt.subplots(figsize=(10, 5))
    ax.plot(df_eda.index, df_eda["기본 식재료 평균"], label="기본 식재료", color="blue", linewidth=2)
    ax.plot(df_eda.index, df_eda["가공식품 평균"], label="가공식품", color="red", linewidth=2)
    ax.set_xlabel("연도", fontsize=12)
    ax.set_ylabel("평균 물가 지수", fontsize=12)
    ax.legend()
    ax.grid(True, linestyle="--", alpha=0.6)
    st.pyplot(fig1)

    st.write("""
    - 전반적으로 시간이 지남에 따라 **평균 수익이 증가하는 양상**을 보입니다.
    - 다만, 직전 기간 대비 큰 폭으로 수익이 감소하는 지점이 존재합니다.
        - 𝟙. 1994~1995년 : **VHS 및 DVD의 등장 및 대중화**로 인해 홈 비디오의 수요가 증가하면서, 영화관에서 상영되는 영화들의 수익이 급격하게 감소하였습니다.
        - 𝟚. 2020년 : **코로나-19**의 여파로 인해 영화 제작 및 수요가 크게 위축되면서 이전 기간 대비 급격한 수익 감소를 보였습니다.
    """)

    st.markdown("---")

    st.subheader("🔥 2024년 물가 상승률 Top 5")
    df_last_year = df_eda[df_eda.index >= df_eda.index.max() - pd.DateOffset(years=1)]
    price_changes = (df_last_year.iloc[-1] - df_last_year.iloc[0]) / df_last_year.iloc[0] * 100
    top_5 = price_changes.nlargest(5)
    fig2, ax = plt.subplots()
    sb.barplot(y=top_5.index, x=top_5.values, ax=ax, palette="Reds_r")
    ax.set_xlabel("상승률 (%)")
    ax.set_ylabel("항목")
    st.pyplot(fig2)

    st.write("""
    - 뮤지컬 영화 및 액션, 어드벤처, 스릴러/서스펜스 장르의 영화 수익이 높게 나타납니다.
        - 뮤지컬 장르의 경우, 작품성으로 인해 높은 수익을 올렸을 가능성도 존재하지만, **영화의 수가 다른 장르에 비해 적기 때문**에 이러한 양상을 보였을 가능성도 있습니다.
        - 액션, 어드벤처, 스릴러/서스펜스 장르의 경우, **가장 메이저한 장르**로 평가받고 이에 따라 관객 수요가 높기 때문에 자연스레 평균 수익 상위권에 올라있는 것으로 분석됩니다.
    - 코미디와 서부극 장르의 영화 수익이 낮은 것으로 파악됩니다.
        - 두 장르 모두, **특정 취향의 관객층**을 타겟팅하는 경향이 있기 때문에 이와 같이 비교적 낮은 순위를 기록하고 있는 것이라고 이해할 수 있습니다.
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
    sb.heatmap(monthly_avg.T, cmap="coolwarm", linewidths=0.5, ax=ax)
    st.pyplot(fig3)

    st.write("""
    - 15세 이상 관람가와 전체 관람가가 가장 높은 수익을 올린 것으로 나타납니다.
        - 대부분의 상업 영화가 15세 이상 관람가 혹은 전체 관람가로 제작된다는 것이 이러한 경향성의 원인으로 보입니다.
    - 12세 관람가 영화의 경우, 상술한 두 등급 영화에 비해 그 수가 비교적 적기 때문에 상대적으로 적은 수익을 올리고 있는 것으로 파악됩니다.
    - 청소년 관람 불가 영화의 경우, **관객층의 범위가 다른 등급의 영화보다 현저히 작기 때문**에 높은 수익을 올리지 못하는 것으로 분석됩니다.
    """)

    st.markdown("---")
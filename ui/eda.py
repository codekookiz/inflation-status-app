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
    price = st.number_input('💵 2025년 1월 가격 (원)', value=10000)
    col1, col2 = st.columns(2)
    with col1 : 
        yearlist = list(range(2014, 2025))
        year = st.selectbox("연도를 선택하세요:", yearlist, index=yearlist.index(2020))
    with col2 :
        monthlist = list(range(1, 13))
        month = st.selectbox("월을 선택하세요:", monthlist, index=monthlist.index(10))
    st.text('')

    if month < 10 :
        new_date = f'{year}-0{month}-01'
    else :
        new_date = f'{year}-{month}-01'
    df_new = df.loc[df.index == new_date, :]
    
    st.dataframe(df_new)


    st.text('이하 미완성')

    st.info("📅 **연도별 평균 전 세계 수익 분석**")
    #df_yearly = df.groupby("개봉 연도")["전세계 박스오피스 수익 ($)"].mean()
    #fig1 = plt.figure()
    #df_yearly.plot(kind="bar", figsize=(10, 5), color="skyblue")
    #plt.ylabel("평균 수익 ($)")
    #plt.xlabel("연도")
    #plt.title("연도별 평균 수익")
    #st.pyplot(fig1)

    st.write("""
    - 전반적으로 시간이 지남에 따라 **평균 수익이 증가하는 양상**을 보입니다.
    - 다만, 직전 기간 대비 큰 폭으로 수익이 감소하는 지점이 존재합니다.
        - 𝟙. 1994~1995년 : **VHS 및 DVD의 등장 및 대중화**로 인해 홈 비디오의 수요가 증가하면서, 영화관에서 상영되는 영화들의 수익이 급격하게 감소하였습니다.
        - 𝟚. 2020년 : **코로나-19**의 여파로 인해 영화 제작 및 수요가 크게 위축되면서 이전 기간 대비 급격한 수익 감소를 보였습니다.
    """)

    st.markdown("---")

    # 장르별 평균 수익 비교
    st.info("🎭 **장르별 평균 전 세계 수익 비교**")
    #df_genre = df.groupby("장르")["전세계 박스오피스 수익 ($)"].mean().sort_values()
    #fig2 = plt.figure()
    #df_genre.plot(kind="barh", figsize=(10, 5), color="lightcoral")
    #plt.xlabel("평균 수익 ($)")
    #plt.ylabel("장르")
    #plt.title("장르별 평균 수익")
    #st.pyplot(fig2)

    st.write("""
    - 뮤지컬 영화 및 액션, 어드벤처, 스릴러/서스펜스 장르의 영화 수익이 높게 나타납니다.
        - 뮤지컬 장르의 경우, 작품성으로 인해 높은 수익을 올렸을 가능성도 존재하지만, **영화의 수가 다른 장르에 비해 적기 때문**에 이러한 양상을 보였을 가능성도 있습니다.
        - 액션, 어드벤처, 스릴러/서스펜스 장르의 경우, **가장 메이저한 장르**로 평가받고 이에 따라 관객 수요가 높기 때문에 자연스레 평균 수익 상위권에 올라있는 것으로 분석됩니다.
    - 코미디와 서부극 장르의 영화 수익이 낮은 것으로 파악됩니다.
        - 두 장르 모두, **특정 취향의 관객층**을 타겟팅하는 경향이 있기 때문에 이와 같이 비교적 낮은 순위를 기록하고 있는 것이라고 이해할 수 있습니다.
    """)

    st.markdown("---")

    # MPAA 등급별 수익 비교
    st.info("🎬 **상영 등급별 평균 전 세계 수익 비교**")
    #df_mpaa = df.groupby("상영 등급")["전세계 박스오피스 수익 ($)"].mean().sort_values()
    #fig3 = plt.figure()
    #df_mpaa.plot(kind="bar", figsize=(8, 5), color="lightgreen")
    #plt.ylabel("평균 수익 ($)")
    #plt.xlabel("상영 등급")
    #plt.xticks(rotation = 0)
    #plt.title("상영 등급별 평균 수익")
    #st.pyplot(fig3)

    st.write("""
    - 15세 이상 관람가와 전체 관람가가 가장 높은 수익을 올린 것으로 나타납니다.
        - 대부분의 상업 영화가 15세 이상 관람가 혹은 전체 관람가로 제작된다는 것이 이러한 경향성의 원인으로 보입니다.
    - 12세 관람가 영화의 경우, 상술한 두 등급 영화에 비해 그 수가 비교적 적기 때문에 상대적으로 적은 수익을 올리고 있는 것으로 파악됩니다.
    - 청소년 관람 불가 영화의 경우, **관객층의 범위가 다른 등급의 영화보다 현저히 작기 때문**에 높은 수익을 올리지 못하는 것으로 분석됩니다.
    """)

    st.markdown("---")

    # 상영관 수 vs 개봉 주말 수익 관계
    st.info("🏛 **상영관 수 vs 개봉 주말 수익 관계 분석**")
    #fig4 = plt.figure(figsize=(8, 6))
    #sb.scatterplot(x=df["상영관 수"], y=df["개봉 주말 수익 ($)"], alpha=0.5, color='purple')
    #plt.xlabel("상영관 수")
    #plt.ylabel("개봉 주말 수익 ($)")
    #plt.title("상영관 수와 개봉 주말 수익의 관계")
    #st.pyplot(fig4)

    st.write("""
    - 대체적으로 완만한 분포도를 보이다가 상영관 수가 약 **3,500개**를 넘어가는 시점부터 급격히 수익이 증가합니다.
        - 배급사, 영화제작사 입장에서 수익 극대화를 위한 상영관 수 설정을 할 때에 도움이 될 수 있는 자료입니다.
    """)

    st.markdown("---")
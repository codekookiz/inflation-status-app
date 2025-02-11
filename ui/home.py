import streamlit as st

def run_home():

    st.text('')
    st.text('')

    # 제목
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            🎥 영화 수익 예측 개요
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.text('')

    # 설명
    st.markdown(
        """
        <p style="font-size: 18px; text-align: center;">
            🎬 과거 영화 데이터를 기반으로 <b>신규 영화의 예상 수익을 예측</b>하는 앱입니다!<br>
            데이터 분석과 머신러닝 모델을 활용하여 <b>흥행 가능성을 미리 확인해보세요.</b>
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 📌 데이터 출처 및 구성
    st.markdown("### 📌 **사용 데이터**")
    st.info(
        """
        🔹 **[top-500-movies.csv](https://www.kaggle.com/datasets/mitchellharrison/top-500-movies-budget)** (출처: Kaggle)  
        * 1991년부터 2022년까지 개봉한 영화 중 전 세계 흥행 순위 1위부터 500위까지의 영화 데이터입니다.\n\n 
        🔹 **new_movie.csv** (상단 데이터 일부 수정 및 추가 데이터 포함)\n\n
        * **중복 데이터**('year(개봉 연도)'와 'released_date(개봉 일자)') 및 **불필요 데이터**('url' 등) 제거\n\n
        * 비슷한 속성을 지닌 영화를 그룹(클러스터)화하여 해당 그룹 정보를 **새로운 컬럼**('영화 유형')에 추가
        """
    )

    st.markdown("---")

    # 이미지 추가
    st.image("image/main_home.png", use_container_width=True)

    st.markdown("---")

    # ⚡ 기능 소개
    st.markdown("### ⚡ **탭별 주요 기능**")
    st.markdown(
        """
        - 📊 **과거 데이터 확인하기**: 기존 영화 데이터를 시각적으로 분석하고, 트렌드를 파악  
        - 🔍 **앱 상세 정보**: 이 앱의 개요와 기능을 한눈에 확인
        - 📈 **영화 수익 예측하기**: 입력한 영화 정보를 바탕으로 AI 모델이 예상 수익을 예측  
        - ⚒️ **통계 데이터**: 관리자 전용 페이지로 추가적인 분석 기능 제공  
        """
    )

    st.markdown("---")

    # 📢 활용 예시
    st.markdown("### 📢 **이렇게 활용할 수 있어요!**")
    st.markdown(
        """
        - 🎬 **영화 제작사** → 제작 전 예상 수익을 분석하여 투자 결정  
        - 🎞 **배급사** → 마케팅 전략을 세우기 전 예상 흥행 여부 판단  
        - 📺 **영화 애호가** → 과거 데이터를 통해 어떤 영화가 성공했는지 확인  
        """
    )

    st.markdown("---")
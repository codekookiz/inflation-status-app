import streamlit as st

def run_home():

    st.text('')
    st.text('')

    # 제목
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B;">
            💵 물가 예측 서비스 개요
        </h2>
        """, 
        unsafe_allow_html=True
    )

    # 설명
    st.markdown(
        """
        <p style="font-size: 18px; text-align: center;">
            💵 2014년부터 10년 간의 물가 데이터를 기반으로 <b>미래의 물가를 예측</b>하는 앱입니다!<br>
            데이터 시각화와 머신러닝 모델을 활용하여 <b>과거와 미래의 물가 수준을 직접 확인해보세요.</b>
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 📌 데이터 출처 및 구성
    st.markdown("### 📌 **사용 데이터**")
    st.info(
        """
        🔹 **[소비자물가지수_11131103.xlsx](https://ecos.bok.or.kr/#/SearchStat)** (출처: 한국은행 경제통계시스템)  
        * **2014년 1월부터 2025년 1월까지** 상품 및 서비스의 물가 지수 데이터입니다.\n\n 
        * 물가 지수의 경우 **2020년을 100으로 산정**하고, 이에 비해 다른 시점의 물가 수준을 숫자로 표현합니다.\n\n
        🔹 **price_level_index.csv** (상단 데이터 .csv 변환 및 일부 수정)\n\n
        * 식료품 관련 데이터만 사용할 계획이므로 **불필요 데이터**('교통', '통신' 등 컬럼) 제거\n\n
        * 각 컬럼명 앞에 붙은 **공백 제거** 및 '계정항목' 컬럼의 데이터 타입을 **날짜 데이터**로 변환
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
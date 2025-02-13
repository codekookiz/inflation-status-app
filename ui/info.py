import streamlit as st

def run_info():

    st.text('')
    st.text('')

    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B; font-family: 'Arial', sans-serif;">
            ℹ 앱 상세 정보
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown(
        """
        <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
            앱 개요
        </h3>
        <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        이 앱은 과거 물가 데이터를 분석하고, 인공지능(AI) 모델을 활용하여 미래의 물가를 예측하는 웹 애플리케이션입니다.  
        사용자는 특정 날짜와 품목을 입력하여 예상 물가를 확인할 수 있으며, 이를 통해 소비 계획을 세우거나 경제적 의사결정을 내리는 데 도움을 받을 수 있습니다.
        </p>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 예상 이용자
    st.markdown(
        """
        <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
            예상 이용자
        </h3>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>🏢 기업 및 자영업자</b> : 원자재 및 운영 비용의 변동을 예측하여 미리 대비하고, 가격 책정 전략을 세울 수 있습니다.<br>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>👨‍👩‍👧‍👦 일반 소비자</b> : 생활 필수품의 가격 변화를 예측하여 합리적인 소비 계획을 세울 수 있습니다.<br>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>📊 경제 분석가 및 연구자</b> : 물가 변동 데이터를 활용하여 경제 흐름을 분석하고 연구할 수 있습니다.<br>
        <br>
           <ul style="font-size: 18px; line-height: 1.8; color: #555;">
            <b>💰 투자자 및 금융 전문가</b> : 물가 변동을 기반으로 투자 전략을 수립하거나 금융 시장에 대한 인사이트를 얻을 수 있습니다.<br>
        </ul>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")

    # 앱의 장점
    st.markdown(
    """
    <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
        앱의 장점
    </h3>
    <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 실시간 물가 분석</b> : 최신 데이터를 반영하여 물가 변동을 보다 정확하게 예측할 수 있습니다.<br>
    <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ AI 기반 미래 예측</b> : 머신러닝 모델을 활용하여 과거 데이터를 학습하고, 미래 물가를 예측합니다.<br>
    <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 데이터 기반 의사결정 지원</b> : 기업, 소비자, 연구자 등 다양한 사용자가 경제적 의사결정을 내리는 데 도움을 받을 수 있습니다.<br>
        <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 직관적인 UI</b> : 누구나 쉽게 사용할 수 있도록 설계된 깔끔한 인터페이스를 제공합니다.<br>
        <br>
    <ul style="font-size: 18px; line-height: 1.8; color: #555;">
        <b>✅ 다양한 카테고리 분석</b> : 식료품뿐만 아니라 다양한 생활 필수품의 물가 변동을 확인할 수 있습니다.<br>
    </ul>
    """, 
    unsafe_allow_html=True
)

    st.markdown("---")

    # 배포 과정
    st.markdown(
    """
    <h3 style="font-size: 26px; color: #333; font-family: 'Arial', sans-serif;">
        배포 과정
    </h3><br>

    <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        📤 앱은 Streamlit을 사용하여 웹 애플리케이션 형태로 배포되었습니다.<br>
    </p>
    <p style="font-size: 18px; line-height: 1.8; letter-spacing: 0.5px; color: #555;">
        🖥️ 초기에는 로컬 환경에서 테스트 후, requirements.txt 파일을 생성하여 외부 환경에서도 실행 가능하도록 설정하였습니다.
    </p>
    """, 
    unsafe_allow_html=True
)

    st.markdown("---")
import streamlit as st

from ui.dev import run_dev
from ui.eda import run_eda
from ui.home import run_home
from ui.info import run_info
from ui.ml import run_ml
from ui.recom import run_recom


def main() :

    st.markdown(
        """
        <h1 style='text-align: center; color: color: #4C82C2;'>
            🎬 app title
        </h1>
        <h2 style='text-align: center; 'color: #4C82C2;'>
            🤖 details
        </h2>
        """, unsafe_allow_html=True
    )

    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["🏠 홈", "ℹ 앱 상세 정보", "⚒️ 개발 정보", "📊 과거 물가 비교하기", "🎬 물가 예측하기", "💿 대체품 추천"])

    # 각 탭에 해당하는 기능 실행
    with tab1:
        run_home()

    with tab2:
        run_info()

    with tab3:
        run_dev()

    with tab4:
        run_eda()

    with tab5:
        run_ml()

    with tab6:
        run_recom()


if __name__ == '__main__' :
    main()
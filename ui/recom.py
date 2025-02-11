import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb


def run_recom() :

    st.text('')
    st.text('')

    st.markdown(
            """
            <h2 style="text-align: center; color: #FF4B4B;">
                💿 통계 데이터
            </h2>
            """, 
            unsafe_allow_html=True
        )

    st.markdown("---")
        
    # 설명 부분 스타일 개선
    st.markdown(
        """
        <p style="font-size: 24px; text-align: center;">
            <b>누적된 영화 예측 데이터 통계를 표시합니다.<b>
        </p>
        """, 
        unsafe_allow_html=True
    )
    st.text('')

    df = pd.read_csv('data/price_level_index.csv')
    #df['개봉 연도'] = df['개봉 연도'].astype(str)
    st.dataframe(df.sort_index(ascending=False))

    st.write("""
    - 앱 사용자들이 수익 예측을 위해 입력한 정보를 별도의 데이터 테이블에 저장합니다.
        - 앱을 통해 입력된 데이터의 분석 및 재가공 목적으로 사용될 수 있습니다.
        - 하단의 차트를 참고하여 경향성 역시 확인이 가능합니다.
    - 사용자들이 입력한 데이터와 머신 러닝 모델을 통해 도출된 예측 결과를 함께 저장합니다.
        - 데이터를 인덱스 역순(descending)으로 정렬하여 최신 입력 데이터가 가장 위에 표시되도록 하였습니다.
    """)


    st.subheader('')

    if not df.empty :
        # 연도별 평균 수익 시각화
        st.info("📅 **연도별 평균 전 세계 수익 분석**")
        #df_yearly = df.groupby("개봉 연도")["전세계 예상 수익 ($)"].mean()
        #fig1 = plt.figure()
        #df_yearly.plot(kind="bar", figsize=(10, 5), color="skyblue")
        #plt.ylabel("평균 수익 ($)")
        #plt.xlabel("연도")
        #plt.title("연도별 평균 수익")
        #st.pyplot(fig1)

        st.markdown("---")

        # 장르별 평균 수익 비교
        st.info("🎭 **장르별 평균 전 세계 수익 비교**")
        #df_genre = df.groupby("장르")["전세계 예상 수익 ($)"].mean().sort_values()
        #fig2 = plt.figure()
        #df_genre.plot(kind="barh", figsize=(10, 5), color="lightcoral")
        #plt.xlabel("평균 수익 ($)")
        #plt.ylabel("장르")
        #plt.title("장르별 평균 수익")
        #st.pyplot(fig2)

        st.markdown("---")

        # MPAA 등급별 수익 비교
        st.info("🎬 **상영 등급별 평균 전 세계 수익 비교**")
        #df_mpaa = df.groupby("상영 등급")["전세계 예상 수익 ($)"].mean().sort_values()
        #fig3 = plt.figure()
        #df_mpaa.plot(kind="bar", figsize=(8, 5), color="lightgreen")
        #plt.ylabel("평균 수익 ($)")
        #plt.xlabel("상영 등급")
        #plt.xticks(rotation = 0)
        #plt.title("상영 등급별 평균 수익")
        #st.pyplot(fig3)
        
        st.markdown("---")
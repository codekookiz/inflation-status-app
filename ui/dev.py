import streamlit as st

def run_dev():
    # 스타일 적용
    st.markdown(
        """
        <style>
            h1, h2, h3 {
                text-align: center;
                color: #FF4B4B;
                font-family: 'Arial', sans-serif;
                display: inline-block;
                width: 100%;
            }
            h1 { font-size: 36px; font-weight: bold; }
            h2 { font-size: 30px; font-weight: bold; }
            h3 { font-size: 26px; font-weight: bold; }
            
            h2::after {
                content: "";
                display: block;
                width: 50%;
                height: 3px;
                background: #FF4B4B;
                margin: 5px auto;
                border-radius: 5px;
            }
            .highlight { color: #FF4B4B; font-weight: bold; }
            .emoji { font-size: 24px; }
        </style>
        """,
        unsafe_allow_html=True
    )

    # 제목
    st.text('')
    st.text('')

    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B; font-family: 'Arial', sans-serif;">
            🛠️ 개발 정보
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")
    
    # 프로젝트 개요
    st.markdown('<h2>📌 프로젝트 개요</h2>', unsafe_allow_html=True)
    st.write("""
    영화 제작 및 배급 과정에서 제작비, 장르, 상영 시간, 개봉 연도 등의 정보를 활용하여
    영화 유형을 분류하고, 박스오피스 수익을 예측하는 모델을 개발했습니다.
    """)
    
    st.markdown('<h4>✅ 프로젝트 목표</h4>', unsafe_allow_html=True)
    st.write("""
    - **영화 유형 분류** – 클러스터링을 이용한 자동 분류  
    - **사용자 입력 기반 유형 예측**  
    - **북미 박스오피스 수익 예측**  
    - **전 세계 박스오피스 수익 예측**  
    """)

    st.markdown("---")
    
    # 데이터 수집 및 전처리
    st.markdown('<h2>🎞 데이터 수집 및 전처리</h2>', unsafe_allow_html=True)
    
    st.markdown('<h4>📌 사용한 데이터</h4>', unsafe_allow_html=True)
    st.write("""
    - **출처:** Kaggle (top-500-movies.csv)  
    - **주요 특성:** 제작비, 개봉 수익, 장르, 상영 시간, 개봉 연도, 상영 등급  
    """)
    
    st.markdown('<h4>📌 전처리 과정</h4>', unsafe_allow_html=True)
    st.write("""
    - 🔹 **결측치 처리** – 누락된 데이터 보완(NaN 값을 해당 컬럼의 mean()값으로 대체)   
    - 🔹 **문자열 데이터 인코딩** – LabelEncoder 적용(장르, 상영 등급 등 문자열 컬럼)    
    """)

    st.markdown("---")
    
    # 영화 유형 분류 (클러스터링)
    st.markdown('<h2>🏷 영화 유형 분류 (클러스터링)</h2>', unsafe_allow_html=True)
    
    st.markdown('<h4>📌 사용한 기법</h4>', unsafe_allow_html=True)
    st.write("""
    - K-Means 클러스터링  
    - 최적 K값 선정: 엘보우 메소드 적용 (2 ≤ K ≤ 10)  
    """)
    
    st.markdown('<h4>📌 엘보우 메소드 차트</h4>', unsafe_allow_html=True)
    st.image('image/elbow_method.png', caption='엘보우 메소드를 이용한 클러스터 개수 결정', use_container_width=True)

    st.markdown('<h4>📌 최적의 클러스터 개수 결정</h4>', unsafe_allow_html=True)
    st.write("""
    - 개발자가 임의로 클러스터 개수를 정하는 것이 아닌, 내부 연산을 통해 스스로 최적의 클러스터 개수를 도출
    - 차트 내 임의의 좌표를 기준으로, 앞뒤의 기울기가 드라마틱하게 변화하는 지점을 최적의 클러스터 개수가 형성되는 지점으로 설정
    """)

    st.markdown('<h4>📌 최적의 클러스터 개수 계산 결과</h4>', unsafe_allow_html=True)
    st.write("""
    - 3개의 클러스터로 분류할 경우 가장 효율적이라는 결론에 도달         
    """)
    
    st.markdown('<h4>📌 결과: 3가지 유형의 영화 분류</h4>', unsafe_allow_html=True)
    st.write("""
    1️⃣ **메가 블록버스터** – 아주 높은 제작비와 수익을 기록하는 초대형 영화  
    2️⃣ **블록버스터** – 중간 정도의 제작비와 높은 수익을 기대할 수 있는 영화  
    3️⃣ **미들 마켓** – 상대적으로 낮은 제작비와 중간 수준의 수익을 내는 영화  
    """)

    st.markdown("---")
    
    # 영화 유형 예측 (KNN 모델)
    st.markdown('<h2>🎭 영화 유형 예측 (KNN 모델)</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 사용한 기법</h4>', unsafe_allow_html=True)
    st.write("""
    - KNN (K-Nearest Neighbors) 분류 모델 (n_neighbors = 5)  
    - 모델 정확도: 75.76%  
    """)
    
    st.markdown('<h4>📌 사용자 입력 예시</h5>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                제작비: 80000000 
                장르: 액션  
                상영 시간: 130  
                개봉 연도: 2023
                """)

    st.markdown('<h4>📌 예측 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 예상 유형: 메가 블록버스터
                """)

    st.markdown("<h4>📌 활용 방안</h4>", unsafe_allow_html=True)
    st.write("""
    ✅ 영화 제작 초기에 유형을 미리 파악하여 마케팅 전략 수립 가능  
    ✅ 투자자들이 영화 프로젝트의 성격을 쉽게 이해할 수 있도록 지원
    """)

    st.markdown("---")
    
    # 북미 박스오피스 수익 예측
    st.markdown('<h2>🎟 북미 박스오피스 수익 예측</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 목표</h4>', unsafe_allow_html=True)
    st.write('- 영화의 북미 개봉 후 예상 수익을 머신러닝을 통해 예측')

    st.markdown('<h4>📌 사용한 기법</h4>', unsafe_allow_html=True)
    st.write("""
    - Linear Regression (선형 회귀)  
    - RandomForestRegressor (랜덤 포레스트)  
    - XGBRegressor (XGBoost)  
    - **최종 선정 모델**: 선형 회귀 (예측 정확도 73%)  
    """)

    st.markdown('<h4>📌 사용자 입력 예시</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                제작비: 80000000 
                장르: 액션  
                상영 시간: 130  
                개봉 연도: 2023
                """)

    st.markdown('<h4>📌 예측 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 예상 북미 박스오피스 수익: 2억 5000만 달러
                """)

    st.markdown('<h4>📌 활용 방안</h4>', unsafe_allow_html=True)
    st.write("""
    ✅ 신작 영화의 예상 수익을 미리 예측하여 투자 리스크 관리 가능  
    ✅ 배급 전략 최적화를 위한 데이터 기반 의사 결정 지원
    """)

    st.markdown("---")
    
    # 전 세계 박스오피스 수익 예측
    st.markdown('<h2>🌍 전 세계 박스오피스 수익 예측</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 목표</h4>', unsafe_allow_html=True)
    st.write('- 북미 박스오피스 수익을 기반으로 전 세계 박스오피스 수익 예측')

    st.markdown('<h4>📌 분석 결과</h4>', unsafe_allow_html=True)
    st.write("""
    - 북미 수익 대비 전 세계 평균 수익 배율: 3.51배  
    - 그러나 이상치(최댓값 315.4)를 고려하여 **중앙값(2.7배)** 을 최종 배율로 적용
    """)

    st.markdown('<h4>📌 예측 공식</h4>', unsafe_allow_html=True)
    st.write('- **전 세계 수익 = 북미 박스오피스 수익 × 2.7**')

    st.markdown('<h4>📌 사용자 입력 예시</h5>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                제작비: 80000000 
                장르: 액션  
                상영 시간: 130  
                개봉 연도: 2023
                """)

    st.markdown('<h4>📌 예측 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 예상 전 세계 박스오피스 수익: 6억 7500만 달러
                """)

    st.markdown('<h4>📌 활용 방안</h4>', unsafe_allow_html=True)
    st.write("""
    ✅ 해외 배급 전략 수립 시 예상 글로벌 수익 분석 가능  
    ✅ 투자 규모 및 마케팅 예산 설정에 도움
    """)

    st.markdown("---")
    
    # 향후 개선 가능성
    st.markdown('<h2>🎯 향후 개선 가능성</h2>', unsafe_allow_html=True)
    st.write("""
    **📌 모델 개선**  
    ✅ Deep Learning 기법 도입하여 예측 정확도 향상  
    ✅ 더 많은 데이터셋을 확보하여 학습 데이터 확장

    **📌 UI 및 사용자 경험 개선**  
    ✅ Streamlit 기반 인터페이스를 개선하여 직관적인 데이터 입력 및 시각화 제공  
    ✅ 색각이상을 고려한 클러스터 시각화 기능 추가  

    **📌 실제 영화 산업 적용**  
    ✅ 영화 제작사 및 배급사와 협업하여 실제 데이터 기반 실험 진행  
    ✅ 글로벌 시장 트렌드를 반영한 수익 예측 모델 개선
    """)

    st.markdown("---")
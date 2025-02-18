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
    st.markdown(
        """
        <h2 style="text-align: center; color: #FF4B4B; font-family: 'Arial', sans-serif;">
            ⚒️ 개발 정보
        </h2>
        """, 
        unsafe_allow_html=True
    )

    st.markdown("---")
    
    # 프로젝트 개요
    st.markdown('<h2>📌 프로젝트 개요</h2>', unsafe_allow_html=True)
    st.write("""
    과거 10년의 물가 변동 데이터를 활용하여, 향후 물가 변동을 예측하는 머신러닝 모델을 개발하였습니다.
    """)
    
    st.markdown('<h4>✅ 프로젝트 목표</h4>', unsafe_allow_html=True)
    st.write("""
    - **식료품의 미래 가격 예측**  
    - **카테고리별 물가 변동 추세 분석**  
    - **대체 상품 추천 시스템 구축**  
    """)

    st.markdown("---")
    
    # 데이터 수집 및 전처리
    st.markdown('<h2>📊 데이터 수집 및 전처리</h2>', unsafe_allow_html=True)
    
    st.markdown('<h4>📌 사용한 데이터</h4>', unsafe_allow_html=True)
    st.write("""
    - **출처:** 한국은행 경제통계시스템 ([소비자물가지수_11131103.xlsx](https://ecos.bok.or.kr/#/SearchStat))
    - **주요 특성:** 계정항목(일자), 빵 및 곡물/교통/통신 등 주요 상품 및 서비스
    """)
    
    st.markdown('<h4>📌 전처리 과정</h4>', unsafe_allow_html=True)
    st.write("""
    - 🔹 **식료품 데이터 추출** – 상품/서비스 데이터 중 식료품 관련 데이터만 추출  
    - 🔹 **문자열 데이터 변환** – 날짜 데이터를 담고 있는 '계정항목' 데이터 타입 문자열로부터 변환  
    - 🔹 **시계열 데이터 변환** – Prophet 모델을 활용하여 물가 추세 예측  
    """)

    st.markdown("---")
    
    st.markdown('<h2>📈 물가 예측 모델</h2>', unsafe_allow_html=True)
    
    st.markdown('<h4>📌 사용한 기법</h4>', unsafe_allow_html=True)
    st.write("""
    - **Prophet (페이스북 시계열 예측 모델)**    
    """)

    st.markdown('<h4>📌 2014년 1월부터 2025년 1월까지의 물가 인덱스 정리</h4>', unsafe_allow_html=True)
    st.write("""
    - 2020년의 물가 수준을 100으로 설정하고, 이를 기반으로 상대적인 물가 수준을 실수 데이터로 표시한 데이터셋
    - 문자열 데이터로 이루어진 '계정항목' 컬럼을 날짜 데이터로 변환(pd.to_datetime)
    - 식료품과 관련된 컬럼만 추출하여 새로운 데이터셋 저장 (price_level_index.csv)
    """)

    st.markdown("---")

    st.markdown('<h2>🎭 과거 물가 데이터 확인</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 코드 프로세스</h4>', unsafe_allow_html=True)
    st.write("""
    - 사용자로부터 확인하고자 하는 **연도**와 **월**, **구매 시점(2025년 1월)의 가격** 데이터를 입력 받음
    - 연도와 월 데이터를 조합하여 날짜 포맷으로 변환하고, 데이터셋에서 해당 날짜에 맞는 물가 인덱스 데이터를 필터링
    - 구매 시점의 가격을 가격 인덱스에 곱하여 사용자가 입력한 시점의 가격 추론
    """)
    
    st.markdown('<h4>📌 사용자 입력 예시</h5>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                식료품 유형: 빵 및 곡물
                세부 유형: 쌀
                2025년 1월 기준 가격: 10000 
                연도: 2014
                """)

    st.markdown('<h4>📌 확인 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 쌀
                ▶ 2014-01-01 : 8770
                ▶ 2014-02-01 : 8770
                ▶ 2014-03-01 : 8720
                ...
                ▶ 2014-11-01 : 8760
                ▶ 2014-12-01 : 8650
                """)

    st.markdown("<h4>📌 활용 방안</h4>", unsafe_allow_html=True)
    st.write("""
    ✅ **과거 대비 물가 분석**: 특정 시점의 가격과 비교하여 물가 상승률을 확인하고, 구매 시점의 가격 적정성을 평가  
    ✅ **예산 계획 수립**: 과거 데이터를 참고하여 향후 예산을 계획하고, 동일 품목의 예상 비용을 추정하는 데 활용 가능  
    ✅ **투자 및 비즈니스 의사 결정**: 식료품의 가격 변동을 분석하여, 사업 운영/투자 전략을 세우는 데 활용  
    ✅ **가격 협상 및 마케팅 전략 수립**: 원재료 비용 변화에 따른 가격 책정 전략을 수립하고, 소비자 대상 마케팅 자료로 활용  
    """)

    st.markdown("---")
    
    st.markdown('<h2>🎟 향후 식료품 물가 수준 예측</h2>', unsafe_allow_html=True)

    st.markdown('<h4>📌 목표</h4>', unsafe_allow_html=True)
    st.write('- 식료품의 미래 예상 물가 수준을 머신러닝을 통해 예측')

    st.markdown('<h4>📌 사용한 기법</h4>', unsafe_allow_html=True)
    st.write("""
    - **Prophet (페이스북 시계열 예측 모델)**   
    """)

    st.markdown('<h4>📌 사용자 입력 예시</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                식료품 유형: 육류
                세부 유형: 수입쇠고기
                연도: 2027  
                월: 6 
                """)

    st.markdown('<h4>📌 예측 결과</h4>', unsafe_allow_html=True)
    st.markdown("""
                ```bash
                ▶ 예상 물가 상승률 : 0.7%, 2030년 12월까지 9% 상승 예상
                """)

    st.markdown('<h4>📌 활용 방안</h4>', unsafe_allow_html=True)
    st.write("""
    ✅ **장기적인 구매 계획 수립**: 가격 변동 예측을 활용하여 대량 구매 시점을 조정하거나, 향후 예산을 계획하는 데 도움을 받을 수 있음.  
    ✅ **소비자 및 기업의 가격 전략 수립**: 소비자는 저렴한 시기를 선택해 구매할 수 있고, 기업은 가격 변동을 고려하여 판매 전략을 최적화할 수 있음.  
    ✅ **공급망 및 재고 관리 최적화**: 미래 가격 변동을 예측하여 원자재 조달 전략을 조정하고, 효율적인 재고 관리가 가능함.  
    ✅ **정부 및 기관의 정책 수립 지원**: 물가 변동을 기반으로 식료품 보조금 정책이나 수급 조절 전략을 설계하는 데 활용 가능.  
    """)
    
    st.markdown("---")
    
    # 향후 개선 가능성
    st.markdown('<h2>🎯 향후 개선 가능성</h2>', unsafe_allow_html=True)
    st.write("""
    ✅ **예측 모델 고도화**: Prophet 외에도 다양한 머신러닝 및 딥러닝 모델을 활용하여 예측 정확도를 향상.  
    ✅ **사용자 맞춤형 추천**: 개인별 소비 패턴을 반영한 맞춤형 대체품 추천 시스템 추가.  
    ✅ **실시간 데이터 반영**: 최신 식료품 가격 데이터를 실시간으로 반영하여 보다 정확한 예측 제공.    
    ✅ **앱 UI/UX 개선**: 보다 직관적인 인터페이스와 사용자 경험을 제공하여 앱 활용도를 극대화.
    """)

    st.markdown("---")
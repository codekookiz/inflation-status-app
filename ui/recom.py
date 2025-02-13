from datetime import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from prophet import Prophet

def run_recom(item, category, curr_price, step1_options, pred_date):
    st.markdown('<h2>📌 대체품 추천</h2>', unsafe_allow_html=True)
    df = pd.read_csv('data/price_level_index.csv')
    
    if item == '-':
        st.error('대체품을 확인하고 싶으시면, 정보 입력 시 세부 유형을 선택해주세요.')
        return
    
    if item == '기타':
        new_item = category
        if new_item == '외식':
            new_item = '음식 서비스'
    else:
        new_item = item

    compare_dict = {}
    for a in step1_options[category]:
        if a == '-' :
            continue
        if a == '기타':
            a = category
            if a == '외식':
                a = '음식 서비스'
        
        df_1 = df[['계정항목', a]]
        df_1.columns = ['ds', 'y']
        
        model = Prophet()
        model.fit(df_1)
        future = model.make_future_dataframe(periods=72, freq='M')
        forecast = model.predict(future)

        if pred_date > datetime.today():
            std_price = df_1.iloc[df_1.index.max(), 1]
            then_price = forecast.loc[forecast['ds'] == pred_date, 'yhat'].values[0]
            inflation_index = (then_price / std_price)
            new_price = int((curr_price * inflation_index).round(-1))
            compare_dict[a] = new_price

    min_key = min(compare_dict, key=compare_dict.get)
    
    st.markdown("---")
    if item == min_key :
        st.success(f"🎉 **{category} 중에서는 {item} 이(가) 가장 저렴합니다!** 🎉")
    else:
        st.markdown(f"### 🔍 대체 추천: **{min_key}**")
        st.info(f'💡 **{min_key}** 은(는) {item} 보다 더 경제적인 선택이 될 수 있습니다!')
        
        df_a = df[['계정항목', item]]
        df_b = df[['계정항목', min_key]]
        df_a.columns = ['ds', 'y']
        df_b.columns = ['ds', 'y']

        model_a = Prophet()
        model_b = Prophet()
        model_a.fit(df_a)
        model_b.fit(df_b)
        future_a = model_a.make_future_dataframe(periods=72, freq='M')
        future_b = model_b.make_future_dataframe(periods=72, freq='M')
        forecast_a = model_a.predict(future_a)
        forecast_b = model_b.predict(future_b)
        
        if pred_date > datetime.today():
            std_price_a = df_a.iloc[df_a.index.max(), 1]
            std_price_b = df_b.iloc[df_b.index.max(), 1]
            then_price_a = forecast_a.loc[forecast_a['ds'] == pred_date, 'yhat'].values[0]
            then_price_b = forecast_b.loc[forecast_b['ds'] == pred_date, 'yhat'].values[0]
            inflation_index_a = (then_price_a / std_price_a)
            inflation_index_b = (then_price_b / std_price_b)
            new_price_a = int((curr_price * inflation_index_a).round(-1))
            new_price_b = int((curr_price * inflation_index_b).round(-1))
            ratio = int((new_price_a - new_price_b) / new_price_b * 100)
            
            st.success(f'💰 **예상 가격 비교**')
            st.markdown(f"- **{item} 예상 가격:** {new_price_a:,}원")
            st.markdown(f"- **{min_key} 예상 가격:** {new_price_b:,}원")
            st.info(f'📉 **{min_key}** 이(가) **{ratio} %** 더 저렴합니다!')
            
            # 가격 변화 그래프 추가
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.plot(forecast_a['ds'], forecast_a['yhat'] / std_price_a * curr_price, label=item, color='red')
            ax.plot(forecast_b['ds'], forecast_b['yhat'] / std_price_b * curr_price, label=min_key, color='blue')
            ax.axvline(datetime.today(), color='red', linestyle='dashed', label='오늘 날짜')
            ax.scatter(pred_date, then_price_a / std_price_a * curr_price, color='maroon', s=30, label=f'{item} 예측 가격', zorder=3)
            ax.scatter(pred_date, then_price_b / std_price_b * curr_price, color='navy', s=30, label=f'{min_key} 예측 가격', zorder=3)
            ax.set_title(f'{item} vs {min_key} 가격 추이')
            ax.set_xlabel('날짜')
            ax.set_ylabel('예상 가격')
            ax.legend()
            st.pyplot(fig)
from datetime import datetime
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
from prophet import Prophet


def run_recom(item, category, curr_price, step1_options, pred_date) :
    st.markdown('<h2>📌 대체품 추천</h2>', unsafe_allow_html=True)
    df = pd.read_csv('data/price_level_index.csv')
    if item == '-' :
        st.error('대체품을 확인하고 싶으시면, 정보 입력 시 세부 유형을 선택해주세요.')
    else :
        if item == '기타':
            new_item = category
            if new_item == '외식' :
                new_item = '음식 서비스'
        else :
            new_item = item
        

        compare_dict = {}
        for a in step1_options[category]:
            if a == '-' :
                continue
            if a == '기타' :
                a = category
                if a == '외식' :
                    a = '음식 서비스'
            df_1 = df[['계정항목', a]]

            df_1.columns = ['ds', 'y']

            model = Prophet()
            model.fit(df_1)
            future = model.make_future_dataframe(periods=72, freq='M')
            forecast = model.predict(future)

            if pred_date > datetime.today() :
                std_price = df_1.iloc[df_1.index.max(), 1]
                then_price = forecast.loc[forecast['ds'] == pred_date, 'yhat'].values[0] # pred_date 아니라 원래 new_date였음
                inflation_index = (then_price / std_price)
                new_price = int((curr_price * inflation_index).round(-1))
                compare_dict[a] = new_price
        
        min_key = min(compare_dict, key=compare_dict.get)

        if min_key == item :
            st.success(f"🎉 {category} 중에서는 {item}이 가장 쌉니다! 🎉")
        else :
            st.info(f'**{min_key}**은(는) 어떠신가요?')
            
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

            if pred_date > datetime.today() :
                std_price_a = df_a.iloc[df_a.index.max(), 1]
                std_price_b = df_b.iloc[df_b.index.max(), 1]
                then_price_a = forecast_a.loc[forecast_a['ds'] == pred_date, 'yhat'].values[0] # pred_date 아니라 원래 new_date였음
                then_price_b = forecast_b.loc[forecast_b['ds'] == pred_date, 'yhat'].values[0] # pred_date 아니라 원래 new_date였음
                inflation_index_a = (then_price_a / std_price_a)
                inflation_index_b = (then_price_b / std_price_b)
                new_price_a = int((curr_price * inflation_index_a).round(-1))
                new_price_b = int((curr_price * inflation_index_b).round(-1))
    
                ratio = int((new_price_a - new_price_b) / new_price_b * 100)
    
                st.info(f'**{ratio}%** 더 저렴합니다!')












        
        st.markdown("---")
import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="自動化股票分析系統", layout="wide")
st.title("自動化股票分析系統")

ticker = st.text_input("請輸入股票代碼 (例如台積電: 2330.TW, 蘋果: AAPL)", value="2330.TW")

if st.button("開始分析"):
    with st.spinner('系統連接資料來源下載歷史資料中...'):
        
        data = yf.download(ticker, period="1y")
        
        if data.empty:
            st.error("找不到該股票代碼的資料，請確認後重新輸入。")
        else:
            df = data[['Close']].copy()
            df.columns = ['收盤價']
            df['每日報酬率'] = df['收盤價'].pct_change()
            
            total_return = (df['收盤價'].iloc[-1] / df['收盤價'].iloc[0]) - 1
            
            daily_volatility = df['每日報酬率'].std()
            annual_volatility = daily_volatility * np.sqrt(252)
            st.markdown("### 投資績效與風險指標")
            
            col1, col2, col3 = st.columns(3)
            col1.metric("最新收盤價", f"{df['收盤價'].iloc[-1]:.2f}")
            col2.metric("近一年累積報酬率", f"{total_return * 100:.2f}%")
            col3.metric("風險程度 (波動率標準差)", f"{annual_volatility * 100:.2f}%")
            
            st.caption("💡 波動越大 → 價格起伏劇烈 → 風險較高；波動越小 → 價格穩定 → 風險較低")
            
            st.divider()
            
            st.markdown("### 資料視覺化成果")
            
            fig = px.line(df, y='收盤價', title=f"{ticker} 近一年價格走勢圖")
            fig.update_xaxes(title_text="時間")
            fig.update_yaxes(title_text="價格")
            st.plotly_chart(fig, use_container_width=True)
            
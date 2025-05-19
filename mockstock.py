#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 18 20:45:46 2025

@author: aishaoyebanji
"""
import streamlit as st
import pandas as pd
import numpy as np
import time
from datetime import datetime

#setupstuff
st.set_page_config(page_title="Fund Ops Dashboard", layout="wide")
st.title("Mock ISMF Live Operations")

        
#data
def generate_positions():
    positions = pd.DataFrame({
        "Ticker": ["AAPL", "NVDA", "MSFT", "AMD", "GOOGL"],
        "Shares": np.random.randint(10, 100, 5),
        "Avg Cost": np.round(np.random.uniform(100, 300, 5), 2),
        "Last Price": np.round(np.random.uniform(80, 350, 5), 2),
    })
    positions["P&L"] = (positions["Last Price"] - positions["Avg Cost"]) * positions["Shares"]
    return positions

def generate_trade_volumes():
    dates = pd.date_range(end=datetime.today(), periods=30)
    return pd.DataFrame({
        "Date": dates,
        "Volume": np.random.randint(100, 5000, len(dates))
    })

#layout
col1, col2 = st.columns(2)

with col1:
    st.subheader("📊 Active Positions")
    positions = generate_positions()  
    st.dataframe(positions.style.highlight_max(axis=0))

    st.subheader("📈 Risk Metrics")
    st.metric("Portfolio Beta", np.round(np.random.uniform(0.8, 1.4), 2))
    st.metric("Value at Risk (1d)", f"${np.random.randint(500, 2000):,}")

with col2:
    st.subheader("Trade Volumes (30d)")
    volumes = generate_trade_volumes()  
    st.bar_chart(volumes, x="Date", y="Volume")

    st.subheader("Recent Activity")
    for _ in range(5):
        st.text(f"{datetime.now().strftime('%H:%M:%S')} - Traded {np.random.choice(['AAPL', 'TSLA'])} (${np.random.randint(1000, 50000):,})")
        time.sleep(0.1) #realtimeupdates

#refresh every 15s
st.rerun()

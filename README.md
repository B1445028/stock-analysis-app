# 自動化股票分析系統 (Automated Stock Analysis System)

這是一個基於 Python 與 Streamlit 開發的輕量級網頁應用程式。使用者只需輸入股票代碼，系統即可自動抓取 Yahoo Finance 的真實歷史股價資料，並計算其投資報酬與風險指標，最後以視覺化互動圖表呈現。

本專案的核心分析理念為：**「不只看報酬，也看風險」**。

**[點我查看即時運作的網頁版本](https://stock-analysis-app-87bxrgk7xjgcsfyjes8hvh.streamlit.app/)**

---

## 系統特色與核心功能

本系統完美實作了全自動化的資料分析流程：

1. **使用者輸入股票代碼**：支援全球股票與 ETF (如台積電 `2330.TW`、蘋果 `AAPL`)。
2. **自動下載歷史資料**：串接 `yfinance` 開源套件，取得近一年的真實市場行情。
3. **資料整理與清洗**：自動萃取每日收盤價並計算每日報酬率。
4. **計算績效與風險指標**：
   * **累積報酬率**：計算區間內的總獲利表現。
   * **風險 (年化波動率)**：透過標準差衡量價格變動幅度，協助比較不同股票的穩定程度。
5. **資料視覺化**：整合 Plotly 互動式圖表，自動生成清晰的歷史價格走勢圖，讓市場趨勢更直觀、更容易做決策。

---

## 使用技術與套件

* **前端介面與網頁框架**：[Streamlit](https://streamlit.io/)
* **資料獲取**：[yfinance](https://pypi.org/project/yfinance/)
* **資料處理與數學計算**：[Pandas](https://pandas.pydata.org/), [NumPy](https://numpy.org/)
* **資料視覺化**：[Plotly Express](https://plotly.com/python/plotly-express/)

---

## 如何在本地端執行？

如果您想將此專案下載到您自己的電腦上執行，請跟著以下步驟操作：

**1. 下載專案**
將本儲存庫 (Repository) 下載或 Clone 到您的本機電腦。

**2. 安裝所需套件**
請確保您的電腦已安裝 Python，接著在終端機輸入以下指令安裝相依套件：
```
pip install -r requirements.txt
```

**3. 啟動網站**
在終端機輸入以下指令啟動 Streamlit 伺服器：
```
python -m streamlit run app.py
```
(啟動後，系統會自動在您的瀏覽器中開啟 http://localhost:8501 顯示網頁)

# 本專案僅供學習與技術展示使用，不構成任何財務投資建議。

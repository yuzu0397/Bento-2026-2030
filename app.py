import streamlit as str_lit

# ページ設定
str_lit.set_page_config(page_title=":( System Error - 000xWinKL", layout="wide", page_icon="🟦")

# --- BSOD画面（メイン:5秒周期/4秒表示、詳細情報:3秒切替） ---
bsod_html = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    background-color: #0078d7 !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
    overflow: hidden !important;
}

header, footer, [data-testid="stSidebar"], [data-testid="stHeader"] {
    display: none !important;
}

.bsod-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #0078d7;
    z-index: 9999999;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 8% 12%;
    box-sizing: border-box;
    color: #ffffff;
}

.bsod-sad-face {
    font-size: 110px;
    font-weight: 300;
    line-height: 1.0;
    margin-bottom: 25px;
    user-select: none;
}

/* --- メインエラー文章（5秒周期 / 4秒表示・全体10秒サイクル） --- */
.main-wrapper {
    position: relative;
    height: 90px;
    width: 100%;
    max-width: 850px;
    margin-bottom: 25px;
}

.main-msg {
    position: absolute;
    top: 0;
    left: 0;
    font-size: 26px;
    font-weight: 300;
    line-height: 1.4;
    opacity: 0;
    animation: cycleMain 10s infinite ease-in-out;
}

.main-ja { animation-delay: 0s; }
.main-en { animation-delay: 5s; }

@keyframes cycleMain {
    0% { opacity: 0; transform: translateY(3px); }
    3% { opacity: 1; transform: translateY(0); }
    40% { opacity: 1; transform: translateY(0); }  /* 4秒間しっかり表示 */
    45% { opacity: 0; transform: translateY(-3px); }
    100% { opacity: 0; }
}

/* --- OS情報・再起動・エラーコード（3秒切替・全体6秒サイクル） --- */
.info-wrapper {
    position: relative;
    height: 100px;
    width: 100%;
    max-width: 850px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 15px;
    line-height: 1.7;
    opacity: 0.95;
}

.info-msg {
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    animation: cycleInfo 6s infinite ease-in-out;
}

.info-ja { animation-delay: 0s; }
.info-en { animation-delay: 3s; }

@keyframes cycleInfo {
    0% { opacity: 0; transform: translateY(2px); }
    5% { opacity: 1; transform: translateY(0); }
    43% { opacity: 1; transform: translateY(0); }
    48% { opacity: 0; transform: translateY(-2px); }
    100% { opacity: 0; }
}
</style>

<div class="bsod-container">
<div class="bsod-sad-face">:(</div>
<div class="main-wrapper">
<div class="main-msg main-ja">致命的なエラーが発生したため、システムはお使いになれません。<br>エラー情報を収集しています。自動的に再起動はされません。</div>
<div class="main-msg main-en">A critical error has occurred. The system is currently unavailable.<br>We're collecting error info, but the system will not restart automatically.</div>
</div>
<div class="info-wrapper">
<div class="info-msg info-ja">対象OS: Windows 10 & 11 Android<br>再起動見込み: なし<br>エラーコード: 000xWinKL</div>
<div class="info-msg info-en">Target OS: Windows 10 & 11 Android<br>Estimated Restart: None<br>Error Code: 000xWinKL</div>
</div>
</div>
"""

str_lit.markdown(bsod_html, unsafe_allow_html=True)

# 完全に処理を停止（ロック状態）
str_lit.stop()

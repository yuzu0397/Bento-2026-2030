import streamlit as str_lit

# ページ設定
str_lit.set_page_config(page_title=":( System Error - 000xWinKL", layout="wide", page_icon="🟦")

# --- BSOD画面（マルチアスペクト比対応：PC 16:9 / スマホ 9:16 & 9:21） ---
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

/* 基本コンテナ（PC 16:9 基準） */
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
    padding: 8vh 10vw;
    box-sizing: border-box;
    color: #ffffff;
}

/* 画面サイズに応じた可変フォントサイズ */
.bsod-sad-face {
    font-size: clamp(80px, 10vw, 120px);
    font-weight: 300;
    line-height: 1.0;
    margin-bottom: 25px;
    user-select: none;
}

/* --- メインエラー文章（5秒周期 / 4秒表示） --- */
.main-wrapper {
    position: relative;
    height: 100px;
    width: 100%;
    max-width: 900px;
    margin-bottom: 20px;
}

.main-msg {
    position: absolute;
    top: 0;
    left: 0;
    font-size: clamp(18px, 2.5vw, 26px);
    font-weight: 300;
    line-height: 1.4;
    opacity: 0;
    animation: cycleMain 10s infinite ease-in-out;
    width: 100%;
}

.main-ja { animation-delay: 0s; }
.main-en { animation-delay: 5s; }

@keyframes cycleMain {
    0% { opacity: 0; transform: translateY(3px); }
    3% { opacity: 1; transform: translateY(0); }
    40% { opacity: 1; transform: translateY(0); }
    45% { opacity: 0; transform: translateY(-3px); }
    100% { opacity: 0; }
}

/* --- 詳細情報（3秒周期切替） --- */
.info-wrapper {
    position: relative;
    height: 100px;
    width: 100%;
    max-width: 900px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: clamp(13px, 1.8vw, 15px);
    line-height: 1.7;
    opacity: 0.95;
}

.info-msg {
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    animation: cycleInfo 6s infinite ease-in-out;
    width: 100%;
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

/* --- スマホ縦長画面用スタイル (9:16 / 9:21 などの縦長端末) --- */
@media (max-aspect-ratio: 1/1) {
    .bsod-container {
        justify-content: flex-start;
        padding: 12vh 7vw 5vh 7vw;
    }
    .bsod-sad-face {
        margin-bottom: 20px;
    }
    .main-wrapper {
        height: 140px; /* 改行考慮で少し高さを確保 */
        margin-bottom: 30px;
    }
    .info-wrapper {
        height: 120px;
    }
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

# 処理を完全停止
str_lit.stop()

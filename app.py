import streamlit as str_lit

# ページ設定
str_lit.set_page_config(page_title=":( Your PC ran into a problem", layout="wide", page_icon="🟦")

# --- 純粋BSOD画面 & 3言語2秒切替アニメーション ---
str_lit.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600&display=swap');

/* 全面をWin10 BSODカラーに固定＆スクロール禁止 */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0078d7 !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
    overflow: hidden !important;
}

/* ヘッダー・サイドバー等を非表示 */
header, footer, [data-testid="stSidebar"], [data-testid="stHeader"] {
    display: none !important;
}

/* BSODコンテナ */
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
    padding: 10% 12%;
    box-sizing: border-box;
    color: #ffffff;
}

/* BSOD顔文字 */
.bsod-sad-face {
    font-size: 120px;
    font-weight: 300;
    line-height: 1.0;
    margin-bottom: 25px;
    user-select: none;
}

/* メッセージ表示エリア (3言語切り替え) */
.message-wrapper {
    position: relative;
    height: 110px;
    width: 100%;
    max-width: 850px;
    margin-bottom: 20px;
}

.lang-msg {
    position: absolute;
    top: 0;
    left: 0;
    font-size: 26px;
    font-weight: 300;
    line-height: 1.4;
    opacity: 0;
    animation: cycleLang 6s infinite ease-in-out;
}

/* 2秒間隔（全体6秒サイクル）のタイマー設定 */
.lang-ja { animation-delay: 0s; }
.lang-en { animation-delay: 2s; }
.lang-ko { animation-delay: 4s; }

@keyframes cycleLang {
    0% { opacity: 0; transform: translateY(4px); }
    5% { opacity: 1; transform: translateY(0); }
    30% { opacity: 1; transform: translateY(0); }
    35% { opacity: 0; transform: translateY(-4px); }
    100% { opacity: 0; }
}

/* STOPコード */
.bsod-code-box {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 14px;
    opacity: 0.95;
    line-height: 1.6;
    margin-top: 10px;
}
</style>

<div class="bsod-container">
    <div class="bsod-sad-face">:(</div>
    
    <div class="message-wrapper">
        <!-- 日本語 (0s ~ 2s) -->
        <div class="lang-msg lang-ja">
            致命的なエラーが発生したため、システムはお使いになれません。<br>
            エラー情報を収集しています。自動的に再起動はされません。
        </div>
        <!-- 英語 (2s ~ 4s) -->
        <div class="lang-msg lang-en">
            A critical error has occurred. The system is currently unavailable.<br>
            We're collecting error info, but the system will not restart automatically.
        </div>
        <!-- 韓国語 (4s ~ 6s) -->
        <div class="lang-msg lang-ko">
            치명적인 오류가 발생하여 시스템을 사용할 수 없습니다.<br>
            오류 정보를 수집하고 있으며, 자동으로 다시 시작되지 않습니다.
        </div>
    </div>

    <div class="bsod-code-box">
        Stop code: CRITICAL_SYSTEM_ERROR_DISABLED<br>
        What failed: bento_system.sys
    </div>
</div>
""", unsafe_allow_html=True)

# 処理を完全停止
str_lit.stop()

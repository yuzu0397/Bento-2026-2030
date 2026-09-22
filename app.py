import streamlit as str_lit

# ページ設定
str_lit.set_page_config(page_title=":( Your PC ran into a problem", layout="wide", page_icon="🟦")

# --- 純粋BSOD画面 & 5言語5秒切替アニメーション ---
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
    padding: 10% 12%;
    box-sizing: border-box;
    color: #ffffff;
}

.bsod-sad-face {
    font-size: 120px;
    font-weight: 300;
    line-height: 1.0;
    margin-bottom: 25px;
    user-select: none;
}

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
    animation: cycleLang 25s infinite ease-in-out;
}

/* 5秒間隔（全体25秒サイクル）のアニメーション設定 */
.lang-ja { animation-delay: 0s; }
.lang-en { animation-delay: 5s; }
.lang-ko { animation-delay: 10s; }
.lang-zh { animation-delay: 15s; }
.lang-ru { animation-delay: 20s; }

@keyframes cycleLang {
    0% { opacity: 0; transform: translateY(4px); }
    1.5% { opacity: 1; transform: translateY(0); }
    18.5% { opacity: 1; transform: translateY(0); }
    20% { opacity: 0; transform: translateY(-4px); }
    100% { opacity: 0; }
}

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
<div class="lang-msg lang-ja">致命的なエラーが発生したため、システムはお使いになれません。<br>エラー情報を収集しています。自動的に再起動はされません。</div>
<div class="lang-msg lang-en">A critical error has occurred. The system is currently unavailable.<br>We're collecting error info, but the system will not restart automatically.</div>
<div class="lang-msg lang-ko">치명적인 오류가 발생하여 시스템을 사용할 수 없습니다.<br>오류 정보를 수집하고 있으며, 자동으로 다시 시작되지 않습니다.</div>
<div class="lang-msg lang-zh">发生致命错误，系统目前无法使用。<br>正在收集错误信息，系统不会自动重新启动。</div>
<div class="lang-msg lang-ru">Произошла критическая ошибка. Система недоступна.<br>Идет сбор информации об ошибке. Автоматическая перезагрузка не выполняется.</div>
</div>
<div class="bsod-code-box">Stop code: CRITICAL_SYSTEM_ERROR_DISABLED<br>What failed: bento_system.sys</div>
</div>
"""

str_lit.markdown(bsod_html, unsafe_allow_html=True)

# 処理を完全停止
str_lit.stop()

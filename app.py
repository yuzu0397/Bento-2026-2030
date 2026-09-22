import streamlit as str_lit

# ページ設定（BSODタイトルとアイコン）
str_lit.set_page_config(page_title=":( System Error - お使いになれません", layout="wide", page_icon="🟦")

# --- 全面エラー画面のCSS (Win10 BSOD + XPクラシックエラー融合) ---
str_lit.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600;700&display=swap');

/* 全面をWin10 BSODのブルーに固定してスクロールを不可に */
html, body, [data-testid="stAppViewContainer"] {
    background-color: #0078d7 !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif !important;
    overflow: hidden !important;
}

/* Streamlitのデフォルトヘッダー・フッター・サイドバーを完全に消去 */
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
    padding: 8% 12%;
    box-sizing: border-box;
}

/* Win10風 巨大スマイリー */
.bsod-sad-face {
    font-size: 110px;
    font-weight: 300;
    line-height: 1.0;
    margin-bottom: 20px;
    user-select: none;
}

/* Win10風 エラータイトル */
.bsod-title {
    font-size: 28px;
    font-weight: 400;
    margin-bottom: 20px;
    line-height: 1.4;
}

/* Windows XP風 クラシックエラーダイアログ */
.xp-error-dialog {
    background: #ece9d8;
    border: 3px solid #0055ea;
    border-radius: 7px 7px 0 0;
    color: #000000 !important;
    width: 100%;
    max-width: 620px;
    box-shadow: 6px 6px 18px rgba(0,0,0,0.4);
    margin-top: 15px;
    margin-bottom: 25px;
    font-family: 'Tahoma', 'Segoe UI', sans-serif;
}

.xp-dialog-header {
    background: linear-gradient(to right, #0058ee, #3593ff);
    color: #ffffff !important;
    padding: 5px 10px;
    font-weight: bold;
    font-size: 13px;
    display: flex;
    align-items: center;
    border-radius: 4px 4px 0 0;
}

.xp-dialog-body {
    padding: 20px;
    color: #000000 !important;
    background: #ece9d8;
    display: flex;
    align-items: center;
    gap: 15px;
}

.xp-icon {
    font-size: 24px;
    color: white;
    background: #e74c3c;
    border-radius: 50%;
    width: 40px;
    height: 40px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-weight: bold;
    flex-shrink: 0;
}

.xp-text {
    color: #000000 !important;
    font-size: 14px;
    line-height: 1.5;
}

.xp-text strong {
    color: #cc0000 !important;
}

/* XP風 16進数STOPコード */
.xp-stop-code {
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 14px;
    background: rgba(0, 0, 0, 0.25);
    padding: 15px 20px;
    border-left: 5px solid #ff4b4b;
    width: 100%;
    max-width: 620px;
    box-sizing: border-box;
    line-height: 1.6;
}
</style>

<div class="bsod-container">
    <!-- Win10要素: 顔文字と大テキスト -->
    <div class="bsod-sad-face">:(</div>
    <div class="bsod-title">
        問題が発生したため、このシステムはお使いになれません。<br>
        エラー情報を収集しています。自動的に再起動はされません。
    </div>

    <!-- WinXP要素: クラシックエラーダイアログ -->
    <div class="xp-error-dialog">
        <div class="xp-dialog-header">
            🛑 システムエラー - 致命的な例外
        </div>
        <div class="xp-dialog-body">
            <div class="xp-icon">✕</div>
            <div class="xp-text">
                <strong>[SYSTEM_DISABLED_ERROR]</strong><br>
                このアプリケーションは現在<strong>お使いになれません</strong>。<br>
                必要なシステムファイルが存在しないか、アクセス権限が拒否されました。<br>
                管理者にお問い合わせの上、システムを再構築してください。
            </div>
        </div>
    </div>

    <!-- WinXP風 STOPコード (ブルースクリーン16進数表記) -->
    <div class="xp-stop-code">
        停止コード: SYSTEM_LICENSE_VIOLATION_OR_NOT_AVAILABLE<br>
        失敗した内容: bento_system_v2.8.exe<br>
        *** STOP: 0x0000007B (0xF78D2524, 0xC0000034, 0x00000000, 0x00000000)
    </div>
</div>
""", unsafe_allow_html=True)

# 完全に処理を停止（これ以降のコードは実行されない）
str_lit.stop()

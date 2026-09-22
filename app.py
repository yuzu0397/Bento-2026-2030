import streamlit as str_lit

# ページ設定
str_lit.set_page_config(
    page_title="Windows - Fatal System Error",
    layout="wide",
    page_icon="⛔",
    initial_sidebar_state="collapsed",
)

# --- 完全ロックダウン CSS & HTML (Windows XP BSOD + XP Critical Error Dialog) ---
str_lit.markdown(
    """
<style>
@import url('https://fonts.googleapis.com/css2?family=Tahoma:wght@400;700&display=swap');

/* Streamlit標準 UI を完全に非表示化 */
[data-testid="stHeader"], [data-testid="stSidebar"], footer {
    display: none !important;
}

/* Windows XP BSOD 背景 */
html, body, .stApp {
    background-color: #000082 !important;
    color: #ffffff !important;
    font-family: 'Courier New', Monospace !important;
    margin: 0;
    padding: 0;
    overflow: hidden !important;
}

.bsod-container {
    padding: 40px;
    font-size: 18px;
    line-height: 1.5;
    color: #ffffff;
}

.bsod-title {
    background-color: #00aaaa;
    color: #000082;
    display: inline-block;
    padding: 2px 10px;
    font-weight: bold;
    margin-bottom: 20px;
}

/* XP エラーダイアログ (画面中央に固定) */
.xp-dialog-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.4);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 999999;
    font-family: 'Tahoma', 'Segoe UI', sans-serif !important;
}

.xp-dialog {
    width: 460px;
    background-color: #ece9d8;
    border: 3px solid #0055ea;
    border-radius: 5px 5px 0 0;
    box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.7);
    color: #000000 !important;
}

.xp-header {
    background: linear-gradient(to right, #0058ee 0%, #3593ff 4%, #288eff 6%, #0055ea 10%, #0055ea 90%, #0046d5 100%);
    color: #ffffff !important;
    font-weight: bold;
    font-size: 13px;
    padding: 5px 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    border-top-left-radius: 3px;
    border-top-right-radius: 3px;
}

.xp-close-btn {
    background: linear-gradient(to bottom, #e1654c, #c03319);
    border: 1px solid #ffffff;
    color: white !important;
    width: 18px;
    height: 18px;
    font-size: 11px;
    line-height: 14px;
    text-align: center;
    font-weight: bold;
    border-radius: 3px;
    box-shadow: inset 1px 1px 0 rgba(255,255,255,0.5);
    cursor: not-allowed;
}

.xp-body {
    padding: 25px 20px;
    display: flex;
    align-items: flex-start;
    gap: 18px;
    background-color: #ece9d8;
}

.xp-icon {
    font-size: 40px;
    line-height: 1;
    user-select: none;
}

.xp-message {
    font-size: 12px;
    color: #000000 !important;
    line-height: 1.6;
}

.xp-footer {
    background-color: #ece9d8;
    padding: 10px 15px 15px 15px;
    text-align: center;
    display: flex;
    justify-content: center;
    gap: 12px;
}

.xp-button {
    background: linear-gradient(to bottom, #ffffff 0%, #ece9d8 100%);
    border: 1px solid #003c74;
    border-radius: 3px;
    padding: 5px 25px;
    font-size: 12px;
    color: #000000 !important;
    box-shadow: inset 0 0 2px #ffffff;
    cursor: not-allowed;
    font-family: 'Tahoma', sans-serif;
    font-weight: bold;
}

.xp-button:hover {
    border-color: #e59700;
    box-shadow: 0 0 3px #e59700;
}
</style>

<div class="bsod-container">
    <div class="bsod-title">Windows</div><br><br>
    A problem has been detected and Windows has been shut down to prevent damage
    to your system.<br><br>
    LICENSE_VIOLATION_PAYMENT_REQUIRED<br><br>
    If this is the first time you've seen this Stop error screen,
    restart your computer. If this screen appears again, follow
    these steps:<br><br>
    Check to make sure your system license is valid and active.
    If a license renewal is required, ask your administrator or pay the required fee.<br><br>
    Technical information:<br><br>
    *** STOP: 0x000000EB (0x00000004, 0x00000000, 0x00000000, 0x00000000)<br><br>
    *** bento_system.sys - Address F86B5A89 base at F86B5000, DateStamp 3d6dd67c
</div>

<div class="xp-dialog-overlay">
    <div class="xp-dialog">
        <div class="xp-header">
            <span>Windows - システムセキュリティ警告</span>
            <div class="xp-close-btn">✕</div>
        </div>
        <div class="xp-body">
            <div class="xp-icon">❌</div>
            <div class="xp-message">
                <b>【重要】ライセンス有効期限切れエラー</b><br><br>
                BENTO System v2.8 の利用期限が終了しました。<br>
                システムロックを解除するには、至急ライセンス料金をお支払いください。<br><br>
                エラーコード: 0x000000EB (PAYMENT_REQUIRED)
            </div>
        </div>
        <div class="xp-footer">
            <button class="xp-button">お支払い画面へ</button>
            <button class="xp-button">キャンセル</button>
        </div>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

# ここでスクリプトの実行を完全停止（これより下の処理は一切動かない）
str_lit.stop()

import base64
import os
import streamlit as str_lit

# ページ設定
str_lit.set_page_config(
    page_title=":( System Error - 000xWinKL", layout="wide", page_icon="🟦"
)


# QRコード画像のbase64化（画像が見つからない場合はダミー枠を表示）
def get_qr_base64(file_path):
  if os.path.exists(file_path):
    with open(file_path, "rb") as f:
      return f"data:image/jpeg;base64,{base64.b64encode(f.read()).decode('utf-8')}"
  return ""


qr_img_data = get_qr_base64("QR.jpg")

# --- BSOD画面 HTML/CSS ---
bsod_html = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600&display=swap');

html, body, [data-testid="stAppViewContainer"] {{
    background-color: #0078d7 !important;
    color: #ffffff !important;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
    overflow: hidden !important;
}}

header, footer, [data-testid="stSidebar"], [data-testid="stHeader"] {{
    display: none !important;
}}

.bsod-container {{
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
    padding: 6% 10%;
    box-sizing: border-box;
    color: #ffffff;
}}

.bsod-sad-face {{
    font-size: 100px;
    font-weight: 300;
    line-height: 1.0;
    margin-bottom: 20px;
    user-select: none;
}}

/* --- メインエラー文章（5秒周期） --- */
.main-wrapper {{
    position: relative;
    height: 80px;
    width: 100%;
    max-width: 850px;
    margin-bottom: 20px;
}}

.main-msg {{
    position: absolute;
    top: 0;
    left: 0;
    font-size: 24px;
    font-weight: 300;
    line-height: 1.4;
    opacity: 0;
    animation: cycleMain 10s infinite ease-in-out;
}}

.main-ja {{ animation-delay: 0s; }}
.main-en {{ animation-delay: 5s; }}

@keyframes cycleMain {{
    0% {{ opacity: 0; transform: translateY(3px); }}
    3% {{ opacity: 1; transform: translateY(0); }}
    40% {{ opacity: 1; transform: translateY(0); }}
    45% {{ opacity: 0; transform: translateY(-3px); }}
    100% {{ opacity: 0; }}
}}

/* --- OS情報・エラーコード（3秒周期） --- */
.info-wrapper {{
    position: relative;
    height: 85px;
    width: 100%;
    max-width: 850px;
    font-family: 'Consolas', 'Courier New', monospace;
    font-size: 14px;
    line-height: 1.6;
    opacity: 0.95;
    margin-bottom: 25px;
}}

.info-msg {{
    position: absolute;
    top: 0;
    left: 0;
    opacity: 0;
    animation: cycleInfo 6s infinite ease-in-out;
}}

.info-ja {{ animation-delay: 0s; }}
.info-en {{ animation-delay: 3s; }}

@keyframes cycleInfo {{
    0% {{ opacity: 0; transform: translateY(2px); }}
    5% {{ opacity: 1; transform: translateY(0); }}
    43% {{ opacity: 1; transform: translateY(0); }}
    48% {{ opacity: 0; transform: translateY(-2px); }}
    100% {{ opacity: 0; }}
}}

/* --- QRコード & 赤チェック & スキャン案内エリア --- */
.qr-section {{
    display: flex;
    align-items: center;
    gap: 20px;
}}

.qr-box {{
    position: relative;
    width: 110px;
    height: 110px;
    background: #ffffff;
    padding: 6px;
    border-radius: 4px;
    box-sizing: border-box;
    display: flex;
    align-items: center;
    justify-content: center;
}}

.qr-img {{
    width: 100%;
    height: 100%;
    object-fit: contain;
}}

/* QR画像がない場合の代替枠 */
.qr-fallback {{
    color: #000;
    font-size: 11px;
    text-align: center;
    font-weight: bold;
}}

/* 赤いチェックマーク */
.red-check {{
    position: absolute;
    top: -10px;
    right: -10px;
    background: #ff2a2a;
    color: #ffffff;
    font-size: 16px;
    font-weight: bold;
    width: 28px;
    height: 28px;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 2px solid #ffffff;
    box-shadow: 0 2px 5px rgba(0,0,0,0.3);
}}

/* スキャンテキストエリア (2秒周期切替) */
.scan-wrapper {{
    position: relative;
    height: 40px;
    width: 300px;
    display: flex;
    align-items: center;
}}

.scan-msg {{
    position: absolute;
    left: 0;
    font-size: 20px;
    font-weight: 400;
    display: flex;
    align-items: center;
    gap: 10px;
    opacity: 0;
    animation: cycleScan 4s infinite ease-in-out;
}}

.scan-ja {{ animation-delay: 0s; }}
.scan-en {{ animation-delay: 2s; }}

@keyframes cycleScan {{
    0% {{ opacity: 0; transform: translateX(-5px); }}
    8% {{ opacity: 1; transform: translateX(0); }}
    42% {{ opacity: 1; transform: translateX(0); }}
    50% {{ opacity: 0; transform: translateX(5px); }}
    100% {{ opacity: 0; }}
}}
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

<div class="qr-section">
<div class="qr-box">
<div class="red-check">✓</div>
{"<img src='" + qr_img_data + "' class='qr-img' alt='QR'>" if qr_img_data else "<div class='qr-fallback'>QR.jpg<br>Not Found</div>"}
</div>
<div class="scan-wrapper">
<div class="scan-msg scan-ja">➡ スキャンしてください</div>
<div class="scan-msg scan-en">➡ Please scan</div>
</div>
</div>

</div>
"""

str_lit.markdown(bsod_html, unsafe_allow_html=True)

# 処理を完全停止
str_lit.stop()

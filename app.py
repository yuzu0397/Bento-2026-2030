import streamlit as str_lit
import psutil
import time
import base64
import os

# ページ設定
str_lit.set_page_config(
    page_title="BENTO System - Development Suspended", 
    layout="wide", 
    page_icon="🚫",
    initial_sidebar_state="collapsed"
)

# --- 状態管理の初期化 ---
if "authenticated" not in str_lit.session_state:
    str_lit.session_state.authenticated = False

if "booted" not in str_lit.session_state:
    str_lit.session_state.booted = False

if "page" not in str_lit.session_state:
    str_lit.session_state.page = "selection"

if "selected_bentos" not in str_lit.session_state:
    str_lit.session_state.selected_bentos = []

# --- 画像をBase64に変換する関数 ---
def get_base64_image(image_path):
    try:
        with open(image_path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode()
    except Exception as e:
        return ""

sony_img_base64 = get_base64_image("Sony.jpg")

# --- CSSスタイル設定（BSoDフルスクリーン対応） ---
str_lit.markdown("""
<style>
/* Streamlit標準UI要素を隠す */
header, footer, [data-testid="stHeader"], [data-testid="stSidebar"] {
    display: none !important;
}

.stApp {
    background-color: #0078d7 !important; /* Windows BSoD Blue */
    color: #ffffff !important;
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
    margin: 0 !important;
    padding: 0 !important;
}

.bsod-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #0078d7;
    color: #ffffff;
    z-index: 9999999;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding: 8% 10%;
    box-sizing: border-box;
    user-select: none;
}

.bsod-emoticon {
    font-size: 100px;
    font-weight: 300;
    margin-bottom: 20px;
    line-height: 1.0;
}

.bsod-message {
    font-size: 28px;
    font-weight: 400;
    line-height: 1.4;
    margin-bottom: 40px;
    max-width: 900px;
}

.bsod-details {
    margin-top: 20px;
    font-size: 14px;
    line-height: 1.6;
    color: #e0e0e0;
}

.bsod-code {
    font-family: 'Consolas', 'Courier New', monospace;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# --- BSoD 開発中止画面の描画 ---
str_lit.markdown("""
<div class="bsod-container">
    <div class="bsod-emoticon">:(</div>
    <div class="bsod-message">
        Development has been cancelled or suspended due to various circumstances.
    </div>
    <div class="bsod-details">
        Your system encountered a permanent halt condition and system deployment was discontinued.<br><br>
        Stop Code: <span class="bsod-code">DEVELOPMENT_HALTED_BY_ADMIN</span><br>
        Error Code: <span class="bsod-code">0x000000ef (CRITICAL_PROCESS_TERMINATED)</span><br>
        Module: <span class="bsod-code">bento_system_v2.8.exe</span><br>
        Timestamp: <span class="bsod-code">2026-08-30 12:22:10 UTC</span>
    </div>
</div>
""", unsafe_allow_html=True)

# システム全体の処理をここで完全停止
str_lit.stop()
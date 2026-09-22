import streamlit as str_lit
import psutil
import time
import base64
import os

# ページ設定（BSOD風タイトルとアイコン）
str_lit.set_page_config(page_title=":( Your System Ran Into a Problem", layout="wide", page_icon="🟦")

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

# --- CSSスタイル設定 (Windows 10 BSOD Theme) ---
str_lit.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Segoe+UI:wght@300;400;600;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    font-family: 'Segoe UI', -apple-system, BlinkMacSystemFont, Roboto, sans-serif !important;
}

.stApp {
    background-color: #0078d7 !important;
    color: #ffffff !important;
}

[data-testid="stSidebar"] {
    background-color: #005a9e !important;
}

h1, h2, h3, h4, h5, h6, p, span, label, div {
    color: #ffffff !important;
    font-family: 'Segoe UI', sans-serif !important;
    text-shadow: none !important;
}

/* 巨大なBSOD顔文字 */
.bsod-sad-face {
    font-size: 110px;
    font-weight: 300;
    line-height: 1.0;
    margin-bottom: 20px;
    user-select: none;
}

/* モーダル / ダイアログ */
div[data-baseweb="modal"], 
div[role="dialog"], 
section[tabindex="-1"] {
    background-color: rgba(0, 90, 158, 0.95) !important;
    backdrop-filter: blur(5px) !important;
}

div[data-baseweb="modal"] > div, 
div[role="dialog"] > div {
    background-color: #0078d7 !important;
    border: 3px solid #ffffff !important;
    border-radius: 0px !important;
    color: #ffffff !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.5) !important;
}

div[data-baseweb="modal"] * , 
div[role="dialog"] * {
    color: #ffffff !important;
}

/* ボタン (BSODフラットスタイル) */
.stButton > button {
    background-color: rgba(255, 255, 255, 0.15) !important;
    border: 2px solid #ffffff !important;
    border-radius: 0px !important;
    color: #ffffff !important;
    font-weight: 600 !important;
    transition: all 0.15s ease !important;
    box-shadow: none !important;
}

.stButton > button:hover {
    background-color: #ffffff !important;
    color: #0078d7 !important;
    border-color: #ffffff !important;
}

.stButton > button:hover * {
    color: #0078d7 !important;
}

.stButton > button:active {
    background-color: #e5e5e5 !important;
    color: #0078d7 !important;
}

/* 入力フォーム */
input {
    background-color: rgba(255, 255, 255, 0.2) !important;
    color: #ffffff !important;
    border: 1px solid #ffffff !important;
    border-radius: 0px !important;
}

input:focus {
    border-color: #ffffff !important;
    background-color: rgba(255, 255, 255, 0.3) !important;
}

/* 3DカードをBSODのフラットタイル風に改修 */
.bento-3d-card {
    background: rgba(255, 255, 255, 0.1);
    border: 2px solid rgba(255, 255, 255, 0.4);
    padding: 12px;
    text-align: center;
    margin-bottom: 8px;
    height: 130px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    transition: all 0.2s ease;
}

.bento-3d-card:hover {
    background: rgba(255, 255, 255, 0.25);
    border-color: #ffffff;
    transform: translateY(-2px);
}

.bsod-code-box {
    font-family: 'Consolas', 'Courier New', monospace !important;
    font-size: 13px;
    line-height: 1.6;
    margin-top: 15px;
    opacity: 0.9;
}

@media print {
    @page {
        size: A4 landscape;
        margin: 2mm;
    }
    body, .stApp {
        background: #ffffff !important;
        color: #000000 !important;
        zoom: 0.8;
    }
    [data-testid="stSidebar"], 
    button, 
    .no-print,
    .stButton,
    .bsod-sad-face {
        display: none !important;
    }
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #000000 !important;
    }
    .print-container {
        font-size: 8px !important;
        line-height: 1.0 !important;
    }
}

.boot-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: #0078d7;
    z-index: 999999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    overflow: hidden;
}

.sony-logo {
    width: 450px !important;
    max-width: 70vw !important;
    height: auto !important;
    filter: brightness(0) invert(1);
    animation: bsodFade 2.6s ease forwards;
}

@keyframes bsodFade {
    0% { opacity: 0; transform: scale(0.95); }
    20% { opacity: 1; transform: scale(1); }
    80% { opacity: 1; transform: scale(1); }
    100% { opacity: 0; transform: scale(1.05); }
}

.error-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: #0078d7;
    z-index: 9999999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 40px;
}

.error-box {
    border: 3px solid #ffffff;
    padding: 35px 45px;
    max-width: 680px;
    width: 100%;
    background: rgba(0, 0, 0, 0.1);
}
</style>
""", unsafe_allow_html=True)

# --- パスワード認証画面 (BSODエラー風) ---
if not str_lit.session_state.authenticated:
    _, center_col, _ = str_lit.columns([1, 2, 1])
    with center_col:
        str_lit.markdown("<div class='bsod-sad-face'>:(</div>", unsafe_allow_html=True)
        str_lit.markdown("## Your BENTO System ran into a problem and needs to authenticate.")
        str_lit.markdown("We're just collecting some security info, and then you can proceed.")
        str_lit.markdown("<br>", unsafe_allow_html=True)
        
        pwd = str_lit.text_input("Enter 4-digit PIN code to restart system:", type="password")
        
        if str_lit.button("Restart & Login", use_container_width=True):
            if pwd == "0531":
                status_placeholder = str_lit.empty()
                progress_bar = str_lit.progress(0)
                
                status_placeholder.text("0% complete : Connecting to host server...")
                time.sleep(1.5)
                progress_bar.progress(20)
                
                status_placeholder.text("20% complete : Initializing system credentials...")
                time.sleep(1.2)
                progress_bar.progress(47)

                status_placeholder.text("47% complete : Verifying TP01 development environment...")
                time.sleep(1.3)
                progress_bar.progress(76)
                
                status_placeholder.text("76% complete : Executing kernel dump & memory check...")
                time.sleep(1.0)
                progress_bar.progress(100)
                
                status_placeholder.text("100% complete : Authentication succeeded. System restarting...")
                time.sleep(0.8)
                
                status_placeholder.empty()
                progress_bar.empty()
                
                str_lit.session_state.authenticated = True
                str_lit.rerun()
            else:
                contact_email = "yuzukyoto0811@gmail." + "com"
                str_lit.error(f"Stop code: SYSTEM_THREAD_EXCEPTION_NOT_HANDLED\nContact Administrator: {contact_email}")
    str_lit.stop()

# --- スペック・環境情報の取得と必須比較 ---
MIN_RAM_GB = 4.0
MIN_CPU_CORES = 4
MIN_CPU_FREQ_GHZ = 2.2

try:
    cpu_cores = psutil.cpu_count(logical=False) or psutil.cpu_count(logical=True)
    total_ram_gb = round(psutil.virtual_memory().total / (1024 ** 3), 1)
    max_cpu_freq_ghz = round(psutil.cpu_freq().max / 1000, 2) if psutil.cpu_freq() and psutil.cpu_freq().max > 0 else 2.5
except Exception:
    cpu_cores, total_ram_gb, max_cpu_freq_ghz = 4, 4.0, 2.2

is_ram_ok = total_ram_gb >= MIN_RAM_GB
is_cpu_ok = (cpu_cores >= MIN_CPU_CORES and max_cpu_freq_ghz >= MIN_CPU_FREQ_GHZ)

if not (is_ram_ok and is_cpu_ok):
    str_lit.markdown(f"""
    <div class="error-screen">
        <div class="bsod-sad-face">:(</div>
        <div class="error-box">
            <h2 style="margin-top: 0; font-size: 24px;">YOUR PC RAN INTO A PROBLEM AND NEEDS TO RESTART.</h2>
            <p style="font-size: 15px; margin-bottom: 20px;">
                Stop code: HARDWARE_SPEC_UNSUPPORTED<br>
                What failed: bento_system.sys<br><br>
                Your device does not meet the minimum hardware requirements (RAM: {total_ram_gb}GB, CPU Cores: {cpu_cores}).
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    str_lit.stop()

# --- 起動画面（Sonyロゴ BSODスタイル：2.6秒） ---
if not str_lit.session_state.booted:
    boot_placeholder = str_lit.empty()
    boot_html = f'''
    <div class="boot-container">
        <div class="bsod-sad-face">:(</div>
        <img class="sony-logo" src="data:image/jpeg;base64,{sony_img_base64}" />
        <p style="margin-top: 20px; font-size: 18px;">System is recovering... Please wait.</p>
    </div>
    '''
    boot_placeholder.markdown(boot_html, unsafe_allow_html=True)
    time.sleep(2.6)
    str_lit.session_state.booted = True
    boot_placeholder.empty()
    str_lit.rerun()

# --- メニューデータ ---
bento_data = {
    "周山御膳": {"items": {"マリネ": 1, "サーモン": 1, "ホタテ": 1, "プチトマト": 1, "オムレツ": 1, "有頭エビフライ": 1, "白身フライ": 2, "パスタ(g)": 7, "ポテトフライ": 3, "牛しゃぶ(g)": 60, "グリル野菜": 1, "ブロッコリー": 2, "鮭フレーク": 1, "豆": 5, "ごはん(g)": 190}},
    "会席膳 八坂": {"items": {"ステーキ": 4, "グリル野菜": 1, "キャベツ": 1, "ゴマ豆腐": 1, "だし巻き": 2, "紅かまぼこ": 3, "海鮮春巻き": 1, "魚": 1, "里芋田楽": 1, "鳥梅ごぼう": 1, "なすはさみ揚げ": 1, "枝豆": 2, "天豆": 1, "じゃばら": 2, "カニテリーヌ": 2, "花レンコン": 1, "錦糸巻き": 2, "がんも": 1, "彩り豆腐": 1, "タケノコ": 1, "かぼちゃ煮": 1, "ふき": 1, "紅葉麩": 1, "えびうま煮": 1, "茶碗蒸し": 1, "お吸い物": 1, "漬物": 1, "えび (26-30)": 1, "天ぷらナス": 1, "れんこん": 1, "オクラ": 1, "ハナイカ": 1, "大根けん": 1, "大葉": 2, "造りマグロ": 3, "お造り鯛": 2, "お造りイカ": 2, "ご飯(g)": 180, "ちりめん": 1}},
    "国産牛すきやきと国産牛ステーキ御膳": {"items": {"がんも": 1, "彩り豆腐": 1, "南京": 1, "タケノコ": 1, "ふき": 1, "もみじ麩": 1, "ステーキ": 4, "グリル野菜": 1, "だし巻き": 1, "魚": 1, "枝豆": 2, "さつまいも": 1, "カニテリーヌ": 1, "酢の物": 1, "牛すき焼き(g)": 50, "豆": 3, "ごはん(g)": 150}},
    "ボリューム唐揚げハンバーグ弁当": {"items": {"ハンバーグ": 1, "ウインナー": 2, "プチトマト": 1, "きゅうり": 2, "ポテトサラダ": 1, "唐揚げ": 3, "だし巻き": 1, "さつまいも": 1, "ナポリタン(g)": 9, "ごはん(g)": 190}},
    "和風 雅": {"items": {"ステーキ": 4, "グリル野菜": 1, "プチトマト": 1, "キャベツ": 1, "だし巻き": 1, "レモン煮": 1, "磯部揚げ": 1, "花レンコン": 1, "梅ごぼう": 1, "餅": 1, "鯛飾": 1, "錦糸卵": 1, "鯛身": 1, "がんも": 1, "彩豆腐": 1, "木の葉": 1, "タケノコ": 1, "ふき": 1, "紅葉麩": 1, "つや姫(g)": 150, "【カップ】 7寸ボルド": 2, "【カップ】 ブロンズ": 1, "【カップ】 黒久松4マス": 1}},
    "和風 なでしこ": {"items": {"だし巻き": 1, "紅かまぼこ": 2, "きゅうり酢の物小": 1, "ひじき小": 1, "レモン煮": 1, "魚": 1, "磯部揚げ": 1, "カニテリーヌ": 1, "餅": 1, "がんも": 1, "小芋": 1, "しいたけ": 1, "タケノコ": 1, "ふき": 1, "紅葉麩": 1, "牛しぐれ煮(g)": 50, "豆": 3, "白ご飯(g)": 150, "【カップ】 7寸ボルド": 2, "【カップ】 ブロンズ": 1, "【カップ】 7寸赤金": 1, "【カップ】 黒久松4マス": 1}},
    "天丼 えびす": {"items": {"ゴロゴロチキン": 1, "ブロッコリー": 1, "だし巻き": 1, "レモン煮": 1, "つくね串": 1, "きゅうり": 2, "鳥照り焼き": 1, "合鴨ロール": 1, "がんも": 1, "しいたけ": 1, "タケノコ": 1, "木の葉": 1, "ふき": 1, "紅葉麩": 1, "いなり": 2, "天ぷらエビ [31-40]": 1, "天ぷら大葉": 1, "天つゆご飯(g)": 80, "天ぷらキス": 1, "紅ショウガ": 1, "アスパラガス": 1, "【カップ】 七寸ナナメ": 1, "【カップ】 ブロンズ": 1, "【カップ】 黒久松4マス": 1}},
    "天丼 四季彩": {"items": {"ゴロゴロチキン": 1, "磯部上げ": 1, "ひじき小": 1, "だし巻き": 1, "レモン煮": 1, "パストラミ": 1, "きゅうり": 2, "トリテリーヌ": 1, "つくね串": 1, "がんも": 1, "小芋": 1, "しいたけ": 1, "タケノコ": 1, "ふき": 1, "紅葉麩": 1, "いなり": 2, "天ぷらエビ [31-40]": 1, "大葉": 1, "天ぷらナス": 1, "レンコン": 1, "天つゆご飯(g)": 80, "【カップ】 七寸ブロンズ": 1, "【カップ】 ナナメ": 2, "【カップ】 黒久松4マス": 1}},
    "鞍馬御膳": {"items": {"ハンバーグ": 1, "グリル野菜": 1, "だし巻き": 1, "レモン煮": 1, "魚": 1, "花レンコン": 1, "餅": 1, "ハナイカ": 1, "天豆": 1, "鯛飾": 1, "鯛身": 1, "がんも": 1, "彩り豆腐": 1, "かぼちゃ煮": 1, "タケノコ": 1, "ふき": 1, "紅葉麩": 1, "つや姫(g)": 150, "【カップ】 七寸ブロンズ": 1, "【カップ】 ボルド": 1, "【カップ】 黒久松4マス": 1}},
    "御所": {"items": {"焼きしゃぶ(g)": 60, "グリル野菜": 1, "プチトマト": 1, "キャベツ": 1, "だし巻き": 2, "れんこんハサミ": 1, "紅かまぼこ": 2, "トリテリーヌ": 1, "なすはさみ揚げ": 1, "カニテリーヌ": 2, "錦糸巻き": 2, "枝豆": 2, "タコ煮": 1, "和菓子": 1, "天豆": 1, "蟹甲羅": 1, "サワラ大": 1, "花レンコン": 1, "にんじん": 1, "小芋": 1, "ゴマ豆腐": 1, "生麩": 1, "つくね串": 1, "がんも": 1, "彩り豆腐": 1, "かぼちゃ煮": 1, "タケノコ": 1, "ふき": 1, "紅葉麩": 1, "天ぷら海老 [21-25]": 2, "天ぷらナス": 1, "れんこん": 1, "オクラ": 1, "天ぷらサツマイモ": 1, "ハナイカ": 1, "みかん半分": 1, "パイナップル(切れ)": 2, "寿司マグロ": 1, "寿司カンパチ": 1, "寿司サーモン": 1, "寿司イカ": 1, "寿司海老": 1, "ガリ": 1, "わさび": 1, "たまり醤油": 1, "お吸い物": 1, "茶碗蒸し": 1, "造りマグロ": 3, "お造り鯛": 3, "お造りイカ": 3, "有頭海老": 1, "大根けん": 1, "大葉": 2}},
    "天丼 華やぎ": {"items": {"豚しゃぶ(g)": 50, "刻み葱": 1, "プチトマト": 1, "だし巻き": 2, "しぐれ煮 小": 1, "豆": 2, "餅": 1, "がんも": 1, "小芋": 1, "しいたけ": 1, "タケノコ": 1, "ふき": 1, "紅葉麩": 1, "いなり": 2, "天ぷら大葉": 1, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天つゆご飯(g)": 80, "【カップ】 七寸ブロンズ": 2, "【カップ】 七寸ボルド": 1, "【カップ】 黒久松4マス": 1}},
    "天丼 誉": {"items": {"牛しゃぶ(g)": 30, "プチトマト": 1, "魚": 1, "花レンコン": 1, "だし巻き": 1, "レモン煮": 1, "パストラミ": 2, "トリテリーヌ": 1, "合鴨ロール": 1, "つくね串": 1, "がんも": 1, "しいたけ": 1, "にんじん": 1, "ふき": 1, "いなり": 3, "天ぷらエビ [31-40]": 1, "キス": 1, "紅かまぼこ": 1, "アスパラガス": 1, "天ぷらナス": 1, "天ぷらサツマイモ": 1, "れんこん": 1, "天つゆご飯(g)": 120, "【カップ】 七寸ナナメ": 2, "【カップ】 長方形七寸": 1, "【カップ】 黒久松4マス": 1}},
    "天丼 松": {"items": {"ステーキ": 3, "キャベツ": 1, "パプリカ": 1, "磯部上げ": 1, "トリテリーヌ": 1, "合鴨ロール": 1, "だし巻き": 1, "レモン煮": 1, "つくね串": 1, "魚": 1, "花レンコン": 1, "酢の物": 1, "がんも": 1, "しいたけ": 1, "彩豆腐": 1, "ふき": 1, "紅葉麩": 1, "いなり": 3, "天ぷら大葉": 1, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 11, "紅ショウガ": 1, "天ぷらサツマイモ": 1, "天ぷらレンコン": 1, "天ぷらナス": 1, "伯方の塩": 1, "【カップ】 黒久松4マス": 1, "【カップ】 7寸ナナメ": 2, "【カップ】 7寸長方形": 1}},
    "いなり A": {"items": {"ゴロゴロチキン": 3, "ブロッコリー": 1, "だし巻き": 1, "レモン煮": 1, "きゅうり": 2, "合鴨ロール": 1, "つくね串": 1, "トリテリーヌ": 1, "プチトマト": 1, "がんも": 1, "しいたけ": 1, "タケノコ": 1, "かぼちゃ煮": 1, "ふき": 1, "にんじん": 1, "いなり": 2, "大葉天ぷら": 1, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天つゆご飯(g)": 80, "【カップ】 七寸ボルド": 1, "【カップ】 ブロンズ": 1, "【カップ】 七寸ナナメ": 1, "【カップ】 黒久松4マス": 1}},
    "いなり天丼 B": {"items": {"ステーキ": 3, "キャベツ": 1, "合鴨ロール": 1, "トリテリーヌ": 1, "だし巻き": 1, "レモン煮": 1, "つくね串": 1, "ポテトサラダ": 1, "きゅうり": 2, "がんも": 1, "しいたけ": 1, "にんじん": 1, "ふき": 1, "いなり": 3, "天ぷら大葉": 1, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天ぷらナス": 1, "天ぷらサツマイモ": 1, "天ぷらレンコン": 1, "天つゆご飯(g)": 120, "【カップ】 七寸ナナメ": 2, "【カップ】 七寸長方形": 1, "【カップ】 黒久松4マス": 1}},
    "いなり天丼 C": {"items": {"牛しゃぶしゃぶ(g)": 30, "プチトマト": 1, "魚": 1, "花レンコン": 1, "だし巻き": 1, "レモン煮": 1, "パストラミ": 2, "トリテリーヌ": 1, "梅ごぼう": 1, "つくね串": 1, "がんも": 1, "しいたけ": 1, "にんじん": 1, "ふき": 1, "いなり": 3, "天ぷら大葉": 1, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天ぷらナス": 1, "天ぷらサツマイモ": 1, "天ぷられんこん": 1, "天つゆご飯(g)": 120, "【カップ】 七寸ナナメ": 2, "【カップ】 七寸長方形": 1, "【カップ】 黒久松4マス": 1}},
    "いなり天丼 E": {"items": {"すき焼き(g)": 60, "豆腐": 1, "にんじん": 1, "長ネギ": 2, "だし巻き": 1, "レモン煮": 1, "梅ごぼう": 1, "磯部揚げ": 1, "里芋田楽": 1, "切干小": 1, "ひじき小": 1, "いなり": 3, "天ぷら大葉": 1, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天ぷらナス": 1, "天ぷらレンコン": 1, "天ぷらサツマイモ": 1, "天つゆご飯(g)": 120, "【カップ】 七寸ブロンズ": 1, "【カップ】 七寸ナナメ": 1, "【カップ】 七寸長方形": 1, "【カップ】 黒久松4マス": 1}},
    "いなり天丼 P": {"items": {"ゴロゴロチキン": 2, "磯部揚げ": 1, "ひじき小": 1, "だし巻き": 1, "レモン煮": 1, "パストラミ": 2, "きゅうり": 2, "トリテリーヌ": 1, "鳥つくね串": 1, "がんも": 1, "小芋": 1, "タケノコ": 1, "かぼちゃ煮": 1, "ふき": 1, "にんじん": 1, "いなり": 2, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天つゆご飯(g)": 80, "【カップ】 七寸ナナメ": 2, "【カップ】 七寸ボルド": 1, "【カップ】 黒久松4マス": 1}},
    "いなり天丼 Q": {"items": {"唐揚げ": 2, "豚ひれ": 1, "ブロッコリー": 1, "だし巻き": 2, "しぐれ小": 1, "豆": 2, "餅": 1, "がんも": 1, "しいたけ": 1, "タケノコ": 1, "ふき": 1, "小芋": 1, "にんじん": 1, "いなり": 2, "天ぷらエビ [31-40]": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天つゆご飯(g)": 80, "【カップ】 七寸ナナメ": 1, "【カップ】 七寸ボルド": 1, "【カップ】 七寸ブロンズ": 1, "【カップ】 黒久松4マス": 1}},
    "いなり天丼 R": {"items": {"豚しゃぶ(g)": 50, "キャベツ": 1, "だし巻き": 2, "しぐれ小": 1, "豆": 2, "餅": 1, "がんも": 1, "しいたけ": 1, "タケノコ": 1, "小芋": 1, "ふき": 1, "にんじん": 1, "いなり": 2, "天ぷらエビ [31-40]": 1, "天ぷら大葉": 1, "キス": 1, "アスパラガス": 1, "紅ショウガ": 1, "天つゆご飯(g)": 80, "【カップ】 七寸ボルド": 2, "【カップ】 七寸ブロンズ": 1, "【カップ】 黒久松4マス": 1}}
}

# ==========================================
# 画面①：お弁当選択画面 (BSODテーマ)
# ==========================================
if str_lit.session_state.page == "selection":
    col1, col2 = str_lit.columns([1, 4])
    with col1:
        if os.path.exists("Kawase.jpg"):
            str_lit.image("Kawase.jpg", width=160)
        else:
            str_lit.markdown("<div class='bsod-sad-face' style='font-size:60px;'>:(</div>", unsafe_allow_html=True)
            
    with col2:
        str_lit.title("BENTO SYSTEM v2.8 BSOD")
        str_lit.markdown("""
        <div class="bsod-code-box">
            Stop code: BENTO_SYSTEM_SELECTION_REQUIRED<br>
            What failed: bento_data.dll
        </div>
        """, unsafe_allow_html=True)

    str_lit.markdown("---")
    str_lit.subheader("🍱 Select Bento & Set Quantity")

    menu_keys = list(bento_data.keys())
    cols_per_row = 4
    rows = [menu_keys[i:i + cols_per_row] for i in range(0, len(menu_keys), cols_per_row)]

    quantities = {}

    for row_items in rows:
        cols = str_lit.columns(len(row_items))
        for idx, bento_name in enumerate(row_items):
            with cols[idx]:
                is_selected = bento_name in str_lit.session_state.selected_bentos
                
                badge = "[ SELECTED ]" if is_selected else "[ UNSELECTED ]"
                bg_style = "background: rgba(255,255,255,0.3); border: 2px solid #ffffff;" if is_selected else "background: rgba(255,255,255,0.1); border: 1px solid rgba(255,255,255,0.4);"

                str_lit.markdown(f"""
                <div class="bento-3d-card" style="{bg_style}">
                    <div style="font-weight: bold; font-size: 13px; color: #ffffff; margin-bottom: 4px; line-height: 1.2;">{bento_name}</div>
                    <div style="font-size: 11px; color: #ffffff; font-family: monospace;">{badge}</div>
                </div>
                """, unsafe_allow_html=True)

                if is_selected:
                    current_qty = str_lit.session_state.get(f"qty_{bento_name}", 1)
                    quantities[bento_name] = str_lit.number_input(
                        f"【{bento_name}】個数", 
                        min_value=1, value=current_qty, step=1, 
                        key=f"qty_{bento_name}"
                    )
                
                btn_label = "Remove" if is_selected else "Select"
                if str_lit.button(btn_label, key=f"card_btn_{bento_name}", use_container_width=True):
                    if is_selected:
                        str_lit.session_state.selected_bentos.remove(bento_name)
                        str_lit.toast(f"Deselected: {bento_name}")
                    else:
                        str_lit.session_state.selected_bentos.append(bento_name)
                        str_lit.toast(f"Selected: {bento_name}")
                    str_lit.rerun()

    str_lit.markdown("---")

    if str_lit.session_state.selected_bentos:
        @str_lit.dialog("⚠️ SYSTEM DIAGNOSTIC")
        def confirm_selection():
            str_lit.write("Are you sure you want to compile and print total ingredients?")
            str_lit.markdown("### 📋 Current Selections:")
            for bento in str_lit.session_state.selected_bentos:
                qty = str_lit.session_state.get(f"qty_{bento}", 1)
                str_lit.write(f"- **{bento}**: {qty} pcs")
            
            str_lit.markdown("<br>", unsafe_allow_html=True)
            col_yes, col_no = str_lit.columns(2)
            with col_yes:
                if str_lit.button("Proceed", type="primary", use_container_width=True):
                    str_lit.session_state.page = "result"
                    str_lit.rerun()
            with col_no:
                if str_lit.button("Cancel", use_container_width=True):
                    str_lit.rerun()

        if str_lit.button("🔍 Execute Diagnostic & Calculate (Print View)", type="primary", use_container_width=True):
            confirm_selection()
    else:
        str_lit.warning("No Bento selected. Please select items from above.")

    # --- フッター表記 ---
    str_lit.markdown("<br><br><div style='text-align: center; color: #ffffff !important; font-size: 13px; font-family: monospace;'>Stop code: SUCCESS_2026_YUZUKI</div>", unsafe_allow_html=True)

# ==========================================
# 画面②：検索結果・印刷用ページ
# ==========================================
elif str_lit.session_state.page == "result":
    str_lit.title("📊 Ingredients Dump & Print Summary")
    str_lit.caption("お父さん用：ブラウザの印刷設定でレイアウトを【横】にして印刷してください。")
    
    str_lit.markdown("---")

    if str_lit.button("⬅️ Return to Selection Screen", use_container_width=True):
        str_lit.session_state.page = "selection"
        str_lit.rerun()

    str_lit.markdown("<br>", unsafe_allow_html=True)

    total_ingredients = {}
    for bento in str_lit.session_state.selected_bentos:
        qty = str_lit.session_state.get(f"qty_{bento}", 1)
        ingredients = bento_data[bento]["items"]
        for ing, count in ingredients.items():
            total_ingredients[ing] = total_ingredients.get(ing, 0) + (count * qty)

    str_lit.markdown('<div class="print-container">', unsafe_allow_html=True)
    
    if total_ingredients:
        items_list = list(total_ingredients.items())
        num_cols = 7
        cols = str_lit.columns(num_cols)
        
        for idx, (ing, total_count) in enumerate(items_list):
            if "(g)" in ing:
                unit = "g"
            elif "(切れ)" in ing:
                unit = "切れ"
            else:
                unit = "個"
            
            target_col = cols[idx % num_cols]
            with target_col:
                str_lit.write(f"・ **{ing}**: **{total_count}{unit}**")
    else:
        str_lit.warning("No data to aggregate.")

    str_lit.markdown('</div>', unsafe_allow_html=True)

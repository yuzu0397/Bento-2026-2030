import streamlit as str_lit
import psutil
import time
import base64
import os

# ページ設定
str_lit.set_page_config(page_title="BENTO System v2.8 3D", layout="wide", page_icon="🍱")

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

# --- CSSスタイル設定 ---
str_lit.markdown("""
<style>
.stApp {
    background: radial-gradient(circle at 50% 20%, #1a2332 0%, #0d1117 80%);
    color: #ffffff;
    animation: appFadeIn 1s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}

@keyframes appFadeIn {
    0% { opacity: 0; transform: scale(0.98); }
    100% { opacity: 1; transform: scale(1); }
}

[data-testid="stSidebar"] {
    background-color: #161b22;
}

h1, h2, h3, h4, h5, h6 {
    color: #79c0ff !important;
    font-weight: 700;
    text-shadow: 0 0 10px rgba(121, 192, 255, 0.3);
}

p, span, label, div {
    color: #f0f6fc !important;
}

div[data-baseweb="modal"], 
div[role="dialog"], 
section[tabindex="-1"] {
    background-color: rgba(13, 17, 23, 0.85) !important;
    backdrop-filter: blur(12px) !important;
}

div[data-baseweb="modal"] > div, 
div[role="dialog"] > div {
    background: linear-gradient(145deg, #1f242c, #161b22) !important;
    border: 2px solid #58a6ff !important;
    border-top: 8px solid #00d2ff !important;
    border-radius: 16px !important;
    color: #f0f6fc !important;
    box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8), 0 0 30px rgba(0, 210, 255, 0.2) !important;
    transform-style: preserve-3d;
    animation: modal3DPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards !important;
}

@keyframes modal3DPop {
    0% {
        opacity: 0;
        transform: perspective(1000px) rotateX(-20deg) scale(0.8) translateZ(-100px);
    }
    100% {
        opacity: 1;
        transform: perspective(1000px) rotateX(0deg) scale(1) translateZ(0px);
    }
}

div[data-baseweb="modal"] * , 
div[role="dialog"] * {
    color: #f0f6fc !important;
}

.stButton > button {
    background: linear-gradient(135deg, #21262d, #161b22) !important;
    border: 1px solid #30363d !important;
    border-radius: 10px !important;
    color: #f0f6fc !important;
    transition: all 0.25s cubic-bezier(0.175, 0.885, 0.32, 1.275) !important;
    transform: perspective(600px) translateZ(0px);
    box-shadow: 0 4px 10px rgba(0,0,0,0.4), inset 0 1px 0 rgba(255,255,255,0.1);
}

.stButton > button:hover {
    background: linear-gradient(135deg, #30363d, #21262d) !important;
    border-color: #58a6ff !important;
    transform: perspective(600px) translateZ(15px) translateY(-3px) rotateX(4deg) !important;
    box-shadow: 0 12px 25px rgba(0, 210, 255, 0.35) !important;
}

.stButton > button:active {
    transform: perspective(600px) translateZ(-8px) translateY(2px) rotateX(-2deg) !important;
    box-shadow: 0 2px 6px rgba(0, 210, 255, 0.2) !important;
}

.bento-3d-card {
    transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
    transform-style: preserve-3d;
    perspective: 800px;
}

.bento-3d-card:hover {
    transform: perspective(800px) rotateX(8deg) rotateY(-4deg) translateZ(12px) translateY(-5px);
}

.bento-icon-3d {
    animation: iconFloat 3s ease-in-out infinite alternate;
}

@keyframes iconFloat {
    0% { transform: translateY(0px) rotate(0deg); }
    100% { transform: translateY(-6px) rotate(5deg); }
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
        animation: none !important;
    }
    [data-testid="stSidebar"], 
    button, 
    .no-print,
    .stButton {
        display: none !important;
    }
    h1, h2, h3, h4, h5, h6, p, span, label, div {
        color: #000000 !important;
        text-shadow: none !important;
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
    background: radial-gradient(circle at center, #1a2333 0%, #080b10 100%);
    z-index: 999999;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    perspective: 1000px;
}

.sony-logo {
    width: 550px !important;
    max-width: 75vw !important;
    height: auto !important;
    object-fit: contain;
    transform-style: preserve-3d;
    animation: sonyDarkFadeOutEffect 2.6s cubic-bezier(0.2, 0.8, 0.2, 1) forwards;
}

@keyframes sonyDarkFadeOutEffect {
    0% {
        opacity: 0;
        filter: brightness(2.5) drop-shadow(0 0 50px rgba(0, 210, 255, 1));
        transform: perspective(1000px) rotateY(-180deg) rotateX(45deg) scale(0.1) translateZ(-800px);
    }
    25% {
        opacity: 1;
        filter: brightness(1.8) drop-shadow(0 0 30px rgba(0, 210, 255, 0.8));
        transform: perspective(1000px) rotateY(10deg) rotateX(-5deg) scale(1.1) translateZ(50px);
    }
    65% {
        opacity: 1;
        transform: perspective(1000px) rotateY(0deg) rotateX(0deg) scale(1) translateZ(0px);
        filter: brightness(1) drop-shadow(0 0 20px rgba(0, 210, 255, 0.5));
    }
    82% {
        opacity: 0.5;
        filter: brightness(0.4) drop-shadow(0 0 8px rgba(0, 210, 255, 0.2));
        transform: perspective(1000px) rotateX(10deg) scale(0.96) translateZ(-30px);
    }
    100% {
        opacity: 0;
        filter: brightness(0) drop-shadow(0 0 0px rgba(0, 0, 0, 0));
        transform: perspective(1000px) rotateX(20deg) scale(0.9) translateZ(-150px);
    }
}

.error-screen {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background-color: rgba(13, 17, 23, 0.95);
    backdrop-filter: blur(8px);
    z-index: 9999999;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 20px;
}

.error-box {
    background: linear-gradient(145deg, #1f242c, #161b22);
    border: 2px solid #ff7b72;
    border-top: 10px solid #ff7b72;
    padding: 35px 45px;
    border-radius: 16px;
    box-shadow: 0 20px 50px rgba(255, 123, 114, 0.3);
    max-width: 620px;
    width: 100%;
    text-align: center;
    animation: modal3DPop 0.4s ease-out;
}
</style>
""", unsafe_allow_html=True)

# --- パスワード認証認証画面 ---
if not str_lit.session_state.authenticated:
    _, center_col, _ = str_lit.columns([1, 2, 1])
    with center_col:
        str_lit.markdown("<br><br><br>", unsafe_allow_html=True)
        str_lit.subheader("🔒 システム認証")
        pwd = str_lit.text_input("パスワードを入力してください", type="password")
        if str_lit.button("ログイン", use_container_width=True):
            if pwd == "0531":
                status_placeholder = str_lit.empty()
                progress_bar = str_lit.progress(0)
                
                status_placeholder.text("サーバーに接続中...")
                time.sleep(0.4)
                progress_bar.progress(30)
                
                status_placeholder.text("認証ハンドシェイクを実行中...")
                time.sleep(0.5)
                progress_bar.progress(70)
                
                status_placeholder.text("セキュリティトークンを検証中...")
                time.sleep(0.4)
                progress_bar.progress(100)
                
                status_placeholder.text("認証成功。システムを起動します...")
                time.sleep(0.3)
                
                status_placeholder.empty()
                progress_bar.empty()
                
                str_lit.session_state.authenticated = True
                str_lit.rerun()
            else:
                str_lit.error("パスワードが違います")
    str_lit.stop()

# --- スペック・環境情報の取得と必須比較 ---
MIN_RAM_GB = 120
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
        <div class="error-box">
            <h2 style="color: #ff7b72 !important; margin-top: 0; font-size: 22px;">⚡ [ SYSTEM ERROR ] Insufficient System Specifications ⚡</h2>
            <p style="font-size: 14px; margin-bottom: 20px;">Your device does not meet the minimum requirements for Bento Management System v2.8.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    str_lit.stop()

# --- 起動画面（Sonyロゴ 3D演出：2.6秒） ---
if not str_lit.session_state.booted:
    boot_placeholder = str_lit.empty()
    boot_html = f'''
    <div class="boot-container">
        <img class="sony-logo" src="data:image/jpeg;base64,{sony_img_base64}" />
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
# 画面①：お弁当選択画面
# ==========================================
if str_lit.session_state.page == "selection":
    col1, col2 = str_lit.columns([1, 4])
    with col1:
        if os.path.exists("Kawase.jpg"):
            str_lit.image("Kawase.jpg", width=180)
    with col2:
        str_lit.title("Bento Management✅ ")
        str_lit.caption("現在このシステムは正常に動作しています✅")

    str_lit.markdown("---")
    str_lit.subheader("🍱 お弁当を選択して個数を入力してください")

    menu_keys = list(bento_data.keys())
    cols_per_row = 4
    rows = [menu_keys[i:i + cols_per_row] for i in range(0, len(menu_keys), cols_per_row)]

    quantities = {}

    for row_items in rows:
        cols = str_lit.columns(len(row_items))
        for idx, bento_name in enumerate(row_items):
            with cols[idx]:
                is_selected = bento_name in str_lit.session_state.selected_bentos
                
                border_color = "#00d2ff" if is_selected else "#30363d"
                bg_color = "linear-gradient(145deg, #1f2a38, #161b22)" if is_selected else "linear-gradient(145deg, #1c2128, #161b22)"
                shadow = "0 10px 25px rgba(0, 210, 255, 0.3)" if is_selected else "0 5px 15px rgba(0, 0, 0, 0.3)"
                badge = "✅ 選択中" if is_selected else "➕ 未選択"
                badge_color = "#00d2ff" if is_selected else "#8b949e"

                str_lit.markdown(f"""
                <div class="bento-3d-card" style="
                    background: {bg_color};
                    border: 2px solid {border_color};
                    border-radius: 14px;
                    padding: 12px;
                    text-align: center;
                    margin-bottom: 8px;
                    box-shadow: {shadow};
                    height: 130px;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                ">
                    <div class="bento-icon-3d" style="font-size: 28px; margin-bottom: 4px;">🍱</div>
                    <div style="font-weight: bold; font-size: 13px; color: #f0f6fc; margin-bottom: 4px; width: 100%; white-space: normal; line-height: 1.2;">{bento_name}</div>
                    <div style="font-size: 11px; color: {badge_color}; font-weight: bold;">{badge}</div>
                </div>
                """, unsafe_allow_html=True)

                if is_selected:
                    current_qty = str_lit.session_state.get(f"qty_{bento_name}", 1)
                    quantities[bento_name] = str_lit.number_input(
                        f"【{bento_name}】個数", 
                        min_value=1, value=current_qty, step=1, 
                        key=f"qty_{bento_name}"
                    )
                
                btn_label = "❌ 解除する" if is_selected else "選択する"
                if str_lit.button(btn_label, key=f"card_btn_{bento_name}", use_container_width=True):
                    if is_selected:
                        str_lit.session_state.selected_bentos.remove(bento_name)
                        str_lit.toast(f"「{bento_name}」の選択を解除しました", icon="❌")
                    else:
                        str_lit.session_state.selected_bentos.append(bento_name)
                        str_lit.toast(f"選択しました：「{bento_name}」", icon="✅")
                    str_lit.rerun()

    str_lit.markdown("---")

    if str_lit.session_state.selected_bentos:
        @str_lit.dialog("⚠️ 確認画面")
        def confirm_selection():
            str_lit.write("以下の内容で検索結果を表示しますか？")
            str_lit.write("よろしいですか？")
            
            str_lit.markdown("### 📋 現在の選択内容:")
            for bento in str_lit.session_state.selected_bentos:
                qty = str_lit.session_state.get(f"qty_{bento}", 1)
                str_lit.write(f"- **{bento}**: {qty}個")
            
            str_lit.markdown("<br>", unsafe_allow_html=True)
            col_yes, col_no = str_lit.columns(2)
            with col_yes:
                if str_lit.button("Yes,I agree.", type="primary", use_container_width=True):
                    str_lit.session_state.page = "result"
                    str_lit.rerun()
            with col_no:
                if str_lit.button("キャンセル", use_container_width=True):
                    str_lit.rerun()

        if str_lit.button("🔍 検索結果を表示（印刷用ページへ）", type="primary", use_container_width=True):
            confirm_selection()
    else:
        str_lit.warning("お弁当が選択されていません。上のカードから選んでください！")

# ==========================================
# 画面②：検索結果・印刷用ページ
# ==========================================
elif str_lit.session_state.page == "result":
    str_lit.title("📊 製造材料の合計個数一覧（印刷用）")
    str_lit.caption("お父さん用：ブラウザの印刷設定でレイアウトを【横】にして印刷してください。")
    
    str_lit.markdown("---")

    if str_lit.button("⬅️ お弁当の選択画面に戻る", use_container_width=True):
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
        str_lit.warning("集計するデータがありません。")

    str_lit.markdown('</div>', unsafe_allow_html=True)

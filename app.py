import streamlit as st
import random

# 全域設定：統一乾淨字體與寬版版面佈局
st.set_page_config(page_title="Cruise Board Game", layout="wide")
st.markdown("""
    <style>
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Arial', sans-serif !important;
    }
    .stAlert {
        border-radius: 4px !important;
        padding: 12px !important;
        margin-bottom: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# 初始化遊戲核心狀態變數（防止快取衝突）
if 'phase' not in st.session_state: st.session_state.phase = 0
if 'group' not in st.session_state: st.session_state.group = ""
if 'brand' not in st.session_state: st.session_state.brand = ""
if 'days' not in st.session_state: st.session_state.days = ""
if 'theme' not in st.session_state: st.session_state.theme = ""
if 'route' not in st.session_state: st.session_state.route = ""
if 'market' not in st.session_state: st.session_state.market = ""
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'chosen_logs' not in st.session_state: st.session_state.chosen_logs = []
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-G" + str(random.randint(11,99)) + "-" + str(random.randint(100,999))

# 精準設定每組專屬的右側及結算資訊數據庫
GROUP_DATA = {
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN Market (High bar spend, wants slow lazy holiday)", "map": "🇺🇸 Miami ➔ 🌊 (Sailing Caribbean Sea) ➔ 🇲🇽 Cozumel"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN Market (Mass family, high casino spend, active fun)", "map": "🇺🇸 Seattle ➔ 🌊 (Sailing Gulf of Alaska) ➔ 🇺🇸 Juneau"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN Market (Rich premium travelers, fine dining)", "map": "🇪🇸 Barcelona ➔ 🌊 (Sailing Mediterranean Sea) ➔ 🇫🇷 Marseille"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN Market (Big families, delicious food, Safety First)", "map": "🇸🇬 Singapore Base ➔ 🌊 (Sailing Andaman Sea) ➔ 🇹🇭 Phuket"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "market": "WESTERN Market (Adventure travelers, loves outdoor tours)", "map": "🇦🇺 Sydney ➔ 🌊 (Sailing Tasman Sea) ➔ 🇳🇿 Auckland"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN Market (Hong Hong high-end rich shoppers, hates delays)", "map": "🇭🇰 Hong Kong Base ➔ 🌊 (Sailing East China Sea) ➔ 🇯🇵 Okinawa"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN Market (Older alumni groups, wants lectures)", "map": "🇩🇰 Copenhagen ➔ 🌊 (Sailing Baltic Sea) ➔ 🇫🇮 Helsinki"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN Market (Singapore segment, wildlife photography tours)", "map": "🇯🇵 Yokohama ➔ 🌊 (Sailing North Pacific) ➔ 🇹🇼 Keelung"}
}

# --- 第一階段：選擇組別與資料鎖定 ---
if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    group_choice = st.selectbox("Select Your Group Number (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    
    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Group Assignment Name:", value=group_choice, disabled=True)
    c1.text_input("Cruise Name:", value=f"{cfg['brand']} ({group_choice})", disabled=True)
    c1.text_input("Cruise Theme Focus:", value=cfg['theme'], disabled=True)
    c2.text_input("Demographic Profile:", value=cfg['market'], disabled=True)
    c2.text_input("Cruise Itinerary Route:", value=cfg['map'], disabled=True)
    
    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.group = group_choice
        st.session_state.brand = f"{cfg['brand']} ({group_choice})"
        st.session_state.days = cfg['duration']
        st.session_state.theme = cfg['theme']
        st.session_state.route = cfg['map']
        st.session_state.market = cfg['market']
        st.session_state.phase = 1
        st.rerun()

# --- 第二、三階段：互動決策面板 ---
elif 1 <= st.session_state.phase <= 3:
    st.markdown(f"### 📊 Scoreboard | {st.session_state.group} Active Profile")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Money left", f"${st.session_state.cash:,}")
    c2.metric("👥 Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    c3.metric("🏥 Sick/Injured", f"{st.session_state.injured} Sick")
    c4.metric("💀 Deaths", f"{st.session_state.dead} Dead")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader(f"🎲 Round {st.session_state.phase} / 3")
        is_asian = "ASIAN" in st.session_state.market
        
        # 依據目前遊輪所屬市場（亞洲/西方）動態調整事件文案與數值
        if st.session_state.phase == 1:
            title = "BAD WEATHER: Big Storm Coming"
            desc = "A dangerous Category 5 hurricane blocks your ship's direct route."
            emoji = "⛈️"
            o1_text = "Safety Detour around storm. (0 hurt, fuel spikes -$6,000)"
            if is_asian:
                o2_text = "Save Fuel money and run at full speed. (85 injuries. Asian retail boycotts cost an extra -$2,000)"
                m2_val = -4000
            else:
                o2_text = "Save Fuel money and run at full speed. (85 injuries, -$2,000 lawsuit fees)"
                m2_val = -2000
            m1_val, i1_val, d1_val, i2_val, d2_val = -6000, 0, 0, 85, 0
            
        elif st.session_state.phase == 2:
            title = "MEDICAL EMERGENCY: Sickness Outbreak on Board"
            desc = "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms."
            emoji = "🏥"
            if is_asian:
                o1_text = "Force in-cabin quarantine. (120 sick, 0 deaths. Asian lines cooperate at -$12,000)"
                o2_text = "Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine)"
                m1_val, m2_val, d2_val = -12000, -35000, 4
            else:
                o1_text = "Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000)"
                o2_text = "Keep theater/public spaces open. (450 sick. Western costs -$22,000)"
                m1_val, m2_val, d2_val = -20000, -22000, 1
            i1_val, d1_val, i2_val = 120, 0, 450
            
        else:
            title = "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer"
            desc = "A luxury retail company requests to lease public decks tonight for a VIP shopping party."
            emoji = "💎"
            if is_asian:
                o1_text = "Accept VIP contract. (Asian shopping surges net revenues by +$35,000)"
                m1_val = 35000
            else:
                o1_text = "Accept VIP contract. (Western assets capture +$20,000)"
                m1_val = 20000
            o2_text = "Decline deal to keep public transit spaces free. (Yields $0 cash injection)"
            m2_val, i1_val, d1_val, i2_val, d2_val = 0, 0, 0, 0, 0

        st.markdown(f"### {emoji} {title}")
        st.write(f"💬 **Current Situation:** {desc}")
        st.write("---")
        st.write("### 🔴 Review Options Carefully:")
        st.info(f"👉 **Option 1:** {o1_text}")
        st.info(f"👉 **Option 2:** {o2_text}")
        
        # 使用防卡死的單一確認按鈕表單
        with st.form(key=f"frm_{st.session_state.phase}"):
            user_choice = st.radio("Select your choice:", ["Option 1", "Option 2"], key=f"sel_{st.session_state.phase}")
            confirm_btn = st.form_submit_button("🚀 Confirm the decision and run it", type="primary", use_container_width=True)
            
            if confirm_btn:
                if "Option 1" in user_choice:
                    st.session_state.cash += m1_val
                    st.session_state.injured += i1_val
                    st.session_state.dead += d1_val
                    log_msg = f"Round {st.session_state.phase} - Selected Option 1: {o1_text} | (Cost/Rev: {m1_val}, Injuries: {i1_val}, Deaths: {d1_val})"
                else:
                    st.session_state.cash += m2_val
                    st.session_state.injured += i2_val
                    st.session_state.dead += d2_val
                    log_msg = f"Round {st.session_state.phase} - Selected Option 2: {o2_text} | (Cost/Rev: {m2_val}, Injuries: {i2_val}, Deaths: {d2_val})"
                
                st.session_state.chosen_logs.append(log_msg)
                st.session_state.phase += 1
                st.rerun()

    # 右側資訊欄：移除有風險的複雜縮排，保證運行無誤
    with col_right:
        st.subheader("📋 Cruise Live Logbook Status")
        st.markdown(f"**🚢 Vessel ID:** `{st.session_state.v_id}`")
        st.markdown(f"**🏢 Cruise Line:** {st.session_state.brand}")
        st.markdown(f"**🎨 Theme Focus:** {st.session_state.theme}")
        st.markdown(f"**🗺️ Route:** {st.session_state.route}")
        st.markdown(f"**👥 Target Market:** {st.session_state.market}")
        st.write("---")
        st.write("📈 **Round Decisions Tracked So Far:**")
        
        if not st.session_state.chosen_logs:
            st.write("* No strategies executed yet. Complete the current active decision.")
        

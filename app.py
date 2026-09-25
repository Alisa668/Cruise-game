import streamlit as st
import random

st.set_page_config(page_title="Cruise Board Game", layout="wide")

# Master CSS override to force clear layout separation and 100% font consistency
st.markdown("""
    <style>
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Arial', sans-serif !important;
    }
    .stAlert { border-radius: 4px !important; padding: 10px !important; margin-bottom: 8px !important; }
    div[data-testid="stVerticalBlock"] > div { margin-bottom: -10px !important; padding-bottom: 0px !important; }
    .option-box-1 {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border-left: 5px solid #EF4444 !important;
        padding: 12px; border-radius: 4px; margin-bottom: 10px; font-weight: bold;
    }
    .option-box-2 {
        background-color: rgba(59, 130, 246, 0.1) !important;
        border-left: 5px solid #3B82F6 !important;
        padding: 12px; border-radius: 4px; margin-bottom: 15px; font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

if 'phase' not in st.session_state: st.session_state.phase = 0
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'history' not in st.session_state: st.session_state.history = []
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-G" + str(random.randint(11,99))

GROUP_DATA = {
    "Group 1": {"brand": "Starry Empress", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN Market (High bar spend, wants slow lazy holiday)", "map": "🇺🇸 Miami ➔ 🌊 (Sailing Caribbean Sea) ➔ 🇲🇽 Cozumel"},
    "Group 2": {"brand": "Oceanic Voyager", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN Market (Mass family, high casino spend, active fun)", "map": "🇺🇸 Seattle ➔ 🌊 (Sailing Gulf of Alaska) ➔ 🇺🇸 Juneau"},
    "Group 3": {"brand": "Royal Sovereign", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN Market (Rich premium travelers, fine dining)", "map": "🇪🇸 Barcelona ➔ 🌊 (Sailing Mediterranean Sea) ➔ 🇫🇷 Marseille"},
    "Group 4": {"brand": "Genting Splendor", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN Market (Big families, delicious food, Safety First)", "map": "🇸🇬 Singapore Base ➔ 🌊 (Sailing Andaman Sea) ➔ 🇹🇭 Phuket"},
    "Group 5": {"brand": "Coral Majestic", "theme": "Business Meetings & Tech Networking", "market": "WESTERN Market (Adventure travelers, loves outdoor tours)", "map": "🇦🇺 Sydney ➔ 🌊 (Sailing Tasman Sea) ➔ 🇳🇿 Auckland"},
    "Group 6": {"brand": "Horizon Dragon", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN Market (Hong Kong high-end rich shoppers, hates delays)", "map": "🇭🇰 Hong Kong Base ➔ 🌊 (Sailing East China Sea) ➔ 🇯🇵 Okinawa"},
    "Group 7": {"brand": "Atlantic Crown", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN Market (Older alumni groups, wants lectures)", "map": "🇩🇰 Copenhagen ➔ 🌊 (Sailing Baltic Sea) ➔ 🇫🇮 Helsinki"},
    "Group 8": {"brand": "Pacific Pacific", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN Market (Singapore segment, wildlife photography tours)", "map": "🇯🇵 Yokohama ➔ 🌊 (Sailing North Pacific) ➔ 🇹🇼 Keelung"}
}

# --- STEP 1: CONFIGURATION FRONT PAGE ---
if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    group_choice = st.selectbox("Select Your Group Number (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    
    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Cruise Name:", value=cfg['brand'] + " (" + group_choice + ")", disabled=True)
    c1.text_input("Cruise Theme Focus:", value=cfg['theme'], disabled=True)
    c2.text_input("Demographic Profile:", value=cfg['market'], disabled=True)
    c2.text_input("Cruise Itinerary Route:", value=cfg['map'], disabled=True)
    
    st.markdown("### 🗺️ Geographic Itinerary Route Map:")
    st.markdown("<div style='background-color:#1E1E24; padding:15px; border-radius:6px; border:1px solid #3A3A43; font-size:18px; font-family:monospace; color:#00FFCC; font-weight:bold; text-align:center;'>🗺️ " + cfg['map'] + "</div>", unsafe_allow_html=True)

    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.history.append("==================================================")
        st.session_state.history.append("🚢 Cruise Name: " + cfg['brand'] + " (" + group_choice + ")")
        st.session_state.history.append("🎨 Cruise Theme Focus: " + cfg['theme'])
        st.session_state.history.append("👥 Demographic Profile: " + cfg['market'])
        st.session_state.history.append("🗺️ Cruise Itinerary Route: " + cfg['map'])
        st.session_state.history.append("==================================================\n")
        st.session_state.phase = 1
        st.rerun()

# --- STEP 2: INTERACTIVE CRISIS SIMULATION ROUNDS ---
elif 1 <= st.session_state.phase <= 3:
    st.markdown("### 📊 Live Scoreboard Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Money left", f"${st.session_state.cash:,}")
    c2.metric("👥 Passengers", f"{st.session_state.passengers:,} Pax")
    c3.metric("🏥 Sick/Injured", f"{st.session_state.injured} Sick")
    c4.metric("💀 Deaths", f"{st.session_state.dead} Dead")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🎲 Step " + str(st.session_state.phase) + " / 3 Rounds")
        is_asian = "ASIAN Market" in "".join(st.session_state.history)
        
        CARDS = [
            {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane blocks your ship's direct route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit strict safety expectations.", "emoji": "⛈️ 🌊 🌪️", "o1": "Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Save Fuel money and run at full speed. (85 injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Save Fuel money and run at full speed. (85 injuries, -$2,000 lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
            {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥 🤢 💊", "o1": "Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
            {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian routes generate massive net auxiliary margins from duty-free luxury spending over casual Western itineraries.", "emoji": "💎 💰 🎰", "o1": "Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0}
        ]
        
        c = CARDS[st.session_state.phase - 1]
        st.markdown("### " + c['emoji'] + " " + c['title'])
        st.write("💬 **Situation:** " + c['desc'])
        st.caption("📌 *Case Benchmark: " + c['h'] + "*")
        st.write("---")
        
        st.write("### 🔴 Review Options Carefully:")
        st.markdown("<div class='option-box-1'>👉 Option 1: " + c['o1'] + "</div>", unsafe_allow_html=True)
        st.markdown("<div class='option-box-2'>👉 Option 2: " + c['o2'] + "</div>", unsafe_allow_html=True)
        
        st.write("---")
        st.write("### 🚀 Cast Your Boardroom Decision Below:")
        st.info("💡 Clicking either button below will instantly execute that strategy and move to the next round!")
        
        # Pure direct immediate button routing strategy to eliminate all Safari freeze loops
        if st.button("🔴 Confirm Decision 1 and run it (Execute Option 1)", type="primary", use_container_width=True):
            st.session_state.cash += c['m1']; st.session_state.injured += c['i1']; st.session_state.dead += c['d1']
            st.session_state.history.append("Phase " + str(st.session_state.phase) + " Decision: Option 1 Chosen\n • Action Taken: " + c['o1'] + f"\n • Financial Shift: Cost=${abs(c['m1']):,} | Injured=+{c['i1']} | Deaths=+{c['d1']}\n")
            st.session_state.phase += 1
            st.rerun()
            
        st.write("")
        if st.button("🔵 Confirm Decision 2 and run it (Execute Option 2)", type="primary", use_container_width=True):
            st.session_state.cash += c['m2']; st.session_state.injured += c['i2']; st.session_state.dead += c['d2']
            st.session_state.history.append("Phase " + str(st.session_state.phase) + " Decision: Option 2 Chosen\n • Action Taken: " + c['o2'] + f"\n • Financial Shift: Cost=${abs(c['m2']):,} | Injured=+{c['i2']} | Deaths=+{c['d2']}\n")
            st.session_state.phase += 1
            st.rerun()

    with col_right:
        st.subheader("📋 Profile & Itinerary Specifications")
        # Direct clean dynamic variable mapping to avoid index list errors
        st.info(st.session_state.history) # Cruise Name

import streamlit as st
import random

# Inject Ocean Boardgame Custom Theme Configurations Globally
st.set_page_config(page_title="Cruise Board Game", layout="wide")
st.markdown("""
    <style>
    /* Ocean Monopoly Theme Styles */
    .stApp {
        background: linear-gradient(135deg, #0A192F 0%, #0F3057 100%) !important;
        color: #E2E8F0 !important;
    }
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Arial', sans-serif !important;
    }
    .stAlert {
        border-radius: 6px !important;
        padding: 12px !important;
        margin-bottom: 12px !important;
        background-color: rgba(255, 255, 255, 0.05) !important;
        border-left: 5px solid #00FFCC !important;
    }
    .stButton > button {
        border-radius: 6px !important;
        font-size: 16px !important;
        font-weight: bold !important;
    }
    /* Distinct card panels for left column options */
    .option-box-1 {
        background-color: rgba(239, 68, 68, 0.15) !important;
        border: 1px solid rgba(239, 68, 68, 0.3) !important;
        padding: 15px; border-radius: 6px; margin-bottom: 10px;
    }
    .option-box-2 {
        background-color: rgba(59, 130, 246, 0.15) !important;
        border: 1px solid rgba(59, 130, 246, 0.3) !important;
        padding: 15px; border-radius: 6px; margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# Defensive variable caching state structures
if 'phase' not in st.session_state: st.session_state.phase = 0
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'history' not in st.session_state: st.session_state.history = []
if 'user_selection' not in st.session_state: st.session_state.user_selection = None
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-G" + str(random.randint(11,99))

# Static profile structures mapped identically to group metrics
GROUP_DATA = {
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "route": "Miami to Cozumel", "market": "WESTERN Market (High bar spend, wants slow lazy holiday)", "map": "🇺🇸 Miami ➔ 🌊 (Sailing Caribbean Sea) ➔ 🇲🇽 Cozumel"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "route": "Seattle to Juneau", "market": "WESTERN Market (Mass family, high casino spend, active fun)", "map": "🇺🇸 Seattle ➔ 🌊 (Sailing Gulf of Alaska) ➔ 🇺🇸 Juneau"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "route": "Barcelona to Marseille", "market": "WESTERN Market (Rich premium travelers, fine dining restaurants)", "map": "🇪🇸 Barcelona ➔ 🌊 (Sailing Mediterranean Sea) ➔ 🇫🇷 Marseille"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "route": "Singapore to Phuket", "market": "ASIAN Market (Big families, delicious food, demands Safety First)", "map": "🇸🇬 Singapore Base ➔ 🌊 (Sailing Andaman Sea) ➔ 🇹🇭 Phuket"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "route": "Sydney to Auckland", "market": "WESTERN Market (Adventure travelers, loves outdoor day tours)", "map": "🇦🇺 Sydney ➔ 🌊 (Sailing Tasman Sea) ➔ 🇳🇿 Auckland"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "route": "Hong Kong to Okinawa", "market": "ASIAN Market (Hong Kong high-end rich shoppers, hates time delays)", "map": "🇭🇰 Hong Kong Base ➔ 🌊 (Sailing East China Sea) ➔ 🇯🇵 Okinawa"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "route": "Copenhagen to Helsinki", "market": "WESTERN Market (Older alumni groups, wants quiet academic study lectures)", "map": "🇩🇰 Copenhagen ➔ 🌊 (Sailing Baltic Sea) ➔ 🇫🇮 Helsinki"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "route": "Yokohama to Keelung", "market": "ASIAN Market (Singapore segment, wildlife photography tours)", "map": "🇯🇵 Yokohama ➔ 🌊 (Sailing North Pacific) ➔ 🇹🇼 Keelung"}
}

st.title("🚢 Cruise Monopoly: Ship Manager Game")
st.write("---")

# --- INITIAL FRONT PAGE CONFIGURATION ---
if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    st.info("💡 Your ship setup is auto-locked based on your Group Number to prevent copying!")
    
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
        st.session_state.phase = 1
        st.session_state.history.append("🚢 CRUISE INITIAL REPORT: " + cfg['brand'] + " (" + group_choice + ")")
        st.session_state.history.append("• Cruise Theme Focus: " + cfg['theme'])
        st.session_state.history.append("• Demographic Profile: " + cfg['market'])
        st.session_state.history.append("• Cruise Itinerary Route: " + cfg['map'])
        st.session_state.history.append("---")
        st.rerun()

# --- INTERACTIVE SIMULATION GAME FOR PHASE 1 - 3 ---
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
        
        hist_str = " ".join(st.session_state.history)
        is_asian = "ASIAN Market" in hist_str
        
        CARDS = [
            {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane is blocking your ship's route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit a strict collectivist safety expectation.", "emoji": "⛈️ 🌊 🌪️", "o1": "Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Save Fuel money and run at full speed. (85 fallback injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Save Fuel money and run at full speed. (85 fallback injuries, -$2,000 medical lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
            {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥 🤢 💊", "o1": "Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
            {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian routes generate massive net auxiliary margins from duty-free luxury spending over casual Western itineraries.", "emoji": "💎 💰 🎰", "o1": "Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0}
        ]
        
        c = CARDS[st.session_state.phase - 1]
        st.markdown("### " + c['emoji'] + " " + c['title'])
        st.write("💬 **Current Situation:** " + c['desc'])
        st.caption("📌 *Case History: " + c['h'] + "*")
        st.write("---")
        
        st.subheader("Review Options Carefully:")
        st.markdown("<div class='option-box-1'>🔴 <b>Option 1:</b> " + c['o1'] + "</div>", unsafe_allow_html=True)
        st.markdown("<div class='option-box-2'>🔵 <b>Option 2:</b> " + c['o2'] + "</div>", unsafe_allow_html=True)
        
        b1, b2 = st.columns(2)
        # Flattened button assignment to completely fix layout indentation error
        if b1.button("👉 Select Option 1", use_container_width=True): st.session_state.user_selection = "1"
        if b2.button("👉 Select Option 2", use_container_width=True): st.session_state.user_selection = "2"

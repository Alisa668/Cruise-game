import streamlit as st
import random

# Global Page Configurations
st.set_page_config(page_title="Cruise Boardroom Monopoly", layout="wide")

# Injecting Monopoly Board Game Boardroom Layout directly
st.markdown("""
    <style>
    /* Dark Ocean Board Game Master Theme */
    .stApp {
        background-color: #0B132B !important;
        background-image: radial-gradient(rgba(255, 255, 255, 0.05) 2px, transparent 0) !important;
        background-size: 30px 30px !important;
    }
    
    /* Left Panel: Crimson Red Monopoly Property Board Card Styling */
    .board-card-left {
        background-color: #1C2541 !important;
        border-top: 12px solid #D90429 !important;
        border-left: 2px solid #48CAE4 !important;
        border-right: 2px solid #48CAE4 !important;
        border-bottom: 2px solid #48CAE4 !important;
        border-radius: 8px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5) !important;
    }
    
    /* Right Panel: Golden Yellow Community Ledger Card Styling */
    .board-card-right {
        background-color: #1C2541 !important;
        border-top: 12px solid #FFB703 !important;
        border-left: 2px solid #FFB703 !important;
        border-right: 2px solid #FFB703 !important;
        border-bottom: 2px solid #FFB703 !important;
        border-radius: 8px !important;
        padding: 24px !important;
        margin-bottom: 20px !important;
        box-shadow: 0 10px 25px rgba(0,0,0,0.5) !important;
    }
    
    /* Universal clear font typography rules */
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Century Gothic', 'Segoe UI', sans-serif !important;
        color: #F8F9FA !important;
    }
    
    h1, h2, h3, h4 {
        font-weight: bold !important;
        letter-spacing: 1px !important;
    }
    
    .monopoly-title {
        color: #48CAE4 !important;
        text-shadow: 2px 2px #000000 !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize master state variables securely
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
if 'v_id' not in st.session_state: st.session_state.v_id = "SHIP-" + str(random.randint(100, 999))

GROUP_DATA = {
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN", "map": "Miami (USA) ➔ Caribbean Sea ➔ Cozumel (Mexico)"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN", "map": "Seattle (USA) ➔ Gulf of Alaska ➔ Juneau (USA)"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN", "map": "Barcelona (Spain) ➔ Mediterranean Sea ➔ Marseille (France)"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN", "map": "Singapore Base ➔ Andaman Sea ➔ Phuket (Thailand)"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "market": "WESTERN", "map": "Sydney (Australia) ➔ Tasman Sea ➔ Auckland (New Zealand)"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN", "map": "Hong Kong Base ➔ East China Sea ➔ Okinawa (Japan)"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN", "map": "Copenhagen (Denmark) ➔ Baltic Sea ➔ Helsinki (Finland)"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN", "map": "Yokohama (Japan) ➔ North Pacific ➔ Keelung (Taiwan)"}
}

# --- PHASE 0: GAME REGISTRATION SETUP HUB ---
if st.session_state.phase == 0:
    st.markdown("<h1 class='monopoly-title'>🚢 CRUISE SHIP BOARDROOM MONOPOLY</h1>", unsafe_allow_html=True)
    st.write("Welcome onboard corporate cruise manager. Setup your company registry portfolio to lock your assets.")
    
    group_choice = st.selectbox("Select Your Board Group Portfolio (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    
    st.markdown("<div class='board-card-left'>", unsafe_allow_html=True)
    st.subheader("📋 Locked Vessel Asset Deed Summary")
    st.text_input("Group Portfolio:", value=group_choice, disabled=True)
    st.text_input("Vessel Ship Identity:", value=f"{cfg['brand']}", disabled=True)
    st.text_input("Theme Attraction Focus:", value=cfg['theme'], disabled=True)
    st.text_input("Target Demographic Demands:", value=f"{cfg['market']} Market Segment", disabled=True)
    st.text_input("Itinerary Coordinate Route Track:", value=cfg['map'], disabled=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    if st.button("🚀 Confirm Asset Deed & Launch Voyage", type="primary", use_container_width=True):
        st.session_state.group = group_choice
        st.session_state.brand = cfg['brand']
        st.session_state.days = cfg['duration']
        st.session_state.theme = cfg['theme']
        st.session_state.route = cfg['map']
        st.session_state.market = cfg['market']
        st.session_state.phase = 1
        st.rerun()

# --- PHASE 1 - 5: THE INTERACTIVE BOARDROOM INTERACTIVE DECISION MATRIX ---
elif 1 <= st.session_state.phase <= 5:
    is_asian = st.session_state.market == "ASIAN"
    
    # 1. Permanent Top Navigation Scoreboard Status
    st.markdown(f"<h2>📊 Assets Scoreboard | {st.session_state.group} Profile</h2>", unsafe_allow_html=True)
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    with m_col1: st.metric("💰 Cash Balance Reserves", f"${st.session_state.cash:,}")
    with m_col2: st.metric("👥 Active Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    with m_col3: st.metric("🏥 Total Injuries Logged", f"{st.session_state.injured} Case")
    with m_col4: st.metric("💀 Total Onboard Casualties", f"{st.session_state.dead} Dead")
    st.markdown("---")
    
    # 2. Enforced Side-by-Side Column Matrix Framework to fix missing panels
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.markdown(f"<h3>🎲 Monopoly Round Card: {st.session_state.phase} / 5</h3>", unsafe_allow_html=True)
        
        # Statically define all scenario numbers to completely eliminate dynamic calculation rendering blocks
        if st.session_state.phase == 1:
            title, emoji = "WEATHER HAZARD: Tropical Storm Path Encounter", "⛈️"
            desc = "A severe meteorological anomaly intersects your primary tracking channel map grids."
            o1_text = "Safety Detour around tracking block. (Cost: -$15,000 | Injuries: +0 | Casualties: +0)"
            o2_text = "Throttling full engine velocity across edge coordinates. (Cost: -$12,000 | Injuries: +140 | Casualties: +0)" if is_asian else "Throttling full engine velocity across edge coordinates. (Cost: -$11,000 | Injuries: +155 | Casualties: +1)"
            m1, i1, d1 = -15000, 0, 0
            m2 = -12000 if is_asian else -11000
            i2 = 140 if is_asian else 155
            d2 = 0 if is_asian else 1
            
        elif st.session_state.phase == 2:
            title, emoji = "CONTAGION ALERT: Internal Norovirus Spread", "🏥"
            desc = "An infectious gastrointestinal pathogen outbreak is isolated within onboard restaurant galleys."
            o1_text = "Enforce lockdown room isolation protocols. (Cost: -$18,000 | Injuries: +60 | Casualties: +0)" if is_asian else "Enforce lockdown room isolation protocols. (Cost: -$25,000 | Injuries: +80 | Casualties: +0)"
            o2_text = "Keep premium recreational decks operational. (Cost: -$22,000 | Injuries: +420 | Casualties: +5)" if is_asian else "Keep premium recreational decks operational. (Cost: -$21,000 | Injuries: +310 | Casualties: +2)"
            m1 = -18000 if is_asian else -25000
            i1, d1 = 60 if is_asian else 80, 0
            m2 = -22000 if is_asian else -21000
            i2 = 420 if is_asian else 310
            d2 = 5 if is_asian else 2
            
        elif st.session_state.phase == 3:
            title, emoji = "COMMERCIAL DEED: Luxury Brand Shopping Festival", "💎"
            desc = "A luxury high-end distributor tenders bid parameters to lease your public atrium spaces."
            o1_text = "Approve VIP shopping platform layout contract. (Revenue: +$35,000 | Injuries: +20 | Casualties: +0)" if is_asian else "Approve VIP shopping platform layout contract. (Revenue: +$22,000 | Injuries: +15 | Casualties: +0)"
            o2_text = "Reject retail bid tracking options to maximize space. (Revenue: +$4,000 | Injuries: +0 | Casualties: +0)"
            m1 = 35000 if is_asian else 22000
            i1, d1 = 20 if is_asian else 15, 0
            m2, i2, d2 = 4000, 0, 0

        elif st.session_state.phase == 4:
            title, emoji = "ECOLOGICAL COMPLIANCE: Minor Bilge Fuel Seepage", "🛢️"

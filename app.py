import streamlit as st
import random

# Global CSS: Force unified clean typography and wide screen framework
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

# Initialize master boardroom state track parameters
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

# Configuration Database mapping for all 8 Corporate Groups
GROUP_DATA = {
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN", "map": "USA Miami -> Sailing Caribbean Sea -> Mexico Cozumel"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN", "map": "USA Seattle -> Sailing Gulf of Alaska -> USA Juneau"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN", "map": "Spain Barcelona -> Sailing Mediterranean Sea -> France Marseille"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN", "map": "Singapore Base -> Sailing Andaman Sea -> Thailand Phuket"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "market": "WESTERN", "map": "Australia Sydney -> Sailing Tasman Sea -> New Zealand Auckland"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN", "map": "Hong Kong Base -> Sailing East China Sea -> Japan Okinawa"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN", "map": "Denmark Copenhagen -> Sailing Baltic Sea -> Finland Helsinki"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN", "map": "Japan Yokohama -> Sailing North Pacific -> Taiwan Keelung"}
}

# --- PHASE 0: CORPORATE INITIAL REGISTRATION Front Page ---
if st.session_state.phase == 0:
    st.header("Step 1: Choose Your Group Number")
    group_choice = st.selectbox("Select Your Group Number (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    
    st.write("### Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Group Assignment Name:", value=group_choice, disabled=True)
    c1.text_input("Cruise Name:", value=f"{cfg['brand']} ({group_choice})", disabled=True)
    c1.text_input("Cruise Theme Focus:", value=cfg['theme'], disabled=True)
    c2.text_input("Demographic Profile:", value=cfg['market'] + " Market", disabled=True)
    c2.text_input("Cruise Itinerary Route Map:", value=cfg['map'], disabled=True)
    
    if st.button("Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.group = group_choice
        st.session_state.brand = f"{cfg['brand']} ({group_choice})"
        st.session_state.days = cfg['duration']
        st.session_state.theme = cfg['theme']
        st.session_state.route = cfg['map']
        st.session_state.market = cfg['market']
        st.session_state.phase = 1
        st.rerun()

# --- PHASE 1 - 5: SIMULATION BALLOT INTERACTIVE CORE ---
elif 1 <= st.session_state.phase <= 5:
    st.markdown(f"### Scoreboard | {st.session_state.group} Active Profile")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Money left", f"${st.session_state.cash:,}")
    c2.metric("Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    c3.metric("Sick/Injured", f"{st.session_state.injured} Sick")
    c4.metric("Deaths", f"{st.session_state.dead} Dead")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader(f"Round {st.session_state.phase} / 5")
        is_asian = st.session_state.market == "ASIAN"
        
        # Completely Flattened Scenario Logic (Zero Nested If-Statements)
        if st.session_state.phase == 1:
            title = "BAD WEATHER: Big Storm Coming"
            desc = "A dangerous Category 5 hurricane blocks your ship's direct route."
            emoji = "[STORM]"
            o1_text = "Safety Detour around storm. (0 dead, fuel costs spikes -$15,000, keeps passengers happy)"
            o2_text = "Save fuel money and run through edge at full speed. (Cost spikes -$12,000 due to minor boycotts, 140 severe injuries, 0 dead)" if is_asian else "Save fuel money and run through edge at full speed. (Lawsuit settlement costs -$11,000, 155 injuries, 1 elderly cardiac death)"
            m1_val, i1_val, d1_val = -15000, 0, 0
            m2_val = -12000 if is_asian else -11000
            i2_val = 140 if is_asian else 155
            d2_val = 0 if is_asian else 1
            
        elif st.session_state.phase == 2:
            title = "MEDICAL EMERGENCY: Sickness Outbreak on Board"
            desc = "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms."
            emoji = "[MEDICAL]"
            o1_text = "Force strict in-cabin quarantine immediately. (Passenger complaints cost -$18,000 refunds, 60 sick, 0 dead)" if is_asian else "Force strict in-cabin quarantine immediately. (Western customer refund storm costs -$25,000, 80 sick, 0 dead)"
            o2_text = "Keep public dining and spaces open to save face. (Massive contagion, 420 sick, 5 critical elderly deaths, -$22,000 medical fine)" if is_asian else "Keep public dining and spaces open to save face. (Contagion grows, 310 sick, 2 deaths, Class-action lawsuit settlement costs -$21,000)"
            m1_val = -18000 if is_asian else -25000
            i1_val = 60 if is_asian else 80
            d1_val = 0
            m2_val = -22000 if is_asian else -21000
            i2_val = 420 if is_asian else 310
            d2_val = 5 if is_asian else 2
            
        elif st.session_state.phase == 3:
            title = "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer"
            desc = "A luxury retail company requests to lease public decks tonight for a VIP shopping party."
            emoji = "[RETAIL]"
            o1_text = "Accept VIP contract. (Shopping turnover nets large revenue +$35,000, but public area congestion causes 20 minor trip injuries)" if is_asian else "Accept VIP contract. (Western asset brand deal captures revenue +$22,000, crowd crush causes 15 minor shoulder injuries)"
            o2_text = "Decline deal to keep transit spaces free. (Revenue stays at +$4,000 general paths, 0 injuries, 0 dead)"
            m1_val = 35000 if is_asian else 22000
            i1_val = 20 if is_asian else 15
            d1_val = 0
            m2_val, i2_val, d2_val = 4000, 0, 0

        elif st.session_state.phase == 4:
            title = "ENVIRONMENTAL CRISIS: Deep Sea Oil Leakage Risk"
            desc = "Engineers notice minor fuel oil leakage near a marine sanctuary zone. Repair requires pausing the voyage."
            emoji = "[ECO_RISK]"
            o1_text = "Emergency Stop for instant mid-sea repair. (Parts and schedule delay cost -$19,000, 0 injured, 0 dead)"
            o2_text = "Ignore warning and dump residue quietly to maintain speed. (Local coastal defense fines cost -$17,500, toxic vapor causes 90 severe nauseous crew injuries, 0 dead)" if is_asian else "Ignore warning and dump residue quietly to maintain speed. (International environmental fines cost -$16,000, chemical reaction causes engine combustion: 110 burns, 3 deaths)"
            m1_val, i1_val, d1_val = -19000, 0, 0
            m2_val = -17500 if is_asian else -16000
            i2_val = 90 if is_asian else 110
            d2_val = 0 if is_asian else 3

        else:
            title = "BOARDROOM SCANDAL: VIP Casino Fraud Accusation"
            desc = "A high-net-worth VIP whale accuses your ship dealers of running rigged card decks."
            emoji = "[SCANDAL]"
            o1_text = "Pay hush money instantly to settle privately. (Discreet cost -$24,000, logo stays clean, 0 injured, 0 dead)" if is_asian else "Pay hush money instantly to settle privately. (Discreet cost -$23,000, avoids legal battles, 0 injured, 0 dead)"
            o2_text = "Refuse payment and challenge them publicly. (Media smear triggers panic, casino stampede causes 130 injuries, 1 security guard death, market asset drop costs -$26,000)" if is_asian else "Refuse payment and challenge them publicly. (Court battle costs -$24,500, angry VIP bodyguard altercation causes 45 injuries, 2 bystander deaths)"
            m1_val = -24000 if is_asian else -23000
            i1_val, d1_val = 0, 0

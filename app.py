import streamlit as st
import random

# Global Layout Configuration Setup
st.set_page_config(page_title="Cruise Boardroom Monopoly", layout="wide")

# Initialize master state logs sequentially to prevent caching corruption
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
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN Market Segment", "map": "Miami (USA) to Cozumel (Mexico)"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN Market Segment", "map": "Seattle (USA) to Juneau (USA)"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN Market Segment", "map": "Barcelona (Spain) to Marseille (France)"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN Market Segment", "map": "Singapore to Phuket (Thailand)"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "market": "WESTERN Market Segment", "map": "Sydney (Australia) to Auckland (New Zealand)"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN Market Segment", "map": "Hong Kong to Okinawa (Japan)"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN Market Segment", "map": "Copenhagen (Denmark) to Helsinki (Finland)"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN Market Segment", "map": "Yokohama (Japan) to Keelung (Taiwan)"}
}

# --- PHASE 0: SETUP ENTRY REGISTRATION ---
if st.session_state.phase == 0:
    st.title("🚢 Cruise Ship Operations Monopoly")
    st.write("Welcome corporate cruise manager. Select your assigned group portfolio configuration below:")
    
    group_choice = st.selectbox("Select Your Board Group Number (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    
    st.write("---")
    st.markdown("### 📋 Locked Vessel Asset Summary Profile")
    st.markdown(f"* **Group Assignment Name:** {group_choice}")
    st.markdown(f"* **Cruise Name:** {cfg['brand']}")
    st.markdown(f"* **Cruise Theme Focus:** {cfg['theme']}")
    st.markdown(f"* **Demographic Profile Target:** {cfg['market']}")
    st.markdown(f"* **Cruise Itinerary Route:** {cfg['map']}")
    st.write("---")
    
    if st.button("Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.group = group_choice
        st.session_state.brand = cfg['brand']
        st.session_state.days = cfg['duration']
        st.session_state.theme = cfg['theme']
        st.session_state.route = cfg['map']
        st.session_state.market = cfg['market']
        st.session_state.phase = 1
        st.rerun()

# --- PHASE 1 - 5: THE INTERACTIVE PROPERTY EVENT GRID PLATFORM ---
elif 1 <= st.session_state.phase <= 5:
    is_asian = "ASIAN" in st.session_state.market
    
    # 1. Permanent Scoreboard Metrics Header (Wording Updated to Requested Formats)
    st.header(f"📊 Operations Scoreboard | {st.session_state.group}")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Cash Balance Reserves", f"${st.session_state.cash:,}")
    m_col2.metric("Active Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    m_col3.metric("Total Number of Injury", f"{st.session_state.injured} Cases")
    m_col4.metric("Total Number of Death", f"{st.session_state.dead} Deaths")
    st.write("---")
    
    # 2. Side-by-Side View Setup to completely protect column parsing
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        st.subheader(f"🎲 Monopoly Round Card: {st.session_state.phase} / 5")
        
        # Static scenario database assignments to avoid dynamic calculation rendering blocks
        if st.session_state.phase == 1:
            title = "WEATHER HAZARD: Tropical Storm Path Encounter"
            desc = "A severe meteorological anomaly intersects your primary tracking channel map grids."
            o1_text = "Safety Detour around tracking block. (Cost: -$15,000 | Injury: +0 | Death: +0)"
            o2_text = "Throttling full engine velocity across edge coordinates. (Cost: -$12,000 | Injury: +140 | Death: +0)" if is_asian else "Throttling full engine velocity across edge coordinates. (Cost: -$11,000 | Injury: +155 | Death: +1)"
            m1, i1, d1 = -15000, 0, 0
            m2 = -12000 if is_asian else -11000
            i2 = 140 if is_asian else 155
            d2 = 0 if is_asian else 1
            
        elif st.session_state.phase == 2:
            title = "CONTAGION ALERT: Internal Norovirus Spread"
            desc = "An infectious gastrointestinal pathogen outbreak is isolated within onboard restaurant galleys."
            o1_text = "Enforce lockdown room isolation protocols. (Cost: -$18,000 | Injury: +60 | Death: +0)" if is_asian else "Enforce lockdown room isolation protocols. (Cost: -$25,000 | Injury: +80 | Death: +0)"
            o2_text = "Keep premium recreational decks operational. (Cost: -$22,000 | Injury: +420 | Death: +5)" if is_asian else "Keep premium recreational decks operational. (Cost: -$21,000 | Injury: +310 | Death: +2)"
            m1 = -18000 if is_asian else -25000
            i1, d1 = 60 if is_asian else 80, 0
            m2 = -22000 if is_asian else -21000
            i2 = 420 if is_asian else 310
            d2 = 5 if is_asian else 2
            
        elif st.session_state.phase == 3:
            title = "COMMERCIAL DEED: Luxury Brand Shopping Festival"
            desc = "A luxury high-end distributor tenders bid parameters to lease your public atrium spaces."
            o1_text = "Approve VIP shopping platform layout contract. (Revenue: +$35,000 | Injury: +20 | Death: +0)" if is_asian else "Approve VIP shopping platform layout contract. (Revenue: +$22,000 | Injury: +15 | Death: +0)"
            o2_text = "Reject retail bid tracking options to maximize space. (Revenue: +$4,000 | Injury: +0 | Death: +0)"
            m1 = 35000 if is_asian else 22000
            i1, d1 = 20 if is_asian else 15, 0
            m2, i2, d2 = 4000, 0, 0

        elif st.session_state.phase == 4:
            title = "ECOLOGICAL COMPLIANCE: Minor Bilge Fuel Seepage"
            desc = "A hull valve pressure line registers a slow residue release near a preservation marine park zone."
            o1_text = "Initiate offshore operational repair stop. (Cost: -$19,000 | Injury: +0 | Death: +0)"
            o2_text = "Bypass alerts quietly to maintain arrival window. (Cost: -$17,500 | Injury: +90 | Death: +0)" if is_asian else "Bypass alerts quietly to maintain arrival window. (Cost: -$16,000 | Injury: +110 | Death: +3)"
            m1, i1, d1 = -19000, 0, 0
            m2 = -17500 if is_asian else -16000
            i2 = 90 if is_asian else 110
            d2 = 0 if is_asian else 3

        else:
            title = "AUDIT CRISIS: VIP Whales Fraud Accusations"
            desc = "A high-rolling high-net-worth casino player registers formal complaints alleging unfair gaming tables."
            o1_text = "Disburse private settlement out of corporate assets. (Cost: -$24,000 | Injury: +0 | Death: +0)" if is_asian else "Disburse private settlement out of corporate assets. (Cost: -$23,000 | Injury: +0 | Death: +0)"
            o2_text = "Deny payment parameters and challenge assertions publicly. (Cost: -$26,000 | Injury: +130 | Death: +1)" if is_asian else "Deny payment parameters and challenge assertions publicly. (Cost: -$24,500 | Injury: +45 | Death: +2)"
            m1 = -24000 if is_asian else -23000
            i1, d1 = 0, 0
            m2 = -26000 if is_asian else -24500
            i2 = 130 if is_asian else 45
            d2 = 1 if is_asian else 2

        st.markdown(f"#### {title}")
        st.write(f"*Situation Context: {desc}*")
        st.write("---")
        
        st.write("### Review Active Board Options:")
        st.info(f"🟢 **Option 1:** {o1_text}")
        st.info(f"🔵 **Option 2:** {o2_text}")
        
        user_choice = st.radio("Select your choice:", ["Option 1", "Option 2"], key=f"radio_step_{st.session_state.phase}")
        st.write("")
        
        if st.button("🚀 Confirm the decision and run it", type="primary", use_container_width=True, key=f"run_action_btn_{st.session_state.phase}"):
            is_opt1 = "Option 1" in user_choice
            final_cost = m1 if is_opt1 else m2
            final_injury = i1 if is_opt1 else i2
            final_death = d1 if is_opt1 else d2
            final_desc = o1_text if is_opt1 else o2_text
            
            st.session_state.cash += final_cost

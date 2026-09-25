import streamlit as st
import random

# Force standard global wide layout config
st.set_page_config(page_title="Cruise Boardroom Monopoly", layout="wide")

# Initialize master boardroom state track parameters securely to protect cache
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

# Configuration Database mapping for all 8 Corporate Groups
GROUP_DATA = {
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN", "map": "Miami (USA) to Cozumel (Mexico)"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN", "map": "Seattle (USA) to Juneau (USA)"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN", "map": "Barcelona (Spain) to Marseille (France)"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN", "map": "Singapore to Phuket (Thailand)"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "market": "WESTERN", "map": "Sydney (Australia) to Auckland (New Zealand)"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN", "map": "Hong Kong to Okinawa (Japan)"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN", "map": "Copenhagen (Denmark) to Helsinki (Finland)"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN", "map": "Yokohama (Japan) to Keelung (Taiwan)"}
}

# --- PHASE 0: SETUP ENTRY HUB ---
if st.session_state.phase == 0:
    st.title("Cruise Ship Operations Monopoly")
    st.write("Welcome corporate cruise manager. Select your group number to initiate your voyage parameters.")
    
    group_choice = st.selectbox("Select Your Board Group Number (1-8):", list(GROUP_DATA.keys()))
    
    if st.button("Confirm Assignment & Start Voyage Game", type="primary", use_container_width=True):
        cfg = GROUP_DATA[group_choice]
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
    is_asian = st.session_state.market == "ASIAN"
    
    # 1. Scoreboard Metrics Header
    st.header(f"Assets Scoreboard | {st.session_state.group}")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Cash Balance Reserves", f"${st.session_state.cash:,}")
    m_col2.metric("Active Onboard Pax", f"{st.session_state.passengers:,} Pax")
    m_col3.metric("Total Injuries Logged", f"{st.session_state.injured} Case")
    m_col4.metric("Total Casualties Logged", f"{st.session_state.dead} Dead")
    st.write("---")
    
    # 2. Live Profile Info Header
    st.subheader("Cruise Live Logbook Status")
    st.markdown(f"**Vessel ID:** {st.session_state.v_id} | **Cruise Line:** {st.session_state.brand} | **Attraction Focus:** {st.session_state.theme} | **Route:** {st.session_state.route} | **Demographics:** {st.session_state.market} Market")
    st.write("---")

    # 3. Core Decisions Engine Logic Blocks
    st.subheader(f"Monopoly Round Card: {st.session_state.phase} / 5")
    
    # Static scenario database assignments to avoid native runtime string parsing failures
    if st.session_state.phase == 1:
        title = "WEATHER HAZARD: Tropical Storm Path Encounter"
        desc = "A severe meteorological anomaly intersects your primary tracking channel map grids."
        o1_text = "Safety Detour around tracking block. (Cost: -$15,000 | Injuries: +0 | Casualties: +0)"
        o2_text = "Throttling full engine velocity across edge coordinates. (Cost: -$12,000 | Injuries: +140 | Casualties: +0)" if is_asian else "Throttling full engine velocity across edge coordinates. (Cost: -$11,000 | Injuries: +155 | Casualties: +1)"
        m1, i1, d1 = -15000, 0, 0
        m2 = -12000 if is_asian else -11000
        i2 = 140 if is_asian else 155
        d2 = 0 if is_asian else 1
        
    elif st.session_state.phase == 2:
        title = "CONTAGION ALERT: Internal Norovirus Spread"
        desc = "An infectious gastrointestinal pathogen outbreak is isolated within onboard restaurant galleys."
        o1_text = "Enforce lockdown room isolation protocols. (Cost: -$18,000 | Injuries: +60 | Casualties: +0)" if is_asian else "Enforce lockdown room isolation protocols. (Cost: -$25,000 | Injuries: +80 | Casualties: +0)"
        o2_text = "Keep premium recreational decks operational. (Cost: -$22,000 | Injuries: +420 | Casualties: +5)" if is_asian else "Keep premium recreational decks operational. (Cost: -$21,000 | Injuries: +310 | Casualties: +2)"
        m1 = -18000 if is_asian else -25000
        i1, d1 = 60 if is_asian else 80, 0
        m2 = -22000 if is_asian else -21000
        i2 = 420 if is_asian else 310
        d2 = 5 if is_asian else 2
        
    elif st.session_state.phase == 3:
        title = "COMMERCIAL DEED: Luxury Brand Shopping Festival"
        desc = "A luxury high-end distributor tenders bid parameters to lease your public atrium spaces."
        o1_text = "Approve VIP shopping platform layout contract. (Revenue: +$35,000 | Injuries: +20 | Casualties: +0)" if is_asian else "Approve VIP shopping platform layout contract. (Revenue: +$22,000 | Injuries: +15 | Casualties: +0)"
        o2_text = "Reject retail bid tracking options to maximize space. (Revenue: +$4,000 | Injuries: +0 | Casualties: +0)"
        m1 = 35000 if is_asian else 22000
        i1, d1 = 20 if is_asian else 15, 0
        m2, i2, d2 = 4000, 0, 0

    elif st.session_state.phase == 4:
        title = "ENVIRONMENTAL CRISIS: Deep Sea Oil Leakage Risk"
        desc = "Engineers notice minor fuel oil leakage near a marine sanctuary zone. Repair requires pausing the voyage."
        o1_text = "Initiate offshore operational repair stop. (Cost: -$19,000 | Injuries: +0 | Casualties: +0)"
        o2_text = "Bypass alerts quietly to maintain arrival window. (Cost: -$17,500 | Injuries: +90 | Casualties: +0)" if is_asian else "Bypass alerts quietly to maintain arrival window. (Cost: -$16,000 | Injuries: +110 | Casualties: +3)"
        m1, i1, d1 = -19000, 0, 0
        m2 = -17500 if is_asian else -16000
        i2 = 90 if is_asian else 110
        d2 = 0 if is_asian else 3

    else:
        title = "AUDIT CRISIS: VIP Whales Fraud Accusations"
        desc = "A high-rolling high-net-worth casino player registers formal complaints alleging unfair gaming tables."
        o1_text = "Disburse private settlement out of corporate assets. (Cost: -$24,000 | Injuries: +0 | Casualties: +0)" if is_asian else "Disburse private settlement out of corporate assets. (Cost: -$23,000 | Injuries: +0 | Casualties: +0)"
        o2_text = "Deny payment parameters and challenge assertions publicly. (Cost: -$26,000 | Injuries: +130 | Casualties: +1)" if is_asian else "Deny payment parameters and challenge assertions publicly. (Cost: -$24,500 | Injuries: +45 | Casualties: +2)"
        m1 = -24000 if is_asian else -23000
        i1, d1 = 0, 0
        m2 = -26000 if is_asian else -24500
        i2 = 130 if is_asian else 45
        d2 = 1 if is_asian else 2

    # Display active situation context
    st.write(f"### {title}")
    st.write(f"*Situation Context: {desc}*")
    st.write("---")
    
    st.write("### Review Active Board Options:")
    st.info(f"Option 1: {o1_text}")
    st.info(f"Option 2: {o2_text}")
    
    # Universal native strategy selection radio component
    user_choice = st.radio("Select your choice:", ["Option 1", "Option 2"], key=f"radio_step_{st.session_state.phase}")
    st.write("")
    
    if st.button("Confirm the decision and run it", type="primary", use_container_width=True, key=f"run_action_btn_{st.session_state.phase}"):
        is_opt1 = "Option 1" in user_choice
        final_cost = m1 if is_opt1 else m2
        final_injury = i1 if is_opt1 else i2
        final_death = d1 if is_opt1 else d2
        final_desc = o1_text if is_opt1 else o2_text
        
        st.session_state.cash += final_cost
        st.session_state.injured += final_injury
        st.session_state.dead += final_death
        
        log_item = f"Round {st.session_state.phase} Strategy Move: Chosen {user_choice} -> {final_desc} [Cost/Rev: {final_cost}, Injuries: +{final_injury}, Casualties: +{final_death}]"
        st.session_state.chosen_logs.append(log_item)
        
        st.session_state.phase += 1
        st.rerun()


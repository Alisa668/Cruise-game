import streamlit as st
import random

st.set_page_config(page_title="Cruise Board Game", layout="wide")

st.markdown("<style>html,body,[data-testid='stMarkdownContainer'],p,span,div,h1,h2,h3{font-family:'Arial',sans-serif !important;}.stAlert{border-radius:4px !important;padding:12px !important;margin-bottom:12px !important;}</style>", unsafe_allow_html=True)

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

# --- STAGE 0: SETUP HUB ---
if st.session_state.phase == 0:
    st.header("Step 1: Choose Your Group Number")
    group_choice = st.selectbox("Select Your Group Number (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    st.write("### Your Auto-Locked Ship Details:")
    st.text_input("Group Assignment Name:", value=group_choice, disabled=True)
    st.text_input("Cruise Name:", value=f"{cfg['brand']} ({group_choice})", disabled=True)
    st.text_input("Cruise Theme Focus:", value=cfg['theme'], disabled=True)
    st.text_input("Demographic Profile:", value=cfg['market'] + " Market", disabled=True)
    st.text_input("Cruise Itinerary Route Map:", value=cfg['map'], disabled=True)
    if st.button("Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.group = group_choice
        st.session_state.brand = f"{cfg['brand']} ({group_choice})"
        st.session_state.days = cfg['duration']
        st.session_state.theme = cfg['theme']
        st.session_state.route = cfg['map']
        st.session_state.market = cfg['market']
        st.session_state.phase = 1
        st.rerun()

# --- STAGE 1 TO 5: MAIN CORE ROUNDS PLATFORM ---
if st.session_state.phase >= 1 and st.session_state.phase <= 5:
    st.markdown(f"### Scoreboard | {st.session_state.group} Active Profile")
    sc1, sc2, sc3, sc4 = st.columns(4)
    sc1.metric("Money left", f"${st.session_state.cash:,}")
    sc2.metric("Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    sc3.metric("Sick/Injured", f"{st.session_state.injured} Sick")
    sc4.metric("Deaths", f"{st.session_state.dead} Dead")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader(f"Round {st.session_state.phase} / 5")
        is_asian = st.session_state.market == "ASIAN"
        
        # Scenario 1 Assets Matrix
        if st.session_state.phase == 1:
            title = "BAD WEATHER: Big Storm Coming"
            desc = "A dangerous Category 5 hurricane blocks your ship's direct route."
            emoji = "[STORM]"
            o1_text = "Safety Detour around storm. (Cost: -15000, Injuries: 0, Deaths: 0)"
            o2_text = "Run through edge at full speed. (Cost: -12000, Injuries: 140, Deaths: 0)" if is_asian else "Run through edge at full speed. (Cost: -11000, Injuries: 155, Deaths: 1)"
            m1_val, i1_val, d1_val = -15000, 0, 0
            m2_val = -12000 if is_asian else -11000
            i2_val = 140 if is_asian else 155
            d2_val = 0 if is_asian else 1
            
        # Scenario 2 Assets Matrix
        if st.session_state.phase == 2:
            title = "MEDICAL EMERGENCY: Sickness Outbreak on Board"
            desc = "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms."
            emoji = "[MEDICAL]"
            o1_text = "Force strict in-cabin quarantine. (Cost: -18000, Injuries: 60, Deaths: 0)" if is_asian else "Force strict in-cabin quarantine. (Cost: -25000, Injuries: 80, Deaths: 0)"
            o2_text = "Keep public dining areas open. (Cost: -22000, Injuries: 420, Deaths: 5)" if is_asian else "Keep public dining areas open. (Cost: -21000, Injuries: 310, Deaths: 2)"
            m1_val = -18000 if is_asian else -25000
            i1_val = 60 if is_asian else 80
            d1_val = 0
            m2_val = -22000 if is_asian else -21000
            i2_val = 420 if is_asian else 310
            d2_val = 5 if is_asian else 2
            
        # Scenario 3 Assets Matrix
        if st.session_state.phase == 3:
            title = "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer"
            desc = "A luxury retail company requests to lease public decks tonight for a VIP shopping party."
            emoji = "[RETAIL]"
            o1_text = "Accept VIP contract layout. (Revenue: +35000, Injuries: 20, Deaths: 0)" if is_asian else "Accept VIP contract layout. (Revenue: +22000, Injuries: 15, Deaths: 0)"
            o2_text = "Decline deal completely. (Revenue: +4000, Injuries: 0, Deaths: 0)"
            m1_val = 35000 if is_asian else 22000
            i1_val = 20 if is_asian else 15
            d1_val = 0
            m2_val, i2_val, d2_val = 4000, 0, 0

        # Scenario 4 Assets Matrix
        if st.session_state.phase == 4:
            title = "ENVIRONMENTAL CRISIS: Deep Sea Oil Leakage Risk"
            desc = "Engineers notice minor fuel oil leakage near a marine sanctuary zone. Repair requires pausing the voyage."
            emoji = "[ECO_RISK]"
            o1_text = "Emergency Stop for repair. (Cost: -19000, Injuries: 0, Deaths: 0)"
            o2_text = "Ignore warning to maintain speed. (Cost: -17500, Injuries: 90, Deaths: 0)" if is_asian else "Ignore warning to maintain speed. (Cost: -16000, Injuries: 110, Deaths: 3)"
            m1_val, i1_val, d1_val = -19000, 0, 0
            m2_val = -17500 if is_asian else -16000
            i2_val = 90 if is_asian else 110
            d2_val = 0 if is_asian else 3

        # Scenario 5 Assets Matrix
        if st.session_state.phase == 5:
            title = "BOARDROOM SCANDAL: VIP Casino Fraud Accusation"
            desc = "A high-net-worth VIP whale accuses your ship dealers of running rigged card decks."
            emoji = "[SCANDAL]"
            o1_text = "Pay hush money to settle privately. (Cost: -24000, Injuries: 0, Deaths: 0)" if is_asian else "Pay hush money to settle privately. (Cost: -23000, Injuries: 0, Deaths: 0)"
            o2_text = "Refuse payment and challenge publicly. (Cost: -26000, Injuries: 130, Deaths: 1)" if is_asian else "Refuse payment and challenge publicly. (Cost: -24500, Injuries: 45, Deaths: 2)"
            m1_val = -24000 if is_asian else -23000
            i1_val, d1_val = 0, 0
            m2_val = -26000 if is_asian else -24500
            i2_val = 130 if is_asian else 45
            d2_val = 1 if is_asian else 2

        st.markdown(f"### {emoji} {title}")
        st.write(f"Situation Overview: {desc}")
        st.write("---")
        st.write("### Review Options Carefully:")
        st.info(f"Option 1: {o1_text}")
        st.info(f"Option 2: {o2_text}")
        
        # Pure global radio element with no form constraints to bypass indentation problems completely
        user_choice = st.radio("Select your choice:", ["Option 1", "Option 2"], key=f"user_radio_select_{st.session_state.phase}")
        st.write("---")
        
        if st.button("Confirm the decision and run it", type="primary", use_container_width=True, key=f"run_btn_{st.session_state.phase}"):
            is_opt1 = "Option 1" in user_choice
            final_cost = m1_val if is_opt1 else m2_val
            final_injury = i1_val if is_opt1 else i2_val
            final_death = d1_val if is_opt1 else d2_val
            final_desc = o1_text if is_opt1 else o2_text
            
            st.session_state.cash += final_cost

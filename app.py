import streamlit as st
import random

# Global Wide Screen Page Configuration
st.set_page_config(page_title="Cruise Boardroom Monopoly", layout="wide")

# Initialize master state properties sequentially to protect cache
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
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN", "map": "Miami (USA) to Cozumel (Mexico)"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN", "map": "Seattle (USA) to Juneau (USA)"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN", "map": "Barcelona (Spain) to Marseille (France)"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN", "map": "Singapore to Phuket (Thailand)"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "market": "WESTERN", "map": "Sydney (Australia) to Auckland (New Zealand)"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN", "map": "Hong Kong to Okinawa (Japan)"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN", "map": "Copenhagen (Denmark) to Helsinki (Finland)"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN", "map": "Yokohama (Japan) to Keelung (Taiwan)"}
}

# --- MATRIX DATA ENGINE: ALL 30 GEOGRAPHICALLY UNIQUE SCENARIOS FOR GROUPS 1-8 ---
# Matrix structure compressed: [Title, Topic Keyword, M1, i1, d1, M2, i2, d2]
DB = {
    "Group 1": [
        ["WEATHER HAZARD: Hurricane Dorian Interception", "Hurricane Dorian", -45000, 0, 0, -5000, 290, 1],
        ["CONTAGION ALERT: Aggressive Buffet Norovirus Outbreak", "Norovirus Outbreak", -38000, 45, 0, -8000, 340, 2],
        ["COMMERCIAL DEED: Massive Luxury Watch Exhibition", "Atrium Exhibition", 2000, 0, 0, 42000, 180, 1],
        ["LOCAL PROXIMITY DISRUPTIONS: Cozumel Extreme Pier Congestion", "Pier Congestion", -35000, 0, 0, -4000, 210, 1],
        ["INFRASTRUCTURE CHALLENGE: Black-Water Tank Valve Seepage", "Wastewater Valve Seepage", -40000, 0, 0, -9000, 160, 0]
    ],
    "Group 2": [
        ["ENVIRONMENTAL RISK: Glacier Bay Whale Sanctuary Speed Cap", "Whale Sanctuary Cap", -39000, 0, 0, -12000, 95, 0],
        ["ENGINEERING EXTREME: Auxiliary Stabilizer Hydrolock Failure", "Stabilizer Blade Failure", -42000, 12, 0, -11000, 310, 2],
        ["DEMOGRAPHIC DEMAND: Active Sports Deck Overcrowding Crisis", "Sports Deck Overcrowding", -36000, 5, 0, -3000, 240, 1],
        ["LOCAL PORT AUDIT: Juneau Custom Border Bottleneck", "Custom Border Bottleneck", -35000, 0, 0, -2000, 190, 1],
        ["SUPPLY CHAIN DISRUPTION: Fuel Quality Contamination", "Fuel Grade Contamination", -46000, 0, 0, -14000, 130, 1]
    ],
    "Group 3": [
        ["LABOR UNREST: Marseille Tugboat Association Strike", "Tugboat Strike", -44000, 0, 0, -7000, 220, 1],
        ["ECOLOGICAL CRISIS: Seagrass Marine Park Anchor Damage", "Anchor Seagrass Damage", -40000, 0, 0, -15000, 85, 0],
        ["BOARDROOM SCANDAL: High-Value Fine Art Authenticity Challenge", "Art Authenticity Claim", -37000, 0, 0, -11000, 0, 0],
        ["SECURITY HAZARD: Organized Port Walkway Theft Pickpocketing", "Port Walkway Pickpocketing", -35000, 0, 0, 0, 260, 1],
        ["OPERATIONAL COMPLIANCE: EU Eco-Zone Sulfur Air Violation", "Sulfur Emissions Output", -39000, 0, 0, -18000, 110, 0]
    ],
    "Group 4": [
        ["WEATHER HAZARD: Southwest Monsoon Offshore Swell Disruptions", "Monsoon Offshore Swell", -45000, 0, 0, -12000, 280, 2],
        ["CONTAGION ALERT: Premium Asian Kitchen Seafood Poisoning", "Seafood Infection Outbreak", -38000, 30, 0, -10000, 390, 4],
        ["COMMERCIAL DEED: Michelin Dim Sum Master Brand Partnership", "Michelin Dim Sum Lease", 3000, 0, 0, 45000, 190, 1],
        ["INFRASTRUCTURE RISK: Strait of Malacca Chokepoint Traffic", "Malacca Strait Gridlock", -41000, 0, 0, -13000, 150, 1],
        ["LOCAL SAFETY AUDIT: Thailand Port Lifeboat Compliance Check", "Port Lifeboat Compliance", -36000, 0, 0, -19000, 140, 1]
    ],
    "Group 5": [
        ["ENGINEERING EXTREME: Tasman Sea Rogue Wave Structural Strut Hit", "Tasman Sea Rogue Wave", -43000, 15, 0, -12000, 340, 3],
        ["OPERATIONAL COMPLIANCE: Great Barrier Reef Pilot Fine", "Barrier Reef Navigation Fine", -40000, 0, 0, -16000, 0, 0],
        ["DEMOGRAPHIC DEMAND: Business Tech Group Private Lounge Monopoly", "Lounge Monopolization Dispute", -35000, 0, 0, -4000, 110, 1],
        ["LOCAL INFRASTRUCTURE: Sydney Bio-Fouling Bio-Security Audit", "Rudder Bio-Fouling Growth", -44500, 0, 0, -22000, 0, 0],
        ["SUPPLY CHAIN DISRUPTION: Fresh Catering Produce Import Embargo", "Catering Produce Embargo", -37000, 0, 0, -5000, 190, 0]
    ],
    "Group 6": [
        ["WEATHER HAZARD: Typhoon In-fa Trajectory Shift", "Typhoon Wind Fields Encounter", -46000, 0, 0, -15000, 320, 2],
        ["AUDIT CRISIS: VIP High Roller Baccarat Blackmail Threat", "High Roller Gambling Blackmail", -38000, 0, 0, -14000, 210, 1],
        ["COMMERCIAL DEED: Lunar New Year Private Shopping Festival", "Promenade Festival Pop-Up", 2000, 0, 0, 45000, 165, 1],
        ["LOCAL PORT DISRUPTION: Hong Kong Terminal Walkout Strike", "Terminal Walkout Strike Actions", -35500, 0, 0, -4000, 180, 1],
        ["INFRASTRUCTURE CHALLENGE: Main HVAC Compressor System Breakdown", "HVAC Compressor Breakdown", -41500, 0, 0, -5000, 230, 2]
    ],
    "Group 7": [
        ["GEOPOLITICAL MARITIME CHANGE: Baltic Naval Drill Restrictions", "Baltic Naval Drill detours", -42500, 0, 0, -12500, 130, 1],
        ["ENGINEERING EXTREME: Bow Thruster Internal Gear Jam", "Bow Thruster System Jam", -39500, 0, 0, -11000, 285, 2],
        ["DEMOGRAPHIC DEMAND: Family Center Safety Overload", "Youth Center Overcrowding Hazard", -36000, 0, 0, -3000, 210, 1],
        ["LOCAL PORT AUDIT: Copenhagen Sanitation Spot-Check", "Sanitation Audit Checkpoint", -35000, 0, 0, -14500, 65, 0],
        ["SUPPLY CHAIN DISRUPTION: Potable Water Supply Pipe Contamination", "Water Intake Pipe Leakage", -38500, 0, 0, -11000, 145, 1]
    ],
    "Group 8": [
        ["WEATHER HAZARD: North Pacific Rogue Wave Structural Impact", "Window Shattering Impact", -45000, 15, 0, -9000, 350, 4],
        ["ECOLOGICAL CRISIS: Protected Coral Reef Anchor Drag Fine", "Anchor Drag Reef Destruction", -41000, 0, 0, -18000, 95, 0],
        ["BOARDROOM SCANDAL: Offshore Private Tour Theft Allegations", "Excursion Larceny Disputes", -35000, 0, 0, -2000, 45, 0],
        ["LOCAL PORT DISRUPTION: Yokohama Harbor Bunkering Plant Explosion", "Bunkering Pipeline Fire Crisis", -44000, 0, 0, -13000, 120, 1],
        ["OPERATIONAL COMPLIANCE: Taiwan Strait Visa Tracking Delays", "Customs Registration Visa Hold", -37500, 0, 0, -6000, 195, 1]
    ]
}

# --- PHASE 0: SETUP ENTRY REGISTRATION (EXACT FRONT PAGE RETAINED) ---
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

# --- PHASE 1 - 5: THE INTERACTIVE SIMULATION BOARDROOM ---
elif 1 <= st.session_state.phase <= 5:
    # 1. Permanent Scoreboard Metrics Header
    st.header(f"📊 Operations Scoreboard | {st.session_state.group}")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Cash Balance Reserves", f"${st.session_state.cash:,}")
    m_col2.metric("Active Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    m_col3.metric("Total Number of Injury", f"{st.session_state.injured} Cases")
    m_col4.metric("Total Number of Death", f"{st.session_state.dead} Deaths")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader(f"🎲 Monopoly Round Card: {st.session_state.phase} / 5")
        
        # Pull the specific unique scenario matrix allocated to this active corporate group
        arr = DB[st.session_state.group][st.session_state.phase - 1]
        
        # Explicit sequential list indexing to guarantee rendering safety on the server
        title = arr[0]
        topic = arr[1]
        m1 = arr[2]
        i1 = arr[3]
        d1 = arr[4]
        m2 = arr[5]
        i2 = arr[6]
        d2 = arr[7]
        
        # Reconstruct choice text strings dynamically
        act1 = "Gain profit" if m1 > 0 else "Pay penalty losses"
        act2 = "Gain profit" if m2 > 0 else "Pay penalty losses"
        o1_text = f"Option A: Execute protective strategy plan for {topic}. ({act1}: \${abs(m1):,} | Injury: +{i1} | Death: +{d1})"
        o2_text = f"Option B: Execute risk-balanced operational option for {topic}. ({act2}: \${abs(m2):,} | Injury: +{i2} | Death: +{d2})"

        st.markdown(f"#### {title}")
        st.write(f"*Boardroom Situation Context: Emergency management incident affecting your assigned local {st.session_state.route} tracking grids.*")
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
            st.session_state.injured += final_injury
            st.session_state.dead += final_death
            
            log_item = f"Round {st.session_state.phase} Move: Chosen {user_choice} ➔ {final_desc}"
            st.session_state.chosen_logs.append(log_item)
            
            st.session_state.phase += 1
            st.rerun()

    with col_right:
        st.subheader("📋 Cruise Live Logbook Status")
        st.markdown(f"* **Vessel ID Profile:** `{st.session_state.v_id}`")
        st.markdown(f"* **Group Name Portfolio:** {st.session_state.group}")
        st.markdown(f"* **Cruise Line Asset Name:** {st.session_state.brand}")
        st.markdown(f"* **Theme Focus Attraction:** {st.session_state.theme}")
        st.markdown(f"* **Cruise Itinerary Route:** {st.session_state.route}")
        st.markdown(f"* **Target Demographics Profile:** {st.session_state.market} Market")
        
        st.write("---")
        st.subheader("📈 Round Decisions Tracked So Far:")
        if not st.session_state.chosen_logs:
            st.write("* No strategies executed yet. Submit choice criteria on the left.")
        else:
            for log in st.session_state.chosen_logs:
                st.markdown(f"* {log}")

# --- PHASE 6: MASTER DIRECT END-GAME FINAL AUDIT REPORT SUITE ---
elif st.session_state.phase == 6:
    st.balloons()
    st.title("🏁 Voyage Completed: Master Boardroom Final Assignment Report")
    st.write("Review your corporate management metrics and final balance sheets below. Use this full data tracking ledger report to evaluate and explain your strategic choice decisions for your class assignment.")
    st.write("---")
    
    st.subheader("⚓ Vessel Properties Summary Breakdown Profile")
    st.markdown(f"* **Group Name Portfolio:** {st.session_state.group}")
    st.markdown(f"* **Cruise Line Asset Name:** {st.session_state.brand}")
    st.markdown(f"* **Cruise Itinerary (Route coordinates):** {st.session_state.route}")
    st.markdown(f"* **Operating Duration Schedule:** {st.session_state.days}")
    st.markdown(f"* **Theme Focus Attractions of the Cruise:** {st.session_state.theme}")
    st.markdown(f"* **Operating Market Profile Demographics:** {st.session_state.market} Market Profile")
    st.write("---")
        
    st.subheader("📊 Final Operational Balance Ledger Accounts")
    st.metric("Final Revenue Balance Reserves", f"\${st.session_state.cash:,}")
    st.markdown(f"* **Final Total Passengers Onboard:** {st.session_state.passengers:,} Pax")
    st.markdown(f"* **Final Accumulated Total Number of Injury:** {st.session_state.injured} Cases")
    st.markdown(f"* **Final Accumulated Total Number of Death:** {st.session_state.dead} Deaths")
    st.write("---")

    st.subheader("📜 Detailed Options Chosen Breakdown Summary Ledger List")
    if not st.session_state.chosen_logs:
        st.write("* No strategies recorded.")
    else:
        for log in st.session_state.chosen_logs:
            st.markdown(f"* {log}")
    st.write("---")
        
    if st.button("Reset Operations Terminal & Start New Simulation Voyage", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

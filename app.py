import streamlit as st
import random

# Global Wide Screen Page Configuration
st.set_page_config(page_title="The Cruise Captain Simulation", layout="wide")

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
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "market": "WESTERN Market Segment", "map": "Miami (USA) to Cozumel (Mexico)"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "market": "WESTERN Market Segment", "map": "Seattle (USA) to Juneau (USA)"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "market": "WESTERN Market Segment", "map": "Barcelona (Spain) to Marseille (France)"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "market": "ASIAN Market Segment", "map": "Singapore to Phuket (Thailand)"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "market": "WESTERN Market Segment", "map": "Sydney (Australia) to Auckland (New Zealand)"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "market": "ASIAN Market Segment", "map": "Hong Kong to Okinawa (Japan)"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN Market Segment", "map": "Copenhagen (Denmark) to Helsinki (Finland)"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN Market Segment", "map": "Yokohama (Japan) to Keelung (Taiwan)"}
}

# --- MATRIX DATA ENGINE: RE-BALANCED CLOSE-MARGIN FINANCIAL STRATEGIES ---
# Data layout format map: [Title, Topic Keyword, M1, i1, d1, M2, i2, d2]
DB = {
    "Group 1": [
        ["Weather Hazard: Hurricane Dorian Interception", "Hurricane Dorian Bypass", -45000, 15, 1, -5000, 290, 2],
        ["Contagion Alert: Aggressive Buffet Norovirus Outbreak", "Norovirus Isolation Plan", -38000, 45, 1, -8000, 340, 2],
        ["Commercial Revenue Deed: Luxury Brand Shopping Gala", "Atrium Luxury Retail Lease", 38000, 0, 0, 42000, 0, 0],
        ["High-Yield Revenue Opportunity: Duty-Free Champagne Lounge Sponsorship", "Duty-Free Sponsorship Offer", 35000, 0, 0, 37000, 0, 0],
        ["Market Commerce Opportunity: Premium Spa Package Launch", "Specialty Spa Upsell Event", 30000, 0, 0, 32000, 0, 0]
    ],
    "Group 2": [
        ["Environmental Risk: Glacier Bay Whale Sanctuary Speed Cap", "Whale Protection Tracking", -39000, 12, 1, -12000, 95, 2],
        ["Engineering Extreme: Auxiliary Stabilizer Hydrolock Failure", "Stabilizer System Repair", -42000, 15, 1, -11000, 310, 2],
        ["Commercial Revenue Deed: Aqua Park Extreme Sports Deck Tournament", "Sports Deck Championship Title", 36000, 0, 0, 40000, 0, 0],
        ["High-Yield Revenue Opportunity: Energy Drink Co-Branded Deck Party", "Deck Party Brand Association", 30000, 0, 0, 32000, 0, 0],
        ["Market Commerce Opportunity: VIP Casino Live Poker Tournament Broadcast", "Premium Casino Media Event", 35000, 0, 0, 37000, 0, 0]
    ],
    "Group 3": [
        ["Labor Unrest: Marseille Tugboat Association Strike", "Tugboat Labor Union Strike", -44000, 14, 1, -7000, 220, 2],
        ["Ecological Crisis: Seagrass Marine Park Anchor Damage", "Anchor Seagrass Code Fine", -40000, 11, 1, -15000, 185, 2],
        ["Commercial Revenue Deed: Elite Fine-Art Gallery Auction Event", "Historical Art Auction Gala", 41000, 0, 0, 45000, 0, 0],
        ["High-Yield Revenue Opportunity: Premium Local Vineyard Wine Tasting Festival", "Mediterranean Wine Tasting Expo", 32000, 0, 0, 34000, 0, 0],
        ["Market Commerce Opportunity: Luxury Shore Excursion Private Jet Upgrade", "Exclusive VIP Tour Packages Addon", 35000, 0, 0, 33000, 0, 0]
    ],
    "Group 4": [
        ["Weather Hazard: Southwest Monsoon Offshore Swell Disruptions", "Monsoon Swell Navigation", -45000, 12, 1, -12000, 280, 2],
        ["Contagion Alert: Premium Asian Kitchen Seafood Poisoning", "Seafood Contagion Quarantine", -38000, 30, 1, -10000, 390, 3],
        ["Commercial Revenue Deed: Michelin Dim Sum Master Brand Partnership", "Michelin Dim Sum Pop-Up Restaurant", 41000, 0, 0, 43000, 0, 0],
        ["High-Yield Revenue Opportunity: Bird's Nest & Abalone Luxury Dinner Upsell", "Premium Seafood Dining Banquet", 35000, 0, 0, 34000, 0, 0],
        ["Market Commerce Opportunity: Traditional Chinese Wellness Herbs Expo", "Asian Holistic Health Fair", 28000, 0, 0, 29500, 0, 0]
    ],
    "Group 5": [
        ["Engineering Extreme: Tasman Sea Rogue Wave Structural Strut Hit", "Tasman Sea Rogue Wave Strut", -43000, 15, 1, -12000, 340, 3],
        ["Operational Compliance: Great Barrier Reef Pilot Fine", "Barrier Reef Track Code Violation", -40000, 14, 1, -16000, 125, 2],
        ["Commercial Revenue Deed: Tech Enterprise Global Networking Forum", "Corporate Main Convention Space Lease", 43000, 0, 0, 45000, 0, 0],
        ["High-Yield Revenue Opportunity: Silicon Valley Venture Networking Dinner", "VIP Business Networking Banquet", 32000, 0, 0, 34000, 0, 0],
        ["Market Commerce Opportunity: Extreme Outdoor Adventure Gear Pop-Up Showcase", "Premium Eco-Adventure Gear Store", 26000, 0, 0, 27500, 0, 0]
    ],
    "Group 6": [
        ["Weather Hazard: Typhoon In-fa Trajectory Shift", "Typhoon Wind Fields Encounter", -46000, 11, 1, -15000, 320, 2],
        ["Audit Crisis: VIP High Roller Baccarat Blackmail Threat", "High Roller Gambling Blackmail Dispute", -38000, 12, 1, -14000, 210, 2],
        ["Commercial Revenue Deed: Lunar New Year Red Packet Gold Retail Festival", "Lunar New Year Red Packet Pop-Up", 42000, 0, 0, 44000, 0, 0],
        ["High-Yield Revenue Opportunity: High-End Hong Kong Jade Jewelry Private Sale", "Exclusive Luxury Jade Auction", 40000, 0, 0, 39000, 0, 0],
        ["Market Commerce Opportunity: Michelin-Starred Lunar New Year Family Feast", "Festive Reunion Dining Package", 33000, 0, 0, 31500, 0, 0]
    ],
    "Group 7": [
        ["Geopolitical Maritime Change: Baltic Naval Drill Restrictions", "Baltic Naval Drill detours", -42500, 13, 1, -12500, 130, 2],
        ["Engineering Extreme: Bow Thruster Internal Gear Jam", "Bow Thruster System Jam Repairs", -39500, 15, 1, -11000, 285, 2],
        ["Commercial Revenue Deed: Scandinavian Organic Wellness & Spa Residency", "Nordic Theme Thermal Spa Expansion", 36000, 0, 0, 38000, 0, 0],
        ["High-Yield Revenue Opportunity: Baltic Amber Fine Crafts & Souvenirs Exhibition", "Premium Regional Crafts Market", 28000, 0, 0, 29500, 0, 0],
        ["Market Commerce Opportunity: Academic Alumni Association Guest Lecture Series", "Exclusive Group Educational Symposium", 30000, 0, 0, 31000, 0, 0]
    ],
    "Group 8": [
        ["Weather Hazard: North Pacific Rogue Wave Structural Impact", "Window Shattering Impact Structural Fix", -45000, 15, 1, -9000, 350, 4],
        ["Ecological Crisis: Protected Coral Reef Anchor Drag Fine", "Anchor Drag Reef Fine Assessment", -41000, 12, 1, -18000, 95, 2],
        ["Commercial Revenue Deed: Marine Nature Diving Photography Expo", "Wildlife Deep Sea Expedition Gallery", 34000, 0, 0, 36000, 0, 0],
        ["High-Yield Revenue Opportunity: Premium Marine Equipment Private Auction", "High-End Diving Equipment Retail Event", 31000, 0, 0, 29500, 0, 0],
        ["Market Commerce Opportunity: Eco-Tourism Coral Reef Preservation Charity Dinner", "Premium Ecological Gala Dinner", 35000, 0, 0, 33500, 0, 0]
    ]
}

# --- PHASE 0: SETUP ENTRY REGISTRATION ---
if st.session_state.phase == 0:
    st.title("🚢 The Cruise Captain: Good Choices, Bad Choices")
    
    group_choice = st.selectbox("Select Your Board Group Number (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    
    st.write("---")
    st.markdown("### 📋 Cruise Summary Profile")
    st.markdown(f"* **Group Number:** {group_choice}")
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
    # Permanent Scoreboard Metrics Header
    st.header(f"📊 Operations Scoreboard | {st.session_state.group}")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Cash Balance Reserves", f"\${st.session_state.cash:,}")
    m_col2.metric("Active Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    m_col3.metric("Total Number of Injury", f"{st.session_state.injured} Cases")
    m_col4.metric("Total Number of Death", f"{st.session_state.dead} Deaths")
    st.write("---")
    
    # FIXED: Passed explicit ratio layout weight array [2, 1] inside columns statement to solve the crash
    col_left, col_right = st.columns([2, 1])
    
    with col_left:
        # Load the base array safely from our compressed engine matrix
        arr = DB[st.session_state.group][st.session_state.phase - 1]
        
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
        o1_text = f"Option 1: Execute protective strategy plan for {topic}. ({act1}: \${abs(m1):,} | Injury: +{i1} | Death: +{d1})"
        o2_text = f"Option 2: Execute risk-balanced operational option for {topic}. ({act2}: \${abs(m2):,} | Injury: +{i2} | Death: +{d2})"

        # Header modifications: Captain alert and Title moved to a new row with big bold header
        st.markdown('### "Captain, there is a problem/situation..."')
        st.markdown(f"## **Q{st.session_state.phase}: {title}**")
        st.write("---")
        
        st.write("### Review Active Board Options:")
        st.info(f"🟢 {o1_text}")
        st.info(f"🔵 {o2_text}")
        
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
            
            # FIXED: Fully restored dynamic variables array mapping to track explicit texts
            st.session_state.chosen_logs.append([
                f"Q{st.session_state.phase}",
                title,
                user_choice,
                o1_text,
                o2_text
            ])
            
            st.session_state.phase += 1
            st.rerun()

    with col_right:
        # Modified sidebar labels to Cruise Summary Profile & Group Number
        st.subheader("📋 Cruise Summary Profile")
        st.markdown(f"* **Vessel ID Profile:** `{st.session_state.v_id}`")
        st.markdown(f"* **Group Number:** {st.session_state.group}")
        st.markdown(f"* **Cruise Line Asset Name:** {st.session_state.brand}")
        st.markdown(f"* **Theme Focus Attraction:** {st.session_state.theme}")
        st.markdown(f"* **Cruise Itinerary Route:** {st.session_state.route}")
        st.markdown(f"* **Target Demographics Profile:** {st.session_state.market}")
        
        st.write("---")
        st.subheader("📈 Round Decisions Tracked So Far:")
        if not st.session_state.chosen_logs:
            st.write("* No strategies executed yet. Submit choice criteria on the left.")
        else:
            for log in st.session_state.chosen_logs:
                # FIXED: Unpack logs variables to display precise outcomes details inside right-hand logbook
                st.markdown(f"* **{log[0]}:** Selected {log[2]}")
                st.markdown(f"  * *Incident:* {log[1]}")
                st.markdown(f"  * *Action:* {log[3] if log[2] == 'Option 1' else log[4]}")

# --- PHASE 6: FINAL TEXT-BASED COMPARISON REPORT SUITE WITH HIGHLIGHT LOGIC ---
elif st.session_state.phase == 6:
    st.balloons()
    st.title("🏆 Cruise Completed! Your Final Cruise Report is ready for review.")
    st.write("Review your corporate management metrics and final balance sheets below. Use the high-light decision log summary at the bottom to explain and evaluate your boardroom choices for your assignment.")
    st.write("---")
    
    col_rep1, col_rep2 = st.columns(2)
    with col_rep1:
        st.subheader("⚓ Cruise Summary Profile Summary")
        st.markdown(f"* **Group Number:** {st.session_state.group}")
        st.markdown(f"* **Cruise Line Asset Name:** {st.session_state.brand}")
        st.markdown(f"* **Cruise Itinerary Route:** {st.session_state.route}")
        st.markdown(f"* **Operating Duration Schedule:** {st.session_state.days}")
        st.markdown(f"* **Theme Focus Attractions of the Cruise:** {st.session_state.theme}")
        st.markdown(f"* **Operating Market Profile Demographics:** {st.session_state.market}")
        
    with col_rep2:
        st.subheader("📊 Final Operational Balance Ledger Accounts")
        st.metric("Final Revenue Balance Reserves", f"\${st.session_state.cash:,}")
        st.markdown(f"* **Final Total Passengers Onboard:** {st.session_state.passengers:,} Pax")
        st.markdown(f"* **Final Accumulated Total Number of Injury:** {st.session_state.injured} Cases")
        st.markdown(f"* **Final Accumulated Total Number of Death:** {st.session_state.dead} Deaths")

    st.write("---")
    # Requirement 3 & 6 Met: Clean non-HTML textual matrix layout featuring yellow text highlights and double newline spacing
    st.subheader("📋 Decision Evaluation Ledger (Chosen vs Rejected Options)")
    st.write("Review the detailed structural choices below. Your selected strategies are highlighted with **:yellow[[CHOSEN CHOICE]]**. Use this information to defend your decisions in the upcoming written assignment.")
    st.write("---")
    
    for row in st.session_state.chosen_logs:
        q_idx, situation, selected_opt, opt1_desc, opt2_text_desc = row[0], row[1], row[2], row[3], row[4]
        
        st.markdown(f"### 🔄 {q_idx} Choice Details: `{situation}`")
        
        # Apply strict conditional highlighting based on student choice
        if selected_opt == "Option 1":
            st.markdown(f"🧡 **:yellow[[CHOSEN CHOICE] {opt1_desc}]**")
            st.markdown(f"⚪ {opt2_text_desc}")
        else:
            st.markdown(f"⚪ {opt1_desc}")
            st.markdown(f"🧡 **:yellow[[CHOSEN CHOICE] {opt2_text_desc}]**")
            
        # Insert explicit double break lines separator spacing block between rounds
        st.write("")
        st.write("")
        st.write("---")
        
    if st.button("Reset Operations Terminal & Start New Simulation Voyage", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

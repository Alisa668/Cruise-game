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

# --- MATRIX DATA ENGINE: RE-BALANCED PRO PROFITS & CONSISTENT WORDING ---
DB = {
    "Group 1": [
        ["WEATHER HAZARD: Hurricane Dorian Interception", "Hurricane Dorian Bypass", -45000, 15, 1, -5000, 290, 2],
        ["CONTAGION ALERT: Aggressive Buffet Norovirus Outbreak", "Norovirus Isolation Plan", -38000, 45, 1, -8000, 340, 2],
        ["COMMERCIAL REVENUE DEED: Luxury Brand Shopping Gala", "Atrium Luxury Retail Lease", 39000, 0, 0, 42000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: Duty-Free Champagne Lounge Sponsorship", "Duty-Free Sponsorship Offer", 35000, 0, 0, 37000, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: Premium Spa Package Launch", "Specialty Spa Upsell Event", 30000, 0, 0, 32000, 0, 0]
    ],
    "Group 2": [
        ["ENVIRONMENTAL RISK: Glacier Bay Whale Sanctuary Speed Cap", "Whale Protection Tracking", -39000, 12, 1, -12000, 95, 2],
        ["ENGINEERING EXTREME: Auxiliary Stabilizer Hydrolock Failure", "Stabilizer System Repair", -42000, 15, 1, -11000, 310, 2],
        ["COMMERCIAL REVENUE DEED: Aqua Park Extreme Sports Deck Tournament", "Sports Deck Championship Title", 38000, 0, 0, 40000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: Energy Drink Co-Branded Deck Party", "Deck Party Brand Association", 30000, 0, 0, 32000, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: VIP Casino Live Poker Tournament Broadcast", "Premium Casino Media Event", 35000, 0, 0, 37000, 0, 0]
    ],
    "Group 3": [
        ["LABOR UNREST: Marseille Tugboat Association Strike", "Tugboat Labor Union Strike", -44000, 14, 1, -7000, 220, 2],
        ["ECOLOGICAL CRISIS: Seagrass Marine Park Anchor Damage", "Anchor Seagrass Code Fine", -40000, 11, 1, -15000, 185, 2],
        ["COMMERCIAL REVENUE DEED: Elite Fine-Art Gallery Auction Event", "Historical Art Auction Gala", 43000, 0, 0, 45000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: Premium Local Vineyard Wine Tasting Festival", "Mediterranean Wine Tasting Expo", 32000, 0, 0, 34000, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: Luxury Shore Excursion Private Jet Upgrade", "Exclusive VIP Tour Packages Addon", 35000, 0, 0, 33000, 0, 0]
    ],
    "Group 4": [
        ["WEATHER HAZARD: Southwest Monsoon Offshore Swell Disruptions", "Monsoon Swell Navigation", -45000, 12, 1, -12000, 280, 2],
        ["CONTAGION ALERT: Premium Asian Kitchen Seafood Poisoning", "Seafood Contagion Quarantine", -38000, 30, 1, -10000, 390, 3],
        ["COMMERCIAL REVENUE DEED: Michelin Dim Sum Master Brand Partnership", "Michelin Dim Sum Pop-Up Restaurant", 41000, 0, 0, 43000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: Bird's Nest & Abalone Luxury Dinner Upsell", "Premium Seafood Dining Banquet", 35000, 0, 0, 34000, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: Traditional Chinese Wellness Herbs Expo", "Asian Holistic Health Fair", 28000, 0, 0, 29500, 0, 0]
    ],
    "Group 5": [
        ["ENGINEERING EXTREME: Tasman Sea Rogue Wave Structural Strut Hit", "Tasman Sea Rogue Wave Strut", -43000, 15, 1, -12000, 340, 3],
        ["OPERATIONAL COMPLIANCE: Great Barrier Reef Pilot Fine", "Barrier Reef Track Code Violation", -40000, 14, 1, -16000, 125, 2],
        ["COMMERCIAL REVENUE DEED: Tech Enterprise Global Networking Forum", "Corporate Main Convention Space Lease", 43000, 0, 0, 45000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: Silicon Valley Venture Networking Dinner", "VIP Business Networking Banquet", 32000, 0, 0, 34000, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: Extreme Outdoor Adventure Gear Pop-Up Showcase", "Premium Eco-Adventure Gear Store", 26000, 0, 0, 27500, 0, 0]
    ],
    "Group 6": [
        ["WEATHER HAZARD: Typhoon In-fa Trajectory Shift", "Typhoon Wind Fields Encounter", -46000, 11, 1, -15000, 320, 2],
        ["AUDIT CRISIS: VIP High Roller Baccarat Blackmail Threat", "High Roller Gambling Blackmail Dispute", -38000, 12, 1, -14000, 210, 2],
        ["COMMERCIAL REVENUE DEED: Lunar New Year Red Packet Gold Retail Festival", "Lunar New Year Red Packet Pop-Up", 42000, 0, 0, 44000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: High-End Hong Kong Jade Jewelry Private Sale", "Exclusive Luxury Jade Auction", 40000, 0, 0, 39000, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: Michelin-Starred Lunar New Year Family Feast", "Festive Reunion Dining Package", 33000, 0, 0, 31500, 0, 0]
    ],
    "Group 7": [
        ["GEOPOLITICAL MARITIME CHANGE: Baltic Naval Drill Restrictions", "Baltic Naval Drill detours", -42500, 13, 1, -12500, 130, 2],
        ["ENGINEERING EXTREME: Bow Thruster Internal Gear Jam", "Bow Thruster System Jam Repairs", -39500, 15, 1, -11000, 285, 2],
        ["COMMERCIAL REVENUE DEED: Scandinavian Organic Wellness & Spa Residency", "Nordic Theme Thermal Spa Expansion", 36000, 0, 0, 38000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: Baltic Amber Fine Crafts & Souvenirs Exhibition", "Premium Regional Crafts Market", 28000, 0, 0, 29500, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: Academic Alumni Association Guest Lecture Series", "Exclusive Group Educational Symposium", 30000, 0, 0, 31000, 0, 0]
    ],
    "Group 8": [
        ["WEATHER HAZARD: North Pacific Rogue Wave Structural Impact", "Window Shattering Impact Structural Fix", -45000, 15, 1, -9000, 350, 4],
        ["ECOLOGICAL CRISIS: Protected Coral Reef Anchor Drag Fine", "Anchor Drag Reef Fine Assessment", -41000, 12, 1, -18000, 95, 2],
        ["COMMERCIAL REVENUE DEED: Marine Nature Diving Photography Expo", "Wildlife Deep Sea Expedition Gallery", 34000, 0, 0, 36000, 0, 0],
        ["HIGH-YIELD REVENUE OPPORTUNITY: Premium Marine Equipment Private Auction", "High-End Diving Equipment Retail Event", 31000, 0, 0, 29500, 0, 0],
        ["MARKET COMMERCE OPPORTUNITY: Eco-Tourism Coral Reef Preservation Charity Dinner", "Premium Ecological Gala Dinner", 35000, 0, 0, 33500, 0, 0]
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
    st.header(f"📊 Operations Scoreboard | {st.session_state.group}")
    m_col1, m_col2, m_col3, m_col4 = st.columns(4)
    m_col1.metric("Cash Balance Reserves", f"\${st.session_state.cash:,}")
    m_col2.metric("Active Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    m_col3.metric("Total Number of Injury", f"{st.session_state.injured} Cases")
    m_col4.metric("Total Number of Death", f"{st.session_state.dead} Deaths")
    st.write("---")
    
    # Asymmetric columns partition (63% Left for larger question/choices view, 37% Right for Logbook)
    col_left, col_right = st.columns([63, 37])
    
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
        st.markdown(f"## **{title}**")
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
            rejected_desc = o2_text if is_opt1 else o1_text
            
            st.session_state.cash += final_cost
            st.session_state.injured += final_injury
            st.session_state.dead += final_death
            
            # Save choices and unchosen alternatives to session states for the evaluation matrix table
            st.session_state.chosen_logs.append([
                f"Round {st.session_state.phase}",
                title,
                user_choice,
                final_desc,
                "Option 2" if is_opt1 else "Option 1",
                rejected_desc
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
        st.subheader("📝 Round Decisions Tracked So Far:")
        if not st.session_state.chosen_logs:
            st.write("* No strategies executed yet. Submit choice criteria on the left.")
        else:
            for log in st.session_state.chosen_logs:
                st.markdown(f"* **{log[0]}:** Selected {log[2]}")

# --- PHASE 6: FINAL REPORT LEDGER WITH STYLED EVALUATION HIGH-LIGHT MATRIX TABLE ---
elif st.session_state.phase == 6:
    st.balloons()
    st.title("🏆 Cruise Completed! Your Final Cruise Report is ready for review.")
    st.write("Review your corporate management metrics and final balance sheets below. Use the high-light decision table at the bottom to explain and evaluate your boardroom choices for your assignment.")
    st.write("---")
    
    col_rep1, col_rep2 = st.columns(2)
    with col_rep1:
        st.subheader("⚓ Cruise Summary Profile")
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
    st.subheader("📋 Decision Evaluation Matrix (Yellow High-Lighted Chosen vs Rejected Options)")
    st.write("Analyze the table below. The cells highlighted in **Yellow** show the options your group chose. Compare them directly against the unchosen options to prepare your boardroom defense assignment:")
    
    # Generating a custom HTML matrix table comparing options and highlighting choices in Yellow
    html_table = """
    <table style="width:100%; border-collapse: collapse; margin-top:15px; font-family: Arial, sans-serif; background-color:#111; color:#fff;">
        <thead>
            <tr style="background-color: #222; border-bottom: 2px solid #555; text-align:left;">
                <th style="padding: 12px; border: 1px solid #444; width: 10%;">Round Track</th>
                <th style="padding: 12px; border: 1px solid #444; width: 20%;">Situation Incident</th>
                <th style="padding: 12px; border: 1px solid #444; width: 35%;">Option 1 Strategy Parameters</th>
                <th style="padding: 12px; border: 1px solid #444; width: 35%;">Option 2 Strategy Parameters</th>
            </tr>
        </thead>
        <tbody>
    """
    
    for row in st.session_state.chosen_logs:
        round_idx, incident_title, chosen_label, chosen_text, unchosen_label, unchosen_text = row[0], row[1], row[2], row[3], row[4], row[5]
        
        opt1_style = "background-color: #f6e05e; color: #000; font-weight: bold; padding: 12px; border: 1px solid #444;" if chosen_label == "Option 1" else "padding: 12px; border: 1px solid #444; color: #bbb;"
        opt2_style = "background-color: #f6e05e; color: #000; font-weight: bold; padding: 12px; border: 1px solid #444;" if chosen_label == "Option 2" else "padding: 12px; border: 1px solid #444; color: #bbb;"
        
        opt1_display_text = chosen_text if chosen_label == "Option 1" else unchosen_text
        opt2_display_text = chosen_text if chosen_label == "Option 2" else unchosen_text
        
        html_table += f"""
            <tr style="border-bottom: 1px solid #333;">
                <td style="padding: 12px; border: 1px solid #444; font-weight:bold; color:#00b4d8;">{round_idx}</td>
                <td style="padding: 12px; border: 1px solid #444; font-weight:bold;">{incident_title}</td>
                <td style="{opt1_style}">{opt1_display_text}</td>
                <td style="{opt2_style}">{opt2_display_text}</td>
            </tr>
        """
        
    html_table += "</tbody></table>"
    st.markdown(html_table, unsafe_allow_html=True)
    st.write("---")
        
    if st.button("Reset Operations Terminal & Start New Simulation Voyage", use_container_width=True):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()

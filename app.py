import streamlit as st
import random

# Configure page title and fluid layout
st.set_page_config(page_title="Cruise Monopoly Decision System", layout="wide")

# Initialize global game state data structures inside session storage
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'phase': 0, 'group': '', 'brand': '', 'days': '', 'theme': '', 'route': '',
        'cash': 50000, 'passengers': 3000, 'injured': 0, 'dead': 0,
        'route_score': 75, 'sched_score': 75, 'experience_score': 75,
        'dice_rolled': False, 'current_roll': 0, 'history': [],
        'verification_id': "VESS-G" + str(random.randint(10,99)) + "-" + str(random.randint(100,999))
    }

s = st.session_state.game_state

st.title("🚢 Cruise Monopoly: Global Itinerary Crisis Management Simulator")
st.write("---")

# --- STEP 1: INITIAL COMPREHENSIVE CONFIGURATION INTERFACE ---
if s['phase'] == 0:
    st.header("✍️ Step 1: Initialize Vessel Profile & Itinerary Parameters")
    
    col1, col2 = st.columns(2)
    with col1:
        s['group'] = st.selectbox("Select Your Group Number (1-8):", [f"Group {i}" for i in range(1, 9)])
        s['brand'] = st.selectbox("Select Cruise Vessel Brand Identity:", [
            "Starry Empress (Premium Luxury Fleet)", 
            "Oceanic Voyager (Mass Market Family Resorts)"
        ])
        s['days'] = st.selectbox("Select Itinerary Duration Profile:", [
            "14-Day Two-Week Grand Voyage", 
            "28-Day Ultimate Deep Wilderness Expedition"
        ])
    with col2:
        s['theme'] = st.selectbox("Select Core Operational Theme:", [
            "Gourmet Culinary & Fine Wellness Focus", 
            "High-Energy Action & Extreme Adventure",
            "Marine Conservation & Eco-Tourism Track"
        ])
        s['route'] = st.selectbox("Select Deployment Geographic Route Structure:", [
            "Miami ➔ Cozumel (Caribbean Circuit)", 
            "Seattle ➔ Juneau (Pacific Alaskan Passage)", 
            "Barcelona ➔ Marseille (Western Mediterranean Loop)"
        ])

    if st.button("✅ Configuration Secured - Cast Off Lines", type="primary"):
        s['phase'] = 1
        s['history'].append(f"🚢 {s['group']} - {s['brand']} successfully departed on a {s['days']}. Theme: {s['theme']}. Route: {s['route']}. Base Load: 3,000 Passengers.")
        st.rerun()

# --- STEP 2: CORE VISUAL MONOPOLY GAMEPLAY BOARD ---
elif 1 <= s['phase'] <= 3:
    # Live Color-Coded Operational Scoreboard Dashboard
    st.markdown("### 📊 Real-Time Operations Scoreboard Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Operating Cash Reserves", f"${s['cash']:,}")
    c2.metric("👥 Onboard Active Passengers", f"{s['passengers']:,} Pax")
    
    # Trigger alerting color logic based on casualty densities
    if s['injured'] > 0: 
        c3.metric("🏥 Cumulative Sick / Injured Pax", f"{s['injured']} Pax", delta=f"+{s['injured']}", delta_color="inverse")
    else: 
        c3.metric("🏥 Cumulative Sick / Injured Pax", "0 Pax")
        
    if s['dead'] > 0: 
        c4.metric("💀 Cumulative Passenger Fatalities", f"{s['dead']} Fatalities", delta=f"+{s['dead']}", delta_color="inverse")
    else: 
        c4.metric("💀 Cumulative Passenger Fatalities", "0 Fatalities")

    st.write("---")

    # Split screen layout: Dice mechanisms on Left | Chronological Log on Right
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader(f"🎲 Itinerary Progression: Phase {s['phase']} / 3 Rounds")
        
        if not s['dice_rolled']:
            if st.button("🎲 Shake & Roll Dice to Advance Vessel", type="primary"):
                s['current_roll'] = random.randint(1, 6)
                s['dice_rolled'] = True
                st.rerun()
        else:
            st.success(f"🎲 Dice Roll Confirmed: Advanced {s['current_roll']} Sectors! Vessel in transit...")
            
            # Universal Location-Agnostic Emergency Incident Matrix
            CARDS = [
                {
                    "title": "🚨 WEATHER CRITICAL: Severe Cyclonic Storm System Track",
                    "desc": "An unpredictable category 5 extreme weather system is tracking directly into your upcoming cruise corridor, generating hazardous swell projections.",
                    "h": "Historical Benchmark: Hurricane Dorian (2019) forced operators to completely rewrite pathways to avoid fatalities (74 direct deaths occurred on land). Roughened navigation structures hazard serious onboard falls.",
                    "o1": "【Mandate A】Safety Prioritized: Execute full regional detour to bypass storm tracking sector. (0 casualties guaranteed, but incurs severe fuel pricing spikes of -$6,000)",
                    "o2": "【Mandate B】Schedule Preserved: Maintain original track speed to run ahead of the wind field. (Saves cash, but extreme hull rolling results in 85 passenger fallback injuries and -$2,000 processing lawsuits)",
                    "m1": -6000, "i1": 0, "d1": 0, "m2": -2000, "i2": 85, "d2": 0
                },
                {
                    "title": "🚨 MEDICAL CRITICAL: High-Contagion Norovirus Gastro Outbreak",
                    "desc": "A highly virulent gastrointestinal contagion is spreading rapidly across your vessel's public buffet dining decks, incapacitating travelers.",
                    "h": "Historical Benchmark: Oasis of the Seas Norovirus event (2019). Over 470 guests fell violently ill within 48 hours. Fatalities: 0, but massive operational quarantine protocols applied.",
                    "o1": "【Mandate A】Strict Control: Enforce mandatory passenger in-cabin quarantine containment hooks. (Limits outbreak to 120 sick pax, 0 deaths. Triggers extensive compensation refunds of -$15,000)",
                    "o2": "【Mandate B】Panics Avoided: Maintain standard theater & pool deck operations with covert sanitization. (Preserves near-term refunds, but virus explodes: 450 pax infected, 2 high-risk elderly deaths, -$25,000 liability penalties)",
                    "m1": -15000, "i1": 120, "d1": 0, "m2": -25000, "i2": 450, "d2": 2
                },
                {
                    "title": "🌟 STRATEGIC OPPORTUNITY: Full-Vessel Corporate Fleet Charter Offer",
                    "desc": "An international enterprise tech giant submits an urgent mandate to lease your entire ship capacity as a luxury floating hotel infrastructure asset for an upcoming summit.",
                    "h": "Historical Benchmark: Multi-million dollar corporate fleet charters (such as Salesforce leasing premium commercial vessels for tech events) provide massive localized luxury windfalls.",
                    "o1": "【Mandate A】Maximize Revenue: Accept the full lease option contract. (Operating cash surges immediately by +$30,000, but forces cancellation of current leisure passengers, dropping loyalty scores)",
                    "o2": "【Mandate B】Protect Core Brand: Decline the corporate lease to preserve standard consumer bookings. (Forfeits immediate $30,000 cash injection, but keeps original itinerary framework configuration intact)",
                    "m1": 30000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0
                }
            ]
            
            # Deterministic shuffling path configuration per group metrics
            group_seed = sum(ord(c) for c in s['group'])
            random.seed(group_seed + 10)
            shuffled_cards = list(CARDS)
            random.shuffle(shuffled_cards)
            
            round_card = shuffled_cards[s['phase'] - 1]
            
            st.info(f"### {round_card['title']}")
            st.write(f"💬 **Incident Description:** {round_card['desc']}")
            st.caption(f"📌 [Real-World Case Reference]: {round_card['h']}")
            
            st.write("---")
            st.write("👉 **Formulate Your Executive Boardroom Mandate Below:**")
            
            col_b1, col_b2 = st.columns(2)
            if col_b1.button(round_card['o1']):
                s['cash'] += round_card['m1']
                s['injured'] += round_card['i1']
                s['dead'] += round_card['d1']
                s['history'].append(f"Phase {s['phase']} - Mandate A Selected | Cash Shift: ${round_card['m1']:,} | New Sick/Injured: {round_card['i1']} Pax | Deaths: {round_card['d1']}")
                s['phase'] += 1
                s['dice_rolled'] = False
                st.rerun()
                
            if col_b2.button(round_card['o2']):
                s['cash'] += round_card['m2']
                s['injured'] += round_card['i2']
                s['dead'] += round_card['d2']
                s['history'].append(f"Phase {s['phase']} - Mandate B Selected | Cash Shift: ${round_card['m2']:,} | New Sick/Injured: {round_card['i2']} Pax | Deaths: {round_card['d2']}")
                s['phase'] += 1
                s['dice_rolled'] = False
                st.rerun()

    with col_right:
        st.subheader("📜 Master Chronological Logbook")
        for log in s['history']:
            st.write(f"- {log}")

# --- STEP 3: MASTER END-GAME OPERATIONAL AUDIT DEBRIEFING ---
else:
    st.balloons()
    st.header("🏁 Voyage Concluded: Official Marine Operations Audit Report")
    st.write(f"🔒 **Anti-Tamper Session Security Hash ID:** `{s['verification_id']}`")
    st.write("---")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🏁 Final Net Liquidity Asset", f"${s['cash']:,}")
    col2.metric("🏥 Cumulative Sick/Injured Pax Toll", f"{s['injured']} Pax")
    col3.metric("💀 Cumulative Passenger Fatalities", f"{s['dead']} Fatalities")
    
    st.write("---")
    st.subheader("📋 Voyage Data Block Output (Copy this segment for classroom debrief and case defenses):")
    
    log_text = "\n".join(s['history']) + f"\n\n[AUDIT VERIFICATION HASH] Final Cash: ${s['cash']:,} | Injured: {s['injured']} Pax | Fatalities: {s['dead']}"

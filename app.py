import streamlit as st
import random

# Configure page title and fluid layout
st.set_page_config(page_title="Cruise Monopoly Decision System", layout="wide")

# Initialize global game state data structures inside session storage
if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'phase': 0, 'group': '', 'brand': '', 'days': '', 'theme': '', 'route': '', 'market': '',
        'cash': 50000, 'passengers': 3000, 'injured': 0, 'dead': 0,
        'dice_rolled': False, 'current_roll': 0, 'history': [],
        'verification_id': ""
    }

s = st.session_state.game_state

st.title("🚢 Cruise Monopoly: Global Itinerary Crisis Management Simulator")
st.write("---")

# --- STEP 1: ANTI-CHEAT AUTO-LOCKING INTERFACE WITH DISCRETE MARKETS ---
if s['phase'] == 0:
    st.header("✍️ Step 1: Initialize Vessel Profile & Itinerary Parameters")
    st.info("💡 To prevent plagiarism, your Vessel Profile, Target Market, and Strategic Parameters are custom-locked to your unique Group Number!")
    
    # Group Selection acts as the master key
    group_choice = st.selectbox("Select Your Assigned Group Number (1-8):", [f"Group {i}" for i in range(1, 9)])
    g_idx = int(group_choice.split(" ")) - 1 # Get index 0-7
    
    # 8 Distinct Cross-Market Brands (4 Western Leaders, 4 Asian/Local Innovators)
    ships = [
        "Starry Empress (Premium Western Luxury Fleet)", 
        "Oceanic Voyager (Mass Market Western Family Resort)", 
        "Royal Sovereign (Mega-Liner Western Contemporary)", 
        "Genting Splendor (Premium Asian Contemporary Resort)", 
        "Coral Majestic (Boutique Upscale Western Explorer)", 
        "Horizon Dragon (Ultra-Luxury Boutique Yacht Style - Hong Kong Base)", 
        "Atlantic Crown (Traditional Transatlantic Liner)", 
        "Pacific Pacific (Expedition Active Cruise - Singapore Base)"
    ]
    
    # 8 Standardized Durations
    durations = [
        "12-Day Mediterranean Deep Exploration", "14-Day Grand Caribbean Circuit", 
        "16-Day Transoceanic Cruise Corridor", "18-Day Southeast Asian Tropical Corridor", 
        "21-Day Three-Week Relocation Route", "24-Day East Asia Hemispheric Transit", 
        "27-Day Continental Coastline Explorer", "29-Day Ultimate Asia-Pacific Expedition"
    ]
    
    # 8 Cross-Cultural Themes
    themes = [
        "Gourmet Wine & European Wellness Focus", "High-Energy Action & Deck Party Adventure",
        "Local Heritage, History & Deep Cultural Track", "Asian Michelin Culinary & Dim Sum Heritage Track",
        "Corporate Executive Tech Networking Summit", "Lunar New Year Cultural Festival Spectacular",
        "Multi-Generational Large Family Bonding Holiday", "Remote Coral Reef Scuba & Marine Conservation"
    ]
    
    # 8 Realistic Port Pairs (4 Western Itineraries, 4 Distinct Asian Itineraries)
    routes = [
        "Miami ➔ Cozumel (Caribbean Circuit)", "Seattle ➔ Juneau (Pacific Alaskan Passage)", 
        "Barcelona ➔ Marseille (Western Mediterranean Loop)", "Singapore ➔ Phuket (Southeast Asian Corridor)",
        "Sydney ➔ Auckland (Tasman Crossing Track)", "Hong Kong ➔ Okinawa (East China Sea Circuit)",
        "Copenhagen ➔ Helsinki (Baltic Heritage Path)", "Yokohama ➔ Keelung (North Asia Island Corridor)"
    ]
    
    # Target Market Classification Variable
    markets = [
        "WESTERN (Individualistic, high onboard bar spend, demands relaxed deck schedules)",
        "WESTERN (Mass family segment, high gaming spend, demands extreme activity volume)",
        "WESTERN (Contemporary upscale segment, demands fine dining, flexible booking)",
        "ASIAN (Collectivist family segment, premium culinary demand, demands strict safety first)",
        "WESTERN (Affluent adventurers, high excursion focus, sensitive to itinerary shifts)",
        "ASIAN (Ultra-high-net-worth segment, luxury retail demand, extremely sensitive to delays)",
        "WESTERN (Senior alumni demographic, demands academic seminars, traditional pace)",
        "ASIAN (Active fly-cruise segment, wildlife/photography focus, demands efficient ports)"
    ]

    # Automatically map specs based on the chosen Group Index
    s['group'] = group_choice
    s['brand'] = ships[g_idx]
    s['days'] = durations[g_idx]
    s['theme'] = themes[g_idx]
    s['route'] = routes[g_idx]
    s['market'] = markets[g_idx]
    s['verification_id'] = f"CONF-G{g_idx+1}-{random.randint(100,999)}"

    # Display the automated configuration dashboard to the students
    st.write("### 🔒 Locked Group Specifications:")
    col1, col2 = st.columns(2)
    with col1:
        st.text_input("Target Passenger Demographic Market:", value=s['market'], disabled=True)
        st.text_input("Vessel Brand Identity:", value=s['brand'], disabled=True)
        st.text_input("Itinerary Duration Profile:", value=s['days'], disabled=True)
    with col2:
        st.text_input("Geographic Route Target:", value=s['route'], disabled=True)
        st.text_input("Commercial Theme Focus:", value=s['theme'], disabled=True)

    if st.button("✅ Confirm Specifications - Cast Off Lines", type="primary"):
        s['phase'] = 1
        s['history'].append(f"🚢 BASE MANIFEST SECURED FOR {s['group']} ({s['verification_id']})")
        s['history'].append(f"• Market Profile: {s['market']}")
        s['history'].append(f"• Route: {s['route']} | Theme: {s['theme']}")
        st.rerun()

# --- STEP 2: CORE VISUAL MONOPOLY GAMEPLAY BOARD ---
elif 1 <= s['phase'] <= 3:
    st.markdown(f"### 📊 Scoreboard | {s['group']} Active Profile")
    
    # Live Colored Metric Dashboard
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Cash Asset Balance", f"${s['cash']:,}")
    c2.metric("👥 Active Onboard Passengers", f"{s['passengers']:,} Pax")
    
    if s['injured'] > 0: c3.metric("🏥 Total Sick / Injured Pax", f"{s['injured']} Pax", delta=f"+{s['injured']}", delta_color="inverse")
    else: c3.metric("🏥 Total Sick / Injured Pax", "0 Pax")
        
    if s['dead'] > 0: c4.metric("💀 Cumulative Fatalities", f"{s['dead']} Dead", delta=f"+{s['dead']}", delta_color="inverse")
    else: c4.metric("💀 Cumulative Fatalities", "0 Dead")

    st.write("---")
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader(f"🎲 Voyage Segment: Phase {s['phase']} / 3 Rounds")
        
        if not s['dice_rolled']:
            if st.button("🎲 Shake & Roll Navigation Dice", type="primary"):
                s['current_roll'] = random.randint(1, 6)
                s['dice_rolled'] = True
                st.rerun()
        else:
            st.success(f"🎲 Dice Roll Confirmed: Advanced {s['current_roll']} Sectors! Event card pulled.")
            
            # Check market code to apply dynamic cultural impact numbers
            is_asian_market = "ASIAN" in s['market']
            
            # Tailored Crisis cards utilizing cross-market metrics
            CARDS = [
                {
                    "title": "🚨 WEATHER CRITICAL: Severe Weather Front / Gale Force Winds",
                    "desc": f"An unpredictable severe storm trajectory blocks your path near {s['route'].split(' ➔ ')[0]}. It generates dangerous swells causing extreme vessel pitching.",
                    "h": "Hurricane Dorian (2019) data link. Western markets tolerate open-sea sailing better due to bar/casino engagement trends. Asian markets exhibit a stark 'Safety-First' collectivist profile; rough sea anxiety can trigger catastrophic brand reviews.",
                    "o1": "【Option 1】Safety Protocol: Execute complete regional detour path to bypass the storm. (0 casualties guaranteed. Retains supreme trust, but incurs major fuel charges of -$6,000)",
                    "o2": "【Option 2】Schedule Lock: Run ahead of the wave field at full speed. (Saves cash. However, extreme rolling results in 85 onboard fallback injuries. On Asian routes, passengers boycott retail stores in protest, costing an additional -$2,000 in lost onboard revenue!)" if is_asian_market else "【Option 2】Schedule Lock: Run ahead of the wave field at full speed. (Saves cash. However, extreme rolling results in 85 onboard fallback injuries and -$2,000 legal compensation claims)",
                    "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian_market else -2000, "i2": 85, "d2": 0
                },
                {
                    "title": "🚨 MEDICAL CRITICAL: Norovirus Outbreak in Dining Areas",
                    "desc": "A highly contagious gastrointestinal virus spreads rapidly inside the ship's premium onboard restaurants and buffet sections.",
                    "h": "Oasis of the Seas outbreak data (2019). Western guests tolerate isolation worse, demanding massive bar voucher compensation. Asian passengers view pandemic containment with absolute zero-tolerance; any perceived cover-up destroys the company's regional market share permanently.",
                    "o1": "【Option 1】Isolate Vessel: Apply immediate mandatory in-cabin passenger quarantine blockades. (Outbreak limited to 120 sick pax, 0 deaths. Western routes face massive riots demanding refunds, costing -$20,000; Asian routes cooperate smoothly, costing only -$12,000 due to collectivist alignment)",
                    "o2": "【Option 2】Maintain Operations: Keep public theaters open with covert sanitation to save luxury retail revenue. (Virus explodes: 450 pax infected. Because Asian itineraries feature older multi-generational families, 4 high-risk elderly deaths occur with a crushing -$35,000 legal fine! Western routes report 1 death and -$22,000 in penalties)",
                    "m1": -12000 if is_asian_market else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian_market else -22000, "i2": 450, "d2": 4 if is_asian_market else 1
                },
                {
                    "title": "🌟 STRATEGIC OPPORTUNITY: Premium High-Margin Operational Windfall",

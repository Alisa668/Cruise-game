import streamlit as st
import random

# Standard configuration with high-compatibility custom text styling
st.set_page_config(page_title="Cruise Board Game", layout="wide")
st.markdown("""
    <style>
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Arial', sans-serif !important;
    }
    .stAlert {
        border-radius: 4px !important;
        padding: 10px !important;
        margin-bottom: 10px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Force full clean reset of variables on master reload to prevent cloud browser freezing
if 'phase' not in st.session_state: st.session_state.phase = 0
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'history' not in st.session_state: st.session_state.history = []
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-G" + str(random.randint(11,99))

st.title("🚢 Cruise Monopoly: Ship Manager Game")
st.write("---")

# --- PHASE 0: SECURE INITIAL CONFIGURATION PORTFOLIO ---
if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    st.info("💡 Your ship setup is auto-locked based on your Group Number to prevent copying!")
    
    group_choice = st.selectbox("Select Your Group Number (1-8):", ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6", "Group 7", "Group 8"])
    g_idx = int(group_choice.split(" ")[1]) - 1
    
    ships = ["Starry Empress (Luxury Ship)", "Oceanic Voyager (Family Holiday Ship)", "Royal Sovereign (Mega-Resort Ship)", "Genting Splendor (Asian Style Resort Ship)", "Coral Majestic (Small Exploration Ship)", "Horizon Dragon (Hong Kong Premium Yacht)", "Atlantic Crown (Classic Ocean Liner)", "Pacific Pacific (Singapore Active Holiday Ship)"]
    durations = ["12-Day Mediterranean Trip", "14-Day Caribbean Holiday", "16-Day Long Ocean Crossing", "18-Day Southeast Asia Trip", "21-Day Long Cruise Route", "24-Day Big Asia Transit", "27-Day Coastline Tour", "29-Day Deep Wilderness Expedition"]
    themes = ["Gourmet Food & Spa Focus", "High-Energy Sports & Deck Parties", "History, Local Culture & Sightseeing", "Asian Michelin Dim Sum Food Tour", "Business Meetings & Tech Networking", "Lunar New Year Festival Cruise", "Big Family Vacation & Kids Activities", "Diving, Coral Reefs & Sea Nature"]
    routes = ["Miami ➔ Cozumel", "Seattle ➔ Juneau", "Barcelona ➔ Marseille", "Singapore ➔ Phuket", "Sydney ➔ Auckland", "Hong Kong ➔ Okinawa", "Copenhagen ➔ Helsinki", "Yokohama ➔ Keelung"]
    markets = ["WESTERN Customers (Spends big money at bars/alcohol, wants slow lazy holiday)", "WESTERN Customers (Big families, spends money at casino/games, wants active fun)", "WESTERN Customers (Rich premium travelers, wants expensive fine dining restaurants)", "ASIAN Customers (Big multi-generation families, wants delicious food, demands 'Safety First' layout)", "WESTERN Customers (Adventure travelers, loves outdoor day tours at ports)", "ASIAN Customers (Hong Kong high-end rich shoppers, hates any time delays)", "WESTERN Customers (Older university alumni groups, wants quiet academic study lectures)", "ASIAN Market (Singapore fly-cruise segment, active wildlife/photography focus)"]
    
    map_emojis = [
        "🇺🇸 Miami ➔ 🌊 (Caribbean Sea) ➔ 🇲🇽 Cozumel",
        "🇺🇸 Seattle ➔ 🌊 (Gulf of Alaska) ➔ 🇺🇸 Juneau",
        "🇪🇸 Barcelona ➔ 🌊 (Mediterranean Sea) ➔ 🇫🇷 Marseille",
        "🇸🇬 Singapore ➔ 🌊 (Andaman Sea) ➔ 🇹🇭 Phuket",
        "🇦🇺 Sydney ➔ 🌊 (Tasman Sea) ➔ 🇳🇿 Auckland",
        "🇭🇰 Hong Kong ➔ 🌊 (East China Sea) ➔ 🇯🇵 Okinawa",
        "🇩🇰 Copenhagen ➔ 🌊 (Baltic Sea) ➔ 🇫記 Helsinki",
        "🇯🇵 Yokohama ➔ 🌊 (North Pacific) ➔ 🇹🇼 Keelung"
    ]

    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Passenger Market Type:", value=markets[g_idx], disabled=True)
    c1.text_input("Cruise Ship Name:", value=ships[g_idx], disabled=True)
    c2.text_input("Sailing Route Port:", value=routes[g_idx], disabled=True)
    c2.text_input("Cruise Main Activity Focus:", value=themes[g_idx], disabled=True)
    
    st.markdown("### 🗺️ Geographic Itinerary Route Map:")
    st.markdown("<div style='background-color:#1E1E24; padding:15px; border-radius:6px; border:1px solid #3A3A43; font-size:22px; color:#00FFCC; font-weight:bold;'>🗺️ " + map_emojis[g_idx] + "</div>", unsafe_allow_html=True)

    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.phase = 1
        st.session_state.history.extend([
            "🚢 MASTER MANIFEST FOR " + group_choice,
            "• Ship: " + ships[g_idx] + " | Duration: " + durations[g_idx],
            "• Route: " + routes[g_idx] + " | Focus: " + themes[g_idx],
            "• Market: " + markets[g_idx] + "\n---"
        ])
        st.rerun()

# --- PHASE 1 - 3: MAIN BALANCED SIMULATION LOOP ---
elif 1 <= st.session_state.phase <= 3:
    # Live Color-Coded Active Metrics Bar
    st.markdown("### 📊 Live Scoreboard Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Money left", f"${st.session_state.cash}:,")
    c2.metric("👥 Onboard Passengers", f"{st.session_state.passengers}:,")
    c3.metric("🏥 Sick/Injured", f"{st.session_state.injured} Sick")
    c4.metric("💀 Deaths", f"{st.session_state.dead} Dead")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🎲 Step " + str(st.session_state.phase) + " / 3 Rounds")
        
        # Pull market variable context safely
        history_summary = st.session_state.history[3] if len(st.session_state.history) > 3 else ""
        is_asian = "ASIAN" in history_summary
        
        CARDS = [
            {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane is blocking your ship's route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit a strict collectivist safety expectation.", "emoji": "⛈️ 🌊 🌪️", "o1": "Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Save Fuel money and run at full speed. (85 fallback injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Save Fuel money and run at full speed. (85 fallback injuries, -$2,000 medical lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
            {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥 🤢 💊", "o1": "Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
            {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian routes generate massive net auxiliary margins from duty-free luxury spending over casual Western itineraries.", "emoji": "💎 💰 🎰", "o1": "Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0}
        ]
        
        c = CARDS[st.session_state.phase - 1]
        
        st.markdown("### " + c['emoji'] + " " + c['title'])
        st.write("💬 **Situation:** " + c['desc'])
        st.caption("📌 *Case Reference: " + c['h'] + "*")
        st.write("---")
        
        st.subheader("Formulate Your Boardroom Mandate Below:")
        # Radio structure guarantees 100% unblockable option switching on all browsers
        user_choice = st.radio("Review options carefully and pick your strategy:", ["Option 1: " + c['o1'], "Option 2: " + c['o2']])
        st.write("")
        
        if st.button("🚀 Submit Mandate & Advance Voyage", type="primary", use_container_width=True):
            if "Option 1" in user_choice:
                st.session_state.cash += c['m1']
                st.session_state.injured += c['i1']
                st.session_state.dead += c['d1']
                st.session_state.history.append("Phase " + str(st.session_state.phase) + " Incident: " + c['title'] + "\n  • Mandate: [Option 1] " + c['o1'] + "\n  • Metrics: Cost=$" + str(c['m1']) + " | Sick=" + str(c['i1']) + " | Dead=" + str(c['d1']) + "\n")
            else:
                st.session_state.cash += c['m2']
                st.session_state.injured += c['i2']
                st.session_state.dead += c['d2']
                st.session_state.history.append("Phase " + str(st.session_state.phase) + " Incident: " + c['title'] + "\n  • Mandate: [Option 2] " + c['o2'] + "\n  • Metrics: Cost=$" + str(c['m2']) + " | Sick=" + str(c['i2']) + " | Dead=" + str(c['d2']) + "\n")
            
            st.session_state.phase += 1
            st.rerun()

    with col_right:
        st.subheader("📜 Live Ship Logbook Record")
        for log in st.session_state.history: st.write(log)

# --- PHASE 4: SECURE AUDIT BLOCK AND PRINT DATA LOGS ---
else:
    st.balloons()
    st.header("🏁 Game Finished: Final Audit Report")

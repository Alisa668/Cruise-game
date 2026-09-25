import streamlit as st
import random

st.set_page_config(page_title="Cruise Game", layout="wide")

# Initialize and lock all base session state memory slots defensively
if 'phase' not in st.session_state: st.session_state.phase = 0
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'history' not in st.session_state: st.session_state.history = []
if 'user_selection' not in st.session_state: st.session_state.user_selection = None
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-" + str(random.randint(100,999))

st.title("🚢 Cruise Monopoly: Ship Manager Game")
st.write("---")

# --- STEP 1: INITIAL CONFIGURATION INTERFACE ---
if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    
    group_choice = st.selectbox("Select Your Group Number (1-8):", ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6", "Group 7", "Group 8"])
    
    g_idx = 0
    if "2" in group_choice: g_idx = 1
    elif "3" in group_choice: g_idx = 2
    elif "4" in group_choice: g_idx = 3
    elif "5" in group_choice: g_idx = 4
    elif "6" in group_choice: g_idx = 5
    elif "7" in group_choice: g_idx = 6
    elif "8" in group_choice: g_idx = 7
    
    ships = ["Starry Empress (Luxury Ship)", "Oceanic Voyager (Family Ship)", "Royal Sovereign (Mega-Resort Ship)", "Genting Splendor (Asian Style Ship)", "Coral Majestic (Exploration Ship)", "Horizon Dragon (Hong Kong Yacht)", "Atlantic Crown (Classic Ocean Liner)", "Pacific Pacific (Singapore Active Ship)"]
    durations = ["12-Day Mediterranean Trip", "14-Day Caribbean Holiday", "16-Day Long Ocean Crossing", "18-Day Southeast Asia Trip", "21-Day Long Cruise Route", "24-Day Big Asia Transit", "27-Day Coastline Tour", "29-Day Deep Wilderness Expedition"]
    themes = ["Gourmet Food & Spa Focus", "High-Energy Sports & Deck Parties", "History, Local Culture & Sightseeing", "Asian Michelin Dim Sum Food Tour", "Business Meetings & Tech Networking", "Lunar New Year Festival Cruise", "Big Family Vacation & Kids Activities", "Diving, Coral Reefs & Sea Nature"]
    routes = ["Miami to Cozumel (Caribbean Circuit)", "Seattle to Juneau (Alaskan Passage)", "Barcelona to Marseille (Western Med Loop)", "Singapore to Phuket (Southeast Asian)", "Sydney to Auckland (Tasman Crossing)", "Hong Kong to Okinawa (East China Sea)", "Copenhagen to Helsinki (Baltic Heritage)", "Yokohama to Keelung (North Asia Island)"]
    markets = ["WESTERN Customers (High bar spend, wants lazy holiday)", "WESTERN Customers (Mass family, high casino spend, active fun)", "WESTERN Customers (Rich premium travelers, fine dining restaurants)", "ASIAN Customers (Big families, delicious food, demands Safety First)", "WESTERN Customers (Adventure travelers, loves outdoor day tours)", "ASIAN Customers (Hong Kong high-end rich shoppers, hates time delays)", "WESTERN Customers (Older alumni groups, wants academic study lectures)", "ASIAN Market (Singapore segment, wildlife photography tours)"]
    
    map_tracks = [
        "📍 USA (Miami) ================ Sailing Caribbean Sea ================> MEXICO (Cozumel) 🏁",
        "📍 USA (Seattle) ================ Sailing Gulf of Alaska ================> ALASKA (Juneau) 🏁",
        "📍 SPAIN (Barcelona) ================ Sailing Mediterranean ================> FRANCE (Marseille) 🏁",
        "📍 SINGAPORE Base ================ Sailing Andaman Sea ================> THAILAND (Phuket) 🏁",
        "📍 AUSTRALIA (Sydney) ================ Sailing Tasman Sea ================> NEW ZEALAND (Auckland) 🏁",
        "📍 HONG KONG Base ================ Sailing East China Sea ================> JAPAN (Okinawa) 🏁",
        "📍 DENMARK (Copenhagen) ================ Sailing Baltic Sea ================> FINLAND (Helsinki) 🏁",
        "📍 JAPAN (Yokohama) ================ Sailing North Pacific ================> TAIWAN (Keelung) 🏁"
    ]

    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Passenger Market Type:", value=markets[g_idx], disabled=True)
    c1.text_input("Cruise Ship Name:", value=ships[g_idx], disabled=True)
    c2.text_input("Sailing Route Port:", value=routes[g_idx], disabled=True)
    c2.text_input("Cruise Main Activity Focus:", value=themes[g_idx], disabled=True)
    
    # 100% Reliable Local Render Graphic Route Box
    st.markdown("### 🗺️ Geographic Itinerary Route Map:")
    st.markdown("<div style='background-color:#1E1E24; padding:20px; border-radius:8px; border:2px solid #00FFCC; font-size:20px; font-family:monospace; color:#00FFCC; font-weight:bold; text-align:center;'>" + map_tracks[g_idx] + "</div>", unsafe_allow_html=True)

    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.phase = 1
        st.session_state.history.extend([
            "🚢 MANIFEST LOCKED FOR: " + group_choice + " (ID: " + st.session_state.v_id + ")",
            "• Vessel Identity: " + ships[g_idx] + " | Duration: " + durations[g_idx],
            "• Route Target: " + routes[g_idx] + " | Focus Theme: " + themes[g_idx],
            "• Demographics Profile: " + markets[g_idx] + "\n---"
        ])
        st.rerun()

# --- STEP 2: CRISIS RUN ENGINE ROUNDS ---
elif 1 <= st.session_state.phase <= 3:
    st.markdown("### 📊 Live Scoreboard Dashboard")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Money left", f"${st.session_state.cash:,}")
    c2.metric("👥 Passengers", f"{st.session_state.passengers:,} Pax")
    c3.metric("🏥 Sick/Injured", f"{st.session_state.injured} Sick")
    c4.metric("💀 Deaths", f"{st.session_state.dead} Dead")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader("🎲 Step " + str(st.session_state.phase) + " / 3 Rounds")
        
        # Safe cross-market boolean parsing
        history_summary = " ".join(st.session_state.history)
        is_asian = "ASIAN" in history_summary
        
        CARDS = [
            {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane is blocking your ship's route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit a strict collectivist safety expectation.", "emoji": "⛈️ 🌊 🌪️", "o1": "Option 1: Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Option 2: Save Fuel money and run at full speed. (85 fallback injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Option 2: Save Fuel money and run at full speed. (85 fallback injuries, -$2,000 medical lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
            {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥 🤢 💊", "o1": "Option 1: Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Option 2: Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
            {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian routes generate massive net auxiliary margins from duty-free luxury spending over casual Western itineraries.", "emoji": "💎 💰 🎰", "o1": "Option 1: Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Option 2: Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0}
        ]
        
        c = CARDS[st.session_state.phase - 1]
        
        st.markdown("### " + c['emoji'] + " " + c['title'])
        st.write("💬 **Situation:** " + c['desc'])
        st.caption("📌 *Case Benchmark: " + c['h'] + "*")
        st.write("---")
        
        st.write("👉 **Review Options Carefully:**")
        st.info("🔴 " + c['o1'])
        st.info("🔵 " + c['o2'])
        
        b1, b2 = st.columns(2)
        if b1.button("🔴 Pick Option 1", use_container_width=True):
            st.session_state.user_selection = "1"
        if b2.button("🔵 Pick Option 2", use_container_width=True):
            st.session_state.user_selection = "2"
            
        st.write("---")
        if st.session_state.user_selection:
            sel = st.session_state.user_selection
            st.warning("🎯 **Ready to Submit:** Option " + sel)
            
            if st.button("🚀 Confirm the decision and run it", type="primary", use_container_width=True):
                if sel == "1":
                    st.session_state.cash += c['m1']
                    st.session_state.injured += c['i1']
                    st.session_state.dead += c['d1']
                    st.session_state.history.append("Phase " + str(st.session_state.phase) + " | Strategy: Option 1 | Money Shift: $" + str(c['m1']) + " | Injured: +" + str(c['i1']) + " | Dead: +" + str(c['d1']))
                else:
                    st.session_state.cash += c['m2']
                    st.session_state.injured += c['i2']
                    st.session_state.dead += c['d2']

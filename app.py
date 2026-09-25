import streamlit as st
import random

st.set_page_config(page_title="Cruise Game", layout="wide")

# Extreme layout compression to force all elements onto a single screen height
st.markdown("""
    <style>
    html, body, p, span, div, h1, h2, h3 { 
        font-family: 'Arial', sans-serif !important; 
    }
    .stAlert { border-radius: 4px !important; padding: 6px !important; margin-bottom: 4px !important; }
    div[data-testid="stVerticalBlock"] > div { margin-bottom: -15px !important; padding-bottom: 0px !important; }
    div[block-container] { padding-top: 1rem !important; padding-bottom: 0rem !important; }
    </style>
""", unsafe_allow_html=True)

if 'phase' not in st.session_state: st.session_state.phase = 0
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'history' not in st.session_state: st.session_state.history = []
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-G" + str(random.randint(11,99))

st.title("🚢 Cruise Monopoly: Ship Manager Game")
st.write("---")

if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    st.info("💡 Your ship setup is auto-locked based on your Group Number to prevent copying!")
    
    group_choice = st.selectbox("Select Your Group Number (1-8):", ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6", "Group 7", "Group 8"])
    
    if group_choice == "Group 1":
        m_txt, s_txt, r_txt, t_txt = "WESTERN Market (High bar spend)", "Starry Empress (Luxury Ship)", "Miami to Cozumel (Caribbean)", "Gourmet Food & Spa Focus"
        map_line = "🇺🇸 Miami ➔ 🌊 (Caribbean Sea) ➔ 🇲🇽 Cozumel"
    elif group_choice == "Group 2":
        m_txt, s_txt, r_txt, t_txt = "WESTERN Market (Mass family resort)", "Oceanic Voyager (Family Ship)", "Seattle to Juneau (Alaska)", "High-Energy Sports & Deck Parties"
        map_line = "🇺🇸 Seattle ➔ 🌊 (Gulf of Alaska) ➔ 🇺🇸 Juneau"
    elif group_choice == "Group 3":
        m_txt, s_txt, r_txt, t_txt = "WESTERN Market (Rich premium travelers)", "Royal Sovereign (Mega-Resort Ship)", "Barcelona to Marseille (Med Loop)", "History, Local Culture & Sightseeing"
        map_line = "🇪🇸 Barcelona ➔ 🌊 (Mediterranean Sea) ➔ 🇫🇷 Marseille"
    elif group_choice == "Group 4":
        m_txt, s_txt, r_txt, t_txt = "ASIAN Market (Big families, Safety First)", "Genting Splendor (Asian Style Ship)", "Singapore to Phuket (Andaman Sea)", "Asian Michelin Dim Sum Food Tour"
        map_line = "🇸🇬 Singapore ➔ 🌊 (Andaman Sea) ➔ 🇹🇭 Phuket"
    elif group_choice == "Group 5":
        m_txt, s_txt, r_txt, t_txt = "WESTERN Market (Adventure travelers)", "Coral Majestic (Exploration Ship)", "Sydney to Auckland (Tasman Sea)", "Business Meetings & Tech Networking"
        map_line = "🇦🇺 Sydney ➔ 🌊 (Tasman Sea) ➔ 🇳🇿 Auckland"
    elif group_choice == "Group 6":
        m_txt, s_txt, r_txt, t_txt = "ASIAN Market (Hong Kong rich shoppers)", "Horizon Dragon (Hong Kong Yacht)", "Hong Kong to Okinawa (East China Sea)", "Lunar New Year Festival Cruise"
        map_line = "🇭🇰 Hong Kong ➔ 🌊 (East China Sea) ➔ 🇯🇵 Okinawa"
    elif group_choice == "Group 7":
        m_txt, s_txt, r_txt, t_txt = "WESTERN Market (Older alumni groups)", "Atlantic Crown (Classic Ocean Liner)", "Copenhagen to Helsinki (Baltic Sea)", "Big Family Vacation & Kids Activities"
        map_line = "🇩🇰 Copenhagen ➔ 🌊 (Baltic Sea) ➔ 🇫🇮 Helsinki"
    else:
        m_txt, s_txt, r_txt, t_txt = "ASIAN Market (Singapore segment, wildlife)", "Pacific Pacific (Singapore Active Ship)", "Yokohama to Keelung (North Pacific)", "Diving, Coral Reefs & Sea Nature"
        map_line = "🇯🇵 Yokohama ➔ 🌊 (North Pacific) ➔ 🇹🇼 Keelung"

    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Passenger Market Type:", value=m_txt, disabled=True)
    c1.text_input("Cruise Ship Name:", value=s_txt, disabled=True)
    c2.text_input("Sailing Route Port:", value=r_txt, disabled=True)
    c2.text_input("Cruise Main Activity Focus:", value=t_txt, disabled=True)
    
    st.markdown("### 🗺️ Geographic Itinerary Route Map:")
    st.markdown("<div style='background-color:#1E1E24; padding:10px; border-radius:4px; border:1px solid #3A3A43; font-size:18px; font-family:monospace; color:#00FFCC; font-weight:bold; text-align:center;'>🗺️ " + map_line + "</div>", unsafe_allow_html=True)

    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.phase = 1
        st.session_state.history.extend([
            "🚢 MANIFEST LOCKED FOR: " + group_choice + " (ID: " + st.session_state.v_id + ")",
            "• Vessel Identity: " + s_txt,
            "• Route Target: " + r_txt + " | Focus Theme: " + t_txt,
            "• Demographics Profile: " + m_txt + "\n---"
        ])
        st.rerun()

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
        history_summary = " ".join(st.session_state.history)
        is_asian = "ASIAN" in history_summary
        
        CARDS = [
            {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane is blocking your ship's route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit strict safety expectations.", "emoji": "⛈️ 🌊 🌪️", "o1": "Option 1: Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Option 2: Save Fuel money and run at full speed. (85 injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Option 2: Save Fuel money and run at full speed. (85 injuries, -$2,000 lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
            {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥 🤢 💊", "o1": "Option 1: Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Option 2: Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
            {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian routes generate massive net auxiliary margins from duty-free luxury spending over casual Western itineraries.", "emoji": "💎 💰 🎰", "o1": "Option 1: Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Option 2: Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0}
        ]
        
        c = CARDS[st.session_state.phase - 1]
        st.markdown("### " + c['emoji'] + " " + c['title'])
        st.write("💬 **Situation:** " + c['desc'])
        st.caption("📌 *Case Benchmark: " + c['h'] + "*")
        st.write("---")
        
        with st.form(key=f"round_form_{st.session_state.phase}", clear_on_submit=True):
            st.info("🔴 " + c['o1'])
            st.info("🔵 " + c['o2'])
            user_choice = st.radio("Select your team's strategy:", ["Option 1", "Option 2"])
            submit_decision = st.form_submit_button("🚀 Confirm the decision and run it", use_container_width=True)
            
            if submit_decision:
                if "Option 1" in user_choice:
                    st.session_state.cash += c['m1']; st.session_state.injured += c['i1']; st.session_state.dead += c['d1']
                    st.session_state.history.append("Phase " + str(st.session_state.phase) + " | Strategy: Option 1 | Money Shift: $" + str(c['m1']) + " | Injured: +" + str(c['i1']))
                else:
                    st.session_state.cash += c['m2']; st.session_state.injured += c['i2']; st.session_state.dead += c['d2']
                    st.session_state.history.append("Phase " + str(st.session_state.phase) + " | Strategy: Option 2 | Money Shift: $" + str(c['m2']) + " | Injured: +" + str(c['i2']))
                st.session_state.phase += 1
                st.rerun()

    with col_right:
        st.subheader("📜 Live Ship Logbook Record")
        for log in st.session_state.history: st.write(log)

else:
    st.balloons()
    st.header("🏁 Game Finished: Final Audit Report")
    st.write("🔒 **Session Security ID:** `" + st.session_state.v_id + "`")
    st.write("---")
    col1, col2, col3 = st.columns(3)
    col1.metric("🏁 Final Money Balance", f"${st.session_state.cash:,}")
    col2.metric("🏥 Total Sick / Injured Pax", f"{st.session_state.injured} People")
    col3.metric("💀 Total Passenger Deaths", f"{st.session_state.dead} Deaths")
    st.write("---")
    st.subheader("📋 Copy this log block below for your presentation assignment:")

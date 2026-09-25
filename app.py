import streamlit as st
import random

# Force unified clean font style and grid containers layout globally
st.set_page_config(page_title="Cruise Board Game", layout="wide")
st.markdown("""
    <style>
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Arial', sans-serif !important;
    }
    .stAlert {
        border-radius: 4px !important;
        padding: 12px !important;
        margin-bottom: 12px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize master state properties using clean structural variables to prevent cache corruption
if 'phase' not in st.session_state: st.session_state.phase = 0
if 'group' not in st.session_state: st.session_state.group = ""
if 'brand' not in st.session_state: st.session_state.brand = ""
if 'days' not in st.session_state: st.session_state.days = ""
if 'theme' not in st.session_state: st.session_state.theme = ""
if 'route' not in st.session_state: st.session_state.route = ""
if 'market' not in st.session_state: st.session_state.market = ""
if 'map_track' not in st.session_state: st.session_state.map_track = ""
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'chosen_logs' not in st.session_state: st.session_state.chosen_logs = []
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-G" + str(random.randint(11,99)) + "-" + str(random.randint(100,999))

GROUP_DATA = {
    "Group 1": {"brand": "Starry Empress", "duration": "12-Day Mediterranean Trip", "theme": "Gourmet Food & Spa Focus", "route": "Miami to Cozumel", "market": "WESTERN Market (High bar spend, wants slow lazy holiday)", "map": "🇺🇸 Miami ➔ 🌊 (Sailing Caribbean Sea) ➔ 🇲🇽 Cozumel"},
    "Group 2": {"brand": "Oceanic Voyager", "duration": "14-Day Caribbean Holiday", "theme": "High-Energy Sports & Deck Parties", "route": "Seattle to Juneau", "market": "WESTERN Market (Mass family, high casino spend, active fun)", "map": "🇺🇸 Seattle ➔ 🌊 (Sailing Gulf of Alaska) ➔ 🇺🇸 Juneau"},
    "Group 3": {"brand": "Royal Sovereign", "duration": "16-Day Long Ocean Crossing", "theme": "History, Local Culture & Sightseeing", "route": "Barcelona to Marseille", "market": "WESTERN Market (Rich premium travelers, fine dining)", "map": "🇪🇸 Barcelona ➔ 🌊 (Sailing Mediterranean Sea) ➔ 🇫🇷 Marseille"},
    "Group 4": {"brand": "Genting Splendor", "duration": "18-Day Southeast Asia Trip", "theme": "Asian Michelin Dim Sum Food Tour", "route": "Singapore to Phuket", "market": "ASIAN Market (Big families, delicious food, Safety First)", "map": "🇸🇬 Singapore Base ➔ 🌊 (Sailing Andaman Sea) ➔ 🇹🇭 Phuket"},
    "Group 5": {"brand": "Coral Majestic", "duration": "21-Day Long Cruise Route", "theme": "Business Meetings & Tech Networking", "route": "Sydney to Auckland", "market": "WESTERN Market (Adventure travelers, loves outdoor tours)", "map": "🇦🇺 Sydney ➔ 🌊 (Sailing Tasman Sea) ➔ 🇳🇿 Auckland"},
    "Group 6": {"brand": "Horizon Dragon", "duration": "24-Day Big Asia Transit", "theme": "Lunar New Year Festival Cruise", "route": "Hong Kong to Okinawa", "market": "ASIAN Market (Hong Kong high-end rich shoppers, hates delays)", "map": "🇭🇰 Hong Kong Base ➔ 🌊 (Sailing East China Sea) ➔ 🇯🇵 Okinawa"},
    "Group 7": {"brand": "Atlantic Crown", "duration": "27-Day Coastline Tour", "theme": "Big Family Vacation & Kids Activities", "market": "WESTERN Market (Older alumni groups, wants lectures)", "map": "🇩🇰 Copenhagen ➔ 🌊 (Sailing Baltic Sea) ➔ 🇫🇮 Helsinki"},
    "Group 8": {"brand": "Pacific Pacific", "duration": "29-Day Deep Wilderness Expedition", "theme": "Diving, Coral Reefs & Sea Nature", "market": "ASIAN Market (Singapore segment, wildlife photography tours)", "map": "🇯🇵 Yokohama ➔ 🌊 (Sailing North Pacific) ➔ 🇹🇼 Keelung"}
}

# --- STEP 1: INITIAL REGISTRATION FRONT PAGE ---
if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    
    group_choice = st.selectbox("Select Your Group Number (1-8):", list(GROUP_DATA.keys()))
    cfg = GROUP_DATA[group_choice]
    
    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Group Assignment Name:", value=group_choice, disabled=True)
    c1.text_input("Cruise Name:", value=f"{cfg['brand']} ({group_choice})", disabled=True)
    c1.text_input("Cruise Theme Focus:", value=cfg['theme'], disabled=True)
    c2.text_input("Demographic Profile:", value=cfg['market'], disabled=True)
    c2.text_input("Cruise Itinerary Route:", value=cfg['map'], disabled=True)
    
    st.markdown("### 🗺️ Geographic Itinerary Route Map:")
    st.markdown("<div style='background-color:#1E1E24; padding:15px; border-radius:6px; border:1px solid #3A3A43; font-size:18px; font-family:monospace; color:#00FFCC; font-weight:bold; text-align:center;'>🗺️ " + cfg['map'] + "</div>", unsafe_allow_html=True)
    
    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.group = group_choice
        st.session_state.brand = f"{cfg['brand']} ({group_choice})"
        st.session_state.days = cfg['duration']
        st.session_state.theme = cfg['theme']
        st.session_state.route = cfg['map']
        st.session_state.market = cfg['market']
        st.session_state.phase = 1
        st.rerun()

# --- STEP 2 & 3: CORE INTERACTIVE BALLOT PLATFORM ---
elif 1 <= st.session_state.phase <= 3:
    st.markdown(f"### 📊 Scoreboard | {st.session_state.group} Active Profile")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Money left", f"${st.session_state.cash:,}")
    c2.metric("👥 Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    c3.metric("🏥 Sick/Injured", f"{st.session_state.injured} Sick")
    c4.metric("💀 Deaths", f"{st.session_state.dead} Dead")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader(f"🎲 Round {st.session_state.phase} / 3")
        is_asian = "ASIAN" in st.session_state.market
        
        CARDS = [
            {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane blocks your ship's direct route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit strict safety expectations.", "emoji": "⛈️", "o1": "Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Save Fuel money and run at full speed. (85 injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Save Fuel money and run at full speed. (85 injuries, -$2,000 lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
            {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥", "o1": "Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
            {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian cruise markets derive high auxiliary margins from luxury retail turnover over Western casual paths.", "emoji": "💎", "o1": "Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0}
        ]
        
        c = CARDS[st.session_state.phase - 1]
        st.markdown(f"### {c['emoji']} {c['title']}")
        st.write(f"💬 **Current Situation:** {c['desc']}")
        st.caption(f"📌 *Case Benchmark: {c['h']}*")
        st.write("---")
        
        st.write("### 🔴 Review Options Carefully:")
        st.info(f"👉 **Option 1:** {c['o1']}")
        st.info(f"👉 **Option 2:** {c['o2']}")
        
        st.write("### 🗔 Cast Your Boardroom Decision Below:")
        user_choice = st.radio("Select your strategy choice:", ["Option 1", "Option 2"], key=f"radio_phase_{st.session_state.phase}")
        st.write("---")
        
        if st.button("🚀 Confirm the decision and run it", type="primary", use_container_width=True, key=f"btn_phase_{st.session_state.phase}"):
            if "Option 1" in user_choice:
                chosen_cost = c['m1']
                chosen_injury = c['i1']
                chosen_death = c['d1']
                chosen_text = c['o1']
            else:
                chosen_cost = c['m2']
                chosen_injury = c['i2']
                chosen_death = c['d2']
                chosen_text = c['o2']
                
            st.session_state.cash += chosen_cost
            st.session_state.injured += chosen_injury
            st.session_state.dead += chosen_death
            
            # Log choices clearly for final report use
            st.session_state.chosen_logs.append({
                "round": st.session_state.phase,
                "title": c['title'],
                "choice_made": user_choice,
                "description": chosen_text,
                "cost": chosen_cost,
                "injuries": chosen_injury,
                "deaths": chosen_death
            })
            

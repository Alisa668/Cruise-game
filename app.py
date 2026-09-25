import streamlit as st
import random

st.set_page_config(page_title="Cruise Board Game", layout="wide")
st.markdown("""
    <style>
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Arial', sans-serif !important;
    }
    .stAlert {
        border-radius: 4px !important;
        padding: 8px !important;
        margin-bottom: 8px !important;
    }
    div[data-testid="stVerticalBlock"] > div {
        margin-bottom: -10px !important;
        padding-bottom: 0px !important;
    }
    </style>
""", unsafe_allow_html=True)

if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'phase': 0, 'group': '', 'brand': '', 'days': '', 'theme': '', 'route': '', 'market': '',
        'cash': 50000, 'passengers': 3000, 'injured': 0, 'dead': 0,
        'dice_rolled': False, 'current_roll': 0, 'history': [], 'verification_id': ""
    }

s = st.session_state.game_state
st.title("🚢 Cruise Monopoly: Ship Manager Game")
st.write("---")

if s['phase'] == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    st.info("💡 Your ship setup is auto-locked based on your Group Number to prevent copying!")
    
    group_choice = st.selectbox("Select Your Group Number (1-8):", ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6", "Group 7", "Group 8"])
    
    g_idx = 0
    if "2" in group_choice: g_idx = 1
    elif "3" in group_choice: g_idx = 2
    elif "4" in group_choice: g_idx = 3
    elif "5" in group_choice: g_idx = 4
    elif "6" in group_choice: g_idx = 5
    elif "7" in group_choice: g_idx = 6
    elif "8" in group_choice: g_idx = 7
    
    ships = ["Starry Empress (Luxury Ship)", "Oceanic Voyager (Family Holiday Ship)", "Royal Sovereign (Mega-Resort Ship)", "Genting Splendor (Asian Style Resort Ship)", "Coral Majestic (Small Exploration Ship)", "Horizon Dragon (Hong Kong Premium Yacht)", "Atlantic Crown (Classic Ocean Liner)", "Pacific Pacific (Singapore Active Holiday Ship)"]
    durations = ["12-Day Mediterranean Trip", "14-Day Caribbean Holiday", "16-Day Long Ocean Crossing", "18-Day Southeast Asia Trip", "21-Day Long Cruise Route", "24-Day Big Asia Transit", "27-Day Coastline Tour", "29-Day Deep Wilderness Expedition"]
    themes = ["Gourmet Food & Spa Focus", "High-Energy Sports & Deck Parties", "History, Local Culture & Sightseeing", "Asian Michelin Dim Sum Food Tour", "Business Meetings & Tech Networking", "Lunar New Year Festival Cruise", "Big Family Vacation & Kids Activities", "Diving, Coral Reefs & Sea Nature"]
    routes = ["Miami ➔ Cozumel", "Seattle ➔ Juneau", "Barcelona ➔ Marseille", "Singapore ➔ Phuket", "Sydney ➔ Auckland", "Hong Kong ➔ Okinawa", "Copenhagen ➔ Helsinki", "Yokohama ➔ Keelung"]
    markets = ["WESTERN Customers (Spends big money at bars/alcohol, wants slow lazy holiday)", "WESTERN Customers (Big families, spends money at casino/games, wants active fun)", "WESTERN Customers (Rich premium travelers, wants expensive fine dining restaurants)", "ASIAN Customers (Big multi-generation families, wants delicious food, demands 'Safety First' layout)", "WESTERN Customers (Adventure travelers, loves outdoor day tours at ports)", "ASIAN Customers (Hong Kong high-end rich shoppers, hates any time delays)", "WESTERN Customers (Older university alumni groups, wants quiet academic study lectures)", "ASIAN Market (Singapore fly-cruise segment, active wildlife/photography focus)"]

    # Deployed 100% stable global vector maps for non-blocking browser loading
    map_emojis = [
        "🇺🇸 Miami ➔ 🌊 (Caribbean Sea) ➔ 🇲🇽 Cozumel",
        "🇺🇸 Seattle ➔ 🌊 (Gulf of Alaska) ➔ 🇺🇸 Juneau",
        "🇪🇸 Barcelona ➔ 🌊 (Mediterranean Sea) ➔ 🇫🇷 Marseille",
        "🇸🇬 Singapore ➔ 🌊 (Andaman Sea) ➔ 🇹🇭 Phuket",
        "🇦🇺 Sydney ➔ 🌊 (Tasman Sea) ➔ 🇳🇿 Auckland",
        "🇭🇰 Hong Kong ➔ 🌊 (East China Sea) ➔ 🇯🇵 Okinawa",
        "🇩🇰 Copenhagen ➔ 🌊 (Baltic Sea) ➔ 🇫🇮 Helsinki",
        "🇯🇵 Yokohama ➔ 🌊 (North Pacific) ➔ 🇹🇼 Keelung"
    ]

    s.update({'group': group_choice, 'brand': ships[g_idx], 'days': durations[g_idx], 'theme': themes[g_idx], 'route': routes[g_idx], 'market': markets[g_idx], 'verification_id': f"CODE-G{g_idx+1}-{random.randint(100,999)}"})

    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Passenger Market Type:", value=s['market'], disabled=True)
    c1.text_input("Cruise Ship Name:", value=s['brand'], disabled=True)
    c2.text_input("Sailing Route Port:", value=s['route'], disabled=True)
    c2.text_input("Cruise Main Activity Focus:", value=s['theme'], disabled=True)
    
    st.markdown("### 🗺️ Geographic Itinerary Route Map:")
    # Render large clean visual route track block
    st.markdown(f"<div style='background-color:#1E1E24; padding:15px; border-radius:6px; border:1px solid #3A3A43; font-size:24px; color:#00FFCC; font-weight:bold;'>🗺️ {map_emojis[g_idx]}</div>", unsafe_allow_html=True)

    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        s['phase'] = 1
        s['history'].extend([f"🚢 MASTER MANIFEST FOR {s['group']} ({s['verification_id']})", f"• Ship: {s['brand']} | Duration: {s['days']}", f"• Route Route: {s['route']} | Focus: {s['theme']}", f"• Market Profile: {s['market']}\n---"])
        st.rerun()

elif 1 <= s['phase'] <= 3:
    st.markdown(f"### 📊 Dashboard Status | {s['group']}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Money left", f"${s['cash']:,}")
    c2.metric("👥 Passengers", f"{s['passengers']:,} Pax")
    c3.metric("🏥 Sick/Injured", f"{s['injured']} Sick", delta=f"+{s['injured']}" if s['injured'] > 0 else None, delta_color="inverse")
    c4.metric("💀 Deaths", f"{s['dead']} Dead", delta=f"+{s['dead']}" if s['dead'] > 0 else None, delta_color="inverse")

    st.write("---")
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader(f"🎲 Step {s['phase']} / 3 Rounds")
        if not s['dice_rolled']:
            if st.button("🎲 Click Here to Roll the Dice", type="primary", use_container_width=True):
                s['current_roll'], s['dice_rolled'] = random.randint(1, 6), True
                st.rerun()
        else:
            is_asian = "ASIAN" in s['market']
            CARDS = [
                {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane is blocking your ship's route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit a strict collectivist safety expectation.", "emoji": "⛈️ 🌊 🌪️", "o1": "Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Save Fuel money and run at full speed. (85 fallback injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Save Fuel money and run at full speed. (85 fallback injuries, -$2,000 medical lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
                {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥 🤢 💊", "o1": "Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
                {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian routes generate massive net auxiliary margins from luxury spending over casual Western itineraries.", "emoji": "💎 💰 🎰", "o1": "Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0}
            ]
            
            g_num_val = 1
            if "2" in s['group']: g_num_val = 2
            elif "3" in s['group']: g_num_val = 3
            elif "4" in s['group']: g_num_val = 4
            elif "5" in s['group']: g_num_val = 5
            elif "6" in s['group']: g_num_val = 6
            elif "7" in s['group']: g_num_val = 7
            elif "8" in s['group']: g_num_val = 8
            
            random.seed(g_num_val + 88)
            shuffled_cards = list(CARDS)
            random.shuffle(shuffled_cards)
            c = shuffled_cards[s['phase'] - 1]
            
            st.markdown(f"### {c['emoji']} {c['title']}")
            st.write(f"🌍 **Passenger Profile:** `{s['market']}`")
            st.write(f"💬 **Current Situation:** {c['desc']}")
            st.caption(f"📌 *Case History: {c['h']}*")
            st.write("---")
            
            st.success(f"👉 **Option 1:** {c['o1']}")
            st.success(f"👉 **Option 2:** {c['o2']}")
            
            if st.button("🔴 Choose Option 1", use_container_width=True):
                s['cash'] += c['m1']; s['injured'] += c['i1']; s['dead'] += c['d1']
                s['history'].append(f"Phase {s['phase']} Incident: {c['title']}\n  • Your Strategy: [Option 1] {c['o1']}\n  • Financial Cost: ${c['m1']:,} | Sick/Injured: +{c['i1']} | Deaths: +{c['d1']}\n")
                s['phase'] += 1; s['dice_rolled'] = False; st.rerun()
            if st.button("🔵 Choose Option 2", use_container_width=True):
                s['cash'] += c['m2']; s['injured'] += c['i2']; s['dead'] += c['d2']

import streamlit as st
import random

# Global uniform font styling and spacing optimization
st.set_page_config(page_title="Cruise Board Game", layout="wide")
st.markdown("""
    <style>
    html, body, [data-testid="stMarkdownContainer"], p, span, div, h1, h2, h3 {
        font-family: 'Arial', sans-serif !important;
    }
    .stAlert {
        border-radius: 6px !important;
        padding: 12px !important;
        margin-bottom: 12px !important;
    }
    div.stButton > button {
        font-size: 16px !important;
        font-weight: bold !important;
        padding: 10px 20px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Master database initializations with defensive state caching to prevent empty final screens
if 'phase' not in st.session_state: st.session_state.phase = 0
if 'cash' not in st.session_state: st.session_state.cash = 50000
if 'passengers' not in st.session_state: st.session_state.passengers = 3000
if 'injured' not in st.session_state: st.session_state.injured = 0
if 'dead' not in st.session_state: st.session_state.dead = 0
if 'history' not in st.session_state: st.session_state.history = []
if 'user_selection' not in st.session_state: st.session_state.user_selection = None
if 'v_id' not in st.session_state: st.session_state.v_id = "VESS-G" + str(random.randint(11,99)) + "-" + str(random.randint(100,999))

st.title("🚢 Cruise Monopoly: Ship Manager Game")
st.write("---")

# --- STEP 1: INITIAL CONFIGURATION INTERFACE WITH REAL GEOGRAPHIC MAPS ---
if st.session_state.phase == 0:
    st.header("✍️ Step 1: Choose Your Group Number")
    st.info("💡 Your ship setup is auto-locked based on your Group Number to prevent copying!")
    
    group_choice = st.selectbox("Select Your Group Number (1-8):", ["Group 1", "Group 2", "Group 3", "Group 4", "Group 5", "Group 6", "Group 7", "Group 8"])
    g_idx = int(group_choice.split(" ")) - 1
    
    ships = ["Starry Empress (Luxury Ship)", "Oceanic Voyager (Family Holiday Ship)", "Royal Sovereign (Mega-Resort Ship)", "Genting Splendor (Asian Style Resort Ship)", "Coral Majestic (Small Exploration Ship)", "Horizon Dragon (Hong Kong Premium Yacht)", "Atlantic Crown (Classic Ocean Liner)", "Pacific Pacific (Singapore Active Holiday Ship)"]
    durations = ["12-Day Mediterranean Trip", "14-Day Caribbean Holiday", "16-Day Long Ocean Crossing", "18-Day Southeast Asia Trip", "21-Day Long Cruise Route", "24-Day Big Asia Transit", "27-Day Coastline Tour", "29-Day Deep Wilderness Expedition"]
    themes = ["Gourmet Food & Spa Focus", "High-Energy Sports & Deck Parties", "History, Local Culture & Sightseeing", "Asian Michelin Dim Sum Food Tour", "Business Meetings & Tech Networking", "Lunar New Year Festival Cruise", "Big Family Vacation & Kids Activities", "Diving, Coral Reefs & Sea Nature"]
    routes = ["Miami ➔ Cozumel (Western Caribbean)", "Seattle ➔ Juneau (Alaskan Passage)", "Barcelona ➔ Marseille (Western Mediterranean)", "Singapore ➔ Phuket (Southeast Asian)", "Sydney ➔ Auckland (Tasman Crossing)", "Hong Kong ➔ Okinawa (East China Sea)", "Copenhagen ➔ Helsinki (Baltic Heritage)", "Yokohama ➔ Keelung (North Asia Island)"]
    markets = ["WESTERN Customers (Spends big money at bars/alcohol, wants slow lazy holiday)", "WESTERN Customers (Big families, spends money at casino/games, wants active fun)", "WESTERN Customers (Rich premium travelers, wants expensive fine dining restaurants)", "ASIAN Customers (Big multi-generation families, wants delicious food, demands 'Safety First' layout)", "WESTERN Customers (Adventure travelers, loves outdoor day tours at ports)", "ASIAN Customers (Hong Kong high-end rich shoppers, hates any time delays)", "WESTERN Customers (Older university alumni groups, wants quiet academic study lectures)", "ASIAN Market (Singapore fly-cruise segment, active wildlife/photography focus)"]
    
    # Real geographic visual route maps mapped directly to each group
    map_images = [
        "https://unsplash.com",  # Caribbean Map Profile
        "https://unsplash.com",  # Alaska Map Profile
        "https://unsplash.com",  # Mediterranean Map Profile
        "https://unsplash.com",  # Southeast Asia Profile
        "https://unsplash.com",  # Tasman Crossing Profile
        "https://unsplash.com",  # East China Sea Profile
        "https://unsplash.com",  # Baltic Sea Profile
        "https://unsplash.com"   # North Asia Corridor
    ]

    st.write("### 🔒 Your Auto-Locked Ship Details:")
    c1, c2 = st.columns(2)
    c1.text_input("Passenger Market Type:", value=markets[g_idx], disabled=True)
    c1.text_input("Cruise Ship Name:", value=ships[g_idx], disabled=True)
    c2.text_input("Sailing Route Port:", value=routes[g_idx], disabled=True)
    c2.text_input("Cruise Main Activity Focus:", value=themes[g_idx], disabled=True)
    
    # Show real image route map immediately without clicking
    st.markdown("### 🗺️ Geographic Itinerary Route Map:")
    st.image(map_images[g_idx], use_container_width=True, caption=f"Active Voyage Corridor Mapping: {routes[g_idx]}")

    if st.button("✅ Confirm Setup - Start the Cruise Now", type="primary", use_container_width=True):
        st.session_state.phase = 1
        st.session_state.history.extend([
            f"🚢 MASTER MANIFEST FOR {group_choice} ({st.session_state.v_id})",
            f"• Ship: {ships[g_idx]} | Duration: {durations[g_idx]}",
            f"• Route: {routes[g_idx]} | Focus: {themes[g_idx]}",
            f"• Market Profile: {markets[g_idx]}\n---"
        ])
        st.rerun()

# --- STEP 2: CRISIS MANAGEMENT ENGINE ROUNDS ---
elif 1 <= st.session_state.phase <= 3:
    st.markdown(f"### 📊 Dashboard Status | {st.session_state.history[0].split(' (')[0].replace('🚢 ', '')}")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Money left", f"${st.session_state.cash:,}")
    c2.metric("👥 Onboard Passengers", f"{st.session_state.passengers:,} Pax")
    c3.metric("🏥 Sick/Injured", f"{st.session_state.injured} Sick", delta=f"+{st.session_state.injured}" if st.session_state.injured > 0 else None, delta_color="inverse")
    c4.metric("💀 Deaths", f"{st.session_state.dead} Dead", delta=f"+{st.session_state.dead}" if st.session_state.dead > 0 else None, delta_color="inverse")
    st.write("---")
    
    col_left, col_right = st.columns(2)
    
    with col_left:
        st.subheader(f"🎲 Step {st.session_state.phase} / 3 Rounds")
        is_asian = "ASIAN" in st.session_state.history[3]
        
        CARDS = [
            {"title": "BAD WEATHER: Big Storm Coming", "desc": "A dangerous Category 5 hurricane blocks your ship's direct route.", "h": "Hurricane Dorian (2019). Western bars/casinos remain highly profitable. Asian markets exhibit a strict collectivist safety expectation.", "emoji": "⛈️ 🌊 🌪️", "o1": "Choice 1: [Option 1] Safety Detour around storm. (0 hurt, fuel spikes -$6,000)", "o2": "Choice 2: [Option 2] Save Fuel money and run at full speed. (85 fallback injuries. Asian retail boycotts cost an extra -$2,000)" if is_asian else "Choice 2: [Option 2] Save Fuel money and run at full speed. (85 fallback injuries, -$2,000 medical lawsuit fees)", "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0},
            {"title": "MEDICAL EMERGENCY: Sickness Outbreak on Board", "desc": "A contagious gastrointestinal virus spreads rapidly inside buffet dining rooms.", "h": "Oasis of the Seas (2019). Western cabins reject quarantine locks. Asian generational densities spark severe fatalities if ignored.", "emoji": "🏥 🤢 💊", "o1": "Choice 1: [Option 1] Force in-cabin quarantine. (120 sick, 0 deaths. Western refunds cost -$20,000; Asian lines cooperate at -$12,000)", "o2": "Choice 2: [Option 2] Keep theater/public spaces open. (450 sick. Asian family structures report 4 elderly deaths, -$35,000 fine; Western costs -$22,000)", "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1},
            {"title": "BIG BUSINESS OPPORTUNITY: Shopping Gala Offer", "desc": "A luxury retail company requests to lease public decks tonight for a VIP shopping party.", "h": "Fleet Charter data. Asian routes generate massive net auxiliary margins from duty-free luxury spending over casual Western itineraries.", "emoji": "💎 💰 🎰", "o1": "Choice 1: [Option 1] Accept VIP contract. (Asian shopping surges net revenues by +$35,000; Western assets capture +$20,000)", "o2": "Choice 2: [Option 2] Decline deal to keep public transit spaces free. (Yields $0 cash injection)", "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0
                }
        ]
        
        c = CARDS[st.session_state.phase - 1]
        
        st.markdown(f"### {c['emoji']} {c['title']}")
        st.write(f"💬 **Current Situation:** {c['desc']}")
        st.caption(f"📌 *Case History: {c['h']}*")
        st.write("---")
        
        st.subheader("Review Options & Cast Your Boardroom Vote:")
        
        # Two large, clear individual review panels with consistent typography wrapper
        st.info(f"🔴 **{c['o1']}**")
        st.info(f"🔵 **{c['o2']}**")
        st.write("")
        
        # Click buttons to toggle selection highlight
        b1, b2 = st.columns(2)
        if b1.button("👉 Select Option 1", use_container_width=True):
            st.session_state.user_selection = "1"

import streamlit as st
import random

st.set_page_config(page_title="Cruise Monopoly System", layout="wide")

if 'game_state' not in st.session_state:
    st.session_state.game_state = {
        'phase': 0, 'group': '', 'brand': '', 'days': '', 'theme': '', 'route': '', 'market': '',
        'cash': 50000, 'passengers': 3000, 'injured': 0, 'dead': 0,
        'dice_rolled': False, 'current_roll': 0, 'history': [], 'verification_id': ""
    }

s = st.session_state.game_state
st.title("🚢 Cruise Monopoly: Global Itinerary Crisis Management Simulator")
st.write("---")

if s['phase'] == 0:
    st.header("✍️ Step 1: Initialize Vessel Profile & Itinerary Parameters")
    st.info("💡 Plagiarism Prevention: Profiles are custom-locked to your unique Group Number!")
    
    group_choice = st.selectbox("Select Your Assigned Group Number (1-8):", [f"Group {i}" for i in range(1, 9)])
    g_idx = int(group_choice.split(" ")) - 1
    
    ships = ["Starry Empress (Western Luxury)", "Oceanic Voyager (Western Family)", "Royal Sovereign (Western Resort)", "Genting Splendor (Asian Resort)", "Coral Majestic (Western Explorer)", "Horizon Dragon (Hong Kong Luxury Yacht)", "Atlantic Crown (Classic Transatlantic)", "Pacific Pacific (Singapore Expedition)"]
    durations = ["12-Day Med Exploration", "14-Day Grand Caribbean", "16-Day Transoceanic", "18-Day Southeast Asian Tropical", "21-Day Relocation Route", "24-Day East Asia Transit", "27-Day Coastline Explorer", "29-Day Asia-Pacific Expedition"]
    themes = ["Gourmet Wine & European Wellness", "High-Energy Action & Deck Parties", "Local Heritage & Cultural Track", "Asian Michelin Culinary & Dim Sum Track", "Corporate Executive Tech Summit", "Lunar New Year Cultural Festival", "Multi-Generational Family Holiday", "Remote Scuba & Marine Conservation"]
    routes = ["Miami ➔ Cozumel", "Seattle ➔ Juneau", "Barcelona ➔ Marseille", "Singapore ➔ Phuket", "Sydney ➔ Auckland", "Hong Kong ➔ Okinawa", "Copenhagen ➔ Helsinki", "Yokohama ➔ Keelung"]
    markets = ["WESTERN Market (High onboard bar spend, relaxed vacation expectations)", "WESTERN Market (Mass family segment, high gaming spend, active schedules)", "WESTERN Market (Upscale segment, demands fine dining, flexible operations)", "ASIAN Market (Collectivist families, premium dining, strict safety expectations)", "WESTERN Market (Affluent adventurers, heavy shore excursion focus)", "ASIAN Market (Hong Kong high-net-worth segment, extreme delay-sensitive)", "WESTERN Market (Senior alumni demographic, traditional slow-paced schedule)", "ASIAN Market (Singapore fly-cruise segment, active wildlife/photography focus)"]

    s.update({'group': group_choice, 'brand': ships[g_idx], 'days': durations[g_idx], 'theme': themes[g_idx], 'route': routes[g_idx], 'market': markets[g_idx], 'verification_id': f"CONF-G{g_idx+1}-{random.randint(100,999)}"})

    st.write("### 🔒 Auto-Locked Group Specifications:")
    c1, c2 = st.columns(2)
    c1.text_input("Target Passenger Demographic Market:", value=s['market'], disabled=True)
    c1.text_input("Vessel Brand Identity:", value=s['brand'], disabled=True)
    c2.text_input("Geographic Itinerary Route:", value=s['route'], disabled=True)
    c2.text_input("Commercial Theme Focus:", value=s['theme'], disabled=True)

    if st.button("✅ Confirm Specifications - Cast Off Lines", type="primary"):
        s['phase'] = 1
        s['history'].extend([f"🚢 BASE MANIFEST SECURED FOR {s['group']} ({s['verification_id']})", f"• Market Profile: {s['market']}", f"• Route: {s['route']} | Theme: {s['theme']}"])
        st.rerun()

elif 1 <= s['phase'] <= 3:
    st.markdown(f"### 📊 Scoreboard | {s['group']} Active Profile")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("💰 Cash Asset Balance", f"\${s['cash']:,}")
    c2.metric("👥 Active Onboard Passengers", f"{s['passengers']:,} Pax")
    c3.metric("🏥 Total Sick / Injured Pax", f"{s['injured']} Pax", delta=f"+{s['injured']}" if s['injured'] > 0 else None, delta_color="inverse")
    c4.metric("💀 Cumulative Fatalities", f"{s['dead']} Dead", delta=f"+{s['dead']}" if s['dead'] > 0 else None, delta_color="inverse")

    st.write("---")
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader(f"🎲 Voyage Segment: Phase {s['phase']} / 3 Rounds")
        if not s['dice_rolled']:
            if st.button("🎲 Shake & Roll Navigation Dice", type="primary"):
                s['current_roll'], s['dice_rolled'] = random.randint(1, 6), True
                st.rerun()
        else:
            st.success(f"🎲 Dice Roll Confirmed: Advanced {s['current_roll']} Sectors!")
            is_asian = "ASIAN" in s['market']
            
            CARDS = [
                {
                    "title": "🚨 WEATHER: Severe Storm Path Entry", 
                    "desc": "A category 5 storm blocks your direct path.", 
                    "h": "Hurricane Dorian (2019). Western markets handle sea rolling well. Asian markets expect safety-first protocols.", 
                    "img": "⛈️",
                    "o1": "【Option 1】Safety Protocol: Execute regional detour. (0 casualties, fuel spikes -\$6,000)", 
                    "o2": "【Option 2】Schedule Lock: Run ahead of the wind at max speed. (Saves cash, but 85 pax slip injuries. On Asian routes, lost retail costs an extra -\$2,000)", 
                    "m1": -6000, "i1": 0, "d1": 0, "m2": -4000 if is_asian else -2000, "i2": 85, "d2": 0
                },
                {
                    "title": "🚨 MEDICAL: Onboard Norovirus Gastro Epidemic", 
                    "desc": "A contagious gastrointestinal virus breaks loose within the main dining layout sections.", 
                    "h": "Oasis of the Seas (2019). Western guests demand heavy bar compensations if locked down. Asian routes feature older families vulnerable to fatalities if ignored.", 
                    "img": "🏥",
                    "o1": "【Option 1】Isolate Vessel: Mandatory in-cabin quarantine. (120 sick pax, 0 deaths. Western complaints cost -\$20,000; Asian collectivism costs -\$12,000)", 
                    "o2": "【Option 2】Maintain Operations: Keep spaces open to save retail revenue. (450 pax infected. Asian multi-generational densities trigger 4 high-risk elderly deaths and -\$35,000 fine; Western costs -\$22,000)", 
                    "m1": -12000 if is_asian else -20000, "i1": 120, "d1": 0, "m2": -35000 if is_asian else -22000, "i2": 450, "d2": 4 if is_asian else 1
                },
                {
                    "title": "🌟 STRATEGIC OPPORTUNITY: High-Margin Premium Charter Proposal", 
                    "desc": "A luxury retail conglomerate requests to lease your public decks tonight for a VIP shopping gala.", 
                    "h": "Corporate charter data. Asian cruise markets generate much higher profit margins from duty-free luxury spending compared to Western casual vacationers.", 
                    "img": "💰",
                    "o1": "【Option 1】Commercial Deal: Accept VIP contract. (Asian routes trigger shopping surge of +\$35,000; Western routes generate +\$20,000)", 
                    "o2": "【Option 2】Consumer Protection: Decline contract to keep public walking spaces open. (Yields \$0 cash injection)", 
                    "m1": 35000 if is_asian else 20000, "i1": 0, "d1": 0, "m2": 0, "i2": 0, "d2": 0
                }
            ]
            
            random.seed(int(s['group'].split(" ")) + 88)
            shuffled_cards = list(CARDS)
            random.shuffle(shuffled_cards)
            c = shuffled_cards[s['phase'] - 1]
            
            # Rendering Visual Elements & Anime Placeholders
            st.markdown(f"## {c['img']} {c['title']}")
            st.markdown(f"🌍 **Target Market Profile:** **`{s['market']}`**")
            st.write(f"💬 **Current Incident Vector:** {c['desc']}")
            st.caption(f"📌 *Benchmark Case Study: {c['h']}*")
            
            st.write("---")
            st.subheader("👉 Formulate Your Executive Boardroom Mandate Below:")
            st.info(f"👉 **Choice 1:** {c['o1']}")
            st.info(f"👉 **Choice 2:** {c['o2']}")
            st.write("")
            
            col_b1, col_b2 = st.columns(2)
            if col_b1.button("🔴 Choose Option 1", use_container_width=True):
                s['cash'] += c['m1']; s['injured'] += c['i1']; s['dead'] += c['d1']
                s['history'].append(f"Phase {s['phase']} - Option 1 Selected | Cash: \${c['m1']:,} | Sick/Injured: +{c['i1']} | Deaths: +{c['d1']}")
                s['phase'] += 1; s['dice_rolled'] = False; st.rerun()
            if col_b2.button("🔵 Choose Option 2", use_container_width=True):
                s['cash'] += c['m2']; s['injured'] += c['i2']; s['dead'] += c['d2']
                s['history'].append(f"Phase {s['phase']} - Option 2 Selected | Cash: \${c['m2']:,} | Sick/Injured: +{c['i2']} | Deaths: +{c['d2']}")
                s['phase'] += 1; s['dice_rolled'] = False; st.rerun()

    with col_right:
        st.subheader("📜 Live Navigation Logbook Record")
        for log in s['history']: st.write(f"- {log}")

else:
    st.balloons()
    st.header("🏁 Voyage Concluded: Official Operations Audit Report")
    st.write(f"🔒 **Anti-Tamper Session Security ID:** `{s['verification_id']}` | **Market Context:** `{s['market']}`")
    st.write("---")
    c1, c2, c3 = st.columns(3)
    c1.metric("🏁 Final Net Asset Cash", f"\${s['cash']:,}")
    c2.metric("🏥 Cumulative Sick/Injured", f"{s['injured']} Pax")
    c3.metric("💀 Cumulative Fatalities", f"{s['dead']} Dead")
    st.write("---")
    log_text = "\n".join(s['history']) + f"\n\n[AUDIT FINGERPRINT] {s['group']} ({s['verification_id']}) | Cash: \${s['cash']:,} | Injuries: {s['injured']} | Fatalities: {s['dead']}"
    st.text_area("Select and Copy log block below:", value=log_text, height=200)
    if st.button("🔄 Reset Simulator (New Session)", use_container_width=True):
        st.session_state.clear()
        st.rerun()

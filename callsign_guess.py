import streamlit as st
import random

# --- Full callsign dictionary ---
callsigns = {
    "AAB": "Abelag", "AAF": "Aigle Azur", "AAL": "American", "AAR": "Asiana",
    "ABN": "Air Albania", "ACA": "Air Canada", "AIC": "Air India",
    "AFR": "Air France", "AZA": "Alitalia", "ASL": "Air Serbia",
    "ATL": "Air Bernina", "AUA": "Austrian", "AUI": "Ukraine International",
    "AVA": "Avianca", "AZW": "Air Zimbabwe", "BAF": "Belgian Airforce",
    "BAW": "Speedbird", "BEL": "City Bird", "BER": "Air Berlin",
    "BMS": "Blue Messenger", "BTI": "Air Baltic", "BUL": "Bulgarian Charter",
    "BVR": "Bavarian", "CAL": "China Airlines", "CCA": "Air China",
    "CES": "China Eastern", "CSN": "China Southern", "CFG": "Condor",
    "CPA": "Cathay", "CYP": "Cyprus", "CLX": "Cargolux", "DAH": "Air Algerie",
    "DAL": "Delta", "DLH": "Lufthansa", "DSO": "Dassault", "DUB": "Dubair",
    "DNM": "Dan Air", "EAT": "Trans Europe", "ELY": "El Al", "ETD": "Etihad",
    "EZY": "Easyjet", "FIN": "Finnair", "FIA": "Finnish Air Force",
    "FTH": "First Flight", "FDX": "Fedex", "GEC": "Lufthansa Cargo",
    "GFA": "Gulf Air", "GLG": "Gill Airways", "GTI": "Grandstar Cargo",
    "GWI": "Germanwings", "HAL": "Hawaiian", "HLX": "Hapag Lloyd",
    "HVN": "Vietnam Airlines", "HOP": "HOP!", "IBE": "Iberia",
    "IAW": "Iraqi Airways", "IRA": "Iran Air", "IRZ": "Mahan Air",
    "ITY": "ITA Airways", "JAF": "Beauty", "JAL": "Japan Air",
    "JBU": "Jet Blue", "JAI": "Jet Airways", "JTG": "Jet Time",
    "KAC": "Kuwait", "KAL": "Korean Air", "KLM": "KLM", "LOT": "LOT",
    "LDA": "Lauda Motion", "LGL": "Luxair", "LZB": "Flying Bulgaria",
    "LXR": "Lux Rescue", "MAH": "Malev", "MAS": "Malaysian",
    "MEA": "Cedar Jet", "MSR": "Egyptair", "MSX": "Egyptair Cargo",
    "MPH": "Martinair", "MON": "Monarch", "MNB": "Black Sea",
    "NAX": "Norwegian", "NJE": "Fraction", "NLY": "Nile Bird",
    "NVR": "Novair", "OAL": "Olympic", "OHY": "Onur Air",
    "OSY": "Open Skies", "OTF": "OrangeSky", "PIA": "Pakistan",
    "PGT": "SunTurk", "PBD": "Pobeda", "PRI": "Primera",
    "PWF": "Private Wings", "QAF": "Amiri", "QFA": "Qantas",
    "QTR": "Qatari", "QGA": "Quadax", "RAM": "Royalair Maroc",
    "RAA": "Rada", "ROU": "Rouge", "RYR": "Ryanair",
    "RWD": "RwandAir", "SAS": "Scandinavian", "SBI": "Siberian",
    "SDM": "Rossiya", "SIA": "Singapore", "SWR": "Swiss",
    "SVR": "Sverdlovsk", "TAM": "Tamazi", "THA": "Thai",
    "THY": "Turkish", "TOM": "Tom Jet", "TRA": "Transavia",
    "TVF": "France Soleil", "TUI": "TuiJet", "TFL": "Orange",
    "UAE": "Emirates", "UKL": "Ukraine Alliance", "UZA": "Uzbekistan",
    "VLG": "Vueling", "VOZ": "Virgin Australia", "VIR": "Virgin",
    "VJC": "VietJet", "VIM": "VIM Airlines", "WZZ": "Wizzair",
    "WKT": "White Knight", "WOW": "Wow Air", "XLF": "Starway",
    "YI": "Eurostar", "YTO": "YTO Cargo", "ZAP": "Zap", "ZIM": "Zimex"
}

# --- Session state ---
if "current" not in st.session_state:
    st.session_state.current = None
if "correct_callsign" not in st.session_state:
    st.session_state.correct_callsign = None
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "answered" not in st.session_state:
    st.session_state.answered = False
if "used" not in st.session_state:
    st.session_state.used = set()
if "next_question_requested" not in st.session_state:
    st.session_state.next_question_requested = False

# --- Generate new question ---
def new_question():
    unused = [item for item in callsigns.items() if item[0] not in st.session_state.used]

    if not unused:
        st.session_state.current = None
        st.session_state.correct_callsign = None
        st.session_state.feedback = "🎉 You've completed all questions! Refresh to start again."
        st.session_state.answered = True
        return

    callsign, airline = random.choice(unused)
    st.session_state.current = airline
    st.session_state.correct_callsign = callsign
    st.session_state.user_input = ""
    st.session_state.feedback = ""
    st.session_state.answered = False
    st.session_state.used.add(callsign)

# --- Trigger new question if requested ---
if st.session_state.next_question_requested:
    new_question()
    st.session_state.next_question_requested = False

# --- Page config ---
st.set_page_config(page_title="Callsign Typing Quiz", page_icon="✈️", layout="centered")
st.title("✈️ Callsign Typing Quiz")

# --- Start quiz ---
if st.session_state.current is None and not st.session_state.feedback:
    new_question()

# --- Show question ---
if st.session_state.current:
    st.subheader(f"What is the **callsign** for: {st.session_state.current}?")

    st.text_input("Enter the 3-letter callsign:", key="user_input", max_chars=4)

    if st.button("Submit", use_container_width=True, disabled=st.session_state.answered):
        user_answer = st.session_state.user_input.strip().upper()
        correct = st.session_state.correct_callsign

        if user_answer == correct:
            st.session_state.feedback = f"✅ Correct! {st.session_state.current} = **{correct}**"
        else:
            st.session_state.feedback = f"❌ Wrong! The correct callsign for {st.session_state.current} is **{correct}**"
        st.session_state.answered = True

# --- Show feedback ---
if st.session_state.feedback:
    if "✅" in st.session_state.feedback:
        st.success(st.session_state.feedback)
    elif "❌" in st.session_state.feedback:
        st.error(st.session_state.feedback)
    else:
        st.info(st.session_state.feedback)

# --- Show next button ---
if st.session_state.answered and st.session_state.current:
    if st.button("➡️ Next Question", use_container_width=True):
        st.session_state.next_question_requested = True
elif not st.session_state.answered and st.session_state.current:
    st.button("➡️ Next Question", use_container_width=True, disabled=True)

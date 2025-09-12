import streamlit as st
import random

# --- Callsign dictionary ---
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

# --- Session state setup ---
if "current_callsign" not in st.session_state:
    st.session_state.current_callsign = None
if "correct_airline" not in st.session_state:
    st.session_state.correct_airline = None
if "user_input" not in st.session_state:
    st.session_state.user_input = ""
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "answered" not in st.session_state:
    st.session_state.answered = False
if "next_question_requested" not in st.session_state:
    st.session_state.next_question_requested = False

# --- Generate new question ---
def new_question():
    callsign, airline = random.choice(list(callsigns.items()))
    st.session_state.current_callsign = callsign
    st.session_state.correct_airline = airline
    st.session_state.user_input = ""
    st.session_state.feedback = ""
    st.session_state.answered = False

# --- Trigger new question if requested ---
if st.session_state.next_question_requested:
    new_question()
    st.session_state.next_question_requested = False

# --- Page setup ---
st.set_page_config(page_title="Callsign Quiz", page_icon="✈️", layout="centered")
st.title("✈️ Callsign Typing Quiz")

# --- Start quiz if not started ---
if st.session_state.current_callsign is None:
    new_question()

# --- Show question ---
if st.session_state.current_callsign:
    st.subheader(f"Which **airline** uses the callsign: **{st.session_state.current_callsign}**?")

    st.text_input("Enter the airline name:", key="user_input")

    if st.button("Submit", use_container_width=True, disabled=st.session_state.answered):
        user_answer = st.session_state.user_input.strip().lower()
        correct_answer = st.session_state.correct_airline.lower()

        if user_answer == correct_answer:
            st.session_state.feedback = f"✅ Correct! {st.session_state.current_callsign} = **{st.session_state.correct_airline}**"
        else:
            st.session_state.feedback = f"❌ Wrong! The correct answer for {st.session_state.current_callsign} is **{st.session_state.correct_airline}**"
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
if st.session_state.answered:
    if st.button("➡️ Next Question", use_container_width=True):
        st.session_state.next_question_requested = True
else:
    st.button("➡️ Next Question", use_container_width=True, disabled=True)

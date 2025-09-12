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

# --- Streamlit state setup ---
if "current" not in st.session_state:
    st.session_state.current = None
if "options" not in st.session_state:
    st.session_state.options = []
if "answer" not in st.session_state:
    st.session_state.answer = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "answered" not in st.session_state:
    st.session_state.answered = False
if "used_callsigns" not in st.session_state:
    st.session_state.used_callsigns = set()
if "next_question_requested" not in st.session_state:
    st.session_state.next_question_requested = False

# --- Function to generate a new question ---
def new_question():
    unused_callsigns = [item for item in callsigns.items() if item[0] not in st.session_state.used_callsigns]

    if not unused_callsigns:
        st.session_state.current = None
        st.session_state.options = []
        st.session_state.answer = None
        st.session_state.feedback = "🎉 You've completed the quiz! Refresh the page to start again."
        st.session_state.answered = True
        return

    callsign, airline = random.choice(unused_callsigns)
    wrong = random.sample([v for v in callsigns.values() if v != airline], 3)
    options = wrong + [airline]
    random.shuffle(options)

    st.session_state.current = callsign
    st.session_state.options = options
    st.session_state.answer = airline
    st.session_state.feedback = ""
    st.session_state.answered = False
    st.session_state.used_callsigns.add(callsign)

# --- Trigger new question if requested ---
if st.session_state.next_question_requested:
    new_question()
    st.session_state.next_question_requested = False

# --- Page setup ---
st.set_page_config(page_title="Callsign Quiz", page_icon="✈️", layout="centered")
st.title("✈️ Callsign Quiz")

# --- Start quiz if not started ---
if st.session_state.current is None and not st.session_state.feedback:
    new_question()

# --- Show current question ---
if st.session_state.current:
    st.subheader(f"Which airline uses callsign: **{st.session_state.current}** ?")

    cols = st.columns(2)
    for i, option in enumerate(st.session_state.options):
        with cols[i % 2]:
            if st.button(option, key=f"option_{i}", use_container_width=True):
                if not st.session_state.answered:
                    if option == st.session_state.answer:
                        st.session_state.feedback = f"✅ Correct! {st.session_state.current} = {option}"
                    else:
                        st.session_state.feedback = f"❌ Wrong! Correct answer: {st.session_state.answer}"
                    st.session_state.answered = True

# --- Show feedback ---
if st.session_state.feedback:
    st.info(st.session_state.feedback)

# --- Show next button ---
if st.session_state.answered and st.session_state.current:
    if st.button("➡️ Next Question", use_container_width=True):
        st.session_state.next_question_requested = True
elif not st.session_state.answered and st.session_state.current:
    st.button("➡️ Next Question", use_container_width=True, disabled=True)

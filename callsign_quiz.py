import streamlit as st
import random
# Full callsign dictionary (from images)
callsigns = {
      "AAB": "Abelag", "AAF": "Aigle Azur", "AAL": "American", "AAR": "Asian",
    "ABN": "Air Albania", "ACA": "Air Canada", "AIC": "Air India",
    "AFR": "Air France", "AZA": "Alitalia", "ASL": "Air Serbia", "ATL": "Air Bernina",
    "AUA": "Austrian", "AUI": "Ukraine International", "AVA": "Avianca",
    "AZW": "Air Zimbabwe", "BAF": "Belgian Airforce", "BAW": "Speedbird",
    "BEL": "City Bird", "BER": "Air Berlin", "BMS": "Blue Messenger",
    "BTI": "Air Baltic", "BUL": "Bulgarian Charter", "BVR": "Bavarian",
    "CAL": "China Airlines", "CCA": "Air China", "CES": "China Eastern",
    "CSN": "China Southern", "CFG": "Condor", "CPA": "Cathay", "CYP": "Cyprus",
    "CLX": "Cargolux", "DAH": "Air Algerie", "DAL": "Delta", "DLH": "Lufthansa",
    "DSO": "Dassault", "DUB": "Dubair", "DNM": "Dan Air", "EAT": "Trans Europe",
    "ELY": "El Al", "ETD": "Etihad", "EZY": "Easyjet", "FIN": "Finnair",
    "FIA": "Finnish Air Force", "FTH": "First Flight", "FDX": "Fedex",
    "GEC": "Lufthansa Cargo", "GFA": "Gulf Air", "GLG": "Gill Airways",
    "GTI": "Grandstar Cargo", "GWI": "Germanwings", "HAL": "Hawaiian",
    "HLX": "Hapag Lloyd", "HVN": "Vietnam Airlines", "HOP": "HOP!",
    "IBE": "Iberia", "IAW": "Iraqi Airways", "IRA": "Iran Air",
    "IRZ": "Mahan Air", "ITY": "ITA Airways", "JAF": "Beauty", "JAL": "Japan Air",
    "JBU": "Jet Blue", "JAI": "Jet Airways", "JTG": "Jet Time", "KAC": "Kuwait",
    "KAL": "Korean Air", "KLM": "KLM", "LOT": "LOT", "LDA": "Lauda Motion",
    "LGL": "Luxair", "LZB": "Flying Bulgaria", "LXR": "Lux Rescue",
    "MAH": "Malev", "MAS": "Malaysian", "MEA": "Cedar Jet", "MSR": "Egyptair",
    "MSX": "Egyptair Cargo", "MPH": "Martinair", "MON": "Monarch",
    "MNB": "Black Sea", "NAX": "Norwegian", "NJE": "Fraction",
    "NLY": "Nile Bird", "NVR": "Novair", "OAL": "Olympic", "OHY": "Onur Air",
    "OSY": "Open Skies", "OZ": "Asiana", "PIA": "Pakistan", "PGT": "SunTurk",
    "PBD": "Pobeda", "PRI": "Primera", "PWF": "Private Wings", "QAF": "Amiri",
    "QFA": "Qantas", "QTR": "Qatari", "QGA": "Quadax", "RAM": "Royalair Maroc",
    "RAA": "Rada", "ROU": "Rouge", "RYR": "Ryanair", "RWD": "RwandAir",
    "SAS": "Scandinavian", "SBI": "Siberian", "SDM": "Rossiya", "SIA": "Singapore",
    "SWR": "Swiss", "SVR": "Sverdlovsk", "TAM": "Tamazi", "THA": "Thai",
    "THY": "Turkish", "TOM": "Tom Jet", "TRA": "Transavia",
    "TVF": "France Soleil", "TUI": "TuiJet", "TFL": "Orange", "UAE": "Emirates",
    "UKL": "Ukraine Alliance", "UZA": "Uzbekistan", "VLG": "Vueling",
    "VOZ": "Virgin Australia", "VIR": "Virgin", "VJC": "VietJet",
    "VIM": "VIM Airlines", "WZZ": "Wizzair", "WKT": "White Knight",
    "WOW": "Wow Air", "XLF": "Starway", "YI": "Eurostar", "YTO": "YTO Cargo",
    "ZAP": "Zap", "ZIM": "Zimex"
}

# Streamlit state initialization
if "current" not in st.session_state:
    st.session_state.current = None
if "options" not in st.session_state:
    st.session_state.options = []
if "answer" not in st.session_state:
    st.session_state.answer = None
if "feedback" not in st.session_state:
    st.session_state.feedback = ""
if "answered" not in st.session_state:
    st.session_state.answered = False  # NEW: Track if user has answered

def new_question():
    callsign, airline = random.choice(list(callsigns.items()))
    wrong = random.sample([v for v in callsigns.values() if v != airline], 3)
    options = wrong + [airline]
    random.shuffle(options)
    st.session_state.current = callsign
    st.session_state.options = options
    st.session_state.answer = airline
    st.session_state.feedback = ""
    st.session_state.answered = False  # Reset answered flag

# Page config
st.set_page_config(page_title="Callsign Quiz", page_icon="✈️", layout="centered")

st.title("✈️ Callsign Quiz")

# Generate first question if none
if st.session_state.current is None:
    new_question()

st.subheader(f"Which airline uses callsign: **{st.session_state.current}** ?")

# Display answer buttons (only if not already answered)
cols = st.columns(2)
for i, option in enumerate(st.session_state.options):
    with cols[i % 2]:
        if st.button(option, key=f"option_{i}", use_container_width=True):
            if not st.session_state.answered:
                if option == st.session_state.answer:
                    st.session_state.feedback = f"✅ Correct! {st.session_state.current} = {option}"
                else:
                    st.session_state.feedback = f"❌ Wrong! Correct answer: {st.session_state.answer}"
                st.session_state.answered = True  # Mark question as answered

# Show feedback
if st.session_state.feedback:
    st.info(st.session_state.feedback)

# Next question button (only enabled after answering)
if st.session_state.answered:
    if st.button("➡️ Next Question", use_container_width=True):
        new_question()
else:
    st.button("➡️ Next Question", use_container_width=True, disabled=True)

import streamlit as st
import random

# --- Callsign dictionary ---
callsigns = {
    "AAL": "American",
    "ABG": "Royal Flight",
    "ACA": "Air Canada",
    "ADB": "Antonov Bureau",
    "ADR": "Adria",
    "AEE": "Aegean",
    "AFL": "Aeroflot",
    "AFR": "Airfrans",
    "AHO": "Air Hamburg",
    "AIZ": "Arkia",
    "AMC": "Air Malta",
    "ASL": "Air Serbia",
    "ATV": "Avanti Air",
    "AUA": "Austrian",
    "AUI": "Ukraine International",
    "AZA": "Alitalia",
    "BAF": "Belgian Airforce",
    "BAW": "Speedbird",
    "BEL": "Beeline",
    "BLA": "Blue Air",
    "BMS": "Blue Messenger",
    "BMW": "Banxico",
    "BPA": "Blue Panorama",
    "BPS": "Base",
    "BRU": "BelAvia",
    "BTI": "Air Baltic",
    "CAL": "Dynasty",
    "CCA": "Air China",
    "CES": "China Eastern",
    "CFG": "Condor",
    "CHH": "Hainan",
    "CPA": "Cathay",
    "CSN": "China Southern",
    "CTN": "Croatia",
    "DAH": "Air Algerie",
    "DAL": "Delta",
    "DLA": "Dolomitti",
    "DLH": "Lufthansa",
    "EAU": "Elite",
    "EGL": "Prestige",
    "EIN": "Shamrock",
    "EIU": "Alpine",
    "ELY": "El Al",
    "ELJ": "Topjet",
    "ETD": "Etihad",
    "ETH": "Ethiopian",
    "EWG": "Eurowings",
    "EXS": "Channex",
    "EZS": "Topswiss",
    "EZY": "Easy",
    "FDX": "Fedex",
    "FIN": "Finnair",
    "FPO": "French Post",
    "GAF": "German Airforce",
    "GEC": "Lufthansa Cargo",
    "GWI": "Germanwings",
    "IBE": "Iberia",
    "JAF": "Beauty",
    "KAL": "Koreanair",
    "KLM": "KLM",
    "LDM": "Lauda Motion",
    "LGL": "Luxair",
    "LOT": "LOT",
    "LZB": "Flying Bulgaria",
    "MEA": "Cedar Jet",
    "MGX": "Montair",
    "MLD": "Air Moldova",
    "MSR": "Egyptair",
    "NAX": "Norshuttle",
    "NWS": "Nordland",
    "NJE": "Fraction",
    "PGT": "Sunturk",
    "QTR": "Qatari",
    "RAC": "Tuzla Air",
    "RJA": "Jordanian",
    "ROT": "Tarom",
    "ROU": "Rouge",
    "RYR": "Ryanair",
    "SAS": "Scandinavian",
    "SBI": "Siberian",
    "SDM": "Rossiya",
    "SIA": "Singapore",
    "SVA": "Saudia",
    "SWR": "Swiss",
    "SWT": "Swift",
    "SXD": "Sunrise",
    "SXS": "Sunexpress",
    "TAP": "Air Portugal",
    "TAR": "Tunair",
    "TDR": "Trade Air",
    "TFL": "Orange",
    "THA": "Thai",
    "THY": "Turkish",
    "TOM": "Tomjet",
    "TRA": "Transavia",
    "TUI": "Tuijet",
    "TVF": "France Soleil",
    "TVS": "Skytravel",
    "UAE": "Emirates",
    "UAL": "United",
    "VJT": "Vista Malta",
    "VLG": "Vueling",
    "VOE": "Volotea",
    "WUK": "Wizz Go",
    "WZZ": "Wizzair",
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

import streamlit as st
import random

# --- Callsign dictionary ---
callsigns = {
    "AAB": "Abelag", "AAF": "Aigle Azur", "AAL": "American", "AAR": "Asiana", "ABG": "Royal Flight",
    "ABN": "Air Albania", "ABR": "Contract", "ACA": "Air Canada", "ACP": "Air Canada", "ADB": "Antonov Bureau",
    "ADR": "Adria", "AEA": "Europa", "AEG": "Aegean", "AEE": "Aegean", "AFR": "Air France", "AGX": "Ameriflight",
    "AIC": "Air India", "AIH": "Air Incheon", "AIZ": "Arkia", "AJM": "Airmalta", "ALK": "Air Lanka", "AMC": "Air Malta",
    "AMQ": "Amas", "AMS": "Amex", "ANA": "All Nippon", "ANG": "Angola", "AUA": "Austrian", "AUI": "Ukraine International",
    "AWC": "Zep", "AZA": "Alitalia", "AZI": "Azzurra", "AZU": "Azul", "BCS": "Cargologic", "BDI": "Bristow",
    "BER": "Air Berlin", "BGA": "Airbus", "BHY": "Balkany Heliair", "BKP": "Bangkok Air", "BLF": "Blueberry", "BLH": "Bul Air",
    "BLK": "Black", "BMW": "Bannico", "BOX": "German Cargo", "BPA": "Blue Panorama", "BPS": "Base", "BRJ": "Boreal Jet",
    "BRU": "Broadward", "BRV": "Belavia", "BTI": "Air Baltic", "BVL": "Bulgarian Charter", "BUL": "Bul Air", "BUR": "Burcharest",
    "BVL": "Bulgarian", "BVR": "Bavarian", "BNI": "Bartolini", "CCL": "Cal Cargo", "CFE": "Flyer", "CFG": "Condor", 
    "CHX": "Swiss Helicopter", "CLH": "Lufthansa CityLine", "CLX": "Cargolux", "CMP": "Copa", "COY": "Coyne Airways",
    "CPE": "Cyprus Eagle", "CSA": "CSA", "CSN": "China Southern", "CXA": "Xiamen", "CTM": "Cottam", "CTN": "Croatia",
    "CXI": "Comlux Aviation", "DHL": "DHL", "DLH": "Lufthansa", "DCS": "DCS", "DHL": "DHL", "DNM": "Danube Wings",
    "DUB": "Dubai", "DUK": "Duk", "EAT": "Trans Europe", "ECA": "East Air", "ECC": "Edcair", "EDW": "Edelweiss",
    "EFU": "Ever flight", "EIN": "Shamrock", "ELG": "Elgo", "ELO": "Elo", "ELD": "Electra", "ELO": "Elot", "ELY": "El Al",
    "ESY": "Easy", "ETD": "Etihad", "ETH": "Ethiopian", "EZS": "Easy Swiss", "EZY": "Easyjet", "FAF": "French Air Force",
    "FBL": "Fly Bulgaria", "FDX": "Fedex", "FHY": "Freebird Air", "FIN": "Finnair", "FLY": "Flytrav", "FPO": "French Post",
    "FRA": "France", "FTH": "First Flight", "GAC": "Dream Team", "GAF": "German Airforce", "GCK": "Glock", "GEC": "Lufthansa Cargo",
    "GFA": "Gulf Air", "GLP": "Globe Air", "GMI": "Germania", "GLG": "Gill Airways", "GTI": "Grandstar Cargo", "GWI": "Germanwings",
    "HAT": "Sky Runner", "HAY": "Hamburg Airways", "HEL": "Heli", "HLX": "Hapag Lloyd", "HOP": "Heliview", "HTH": "Heli Air",
    "HTM": "Alboran", "HZA": "Horiz Air", "IBE": "Iberia", "IBK": "Iberia Express", "ICL": "CargoCol Italia", "IGA": "Iguana",
    "IRA": "Iran Air", "IRN": "Iranian", "IRA": "Iran Air", "ISM": "Mahan Air", "ISS": "Israel", "ITA": "Air Italy",
    "ITY": "ITA Airways", "JAF": "Beauty", "JAL": "Japan Air", "JBU": "Jet Blue", "JAI": "Jet Airways", "JTG": "Jet Time",
    "JMP": "JetMagic", "JNL": "Jet Netherlands", "JOR": "Blue Transport", "JSU": "Stream Air", "JTY": "Jet Sky", "JTE": "Jetex",
    "JTI": "JetTime", "KAC": "Kuwait", "KAL": "Korean Air", "KZR": "Air Astana", "KLM": "KLM", "LOT": "LOT", "LDM": "Lauda Motion",
    "LGL": "Luxair", "LLP": "Skypol", "LZB": "Flying Bulgaria", "MAE": "Mali Airexpress", "MAF": "Missi", "MEA": "Cedar Jet",
    "MSR": "Egyptair", "MSX": "Egyptair Cargo", "MNB": "Black Sea", "MOV": "Movair", "MPH": "Martinair", "MYX": "MyJet X",
    "NAF": "Netherlands Air Force", "NAM": "Namibian", "NOS": "Norshuttle", "NAX": "Norwegian", "NJE": "Fraction", "NLY": "Nile Bird",
    "NVR": "Novair", "OAL": "Olympus", "OHY": "Onur Air", "OMA": "Oman Air", "OPJ": "Opera Jet", "OSY": "Open Skies",
    "OTF": "OrangeSky", "PAJ": "Air Panama", "PBD": "Pobeda", "PGT": "SunTurk", "PIA": "Pakistan", "PINK": "Air Pink",
    "PWF": "Private Wings", "QAF": "Amiri", "QFA": "Qantas", "QTR": "Qatari", "QGA": "Quadax", "RAM": "Royalair Maroc",
    "RAA": "Rada", "ROU": "Rouge", "RYR": "Ryanair", "RWD": "RwandAir", "SAS": "Scandinavian", "SBI": "Siberian",
    "SDM": "Rossiya", "SIA": "Singapore", "SWR": "Swiss", "SVR": "Sverdlovsk", "TAM": "Tamazi", "THA": "Thai",
    "THY": "Turkish", "TOM": "Tom Jet", "TRA": "Transavia", "TVF": "France Soleil", "TUI": "TuiJet", "TFL": "Orange",
    "UAE": "Emirates", "UKL": "Ukraine Alliance", "UZA": "Uzbekistan", "VLG": "Vueling", "VOZ": "Virgin Australia",
    "VIR": "Virgin", "VJC": "VietJet", "VIM": "VIM Airlines", "WZZ": "Wizzair", "WKT": "White Knight", "WOW": "Wow Air",
    "XLF": "Starway", "YTO": "YTO Cargo", "ZAP": "Zap", "ZIM": "Zimex"
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

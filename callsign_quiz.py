import streamlit as st
import random

# --- Full callsign dictionary ---
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

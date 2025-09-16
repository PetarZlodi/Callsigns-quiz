import streamlit as st
import random

# --- Full callsign dictionary ---
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
if "correct_answers" not in st.session_state:
    st.session_state.correct_answers = 0
if "total_questions" not in st.session_state:
    st.session_state.total_questions = 0

# --- Function to generate a new question ---
def new_question():
    unused_callsigns = [item for item in callsigns.items() if item[0] not in st.session_state.used_callsigns]

    if not unused_callsigns:
        st.session_state.current = None
        st.session_state.options = []
        st.session_state.answer = None
        st.session_state.feedback = ""
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
if st.session_state.current is None and not st.session_state.feedback and len(st.session_state.used_callsigns) < len(callsigns):
    new_question()

# --- Show current question ---
if st.session_state.current:
    st.subheader(f"Which airline uses callsign: **{st.session_state.current}** ?")

    cols = st.columns(2)
    for i, option in enumerate(st.session_state.options):
        with cols[i % 2]:
            if st.button(option, key=f"option_{i}", use_container_width=True):
                if not st.session_state.answered:
                    st.session_state.total_questions += 1
                    if option == st.session_state.answer:
                        st.session_state.correct_answers += 1
                        st.session_state.feedback = f"✅ Correct! {st.session_state.current} = {option}"
                    else:
                        st.session_state.feedback = f"❌ Wrong! Correct answer: {st.session_state.answer}"
                    st.session_state.answered = True

# --- Show feedback ---
if st.session_state.feedback:
    st.info(st.session_state.feedback)

# --- Show next or final result ---
total = len(callsigns)
used = len(st.session_state.used_callsigns)

if used == total:
    percent = round((st.session_state.correct_answers / total) * 100)
    st.markdown("---")
    st.subheader("🎯 Final Score")
    st.markdown(f"**✅ Correct Answers: {st.session_state.correct_answers} / {total}**")
    st.markdown(f"**📊 Accuracy: {percent}%**")

    if percent == 100:
        st.success("🎉 Bravo majstore!!!", icon="🏆")
    else:
        st.error("😅 Aj ti ipak to ponovi malo.", icon="🔁")
else:
    if st.session_state.answered and st.session_state.current:
        if st.button("➡️ Next Question", use_container_width=True):
            st.session_state.next_question_requested = True
    elif not st.session_state.answered and st.session_state.current:
        st.button("➡️ Next Question", use_container_width=True, disabled=True)

import streamlit as st
import random

# --- Full callsign dictionary (truncated for example) ---
callsigns = {
    "AAB": "Abelag", "AAF": "Aigle Azur", "AAL": "American", "AAR": "Asian",
    "ABN": "Air Albania", "ACA": "Air Canada", "AIC": "Air India",
    "AFR": "Air France", "AZA": "Alitalia", "ASL": "Air Serbia",
    "ATL": "Air Bernina", "AUA": "Austrian", "AUI": "Ukraine International",
    "AVA": "Avianca", "AZW": "Air Zimbabwe", "BAF": "Belgian Airforce",
    # ... Add all remaining entries here
}

# --- Initialize session state ---
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


# --- Function to generate new question ---
def new_question():
    unused_callsigns = [item for item in callsigns.items() if item[0] not in st.session_state.used_callsigns]

    if not unused_callsigns:
        st.session_state.current = None
        st.session_state.options = []
        st.session_state.answer = None
        st.session_state.feedback = "🎉 You've completed the quiz! Refresh to start again."
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


# --- Trigger next question on rerun ---
if st.session_state.next_question_requested:
    new_question()
    st.session_state.next_question_requested = False


# --- UI Layout ---
st.set_page_config(page_title="Callsign Quiz", page_icon="✈️", layout="centered")
st.title("✈️ Callsign Quiz")

# Initial question
if st.session_state.current is None and not st.session_state.feedback:
    new_question()

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

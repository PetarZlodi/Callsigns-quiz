import streamlit as st
import random

# --- Full callsign dictionary ---
callsigns = {
    "AAB": "Abelag", "AAF": "Aigle Azur", "AAL": "American", "AAR": "Asiana",
    # ... (rest unchanged)
    "ZAP": "Zap", "ZIM": "Zimex"
}

# --- Session state ---
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
if "used" not in st.session_state:
    st.session_state.used = set()
if "next_question_requested" not in st.session_state:
    st.session_state.next_question_requested = False

# --- Generate new question ---
def new_question():
    unused = [item for item in callsigns.items() if item[0] not in st.session_state.used]

    if not unused:
        st.session_state.current_callsign = None
        st.session_state.correct_airline = None
        st.session_state.feedback = "🎉 You've completed all questions! Refresh to start again."
        st.session_state.answered = True
        return

    callsign, airline = random.choice(unused)
    st.session_state.current_callsign = callsign
    st.session_state.correct_airline = airline
    st.session_state.user_input = ""
    st.session_state.feedback = ""
    st.session_state.answered = False
    st.session_state.used.add(callsign)

# --- Trigger new question if requested ---
if st.session_state.next_question_requested:
    new_question()
    st.session_state.next_question_requested = False

# --- Page config ---
st.set_page_config(page_title="Callsign Abbreviation Quiz", page_icon="✈️", layout="centered")
st.title("✈️ Callsign Abbreviation Quiz")

# --- Start quiz ---
#if st.session_state.current_callsign is None and not st.session_state.feedback:
    #new_question()

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
if st.session_state.answered and st.session_state.current_callsign:
    if st.button("➡️ Next Question", use_container_width=True):
        st.session_state.next_question_requested = True
elif not st.session_state.answered and st.session_state.current_callsign:
    st.button("➡️ Next Question", use_container_width=True, disabled=True)

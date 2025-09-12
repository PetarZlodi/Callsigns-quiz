import streamlit as st
import random
# Full callsign dictionary (from images)
callsigns = {
    # your dictionary unchanged...
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

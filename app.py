import streamlit as st
import tempfile

from speech_to_text import transcribe_audio
from semantic_eval import semantic_score
from audio_utils import extract_audio_features
from scoring_engine import generate_score
from report_generator import generate_report

st.set_page_config(page_title="VBCUA AI System", page_icon="🎤", layout="wide")

# UI STYLE
st.markdown("""
<style>
body { background-color: #f5f7fb; }

.title {
    text-align: center;
    font-size: 38px;
    font-weight: bold;
    color: #1a73e8;
}

.card {
    background: white;
    padding: 15px;
    border-radius: 10px;
    box-shadow: 0px 2px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

st.markdown("<div class='title'>🎤 Voice Based Concept Understanding Analyzer</div>", unsafe_allow_html=True)

# INPUT
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("Upload Audio", type=["wav", "mp3"])

with col2:
    reference_answer = st.text_area("Enter Reference Answer")

# PROCESS
if uploaded_file and reference_answer:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.getbuffer())
        audio_path = tmp.name

    st.audio(uploaded_file)

    with st.spinner("Analyzing..."):

        transcript = transcribe_audio(audio_path)
        semantic = semantic_score(transcript, reference_answer)
        features = extract_audio_features(audio_path)

        score, label, feedback = generate_score(
            semantic,
            features["rms_energy"],
            features["pause_ratio"]
        )

        generate_report("report.pdf", transcript, score, label)

    # OUTPUT
    st.markdown("## 📊 Results")

    c1, c2, c3 = st.columns(3)
    c1.metric("Semantic Score", f"{semantic}%")
    c2.metric("Voice Energy", features["rms_energy"])
    c3.metric("Pause Ratio", features["pause_ratio"])

    st.markdown("## 🧠 AI Feedback")
    st.info(feedback)

    # ✅ TRANSCRIPT FIXED HERE
    st.markdown("## 📝 Transcript")
    st.text_area("Speech Output", transcript, height=150)

    st.markdown("## 🏆 Final Score")
    st.progress(min(int(score), 100))

    if score >= 80:
        st.success(f"{score}/100 - {label}")
    elif score >= 60:
        st.warning(f"{score}/100 - {label}")
    else:
        st.error(f"{score}/100 - {label}")

    with open("report.pdf", "rb") as f:
        st.download_button("📥 Download Report", f, file_name="VBCUA_Report.pdf")
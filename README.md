# 🎤 Voice-Based Concept Understanding Analyzer (VBCUA)

An AI-powered web application that evaluates a user's conceptual understanding through spoken responses. The system converts speech into text, analyzes semantic similarity with the expected answer, extracts audio features, and generates an automated performance report.

---

## 📌 Project Overview

The Voice-Based Concept Understanding Analyzer (VBCUA) is designed to automate the evaluation of spoken answers. Instead of relying only on manual assessment, the application uses Artificial Intelligence and Machine Learning techniques to measure conceptual understanding and provide instant feedback.

This project is developed using Python and Streamlit with state-of-the-art AI models for speech recognition and semantic analysis.

---

## ✨ Features

- 🎙️ Speech-to-Text Conversion using OpenAI Whisper
- 🧠 Semantic Similarity Analysis using Sentence Transformers (SBERT)
- 🎵 Audio Feature Extraction using Librosa
- 📊 Automated Performance Scoring
- 📄 PDF Report Generation
- 🌐 Interactive Streamlit Web Interface
- ⚡ Fast and Accurate Evaluation

---

## 🛠️ Technologies Used

- Python
- Streamlit
- OpenAI Whisper
- Sentence Transformers (SBERT)
- Librosa
- NumPy
- ReportLab
- Torch

---

## 📂 Project Structure

```
VBCUA/
│── app.py
│── speech_to_text.py
│── semantic_eval.py
│── audio_utils.py
│── scoring_engine.py
│── report_generator.py
│── requirements.txt
│── README.md
│── uploads/
│── reports/
│── assets/
└── screenshots/
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/siddhikshaik/Voice-Based-Concept-Understanding-Analyser-VBCUA-.git
```

```bash
cd Voice-Based-Concept-Understanding-Analyser-VBCUA-
```

### Create Virtual Environment

Windows

```bash
python -m venv vbcua_env
```

Activate

```bash
vbcua_env\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Project

```bash
python -m streamlit run app.py
```

Open your browser and visit

```
http://localhost:8501
```

---

## 📖 Workflow

1. Launch the Streamlit application.
2. Upload or record a voice response.
3. Convert speech to text using Whisper.
4. Compare the transcript with the expected answer.
5. Perform semantic similarity analysis.
6. Extract audio features.
7. Generate an overall score.
8. Download the detailed PDF report.

---

## 📸 Screenshots
<img width="1917" height="1007" alt="output screenshot" src="https://github.com/user-attachments/assets/b4ffa251-12d3-426c-bdfe-ac6a1d321694" />
<img width="1918" height="1007" alt="Screenshot 2026-07-11 092741" src="https://github.com/user-attachments/assets/3089053f-9a30-44fb-835e-c0bd196b6fd9" />
<img width="1557" height="623" alt="Screenshot 2026-07-10 183301" src="https://github.com/user-attachments/assets/6c6da48e-f4f8-4dd5-bdf9-02b8e8dbc571" />



## 🚀 Future Enhancements

- Multi-language support
- Real-time voice recording
- Cloud database integration
- User authentication
- Dashboard for teachers
- Advanced AI feedback

---

## 🎯 Applications

- Educational Institutions
- Online Learning Platforms
- Interview Preparation
- Skill Assessment
- Training Organizations

---

## 👨‍💻 Author

**Siddhik Shaik**

B.Tech – Computer Science and Engineering

Lakireddy Bali Reddy College of Engineering

GitHub: https://github.com/siddhikshaik

---

## 📄 License

This project is developed for educational and learning purposes.

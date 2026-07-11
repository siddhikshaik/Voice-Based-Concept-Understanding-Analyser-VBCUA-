import os
import whisper

model = whisper.load_model("base")


def transcribe_audio(audio_path):

    try:

        if not os.path.exists(audio_path):
            return "ERROR: Audio file not found."

        if os.path.getsize(audio_path) == 0:
            return "ERROR: Empty audio file."

        result = model.transcribe(
            audio_path,
            fp16=False,
            language="en"
        )

        text = result.get("text", "").strip()

        if text == "":
            return "ERROR: No speech detected."

        return text

    except Exception as e:
        return f"ERROR: {e}"
import librosa
import numpy as np

def extract_audio_features(audio_path):

    y, sr = librosa.load(audio_path, sr=None)

    rms = float(np.mean(librosa.feature.rms(y=y)))

    pause_ratio = np.sum(np.abs(y) < 0.02) / len(y)

    return {
        "rms_energy": round(rms, 3),
        "pause_ratio": round(pause_ratio, 3)
    }
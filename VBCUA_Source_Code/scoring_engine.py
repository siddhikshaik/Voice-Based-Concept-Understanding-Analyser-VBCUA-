def generate_score(semantic_score, rms_energy, pause_ratio):

    rms_score = min(rms_energy * 100, 100)
    pause_score = (1 - pause_ratio) * 100

    final_score = (
        semantic_score * 0.75 +
        rms_score * 0.15 +
        pause_score * 0.10
    )

    if final_score >= 80:
        label = "Strong Understanding"
        feedback = "Excellent explanation with clear understanding."
    elif final_score >= 60:
        label = "Moderate Understanding"
        feedback = "Partially correct but needs more depth."
    else:
        label = "Weak Understanding"
        feedback = "Concept is unclear. Improve your answer."

    return round(final_score, 2), label, feedback
def detect_subject(title):
    title = title.lower()

    if any(word in title for word in ["algebra", "calculus", "geometry"]):
        return "mathematics"
    if any(word in title for word in ["algorithm", "data", "computer"]):
        return "computer_science"
    if any(word in title for word in ["thermodynamics", "mechanics"]):
        return "mechanical"

    return "general"

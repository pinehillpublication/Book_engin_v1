from deepseek_writer import write_text

def generate_blueprint(title, level, pages, subject):
    prompt = f"""
    Create academic book structure.
    Title: {title}
    Level: {level}
    Target pages: {pages}
    Subject: {subject}
    Include logical chapter progression.
    """

    response = write_text(prompt)

    chapters = [line.strip() for line in response.split("\n") if line.strip()]

    return chapters

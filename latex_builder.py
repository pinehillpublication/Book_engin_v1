import os
from config import TEMPLATE_PATH, OUTPUT_DIR

def build_latex(title, chapters_content):
    with open(TEMPLATE_PATH, "r") as f:
        template = f.read()

    final_tex = template.replace("<<TITLE>>", title)
    final_tex = final_tex.replace("<<CHAPTERS>>", chapters_content)
    final_tex = final_tex.replace("<<PREFACE>>", "This book explores the subject in depth.")
    final_tex = final_tex.replace("<<ACK>>", "Acknowledgements.")
    final_tex = final_tex.replace("<<BIB>>", "References will be added.")

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    tex_path = os.path.join(OUTPUT_DIR, "book.tex")

    with open(tex_path, "w") as f:
        f.write(final_tex)

    return tex_path

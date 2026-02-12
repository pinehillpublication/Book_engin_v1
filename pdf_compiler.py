import os
from config import OUTPUT_DIR

def compile_pdf(tex_path):
    os.system(f"pdflatex -output-directory={OUTPUT_DIR} {tex_path}")
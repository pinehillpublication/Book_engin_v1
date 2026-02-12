from deepseek_writer import write_text

def generate_full_book(job, chapters, subject):
    full_content = ""

    total_words = job["pages"] * 450
    words_per_chapter = total_words // len(chapters)

    for index, chapter in enumerate(chapters):
        job["current_chapter"] = index + 1

        outline_prompt = f"""
        Create structured outline for chapter:
        {chapter}
        Level: {job['level']}
        """

        outline = write_text(outline_prompt)

        section_content = ""
        sections = outline.split("\n")

        for sec in sections:
            section_prompt = f"""
            Write LaTeX section for:
            {sec}
            Subject: {subject}
            Level: {job['level']}
            Word limit: {words_per_chapter // len(sections)}
            Maintain academic clarity and natural tone.
            """

            section_text = write_text(section_prompt)
            section_content += section_text + "\n"

        full_content += f"\\chapter{{{chapter}}}\n" + section_content

    return full_content

import PyPDF2

FILENAME = "LSP.pdf"
DRECTORY = "lsptxt"

with open(FILENAME, "rb") as pdf_file:
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    COUNTER = 1
    TEXT = ""

    for page_num, page in enumerate(pdf_reader.pages):
        page = pdf_reader.pages[page_num]
        page_text = page.extract_text()
        TEXT += page_text

        if len(TEXT) >= 4096:
            with open(
                f"{DRECTORY}/example_{COUNTER}.txt", "w", encoding="utf-8"
            ) as txt_file:
                txt_file.write(TEXT)
                TEXT = ""
                COUNTER += 1
    if TEXT:
        with open(f"example_{COUNTER}.txt", "w", encoding="utf-8") as txt_file:
            txt_file.write(TEXT)

print(f"Text extracted and saved to {COUNTER} files.")

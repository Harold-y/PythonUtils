import docx
document = docx.opendocx("Top30.docx")
all_paragraphs = document.paragraphs
for paragraph in all_paragraphs:
    print(paragraph.text)

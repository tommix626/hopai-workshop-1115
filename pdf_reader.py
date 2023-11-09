import PyPDF2

from gpt import CLS_GPTBot


def extract_text_from_pdf(pdf_path):
    text_data = []

    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)

        for page in pdf_reader.pages:
            # Extract text from each page
            text_data.append(page.extract_text())

    return text_data


if __name__ == '__main__':
    pdf_path = 'example.pdf'  # Replace this with your PDF file path
    pdf_text = extract_text_from_pdf(pdf_path)
    prompt = "Analyze the following text extracted from a course lecture's pdf, please provide a summary and give the relevant page for part of the summary.\n Text:"
    prompt = "Create flash cards for the definitions and potential quiz problem you see; you should produce each flash card in the following style:\n Question={}\n Answer={}\n ppt_page={}\n\n"
    for page_number, text in enumerate(pdf_text, start=1):
        prompt += "page"+ str(page_number) + " text:" + text + "\n"
    # print(prompt)
    api_key = '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'
    gpt = CLS_GPTBot(api_key)
    response = gpt.query(prompt)
    print(response)


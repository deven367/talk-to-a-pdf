import click
from PyPDF2 import PdfReader

from ttf.utils import chat_with


def chat_with_pdf(path: str, prompt:str) -> str:

    reader = PdfReader(path)
    text = "\n".join([page.extract_text() for page in reader.pages])

    user_input = prompt + ":\n\n" + text
    chat_with(user_input)



@click.command()
@click.option("--pdf", "-p", type=click.Path(exists=True), required=True)
@click.option("--prompt", "-pr", type=str, default="Summarize the following text")
def main(pdf, prompt):
    chat_with_pdf(pdf, prompt)

if __name__ == "__main__":
    main()

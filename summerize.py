import click
from PyPDF2 import PdfReader

from utils import chat_with


def summarize_pdf(path: str, prompt:str) -> str:

    reader = PdfReader(path)
    text = "\n".join([page.extract_text() for page in reader.pages])

    user_input = prompt + ":\n\n" + text
    chat_with(user_input)



@click.command()
@click.option("--path", "-p", type=click.Path(exists=True), required=True)
@click.option("--prompt", "-pr", type=str, default="Summarize the following text")
def main(path, prompt):
    summarize_pdf(path, prompt)

if __name__ == "__main__":
    main()

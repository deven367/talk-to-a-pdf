import click
import pandas as pd
from PyPDF2 import PdfReader

from ttf.utils import chat_with


def chat_with_file(path: str, prompt: str) -> str:
    """
    Chat with a file.

    Args:
        path (str): The path to the file.
        prompt (str): The prompt to the chatbot.

    Returns:
        str: The response from the chatbot.
    """

    if path.endswith(".pdf"):
        reader = PdfReader(path)
        text = "\n".join([page.extract_text() for page in reader.pages])

    elif path.endswith(".txt"):
        text = open(path, "r").read()
    elif path.endswith(".csv"):
        text = pd.read_csv(path)[["date", "text"]][500:600].to_string()
    else:
        extension = path.split(".")[-1]
        raise ValueError(f'Files ending in "{extension}" are not yet supported')

    user_input = prompt + ":\n\n" + text
    chat_with(user_input)


@click.command()
@click.option("--file", "-f", type=click.Path(exists=True), required=True)
@click.option("--prompt", "-pr", type=str, default="Summarize the following text")
def main(file, prompt):
    chat_with_file(file, prompt)


if __name__ == "__main__":
    main()

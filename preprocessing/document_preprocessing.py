import re


def clean_legal_text(text):
    """
    Clean text extracted from a legal document.
    """

    text = text.lower()

    text = re.sub(
        r"\s+",
        " ",
        text
    )

    text = re.sub(
        r"[^\w\s.,;:()/-]",
        "",
        text
    )

    text = text.strip()

    return text


def chunk_text(text, chunk_size=300):
    """
    Split cleaned legal text into chunks.

    chunk_size = approximate number of words per chunk.
    """

    words = text.split()

    chunks = []

    for i in range(
        0,
        len(words),
        chunk_size
    ):

        chunk = " ".join(
            words[i:i + chunk_size]
        )

        if chunk.strip():

            chunks.append(
                chunk
            )

    return chunks


def chunk_text_with_pages(
    page_texts,
    chunk_size=300,
    overlap=50
):

    chunks = []

    chunk_id = 0

    for page_number, page_text in page_texts:

        if not page_text:
            continue

        words = page_text.split()

        start = 0

        while start < len(words):

            end = start + chunk_size

            chunk_words = words[
                start:end
            ]

            if not chunk_words:
                break

            chunk_text_value = " ".join(
                chunk_words
            )

            chunks.append({
                "chunk_id": chunk_id,
                "page": page_number,
                "text": chunk_text_value
            })

            chunk_id += 1

            start += (
                chunk_size - overlap
            )

    return chunks
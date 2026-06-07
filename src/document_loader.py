from io import BytesIO
from pypdf import PdfReader


def extract_text_from_pdf(file_bytes: bytes) -> str:
    """
    Extracts text from a PDF file.
    Works best for digital PDFs, not scanned image-only PDFs.
    """
    reader = PdfReader(BytesIO(file_bytes))
    pages = []

    for index, page in enumerate(reader.pages):
        text = page.extract_text() or ""
        text = text.strip()

        if text:
            pages.append(f"\n\n--- Page {index + 1} ---\n{text}")

    full_text = "\n".join(pages).strip()

    if not full_text:
        raise ValueError(
            "No readable text found. This may be a scanned PDF or image-based poster."
        )

    return full_text


def chunk_text(text: str, max_chars: int = 12000, overlap: int = 800) -> list[str]:
        #We Split the long documents into overlapping chunks, which keeps prompts inside model context limits.
    chunks = []
    start = 0

    while start < len(text):
        end = start + max_chars
        chunk = text[start:end]
        chunks.append(chunk)

        if end >= len(text):
            break

        start = end - overlap

    return chunks
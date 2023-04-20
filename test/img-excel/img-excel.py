from PIL import Image as PILImage
import pytesseract
import pandas as pd
from img2table.document import Image
from img2table.ocr import TesseractOCR
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from dataclasses import dataclass
from io import BytesIO
@dataclass
class TableData:
    header: str


def similarity_strings(str1: str, str2: str) -> float:
    "Calculate similarity between two strings using cosine_similarity"
    # Create a CountVectorizer object to tokenize and count the words in the strings
    vectorizer = CountVectorizer().fit_transform([str1, str2])
    # Calculate the cosine similarity between the vectors
    similarity = cosine_similarity(vectorizer)
    return similarity[0][1]


def get_image_text(image_path) -> list:
    "Allow to get text of image with teseract"
    image = PILImage.open(image_path)
    text: str = pytesseract.image_to_string(image,
                                            lang='eng',
                                            config='--psm 6')
    # To convert to df df = pd.read_csv(io.StringIO(text), delimiter='\t')
    text = text.split('\n')
    # Deleting white lines
    text = [text_line for text_line in text if text_line.strip() != ""]
    return text


def get_image_datatable(image_path) -> pd.DataFrame:
    "Considering that image has only one table"
    ocr = TesseractOCR(n_threads=1, lang="eng")
    pil_image = PILImage.open(image_path)
    bytes_buffer = BytesIO()
    pil_image.save(bytes_buffer, format='PNG')
    bytes_value = bytes_buffer.getvalue()
    image = Image(bytes_value,
                  dpi=200,
                  detect_rotation=False)
    # Table extraction
    extracted_tables = image.extract_tables(ocr=ocr,
                                            implicit_rows=True,
                                            borderless_tables=False,
                                            min_confidence=10)
    # Extraction of tables and creation of an xlsx file containing tables
    if extracted_tables:
        return extracted_tables[0].df
    return None


path_image = 'example2.png'
dataframe_data = get_image_datatable(path_image)
print(dataframe_data)

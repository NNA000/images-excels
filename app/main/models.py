import requests
import os
from dataclasses import dataclass
from PIL import Image as PILImage
from io import BytesIO
import pytesseract
import pandas as pd
from img2table.document import Image
from img2table.ocr import TesseractOCR
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import logging

@dataclass
class ResponseMethod:
    succes: bool
    content: list
    message: str = 'No error'


class Aditionals:
    @staticmethod
    def similarity_strings(str1: str, str2: str) -> float:
        "Calculate similarity between two strings using cosine_similarity"
        # Create a CountVectorizer object to tokenize and count the words in the strings
        vectorizer = CountVectorizer().fit_transform([str1, str2])
        # Calculate the cosine similarity between the vectors
        similarity = cosine_similarity(vectorizer)
        return similarity[0][1]


class UtilImage:
    @staticmethod
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

    @staticmethod
    def get_image_datatable(img: BytesIO) -> pd.DataFrame:
        "Considering that image has only one table"
        ocr = TesseractOCR(n_threads=1, lang="eng")
        image = Image(src=img,
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


class ModelImage:
    def __init__(self) -> None:
        self.default_path_files = './files'
        self.path_img = f'{self.default_path_files}/img'
        self.path_excel = f'{self.default_path_files}/excel'

    def get_images(self, link_images: list[dict]) -> list:
        """
        Get images given url of images
           Input format of link images is: {name:index, url:url_imagen}
           Output: list of images [PIL.Image]
           """
        images = []
        for image in link_images:
            response = requests.get(image.get("url"))
            if response.status_code == 200:
                images.append({'name':image.get('name'),
                               'image': BytesIO(response.content)})
            else:
                logging.warning(f'Error getting image {response.status_code=} for {image.get("url")=}')
        return images
    def get_data_images(self, images):


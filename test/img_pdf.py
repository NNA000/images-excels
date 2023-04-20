import urllib.request
from io import BytesIO
from PIL import Image
from PyPDF2 import PdfWriter, PdfReader

# Define the web links for the images
image_links = [
    'https://s3.amazonaws.com/hr-challenge-images/19503/1458523388-0896218137-ScreenShot2016-03-21at6.51.45AM.png',
    'https://s3.amazonaws.com/hr-challenge-images/19503/1458523022-771511df90-ScreenShot2016-03-21at6.40.37AM.png',
    'https://s3.amazonaws.com/hr-challenge-images/19503/1458523374-7ecc39010f-ScreenShot2016-03-21at6.51.56AM.png'
]

# Create a new PDF file
output_pdf = PdfWriter()

# Loop through the image links and add the images to the PDF file
for link in image_links:
    # Download the image from the web link
    image_data = urllib.request.urlopen(link).read()

    # Open the image as a Pillow image
    image = Image.open(BytesIO(image_data))

    # Create a new page in the PDF file and add the image to it
    page = output_pdf.add_blank_page(width=image.width, height=image.height)
    page.mergeTranslatedPage(PdfReader(BytesIO(image_data)).getPage(0),
                             0,
                             image.height)


# Save the PDF file to disk
with open('output.pdf', 'wb') as f:
    output_pdf.write(f)

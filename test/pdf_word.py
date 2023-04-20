import pathlib
import win32com.client

current_file = pathlib.Path(__file__).parent.resolve()

print(current_file)
# Create a new instance of the Word application
word = win32com.client.Dispatch("Word.Application")

# Make the Word application visible
word.Visible = True


# Open the PDF file in Word
doc = word.Documents.Open(f"{current_file}/test.pdf")

# Save the document as a Word document
doc.SaveAs2(f"{current_file}/test.docx", FileFormat=16)

# Close the document and the Word application
doc.Close()
word.Quit()

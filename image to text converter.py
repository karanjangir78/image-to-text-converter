import os
import time
from PIL import Image
from pytesseract import pytesseract
import pyautogui as pag
from tkinter.filedialog import askopenfilename

# Set Tesseract path
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Function to extract text from image
def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()

# Let user select an image
image_path = askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])

if image_path:
    # Extract text
    text = extract_text(image_path)
    
    # Open Notepad
    os.system("notepad")
    
    # Wait for Notepad to open
    time.sleep(2)
    
    # Type the extracted text into Notepad
    pag.typewrite(text, interval=0.01)
else:
    print("No image selected.")

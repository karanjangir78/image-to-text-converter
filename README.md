# Image to Text Extractor using Python OCR

## Overview

This project is a simple **OCR (Optical Character Recognition)** application built with Python.
It allows users to select an image file, extract text from the image using **Tesseract OCR**, and automatically type the extracted text into **Notepad**.

The project demonstrates:

* OCR text extraction
* GUI file selection
* Automation using PyAutoGUI
* Integration with external software

---

# Features

* Select image files (`.png`, `.jpg`, `.jpeg`)
* Extract text using Tesseract OCR
* Automatically open Notepad
* Auto-type extracted text into Notepad
* Simple and beginner-friendly implementation

---

# Technologies Used

* Python
* Pillow (PIL)
* pytesseract
* pyautogui
* tkinter

---

# Requirements

Install the required Python libraries:

```bash
pip install pillow pytesseract pyautogui
```

---

# Install Tesseract OCR

Download and install Tesseract OCR from:

https://github.com/tesseract-ocr/tesseract

After installation, update the path in the code if necessary:

```python
pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

---

# Project Workflow

1. User selects an image file
2. OCR extracts text from the image
3. Notepad opens automatically
4. Extracted text is typed into Notepad

---

# Code Explanation

## Import Required Libraries

```python
import os
import time
from PIL import Image
from pytesseract import pytesseract
import pyautogui as pag
from tkinter.filedialog import askopenfilename
```

---

## Extract Text Function

```python
def extract_text(image_path):
    image = Image.open(image_path)
    text = pytesseract.image_to_string(image)
    return text.strip()
```

This function:

* Opens the image
* Extracts text using OCR
* Removes extra spaces

---

## File Selection

```python
image_path = askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")]
)
```

Allows users to select an image from their system.

---

## Open Notepad and Type Text

```python
os.system("notepad")
time.sleep(2)
pag.typewrite(text, interval=0.01)
```

* Opens Notepad
* Waits for Notepad to load
* Types extracted text automatically

---

# Example Use Cases

* Digitizing printed documents
* Extracting text from screenshots
* Automating note-taking
* OCR learning project for beginners

---

# Future Improvements

* Add support for PDF files
* Build a GUI interface
* Save extracted text directly to `.txt` files
* Add multi-language OCR support
* Improve OCR accuracy with preprocessing

---

# Sample Output

Input Image:

```text
HELLO WORLD
```

Extracted Output in Notepad:

```text
HELLO WORLD
```

---

# Author

Your Name

---

# License

This project is open-source and free to use.

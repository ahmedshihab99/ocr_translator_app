# OCR Translator App

This is a desktop application that allows users to select a portion of their screen, extract text from it using Optical Character Recognition (OCR), and then translate that text into a different language. The translated text is then displayed as an overlay on the same area of the screen.

## Features

*   **Screen Capture**: Select any part of your screen for text extraction.
*   **OCR**: Uses Tesseract OCR to extract text from the captured image.
*   **Translation**: Translates the extracted text to a specified language (default is Arabic).
*   **Overlay Display**: Shows the translated text in a transparent window over the captured area.
*   **Hotkey Activation**: Trigger the screen capture by pressing a global hotkey (default: `Ctrl+Shift+X`).

## Setup and Installation

1.  **Prerequisites**:
    *   Python 3.x
    *   Tesseract OCR engine. You can download it from [here](https://github.com/tesseract-ocr/tesseract). Make sure to add the Tesseract installation directory to your system's PATH.

2.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/ocr_translator_app.git
    cd ocr_translator_app
    ```

3.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application**:
    ```bash
    python src/main.py
    ```

2.  **Activate the screen capture**:
    *   Press the hotkey `Ctrl+Shift+X`.
    *   Your screen will dim, and your cursor will turn into a crosshair.

3.  **Select an area**:
    *   Click and drag to select the rectangular area of the screen you want to translate.

4.  **View the translation**:
    *   The translated text will appear in an overlay in the same area you selected.

5.  **Close the translation**:
    *   Click the "X" button on the overlay to close it.

## Configuration

You can customize the application's settings in `src/utils/config.py`, including the hotkey, default languages, and API keys if you choose to use a different OCR or translation service.
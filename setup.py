from setuptools import setup, find_packages

setup(
    name='OCRTranslatorApp',
    version='1.0.0',
    packages=find_packages(),
    install_requires=[
        'pytesseract',
        'Pillow',
        'pynput',
        'googletrans==4.0.0-rc1',
        'pyautogui',
    ],
    entry_points={
        'console_scripts': [
            'ocr_translator = src.main:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='A desktop app to OCR and translate a selected screen area.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/your-username/ocr_translator_app',
)
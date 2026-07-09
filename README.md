# Translator App

This is my internship project for Zynvex Solutions. It's a simple desktop app made using Python and Tkinter that lets you translate text from one language to another.

## About the Project

I built this app to practice GUI development in Python along with using an external API/library for real functionality instead of just a static interface. The app has two text boxes - you type your text in the left one, pick the source and target language from the dropdowns, hit the Translate button, and the translated text shows up in the right box.

## Features

- Translate text between multiple languages
- Dropdown menus to select source and target language
- Scrollable text boxes so you can paste longer paragraphs too
- Shows proper error messages if you forget to enter text or select a language
- Works even if you don't have the icon/arrow image files (it just skips them instead of crashing)

## Technologies Used

- Python 3
- Tkinter (for the GUI)
- deep-translator (for actually translating the text)
- Pillow / PIL (for handling images in the app)

## How to Run this Project

1. Clone or download this repo
2. Install the required libraries:
pip install -r requirements.txt
3. Run the app:
python Translator.py

That's it, the app window will open and you can start translating.

## Some Issues I Faced While Making This

- Originally I was using the `googletrans` library but it kept giving errors because Google changed something on their end and that library isn't maintained anymore. Switched to `deep-translator` and it worked fine after that.
- Had an image path hardcoded to my own laptop's drive which obviously doesn't work on any other PC, so I fixed that.
- One of my dropdowns had a wrong option (`state="r"`) which isn't even a valid Tkinter value, changed it to `"readonly"`.

## Note

You need an active internet connection for the translation to actually work since it fetches results from Google Translate through the library.

## Author

Sundas Bibi
Internship Project - Zynvex Solutions

# Translator App using Tkinter (GUI) + deep-translator (for actual translation)
# This app lets user type text, pick source and target language, and get translation

import os
from tkinter import *
from tkinter import ttk, messagebox

from PIL import Image, ImageTk
from deep_translator import GoogleTranslator

# getting list of all languages supported (returns dict like {'english': 'en', 'urdu': 'ur', ...})
LANGUAGES = GoogleTranslator().get_supported_languages(as_dict=True)
LANGUAGE_NAMES = sorted(name.title() for name in LANGUAGES.keys())  # making it look nice like "English" instead of "english"

# this gives the folder where this file is saved, so images can be loaded properly
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# main window setup
root = Tk()
root.title("Translate App")
root.geometry("1060x400")
root.configure(bg="white")


# this function keeps updating the top labels to show which language is selected
def label_change():
    label1.configure(text=combo1.get())
    label2.configure(text=combo2.get())
    root.after(1000, label_change)  # calls itself again after 1 sec (loop)


# actual translation logic, takes text + source + target language
def translate_text(text, src="english", dest="urdu"):
    translator = GoogleTranslator(source=src.lower(), target=dest.lower())
    return translator.translate(text)


# this runs when user clicks the Translate button
def translate_now():
    try:
        src_lang = combo1.get().strip()
        dest_lang = combo2.get().strip()

        # basic check so app doesn't crash if user forgets to select something
        if not src_lang or not dest_lang or dest_lang == "SELECT LANGUAGE":
            messagebox.showerror("Translator", "Please select both source and target languages.")
            return

        text_to_translate = text1.get(1.0, END).strip()
        if not text_to_translate:
            messagebox.showerror("Translator", "Please enter some text to translate.")
            return

        result = translate_text(text_to_translate, src=src_lang, dest=dest_lang)
        text2.delete(1.0, END)
        text2.insert(END, result)

    except Exception as e:
        # if something goes wrong (like no internet), show it in a popup instead of crashing
        messagebox.showerror("Translator error", str(e))


# small function to load an image safely
# if image file is not found it just returns None instead of crashing the whole app
def load_optional_image(path):
    try:
        return ImageTk.PhotoImage(Image.open(path))
    except Exception:
        return None


# app icon (optional, only shows if the image file exists in same folder)
icon_path = os.path.join(BASE_DIR, "translate_icon.jpg")
image_icon = load_optional_image(icon_path)
if image_icon:
    root.iconphoto(False, image_icon)

# arrow image between the two text boxes (also optional)
arrow_path = os.path.join(BASE_DIR, "arrow.png")
arrow_img = load_optional_image(arrow_path)
if arrow_img:
    arrow_label = Label(root, image=arrow_img, width=150, bg="white")
    arrow_label.image = arrow_img  # keeping reference so python doesn't delete the image from memory
    arrow_label.place(x=460, y=50)
else:
    # agar image nahi mili to sirf ek arrow symbol dikha dete hain
    arrow_label = Label(root, text="\u27A1", font="Arial 40 bold", bg="white")
    arrow_label.place(x=500, y=60)

# ---------------- LEFT SIDE (source language box) ----------------

combo1 = ttk.Combobox(root, values=LANGUAGE_NAMES, font="Roboto 14", state="readonly")
combo1.place(x=110, y=20)
combo1.set("English")  # default value

label1 = Label(root, text="ENGLISH", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label1.place(x=10, y=50)

f = Frame(root, bg="Black", bd=5)
f.place(x=10, y=118, width=440, height=210)

text1 = Text(f, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=430, height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right", fill="y")
scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

# ---------------- RIGHT SIDE (target language box) ----------------

combo2 = ttk.Combobox(root, values=LANGUAGE_NAMES, font="Roboto 14", state="readonly")
combo2.place(x=700, y=20)
combo2.set("Urdu")  # default value

label2 = Label(root, text="URDU", font="segoe 30 bold", bg="white", width=18, bd=5, relief=GROOVE)
label2.place(x=600, y=50)

f1 = Frame(root, bg="Black", bd=5)
f1.place(x=600, y=118, width=440, height=210)

text2 = Text(f1, font="Robote 20", bg="white", relief=GROOVE, wrap=WORD)
text2.place(x=0, y=0, width=430, height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right", fill="y")
scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)


# ---------------- Translate button ----------------

translate_btn = Button(
    root,
    text="Translate",
    font="Roboto 15 bold italic",
    activebackground="purple",
    cursor="hand2",
    bd=5,
    bg="red",
    fg="white",
    command=translate_now,
)
translate_btn.place(x=470, y=250)

# start the label update loop and run the app
label_change()
root.mainloop()
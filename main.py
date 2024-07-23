from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox

from PIL import ImageTk, Image
from openpyxl import Workbook
import pathlib


BACKGROUND_COLOR = "#06283D"
FRAME_BG_COLOR = "#EDEDED"
FRAME_FG_COLOR = "#06283D"


root = Tk()
root.title("Student Registration System")
root.geometry("1250x700+210+100")
root.config(bg=BACKGROUND_COLOR)


file_path = pathlib.Path("Student_data.xlsx")
if not file_path.exists():
    workbook = Workbook()
    sheet = workbook.active
    headers = [
        "Registration No.", "Name", "Class", "Gender", "DOB",
        "Date Of Registration", "Religion", "Skill",
        "Father Name", "Mother Name", "Father's Occupation", "Mother's Occupation"
    ]
    for col, header in enumerate(headers, start=1):
        sheet.cell(row=1, column=col, value=header)
    workbook.save(file_path)

#top frames
Label(root, text="Email: nazaruk649@ukr.net", width=10, height=3, bg='#f0687c', anchor='e').pack(side=TOP, fill=X)
Label(root, text="STUDENT REGISTRATION", width=10, height=2, bg='#c36464',fg="#fff", font='arial 20 bold').pack(side=TOP, fill=X)

#search box to update

Search = StringVar()
Entry(root, textvariable=Search, width=17, bd=2, font='arial 20').place(x=820, y=65)
original_image = Image.open("/Users/ivan/Desktop/coding/programming/petprojects/Student_RegistrationSystem/media/search.png")
resized_image = original_image.resize((20, 20))
imageicon3 = ImageTk.PhotoImage(resized_image)

Srch = Button(
    root,
    text="Search",
    compound=LEFT,
    image=imageicon3,
    width=100,
    height=30,
    bg="#ADD8E6",
    font="arial 13 bold"
)
Srch.place(x=1060, y=65)

root.mainloop()

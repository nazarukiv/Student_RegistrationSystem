from datetime import date
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


#gender
def selection():
    value = radio.get()
    if value == 1:
        gender = "Male"
        print(gender)
    else:
        gender = "Female"
        print(gender)

#Exit command
def Exit():
    root.destroy()

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


#update button
original_image2 = Image.open(
        "/Users/ivan/Desktop/coding/programming/petprojects/Student_RegistrationSystem/media/update.png")
resized_image = original_image2.resize((40, 40))
imageicon4 = ImageTk.PhotoImage(resized_image)

Update_button = Button(root, image=imageicon4, bg="#c36464", borderwidth=0)
Update_button.place(x=110, y=60)

# Registration and Date
Label(root, text="Registration No:", font="arial 13", fg="white", bg=BACKGROUND_COLOR).place(x=30, y=150)
Label(root, text="Date:", font="arial 13", fg="white", bg=BACKGROUND_COLOR).place(x=500, y=150)

Registration=StringVar()
Date = StringVar()

reg_entry = Entry(root, textvariable=Registration, width=15, font='arial 10')
reg_entry.place(x=160, y=150)

today = date.today()
d1 = today.strftime("%d/%m/%Y")
date_entry = Entry(root, textvariable=Date, width=15, font="arial  10")
date_entry.place(x=550, y=150)

Date.set(d1)

#Student details
obj=LabelFrame(root, text="Student's Details", font=20, bd=2, width=900, bg=BACKGROUND_COLOR, fg='white', height=250, relief=GROOVE)
obj.place(x=30, y=200)

Label(root, text='Full Name:', font='arial 13', bg=FRAME_BG_COLOR, fg=BACKGROUND_COLOR).place(x=40, y=250)
Label(root, text='Date of Birth:', font='arial 13', bg=FRAME_BG_COLOR, fg=BACKGROUND_COLOR).place(x=40, y=300)
Label(root, text='Gender:', font='arial 13', bg=FRAME_BG_COLOR, fg=BACKGROUND_COLOR).place(x=40, y=350)

Label(root, text='Class:', font='arial 13', bg=FRAME_BG_COLOR, fg=BACKGROUND_COLOR).place(x=500, y=250)
Label(root, text='Religion:', font='arial 13', bg=FRAME_BG_COLOR, fg=BACKGROUND_COLOR).place(x=500, y=300)
Label(root, text='Skill:', font='arial 13', bg=FRAME_BG_COLOR, fg=BACKGROUND_COLOR).place(x=500, y=350)

Name=StringVar()
name_entry = Entry(obj, textvariable=Name, width=20, font='arial 10')
name_entry.place(x=160, y=30)

radio = IntVar()
R1 = Radiobutton(obj, text="Male", variable=radio, value=1, bg="white", fg=BACKGROUND_COLOR, command=selection)
R1.place(x=150, y = 133)

R2 = Radiobutton(obj, text="Female", variable=radio, value=2, bg="white", fg=BACKGROUND_COLOR, command=selection)
R2.place(x=230, y = 133)

Religion=StringVar()
religion_entry = Entry(obj, textvariable=Religion, width=20, font='arial 10')
religion_entry.place(x=630, y=80)

Skill=StringVar()
skill_entry = Entry(obj, textvariable=Skill, width=20, font='arial 10')
skill_entry.place(x=630, y=135)

Class = Combobox(obj, values = ["ICT", "Math", "Science", "English", "History", "Geography", "Art", "Physical Education"] , font="Roboto 10", width=17, state='r')
Class.place(x=630, y=30)
Class.set("Select Class")



# Parent details
parent_frame = LabelFrame(root, text="Parent's Details", font=20, bd=2, width=900, bg=BACKGROUND_COLOR, fg='white', height=220, relief=GROOVE)
parent_frame.place(x=30, y=470)

Label(parent_frame, text="Father's Name:", font="arial 13", bg=BACKGROUND_COLOR, fg=FRAME_BG_COLOR).place(x=30, y=50)
Label(parent_frame, text="Occupation:", font="arial 13", bg=BACKGROUND_COLOR, fg=FRAME_BG_COLOR).place(x=30, y=100)

F_Name = StringVar()
f_name_entry = Entry(parent_frame, textvariable=F_Name, width=20, font='arial 10')
f_name_entry.place(x=150, y=50)

Father_Occupation = StringVar()
FO_entry = Entry(parent_frame, textvariable=Father_Occupation, width=20, font='arial 10')
FO_entry.place(x=150, y=100)


Label(parent_frame, text="Mother's Name:", font="arial 13", bg=BACKGROUND_COLOR, fg=FRAME_BG_COLOR).place(x=500, y=50)
Label(parent_frame, text="Occupation:", font="arial 13", bg=BACKGROUND_COLOR, fg=FRAME_BG_COLOR).place(x=500, y=100)

M_Name = StringVar()
m_name_entry = Entry(parent_frame, textvariable=M_Name, width=20, font='arial 10')
m_name_entry.place(x=620, y=50)

Mother_Occupation = StringVar()
MO_entry = Entry(parent_frame, textvariable=Mother_Occupation, width=20, font='arial 10')
MO_entry.place(x=620, y=100)

# Image Frame
f = Frame(root, bd=3, bg="black", width=200, height=200, relief=GROOVE)
f.place(x=1000, y=150)

original_image = Image.open("/Users/ivan/Desktop/coding/programming/petprojects/Student_RegistrationSystem/media/profile.png")
resized_image = original_image.resize((200, 200))
img_profile = ImageTk.PhotoImage(resized_image)
lbl = Label(f, bg="black", image=img_profile)
lbl.place(x=0, y=0)


#button
upload_button = Button(root, text="Upload", width=19, height=2, font="arial 12 bold", bg="lightblue")
upload_button.place(x=1000, y=370)

save_button = Button(root, text="Save", width=19, height=2, font="arial 12 bold", bg="lightgreen")
save_button.place(x=1000, y=450)

reset_button = Button(root, text="Reset", width=19, height=2, font="arial 12 bold", bg="lightpink")
reset_button.place(x=1000, y=530)

exit_button = Button(root, text="Exit", width=19, height=2, font="arial 12 bold", bg="grey")
exit_button.place(x=1000, y=610)

root.mainloop()

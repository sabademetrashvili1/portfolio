import random
import string
from tkinter import *
import pandas as pd
import os
from datetime import datetime

root = Tk()
root.config(background='grey')
root.title('Password Generator')


label_email = Label(root, text="Email", width=18, border=3)
label_email.grid(row=0, column=0)

entry_email = Entry(root, width=40, border=3)
entry_email.grid(row=0, column=1)

data_email = []
data_password = []

def email():
    if entry_email.get()[-10:] != '@gmail.com':
        entry_email.delete(0, END)
        entry_password.delete(0, END)
    else:
        data_email.append(entry_email.get())
        data_password.append(entry_password.get())

    try:
        entry_email.delete(0, END)
        entry_password.delete(0, END)
    except:
        pass

button_email = Button(root, text='Submit', command=email)
button_email.grid(row=3, column=0, columnspan=3)

label_password = Label(root, text='Password', width=18, border=3)
label_password.grid(row=2, column=0)

entry_password = Entry(root, width=40, border=3, show='*')
entry_password.grid(row=2, column=1)

def insert_password():
    try:
        entry_password.delete(0, END)
    except:
        pass

    characters = list(string.ascii_letters + string.digits + '!@#$%&')

    random.shuffle(characters)

    length = 12
    genrated_password = ''.join(characters[:length])

    entry_password.insert(INSERT, genrated_password)

label_generate_password = Label(root, text='Generate Password', border=3, width=18)
label_generate_password.grid(row=1, column=0)

button_generate_password = Button(root, text='Submit', border=3, width=34, command=insert_password)
button_generate_password.grid(row=1, column=1)

root.mainloop()


full_data = pd.DataFrame({'Email': data_email,
                          'Password': data_password}, index=[i for i in range(len(data_password))])

print(full_data)


timestamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = 'data '+ timestamp + '.xlsx'
full_data.to_excel(file_name, sheet_name='Sheet1')

file_name = "data.xlsx"
path = os.path.join(os.path.expanduser("~"), "Documents", file_name)
if os.path.exists(path):
    file_name = f"data_{datetime.now().strftime('%Y%m%d%H%M%S')}.xlsx"

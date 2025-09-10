from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generate():

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    p_letters = [random.choice(letters) for _ in range(nr_letters)]
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    p_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    p_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = p_letters + p_symbols + p_numbers

    random.shuffle(password_list)

    password = ""
    for char in password_list:
      password += char

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_the_password():
    website = web_input.get()
    email = email_username_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password": password,

        }
    }
    if web_input.get() and email_username_input.get() and password_input.get():
        is_ok = messagebox.askokcancel(title=web_input.get(), message=f"These are the details entered: {web_input.get()} | {email_username_input.get()} | {password_input.get()}\n Is it ok to save?")
        if is_ok:
            try:
                with open("password_manager.json", "r") as data_file:
                    # 📌 기존 데이터 불러오기
                    data = json.load(data_file)
            except FileNotFoundError:
                data = {}
            except json.decoder.JSONDecodeError:
                data = {}

                # 📌 기존 데이터에 새로운 정보 추가
            data.update(new_data)

            # 📌 다시 파일에 덮어쓰기
            with open("password_manager.json", "w") as data_file:
                json.dump(data, data_file, indent=4)

            # 입력칸 초기화 (선택사항)
            web_input.delete(0, END)
            password_input.delete(0, END)
    else:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
bg_photo = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=bg_photo)
canvas.grid(column=1, row=0)

web_label = Label(text="Website:")
web_label.grid(column=0, row=1)
email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

web_input = Entry(width=35)
web_input.grid(column=1, row=1, columnspan=2)
web_input.focus()

email_username_input = Entry(width=35)
email_username_input.grid(column=1, row=2, columnspan=2)
email_username_input.insert(0, "luckey1212@naver.com")

password_input = Entry(width=23)
password_input.grid(column=1, row=3, sticky="e", padx=6)  # Entry 왼쪽 정렬

password_button = Button(text="Generate Password", command=password_generate)
password_button.grid(column=2, row=3, sticky="w")  # 버튼 왼쪽 정렬

add_button = Button(text="add", width=36, command=save_the_password)
add_button.grid(column=1, row=4, columnspan=2)




window.mainloop()
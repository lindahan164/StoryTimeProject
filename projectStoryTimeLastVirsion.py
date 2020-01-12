from tkinter import *
from tkinter import messagebox as ms

import sqlite3

from typing import List, Any

from PIL import ImageTk, Image

from docx import Document
from docx.shared import Inches

import os
# make database and users (if not exists already) table at programme start up
users = sqlite3.connect("users.db")
images = sqlite3.connect("images.db")
stories = sqlite3.connect("stories.db")



# users.cursor().execute("drop table users")
# images.cursor().execute("drop table images")
# stories.cursor().execute("drop table stories")


users.cursor().execute(
    "CREATE TABLE IF NOT EXISTS users (username TEXT PRIMARY KEY ,password TEXT, age INT, role TEXT, child TEXT, class TEXT)"
)

images.cursor().execute(
    "CREATE TABLE IF NOT EXISTS images (username TEXT PRIMARY KEY ,images TEXT)"
)

stories.cursor().execute(
    "CREATE TABLE IF NOT EXISTS stories (username TEXT PRIMARY KEY, story TEXT)"
)

# conn.cursor().execute("UPDATE users SET story=NULL WHERE username='s'")

# conn.cursor().execute("UPDATE users SET class='yud' WHERE username='s'")

# conn.cursor().execute("UPDATE users SET images='img1.jpeg img2.jpeg img3.jpeg img4.jpeg' WHERE username='s'")

# print(conn.cursor().execute('SELECT child FROM users WHERE username = "p"').fetchone())


# print(conn.cursor().execute('SELECT * FROM users').fetchall())

print(
    users.cursor()
    .execute("SELECT username, role, child, class FROM users")
    .fetchall()
)

print(
    images.cursor()
    .execute("SELECT username ,images from images")
    .fetchall()
)

print(
    stories.cursor()
    .execute("SELECT * from stories")
    .fetchall()
)


# print(conn.cursor().execute('SELECT * FROM classes').fetchall())

TEACHER = "teacher"
PARENT = "parent"
STUDENT = "student"

imgs = {}




# Login Function
    def login(self):
        # Establish Connection
        # with sqlite3.connect('quit.db') as db:
        c = self.users_db.cursor()
        # Find user If there is any take proper action
        find_user = "SELECT * FROM users WHERE username = ? and password = ?"
        c.execute(find_user, [(self.username.get()), (self.password.get())])
        result = c.fetchone()
        if not result:
            ms.showerror("אוי", "שם המשתמש או הסיסמא לא תקינים")
            return
        self.logf.pack_forget()
        # self.head['text'] = f'Logged In As\n {self.username.get()}'
        # self.head['pady'] = 150
        username = result[0]
        role: str = result[3].lower()
        if role == TEACHER:
            c.execute(
                "SELECT class FROM users WHERE username=?", (self.username.get(),)
            )
            self.classname.set(c.fetchone()[0])
            self.show_teacher_frame()
        elif role == PARENT:
            self.setup_parent()
            self.show_parent_frame()
            # show parents frame
            pass
        elif role == STUDENT:
            c.execute(
                "SELECT class FROM users WHERE username=?", (self.username.get(),)
            )
            self.classname.set(c.fetchone()[0])
            self.show_student_frame()
        else:
            print(f"לא מכיר את התפקיד {username} - {role}")
            return

    def new_user(self):
        # Establish Connection
        users_cursor = self.users_db.cursor()
        imagess_cursor = self.images_db.cursor()
        stories_cursor = self.stories_db.cursor()

        # Find Existing username if any take proper action
        # find_user = "SELECT * FROM users WHERE username = ?"
        # users_cursor.execute(find_user, [(self.username.get())])
        # if users_cursor.fetchall():
        #     ms.showerror("Error!", "Username Taken Try a Diffrent One.")
        #     return

        if self.n_role.get() not in [TEACHER, STUDENT, PARENT]:
            ms.showerror(
                "תקלה!",
                f"התפקיד {self.n_role.get()} לא קיים",
            )
            return

        # Create New Account
        insert_users = "INSERT INTO users(username, password, age, role) VALUES(?,?,?,?)"
        insert_images = "INSERT INTO images(username) VALUES(?)"
        insert_stories = "INSERT INTO stories(username) VALUES(?)"
        try:
            users_cursor.execute(
            insert_users,
            [
                (self.n_username.get()),
                (self.n_password.get()),
                self.n_age.get(),
                self.n_role.get().lower(),
            ],
        )
        except Exception:
            return ms.showerror("!תקלה", "שם המשתמש קיים")
        imagess_cursor.execute(
            insert_images,
            [
                (self.n_username.get()),
            ],
        )
        stories_cursor.execute(
            insert_stories,
            [
                (self.n_username.get()),
            ],
        )
        self.users_db.commit()
        self.images_db.commit()
        self.stories_db.commit()
        ms.showinfo("בוצע", "המשתמש נוצר בהצלחה")
        self.login_frame()

    # Frame Packing Methords
    def login_frame(self):
        self.username.set("")
        self.password.set("")
        self.crf.pack_forget()
        self.teacher_frame.pack_forget()
        self.head["text"] = "התחברות"
        self.logf.pack()

    def create_acc_frame(self):
        self.n_username.set("")
        self.n_password.set("")
        self.logf.pack_forget()
        self.logf.pack_forget()
        self.head["text"] = "יצירת משתמש"
        self.crf.pack()


    def show_teacher_frame(self):
        self.parents_suggestions.pack_forget()
        self.logf.pack_forget()
        self.lesson.pack_forget()
        # self.head.pack_forget()
        self.head["text"] = f"ברוכים הבאים למסך המורה {self.username.get()}"
        self.teacher_frame.pack()
     


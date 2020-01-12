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


    def show_student_frame(self):
        if self.get_images_for_student() == -1:
            self.logf.pack()
            return
        self.logf.pack_forget()
        self.student_frame.pack()
        self.head["text"] = "הינה הקלפים לשיעורינו. "
        for i in range(4):
            Label(self.student_frame, image=imgs[self.images[i]]).grid(row=0, column=i)

    def show_parent_frame(self):
        self.suggest.pack_forget()
        self.head["text"] = "מסך הורה"
        self.parent_frame.pack()

    def suggest_to_teacher(self):
        if self.student.get() == "None":
            ms.showerror("תקלה", "לא הגדרת ילד")
            return
        c = self.users_db.cursor()
        child_class = "SELECT class FROM users WHERE username = ?"
        classname = c.execute(child_class, (self.student.get(),)).fetchone()
        self.head["text"] = "הצע תמונות למורה של ילדך"
        self.parent_frame.pack_forget()
        self.suggest.pack()

    def start_lesson(self):
        self.logf.pack_forget()
        self.teacher_frame.pack_forget()
        self.lesson.pack()
        self.head["text"] = "בחר קלפים לשיעור "
        img = None
        i = 0
        for child in self.lesson.children.values():
            if not isinstance(child, Button):
                continue
            i += 1
            if i > 12:
                return
            img = imgs[f"img{i}.jpeg"]
            child.configure(image=img)
            # child.image = img

    def image_button(self, button_id, frame):
        if len(self.images) >= 4:
            return ms.showerror("כבר נבחר", "כבר נבחרו 4 קלפים")
        button = list(frame.children.values())[button_id - 1]
        button.grid_remove()
        self.add_image(f"img{button_id}.jpeg")
        print(self.images)
        c = self.images_db.cursor()
        update_users = "INSERT OR REPLACE INTO images (images, username) VALUES (?, ?)"
        # update_classes = ('UPDATE classes SET images = ? WHERE name = ?')
        user_params = [(" ".join(self.images)), (self.username.get())]
        # class_params = [(' '.join(self.images)), (self.classname.get())]
        c.execute(update_users, user_params)
        # c.execute(update_classes, class_params)
        self.images_db.commit()

    def add_image(self, name: str):
        if name not in self.images:
            self.images.append(name)


    def create_class(self):
        c = self.users_db.cursor()
        c.execute("SELECT class FROM users WHERE username=?", (self.username.get(),))
        classname = c.fetchone()[0]
        print(classname)
        if classname:
            self.classname.set(classname)
            ms.showerror("טעות", "כבר יש לך כיתה!")
            return
        uname = self.username.get()
        classname = self.classname.get()
        if classname == "None":
            ms.showerror("טעות", "את חייבת לבחור שם לכיתה")
            return

        update_users = "UPDATE users SET class = ? WHERE username = ?"
        # insert_classes = ('INSERT INTO classes(name, teacher) VALUES (?, ?)')
        c.execute(update_users, [(classname), (uname)])
        # c.execute(insert_classes, [(classname), (uname)])
        self.users_db.commit()
        ms.showinfo("הצלחה", "הכיתה נוצרה")

    def add_student(self):
        if not self.classname.get():
            ms.showerror("טעות", "עדיין לא יצרת כיתה")
            return
        c = self.users_db.cursor()
        find_user = "SELECT * FROM users WHERE username = ? AND role = ?"
        c.execute(find_user, [(self.student.get()), (STUDENT)])
        student = c.fetchone()
        if not student:
            ms.showerror("Error!", "Student in that name is not found")
            return
        # Create New Account
        update = "UPDATE users SET class = ? WHERE username = ?"
        c.execute(update, [(self.classname.get()), (self.student.get())])
        self.users_db.commit()
        ms.showinfo(
            "הצלחה",
            f"התווסף {self.student.get()} לכיתה-  {self.classname.get()}",)


      

     


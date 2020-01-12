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


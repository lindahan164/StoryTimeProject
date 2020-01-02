import tkinter as tk
    

def perent_start_window():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry("350x350")
root.title("Perent screen-story time")
button = tk.Button(frame, 
                   text="צא מהמערכת", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="הפק דוח תלמיד",
                   command=perent_start_window)
slogan.pack(side=tk.LEFT)

root.mainloop()



def techer_start_window():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.geometry("350x350")
root.title("techer screen-story time")
button = tk.Button(frame, 
                   text="צא מהמערכת", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="להפקת דוח בחירת תלמיד",
                   command=techer_start_window)
slogan.pack(side=tk.LEFT)

button2=tk.Button(frame,text="בחירת תוכן שיעור",fg="blue",command=techer_start_window)
button2.pack(side=tk.LEFT)
root.mainloop()

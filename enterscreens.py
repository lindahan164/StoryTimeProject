import tkinter as tk
    

def write_slogan():
    print("Tkinter is easy to use!")

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()

button = tk.Button(frame, 
                   text="צא מהמערכת", 
                   fg="red",
                   command=quit)
button.pack(side=tk.LEFT)
slogan = tk.Button(frame,
                   text="הפק דוח תלמיד",
                   command=write_slogan)
slogan.pack(side=tk.LEFT)

root.mainloop()

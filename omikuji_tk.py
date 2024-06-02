# s24009
#GUIおみくじプログラム
import tkinter as tk
root = tk.Tk()
root.geometry("300x200")
import random
omikuji = ["大吉","中吉","小吉""凶"]
lbl = tk.Label(text=(random.choice(omikuji)))
lbl.pack()
root.mainloop()

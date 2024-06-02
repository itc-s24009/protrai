# GUIで動くアプリを作ってみよう

import tkinter as tk

root = tk.Tk()

root.geometry("1000x1000")
root.title("ハローアプリ")
lbl = tk.Label(text="こんにちは世界")
lbl.pack()
lbl = tk.Label(text="初めてのGUIアプリ")
lbl.pack()
root.mainloop()

#s24009
#標準入力を税込み(+10%)するプログラム
import tkinter as tk

def dispLabel():
    a =entry.get()
    if a.isdecimal() == True:
        a = int(a)
        s = a * 1.1
        s = int(s)
        lbl.config(text=f"税込み価格は{s}円")
    else:
        lbl.config(text="数字を入れてね")
root = tk.Tk()
root.title("エントリーウィジェット")
root.geometry("400x200")

lbl = tk.Label(text="ラベル",font=("Helvetica",20))
entry = tk.Entry(font=("Helvetica",20))
btn = tk.Button(text="ボタン",font=("Helvetica",20),command=dispLabel)



lbl.pack()
entry.pack()
btn.pack()
tk.mainloop()

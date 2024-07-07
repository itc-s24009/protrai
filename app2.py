import tkinter as tk
def dispLabel():
    lbl.config(text="こんにちは")

root = tk.Tk()#画面作る
root.geometry("400x200")#画面のサイズ決める

lbl = tk.Label(text="LABEL", font=("Helvetica" , 20))#ラベル作る
btn = tk.Button(text="PUSH", command=dispLabel, font=("Helvetica" , 20))#ボタン作る

lbl.pack()#ラベルを画面に置く
btn.pack()#ボタンを画面に置く
lbl2 = tk.Label(text="ラベル２", font=("Helvetica" , 20))
btn2 = tk.Button(text="何もしないボタン", font=("Helvetica" , 20))
lbl2.pack()
btn2.pack()
tk.mainloop()#画面を表示する

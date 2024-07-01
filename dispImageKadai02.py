#24009
# 画像をグレー、90度回転し水平方向に反転
import tkinter as tk
import tkinter.filedialog as fd
import PIL.Image, PIL.ImageTk
def dispPhoto(path):
    newImage = PIL.Image.open(path).convert("L").rotate(90).transpose(PIL.Image.FLIP_LEFT_RIGHT).resize((300,300))
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData
def openFile():
    fpath = fd.askopenfilename()
    if fpath:
        dispPhoto(fpath)
        print(fpath)
        lbl3 = tk.Label(text=fpath)
        lbl3.pack()
root = tk.Tk()
root.geometry("400x400")
lbl2 = tk.Label(text="🎨画像表示アプリ バージョン2.0🎨")
btn = tk.Button(text="ファイルを開く", command = openFile)
imageLabel = tk.Label()
lbl2.pack()
btn.pack()
imageLabel.pack()
tk.mainloop()

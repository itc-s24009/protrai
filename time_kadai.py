#24009
#実行で時間を表示するアプリ

import datetime
import tkinter as tk #アプリにするやつ
#時間を出力する関数
def update_time():
    now = datetime.datetime.now()
    current_time = now.strftime("%Y年%m月%d日　%H時%M分%S秒")#表記方法
    lbl.config(text=current_time)#テキストの代入
    root.after(1000, update_time)#繰り返し実行

root = tk.Tk()#画面の作成

root.title("時計アプリ")#タブ名

lbl = tk.Label()#テキスト作成
lbl.config(text="", font=("Helvetica", 20))#サイズとフォント
lbl.pack()#テキスト配置

update_time()#時間の出力

root.mainloop()#画面の出力

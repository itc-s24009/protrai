#24009
#「こんにちは世界」と書かれたHTML文章を表示するプログラム

#事前にflaskモジュールをインストールすると使える
from flask import Flask,render_template

#Flaskライブラリをインスタンス化し、app変数に割り当て
#その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

#ルートＵＲＬに対するリクエストｗｐ処理するデコレーター
#引数にルート'/'を指定するとアクセスした際index()関数が呼び出される

@app.route('/')
def index():
    #templates/index.html
    return render_template('index.html')

@app.route('/himitu')
def himitu():
    #templates/himitu.html
    return render_template('himitu.html')



if __name__ == '__main__':
    app.run(host='0.0.0.0',port=6423)


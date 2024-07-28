#24009
#Flaskの練習　Hello Worldを出力する

#事前にflaskモジュールをインストールすると使える
from flask import Flask

#Flaskライブラリをインスタンス化し、app変数に割り当て
#その際、コンストラクタへの引数は実行中のモジュールを指定する
app = Flask(__name__)

#ルートＵＲＬに対するリクエストｗｐ処理するデコレーター
#引数にルート'/'を指定するとアクセスした際index()関数が呼び出される

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

if __name__ == '__main__':
    app.run(debug=True)

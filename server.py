from flask import Flask,request,render_template
app = Flask(__name__)
file_path ="./sensor_data.csv"
port_num=20022

@app.route('/',methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/lux',methods=['POST'])
def update_lux():
    time = request.form["time"]
    lux = request.form["lux"]
    try:
        f = open(file_path,'w')
        f.write(time+","+lux)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()                      
@app.route('/lux',methods=['GET'])

def get_lux():
    try:
        f = open(file_path,'r')
        for row in f:
            lux = row
    except Exception as e:
        print(e)
    finally:
        f.close()
        return lux

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port=port_num)        
    """
server.pyの仕様について
・ルートパス(/)にGETメソッドでアクセスした時にindex.htmlを返す
・/luxパスにGETメソッドでアクセスすると、sensor_data.csvの内容を返す
・/luxパスにPOSTメソッドで、時間と照明値のパラメータを付与してアクセスするとsensor_data.csvに内容を上書きで書き込む

GETメソッド・・・HTTP通信でWebブラウザ等のクライアントからWebサーバへ送られる、HTTPリクエストの一種である。
webサーバから情報を取り出すために使用される。(HTTPリエスト歯、リクエスト行、ヘッダ、メッセージボディの３つの部分で構成される。)

POSTメソッド・・・HTTP通信でWebブラウザ等のクライアントからWebサーバへと送られる、HTTPリクエストの一種です。 基本的に、
ebサーバに情報を送り出す（POST）するために使用されます。 HTTPリクエストは、リクエスト行、ヘッダ、メッセージ ボディの3つの部分で構成されます。
"""


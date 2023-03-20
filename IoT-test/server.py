from flask import Flask,request,render_template
import pandas as pd
app = Flask(__name__)
file_path ="./sensor_data.csv"
port_num=20022

list1 = [["NULL","NULL","NULL"],["NULL","NULL","NULL"],["NULL","NULL","NULL"]]
index1 = ["locate_A","locate_B","locate_C"]
columns1 = ["state","time","count"]
book_store = pd.DataFrame(data = list, index = index1, columns = columns1)
book_store.to_csv(r"/home/selab/20022/Iot-test/server/IoT-test/book_store.csv")

@app.route('/',methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/state',methods=['POST'])
def update_state():
    time = request.form["time"]
    state = request.form["state"]
    count = request.form["count"]   
    #book_store.to_csv(r"/home/selab/20022/server1/book_store.csv")

    try:
        book_store.at["locate_A","state"] = state
        book_store.at["locate_A","time"] = time
        book_store.at["locate_A","count"] = count  
        book_store.to_csv(r"/home/selab/20022/server1/book_store.csv")
        #f = open(file_path,'w')
        #f.write(time+","+state)
        return "succeeded to write"
    
    except Exception as e:  
        print(e)
        return "failed to write"
    finally:
        pass
        #f.close()      

@app.route('/state',methods=['GET'])
def get_state():
    try:
        state = book_store.at["locate_A","state"]
        time = book_store.at["locate_A","time"]
        count = book_store.at["locate_A","count"]

    except Exception as e:
        print(e)
    finally:
        #f.close()
        return ( state + "," + time + "," + count )

if __name__=='__main__':
    app.run(debug=True,host='0.0.0.0',port = port_num)        

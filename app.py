from flask import Flask, render_template,request
import requests

app=Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/weatherapp',methods=['POST','GET'])
def get_weatherData():
    url="https://api.openweathermap.org/data/2.5/weather"
    params={
        'q':request.form.get("city"),
        'appid':"c8748377a756c2f5960704361bf6b272",
        'units':request.form.get("metric")
    }
    response=requests.get(url,params=params)
    print(response)
    data=response.json()
    return f"data: {data}"

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5002)

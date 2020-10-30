import joblib
from flask import Flask, request, render_template
import numpy as np

app = Flask(__name__)
res = joblib.load('hppmodel.pkl')


@app.route('/')
def index():

    return render_template('index.html')


@app.route('/result', methods=['post', 'get'])
def login():
    if request.method == 'POST':
        Builder = 0
        Dealer = 0
        Owner = 0
        BHK = 0
        RK = 0

        if(request.form["posted"]=='Builder'):
            Builder=1
        elif (request.form["posted"]=='Dealer'):
            Dealer=1
        elif (request.form["posted"]=='Owner'):
            Owner=1

        if(request.form["bhk"]=='BHK'):
            BHK=1
        elif(request.form["bhk"]=='RK'):
            RK=1

        cons = request.form["construction"]
        cons = int(cons)
        rer = request.form["rera"]
        rer = int(rer)
        nobhk = request.form["nbhk"]
        nobhk = int(nobhk)
        square = request.form["sqf"]
        square = float(square)
        isready = request.form["ready"]
        isready = int(isready)
        resal = request.form["resale"]
        resal = int(resal)
        latt = request.form["lat"]
        latt = float(latt)
        longg = request.form["long"]
        longg = float(longg)

        out = res.predict([[Builder,Dealer,Owner,BHK,RK,cons,rer,nobhk,square,isready,resal,latt,longg]])
        out = abs(out)
        out=float(out)
        out = round(out, 2)
    return render_template("index.html", val=out)



if __name__ == '__main__':
    app.run(debug=True)
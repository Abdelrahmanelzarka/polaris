import warnings
warnings.filterwarnings('ignore')
from flask import Flask,request,render_template
from Api_model import Prediction
app = Flask(__name__)

#pre = Prediction("pulsar.pkl")

@app.route('/', methods= ['GET']) ## page name 
def home():
    return render_template("main.html")

@app.route("/pulsarPredict" , methods = ["POST"]) ## page name 
def pulsarPredict():
    pre = Prediction("pulsar.pkl")
    mip = min(max(float(request.form.get("mip")),61.513672),166.466797)
    stdip = min(max(float(request.form.get("stdip")),29.436902),63.904423)
    sip = min(max(float(request.form.get("sip")),-1.791886),2.613147)
    mc = min(max(float(request.form.get("mc")),0.213211),10.667329)
    ec = min(max(float(request.form.get("ec")),-1.584232),18.115223)
    
    ans = pre.prediect([mip,stdip,sip,mc,ec])
    if(ans[0]):
        out = "IS pulsar"
    else:
        out = "NOT pulsar"
    
    data = {"ans":out}
    return render_template("ans.html", data=data)


#starTypes
@app.route("/StarPredict" , methods = ["POST"]) ## page name 
def StarPredict():
    pre = Prediction("starType.pkl")
    k = float(request.form.get("k"))
    lo = float(request.form.get("lo"))
    ro = float(request.form.get("ro"))
    mv = float(request.form.get("mv"))
    sc = float(request.form.get("sc"))
    
    ans = pre.prediect([mv,ro,lo,sc,k])
    
    if(ans[0] == 0):
        out = "Brown Dwarf"
    elif(ans[0] == 1):    
        out = "Red Dwarf" 
    elif(ans[0] == 2):
        out = "White Dwarf" 
    elif(ans[0] == 3):
        out = "Main Sequence" 
    elif(ans[0] == 4):
        out = "Supergiant" 
    elif(ans[0] == 5):
        out = "Hypergiant" 
    
    data = {"ans":out}
    return render_template("ans.html", data=data)


@app.route("/pulsar", methods= ['GET'])
def fun1():
    return render_template("pulsar.html")


@app.route("/types", methods= ['GET'])
def fun2():
    return render_template("type.html")

if __name__=='__main__':
    app.run(port=3000,debug=True)
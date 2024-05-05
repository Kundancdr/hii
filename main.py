from flask import Flask,render_template,request,redirect,url_for,jsonify

app=Flask(__name__)

@app.route("/", methods=["GET"])
def welcome():
    return "Welcome to my first flask project"

@app.route("/index",methods=["GET"])
def index():
    return "This is my index Page"

@app.route('/sucess/<int:score>')
def sucess(score):
    return "the person has passed and thr score is :" +str(score)

@app.route('/fail/<int:score>')
def fail(score):
    return "the person has failed and thr score is :" +str(score)

@app.route('/form',methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3

        # return render_template('form.html',score=average_marks)
        res=""

        if average_marks>=50:
            res ="sucess"
        else:
            res="fail"

        return redirect(url_for(res,score=average_marks))
    
    #creating apis
@app.route('/api',methods=['POST'])
def calculate_sum():
        data=request.get_json()
        a_value=float(dict(data)['a'])
        b_value=float(dict(data)['b'])
        return jsonify(a_value + b_value)

if __name__=="__main__":
    app.run(debug=True)
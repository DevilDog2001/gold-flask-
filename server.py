from flask import Flask,render_template,session,request,redirect
import random
app = Flask(__name__)
app.secret_key = 'Ninja_Gold'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_money',methods=['POST'])
def process_money():
    counter = []
    if request.form['building'] == 'farm':
        count = random.randint(10,20)
        session['gold'] += counter['count']
        
    if request.form['building'] == 'cave':
        count = random.randint(5,10)
        session['gold'] += counter['count']
    
    if request.form['building'] == 'house':
        count = random.randint(2,5)
        session['gold'] += counter['count']
        
    if request.form['building'] == 'casino':
        count = random.randint(-51,51)
        session['gold'] += counter['count']
    return redirect('/')

@app.route('/restart')
def reset():
    session.clear
    return render_template('/index.html')



if __name__=='__main__':
    app.run(debug=True)
    
from flask import Flask, render_template, request, redirect, session
import math
app = Flask(__name__)
app.secret_key = 'alovio1313' 

@app.route('/')
def index():
    session['cont']
    if 'cont' in session:
        print('la llave existe!')
        session['cont']+=1
        
    else:
        print("la llave 'cont' NO existe")
    return render_template("index.html", cont=session['cont'])

        
@app.route('/destroy_session', methods=['POST'])
def destroy_session():
    session.pop('cont')	
    session['cont']=0
    return redirect("/")	 

@app.route('/aumenta2', methods=['POST'])
def aumenta2():
    session['cont']+=1
    return redirect("/")	

@app.route('/aumentan', methods=['POST'])
def aumentan():
    n=int(request.form['cant'])
    n-=1
    session['cont']+=n
    return redirect("/")



if __name__ == "__main__":
    app.run(debug=True)
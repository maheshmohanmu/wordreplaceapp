import os
from flask import Flask, request, redirect, url_for, render_template,jsonify

app = Flask(__name__)

def replace_word(inptext):
   replc_dict = {
    "Oracle" : "Oracle©", 
    "Google" : "Google©", 
    "Microsoft" : "Microsoft©", 
    "Amazon" : "Amazon©", 
    "Deloitte" : "Deloitte©"
   }
   
   temp = inptext.split()
   replc = []
   for wrd in temp:
    replc.append(replc_dict.get(wrd, wrd))
	
   replc = ' '.join(replc)
   return str(replc)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/join', methods=['GET','POST'])
def my_form_post():
    inptext = request.form['inptext']
    #word = request.args.get('inptext')
    replc = replace_word(inptext)
    result = {
        "output": replc
    }
    result = {str(key): value for key, value in result.items()}
    return jsonify(result=result)
    #return redirect(url_for('home'))
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
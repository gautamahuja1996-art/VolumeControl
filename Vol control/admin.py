from flask import Flask, render_template, redirect, request

app = Flask(__name__)

name_list = ['gautam', 'manoj', 'ganpat', 'vicky', 'nayan', 'shalini']

@app.route('/', methods = ['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('form.html')
    else:
        name = request.form.get('name')
        if name in name_list:
            return "Welcome" + '\t' + name
        else:
            return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)

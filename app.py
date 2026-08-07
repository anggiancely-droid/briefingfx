from flask import Flask, render_template

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/metar.html')
def metar():
    return render_template('metar.html')

@app.route('/satelit.html')
def satelit():
    return render_template('satelit.html')

@app.route('/hazard.html')
def hazard():
    return render_template('hazard.html')

@app.route('/wind3000.html')
def wind3000():
    return render_template('wind3000.html')

@app.route('/charts.html')
def charts():
    return render_template('charts.html')

@app.route('/print.html')
def print_page():
    return render_template('print.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
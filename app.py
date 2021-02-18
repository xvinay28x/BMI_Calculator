from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template("index.html")

@app.route('/calculate', methods=['POST'])
def home():
    weight = request.form['w']
    height = request.form['h']
    w = int(weight)
    h = int(height)
    bmi = (w/(h/100*h/100))
    a = str(bmi)
    b = a[:4]
    return render_template("index.html",bmi=b, answer = "YOUR BMI IS : {}".format(b))

if __name__ == "__main__":
    app.run(debug = True)
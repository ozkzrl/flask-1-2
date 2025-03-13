from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def head():
   num1 = 456
   num2 = 258
   return render_template('index.html', num1=num1, num2=num2)

@app.route('/sum')
def number():
   # num1 ve num2, index.html sayfasından gelen değerlerdir
   value1 = 456  # Bunları yine index.html sayfasından alabilirsiniz
   value2 = 258
   return render_template('body.html', value1=value1, value2=value2, sum=value1 + value2)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)

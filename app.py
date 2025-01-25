from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # Your Python program logic here
    python_output = "Hello, this is the result from Python!"
    return render_template('index.html', result=python_output)

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # You can pass dynamic data here in the future
    return render_template('index.html')

if __name__ == '__main__':
    # Runs the app on port 5000 with debug mode enabled for easy development
    app.run(debug=True, host='0.0.0.0', port=5000)
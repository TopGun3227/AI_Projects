# InsightBrew Landing Page
# Enhanced with Colorful Designs and Visual Improvements
# Current Date: 2026-03-16 15:12:20

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
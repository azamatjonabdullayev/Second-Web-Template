from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/service')
def service():
    return render_template("service.html")

@app.route('/team')
def team():
    return render_template("team.html")

@app.route('/why')
def why():
    return render_template("why.html")

if __name__ == "__main__":
    app.run(debug=True)

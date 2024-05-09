from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder="templates")

@app.route("/")
def render_index():
    return render_template("index.html")

@app.route('/<path:path>')
def static_file(path):
    return send_from_directory('static', path)

if __name__ == "__main__":
    app.run(debug = True)
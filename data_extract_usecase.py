from flask import Flask, request, render_template_string

app = Flask(__name__)

submitted_data = []

@app.route("/")
def home():
    return '''
        <h2>Upload Demo</h2>
        <a href="/view">View Submitted Data</a>
    '''

@app.route("/submit", methods=["POST"])
def submit():
    name = request.form.get("name")
    location = request.form.get("location")
    if name and location:
        submitted_data.append((name, location))
        return f"Received: {name}, {location}"
    return "Invalid data", 400

@app.route("/view", methods=["GET"])
def view():
    html = "<h2>Submitted Data</h2><ul>"
    for name, location in submitted_data:
        html += f"<li>{name} - {location}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(debug=True)

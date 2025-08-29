from flask import Flask, request, jsonify

app = Flask(__name__)

# Store submitted rows in memory
submitted_data = []

@app.route("/submit", methods=["POST"])
def submit_data():
    name = request.form.get("name")
    location = request.form.get("location")
    if name and location:
        submitted_data.append({"name": name, "location": location})
        print(f"Received: {name}, {location}")  # Also print in terminal
        return jsonify({"status": "success", "message": f"Received {name}, {location}"}), 200
    return jsonify({"status": "error", "message": "Missing data"}), 400

@app.route("/view")
def view_data():
    html = """
    <html>
    <head>
        <title>Submitted Data</title>
        <!-- Auto-refresh every 5 seconds -->
        <meta http-equiv="refresh" content="5">
        <style>
            body { font-family: Arial, sans-serif; margin: 20px; }
            table { border-collapse: collapse; width: 60%; }
            th, td { border: 1px solid #ccc; padding: 8px; text-align: left; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h2>Submitted Data</h2>
        <table>
            <tr><th>Name</th><th>Location</th></tr>
    """
    for row in submitted_data:
        html += f"<tr><td>{row['name']}</td><td>{row['location']}</td></tr>"
    html += """
        </table>
    </body>
    </html>
    """
    return html

if __name__ == "__main__":
    app.run(debug=True)

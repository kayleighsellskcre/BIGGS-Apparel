from flask import Flask, render_template, request

app = Flask(__name__)

# Example data – later you can pull from a database
CLIENTS = [
    {"slug": "riverview-apparel", "name": "Riverview Apparel"},
    {"slug": "mv-cheer", "name": "Mill Valley Cheer"},
    {"slug": "desoto-cheer", "name": "De Soto Cheer"},
]

BELLA_STYLES = [
    {"code": "3001", "name": "Bella+Canvas 3001 Unisex Tee"},
    {"code": "3901", "name": "Bella+Canvas 3901 Crewneck"},
    {"code": "3719", "name": "Bella+Canvas 3719 Hoodie"},
    {"code": "3501", "name": "Bella+Canvas 3501 Long Sleeve"},
]

PLACEMENTS = [
    "Front Center",
    "Front Left Chest",
    "Back Center",
    "Upper Back",
    "Sleeve",
]

@app.route("/")
def home():
    return render_template("index.html", clients=CLIENTS)

@app.route("/order")
def order():
    client_slug = request.args.get("client")
    return render_template(
        "order.html",
        clients=CLIENTS,
        bella_styles=BELLA_STYLES,
        placements=PLACEMENTS,
        selected_client=client_slug,
    )

if __name__ == "__main__":
    app.run(debug=True)

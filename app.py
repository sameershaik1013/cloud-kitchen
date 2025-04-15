from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/menu")
def menu():
    items = []
    with open('menu.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            items.append(row)
    return render_template("menu.html", items=items)

@app.route("/order", methods=["POST"])
def order():
    name = request.form.get("name")
    item = request.form.get("item")
    print(f"Order received: {name} wants {item}")
    return render_template("order.html", name=name, item=item)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=True)

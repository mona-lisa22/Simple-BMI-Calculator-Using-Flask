from flask import Flask, render_template, request

app = Flask(__name__)


def calculate(weight, height, unit):
    if unit == "metric":
        height = height / 100  # Convert cm to meters
        bmi = weight / (height ** 2)
    else:  # Imperial
        bmi = (weight / (height ** 2)) * 703
    return round(bmi, 2)


def classification(bmi):

    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal weight"
    elif bmi < 29.9:
        return "Overweight"
    elif bmi < 34.9:
        return "Obese"
    elif bmi < 39.9:
        return "Severely Obese"
    else:
        return "Morbidly Obese"


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        unit = request.form["unit"]
        weight = float(request.form["weight"])
        height = float(request.form["height"])

        bmi = calculate(weight, height, unit)
        category = classification(bmi)

        return render_template("index.html", bmi=bmi, category=category)

    return render_template("index.html", bmi=None, category=None)


if __name__ == "__main__":
    app.run(debug=True)

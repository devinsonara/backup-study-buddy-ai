import os
import matplotlib.pyplot as plt
from flask import Flask, render_template, request
from question_bank import QUESTION_BANK

app = Flask(__name__)


# ✅ DOUBT SOLVER
def solve_doubt(subject, user_question):
    if not subject or not user_question:
        return "❌ Please select subject and enter a question!"

    subject = subject.lower().strip()
    user_question = user_question.strip()

    if subject not in QUESTION_BANK:
        return "❌ Subject not found! Please select Maths / Physics / MTC / English / C"

    for item in QUESTION_BANK[subject]:
        if user_question.lower() == item["q"].lower():
            return item["a"]

    return "❌ Sorry! This question is not available in prototype question bank."


# ✅ TIMETABLE GENERATOR
def generate_timetable(user_input):
    subjects = [s.strip() for s in user_input.split(",") if s.strip()]

    if len(subjects) == 0:
        return "❌ Please enter subjects like: Maths, Physics, C"

    slots = [
        "7:00 - 8:00",
        "8:00 - 9:00",
        "9:00 - 10:00",
        "10:30 - 11:30",
        "11:30 - 12:30",
        "2:00 - 3:00",
        "3:00 - 4:00",
        "4:00 - 5:00"
    ]

    timetable = "✅ Your Timetable:\n\n"
    i = 0
    for slot in slots:
        timetable += f"{slot}  →  {subjects[i % len(subjects)]}\n"
        i += 1

    timetable += "\n✨ Tip: 50 min study + 10 min break 💙"
    return timetable


# ✅ GRAPH GENERATOR
def generate_graph(user_input):
    user_input = user_input.strip()

    if user_input == "":
        return None

    x = list(range(-10, 11))
    y = []

    expr = user_input.replace("^", "**")

    for val in x:
        try:
            y_val = eval(expr, {"x": val, "__builtins__": {}})
            y.append(y_val)
        except:
            return None

    plt.figure()
    plt.plot(x, y)
    plt.title(f"y = {user_input}")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.grid(True)

    if not os.path.exists("static"):
        os.makedirs("static")

    graph_path = os.path.join("static", "graph.png")
    plt.savefig(graph_path)
    plt.close()

    return "graph.png"


# ✅ HOME
@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    user_input = ""
    graph_img = ""

    if request.method == "POST":
        user_input = request.form.get("user_input", "")
        feature = request.form.get("feature", "doubt")

        if feature == "doubt":
            subject = request.form.get("subject")
            response = solve_doubt(subject, user_input)
            graph_img = ""

        elif feature == "timetable":
            response = generate_timetable(user_input)
            graph_img = ""

        elif feature == "graph":
            graph_file = generate_graph(user_input)
            if graph_file:
                response = "✅ Graph generated successfully!"
                graph_img = graph_file
            else:
                response = "❌ Graph generate nahi hua! Try: x^2, x+5"
                graph_img = ""

    return render_template("index.html", response=response, user_input=user_input, graph_img=graph_img)


if __name__ == "__main__":
    app.run(debug=True)

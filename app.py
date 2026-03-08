from flask import Flask, render_template, request

app = Flask(__name__)

programs = {
    "Fat Loss (FL)": {
        "workout": "\nMon: 5x5 Back Squat + AMRAP\nTue: EMOM 20min Assault Bike\nWed: Bench Press + 21-15-9\nThu: 10RFT Deadlifts/Box Jumps\nFri: 30min Active Recovery",
        "diet": "\nB: 3 Egg Whites + Oats Idli\nL: Grilled Chicken + Brown Rice\nD: Fish Curry + Millet Roti\nTarget: 2,000 kcal",
        "color": "#e74c3c"
    },
    "Muscle Gain (MG)": {
        "workout": "\nMon: Squat 5x5\nTue: Bench 5x5\nWed: Deadlift 4x6\nThu: Front Squat 4x8\nFri: Incline Press 4x10\nSat: Barbell Rows 4x10",
        "diet": "\nB: 4 Eggs + PB Oats\nL: Chicken Biryani (250g Chicken)\nD: Mutton Curry + Jeera Rice\nTarget: 3,200 kcal",
        "color": "#2ecc71"
    },
    "Beginner (BG)": {
        "workout": "\nCircuit Training: Air Squats, Ring Rows, Push-ups.\nFocus: Technique Mastery & Form (90% Threshold)",
        "diet": "\nB: 3 Egg Whites + Oats Idli\nL: Grilled Chicken + Brown Rice\nD: Fish Curry + Millet Roti\nTarget: 2,000 kcal",
        "color": "#3498db"
    }
}

@app.route("/", methods=["GET", "POST"])
def index():
    selected = None
    workout = ""
    diet = ""
    color = "white"

    if request.method == "POST":
        selected = request.form.get("program")
        if selected in programs:
            workout = programs[selected]["workout"]
            diet = programs[selected]["diet"]
            color = programs[selected]["color"]

    return render_template(
        "index.html",
        programs=programs,
        selected=selected,
        workout=workout,
        diet=diet,
        color=color
    )

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True )
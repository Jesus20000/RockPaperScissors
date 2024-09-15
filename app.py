from flask import Flask, render_template, request
import random

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    choices = ["rock", "paper", "scissors"]
    images = {"rock": "rock.jpg", "paper": "paper.jpg", "scissors": "scissors.jpg"}

    if request.method == "POST":
        player_choice = request.form.get("choice")
        computer_choice = random.choice(choices)
        if player_choice == computer_choice:
            result = "It's a draw"
        elif (player_choice == "rock" and computer_choice == "scissors") or \
                (player_choice == "paper" and computer_choice == "rock") or \
                (player_choice == "scissors" and computer_choice == "paper"):
            result = "You win!"
        else:
            result = "You lose"

        return render_template(
            "index.html",
            result=result,
            player_image=images[player_choice],
            computer_image=images[computer_choice]
        )

    return render_template("index.html", result="", player_image="", computer_image="")


if __name__ == "__main__":
    app.run(debug=True)
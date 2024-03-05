from flask import Flask, render_template

app = Flask(__name__)

TICKETS = [
  {
    "id": 1,
    "title": "From Non-Tech to Tech",
    "category": "Personal Development",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  },
  {
    "id": 2,
    "title": "Why I Learn to Code?",
    "category": "Programming",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  },
  {
    "id": 3,
    "title": "What Causes Monsoon?",
    "category": "Curiosity Chronicles",
  },
  {
    "id": 4,
    "title": "Lang Tengah Island",
    "category": "Projects",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit"
  } 
]

@app.route("/")
def hello_world():
    return render_template('home.html', tickets=TICKETS, name="Merang Jetty Boat Ticket Online")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
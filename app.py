from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

TICKETS = [
  {
    "id": 1,
    "title": "Redang Island ",
    "price": "MYR 110.00",
    "content": "Return Speedboat Transfer Merang - Redang Island - Merang"
  },
  {
    "id": 2,
    "title": "Lang Tengah Island",
    "price": "MYR 160.00",
    "content": "Return Speedboat Transfer Merang - Lang Tengah Island - Merang"
  },
  {
    "id": 3,
    "title": "热浪岛船票",
    "price": "马币 110.00",
    "content": "往返默浪码头 - 热浪岛船票"
  },
  {
    "id": 4,
    "title": "浪中岛船票",
    "price": "马币 160.00",
    "content": "往返默浪码头 - 浪中岛船票"
  } 
]

@app.route("/")
def hello_world():
    return render_template('home.html', tickets=TICKETS, name="Merang Jetty Boat Services")
  

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
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

@app.route("/ticket/<id>/book", methods=["post"])
def book_ticket(id):
    full_name = request.form.get("full_name")
    phone = request.form.get("phone")
    email = request.form.get("email")
    hotel = request.form.get("hotel")
    boat_in = request.form.get("boat_in")
    boat_out = request.form.get("boat_out")
    adult = request.form.get("adult")
    child = request.form.get("child")
    infant = request.form.get("infant")
    return jsonify(full_name=full_name, phone=phone, email=email, hotel=hotel, boat_in=boat_in, boat_out=boat_out, adult=adult, child=child, infant=infant)
  
  
    




if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
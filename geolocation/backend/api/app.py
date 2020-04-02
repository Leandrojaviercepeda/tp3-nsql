from flask import Flask, jsonify
from functionsDB import generate_points, add_point, user_radio

app = Flask(__name__)

@app.route('/generate-points')
def load_chapters():
    """Generar puntos de interes."""
    msj = generate_points()
    return msj

@app.route('/points/add/<point>/<longitude>/<latitude>/<name>')
def add_point_to_points(point,longitude,latitude,name):
    """Añadir punto de interes."""
    msj = add_point(point,longitude,latitude,name)
    return msj

@app.route('/user-radio/<point>/<longitude>/<latitude>')
def points_in_user_radius(point,longitude,latitude):
    """Listado de puntos de interes en un radio de 5km del usuario."""
    points = user_radio(point,longitude,latitude)
    return jsonify(points)
    
if __name__ == "__main__":
    app.run(host='localhost', port='5000', debug=True)


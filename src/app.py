from flask import Flask, jsonify, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from settings import Config

# Creating app and setting the configurations
app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Model creation
class Greeting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(255), nullable=False)

# Routes and endpoint handlers 
@app.route("/saludos", methods=['GET', 'POST'])
def greetings_list():
    if request.method == 'GET':
        greetings = Greeting.query.all()
        return jsonify([{'id': greeting.id, 'message': greeting.message} for greeting in greetings])
    elif request.method == 'POST':
        data = request.json
        print("DATA", data)
        greeting = Greeting(message=data['message'])
        db.session.add(greeting)
        db.session.commit()
        return jsonify({'id': greeting.id, 'message': greeting.message})
    
@app.route("/saludos/<int:id>", methods=['GET'])
def retrieve_greeting(id):
    greeting = Greeting.query.get(id)

    if not greeting:
        return jsonify({'error': 'Saludo no encontrado.'}), 404
    
    return jsonify({
        'id': greeting.id,
        'message': greeting.message
    })


if __name__ == "__main__":
    app.run(debug=Config.DEBUG, host=Config.HOST_NAME, port=Config.PORT)
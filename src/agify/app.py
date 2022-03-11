from flask import Flask, jsonify, request
import controllers
import db

app = Flask(__name__)


@app.route('/api/persons', methods=['GET'])
def api_get_persons():
    return jsonify(controllers.get_persons())


@app.route('/api/persons/<string:name>', methods=['GET'])
def api_get_person_by_name(name):
    return jsonify(controllers.get_person_by_name(name))


@app.route('/api/persons/add/<string:name>/<int:age>/<int:count>', methods=['PUT'])
def api_add_person(name, age, count):
    return jsonify(controllers.add_person(name, age, count))


@app.route('/api/persons/delete/<string:name>', methods=['DELETE'])
def api_delete_person(name):
    return jsonify(controllers.delete_person(name))


if __name__ == '__main__':
    db.create_agify_db_table()
    # db.initialize_agify_db()
    app.run(debug=True)

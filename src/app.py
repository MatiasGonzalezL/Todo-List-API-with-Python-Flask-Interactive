from flask import Flask, jsonify, request, json
app = Flask(__name__)


todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]


@app.route('/blabla', methods=['GET'])
def hello_world():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['GET'])
def todolist():
    json_text = jsonify(todos)
    return json_text


@app.route('/todos', methods=['POST'])
def add_new_todo():
    # the request body is already json decoded and it comes in the request.json variable
    request_body = json.loads(request.data)
    #decoded_object = json.loads(request.data)
    #json_text = jsonify(decoded_object)
    todos.append(request_body)
    return jsonify(todos)


@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete: ",position)
    del todos[position]
    return jsonify(todos)


# @app.route('/todos', methods=['POST'])
# def add_new_todo():
    # request_body = request.json
    # print("Incoming request with the following body", request_body)
    # return 'Response for the POST todo'



# These two lines should always be at the end of your app.py file.
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
from flask import Flask
from flask import request, make_response, jsonify
from flask_cors import CORS
# from core import logic

app = Flask(__name__, static_folder="./build/static", template_folder="./build")
CORS(app) #Cross Origin Resource Sharing

@app.route("/", methods=['GET'])
def index():
    return "text parser:)"

# TODO: /logic への遷移先作成
@app.route("/logic", methods=['GET','POST'])
def parse():
    #print(request.get_json())
    data = request.get_json()
    text = data['post_text']

    res = logic(text) # wakati だった
    response = {'result': res}
    #print(response)
    return make_response(jsonify(response))

if __name__ == "__main__":
    app.debug = True
    app.run(host='127.0.0.1', port=5000)

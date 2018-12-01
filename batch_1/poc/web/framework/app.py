from flask import Flask, json, request, render_template
import logging

FORMAT = '%(asctime)-15s %(filename)-5s %(funcName)-5s %(message)s'
logging.basicConfig(format=FORMAT, level="DEBUG")

logger = logging.getLogger("scope.test")

logger.setLevel("DEBUG")


app = Flask(__name__)

@app.route('/hi/<string:name>')
def m1(name=None):
    # db insert
    # DB GET
    result = json.jsonify({"hi":"This is response from GET API" + name})
    print("Printing result object :: ", result.data)
    logger.info("debug Printing result object...."+ str(result.data))
    return result, 200


@app.route('/hi', methods=['POST'])
def m2():
    # db insert
    # DB GET
    result = json.jsonify({"hi":"This is response from POST API :: " + request.args.get("name")})
    print("Printing result object :: ", result.data, request.args.get("name"))

    request.get_json()
    logger.debug("debug Printing result object...."+ str(result.data))
    return result, 200



@app.route('/')
def staticFileServing():
    return render_template('index.html')


app.run(port=8080)
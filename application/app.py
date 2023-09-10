import logging
from flask import Flask, json

app = Flask(__name__)

# Type hinting for app.logger
app.logger: logging.Logger

@app.route('/status')
def healthcheck():
    """
    Endpoint to check the health status.
    """
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status request successful')
    return response

@app.route('/metrics')
def metrics():
    """
    Endpoint to provide metrics data.
    """
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {"UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Metrics request successful')
    return response

@app.route('/')
def hello():
    """
    Default endpoint to greet the world.
    """
    app.logger.info('Main request successful')
    return "Hello World!"

if __name__ == "__main__":
    # Stream logs to a file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0')

# sample_web/app.py

from flask import Flask
app = Flask(__name__)

@app.route('/test1')
def test_app():
    return 'Testing Python DevOps Platform!'

@app.route('/test2')
def test_app():
    return 'Testing Angular DevOps Platform!'

@app.route('/test3')
def test_app():
    return 'Testing Scala DevOps Platform!'

@app.route('/test4')
def test_app():
    return 'Testing XML DevOps Platform!'

@app.route('/test5')
def test_app():
    return 'Testing JAVA DevOps Platform!'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
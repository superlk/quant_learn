import flask
import json
import time
from concurrent.futures import ThreadPoolExecutor

app = flask.Flask(__name__)
pool = ThreadPoolExecutor()


def read_file():
    time.sleep(0.1)
    return 'file result '


def read_db():
    time.sleep(0.2)
    return 'db result'


def read_api():
    time.sleep(0.3)
    return 'api result'


@app.route("/")
def index():
    #  单线程
    # result_file = read_file()
    # result_db = read_db()
    # result_api = read_api()
    # return json.dumps({
    #     "result_file": result_file,
    #     "result_db": result_db,
    #     "result_api": result_api
    # })
    result_file = pool.submit(read_file)
    result_db = pool.submit(read_db)
    result_api = pool.submit(read_api)
    return json.dumps({
        "result_file": result_file.result(),
        "result_db": result_db.result(),
        "result_api": result_api.result()
    })


if __name__ == '__main__':
    app.run()

"""
单线程访问时间
 time curl http://127.0.0.1:5000/
{"result_file": "file result ", "result_db": "db result", "result_api": "api result"}
real	0m0.621s
user	0m0.003s
sys	0m0.004s

多线程访问时间
time curl http://127.0.0.1:5000/
{"result_file": "file result ", "result_db": "db result", "result_api": "api result"}
real	0m0.313s
user	0m0.004s
sys	0m0.005s
"""

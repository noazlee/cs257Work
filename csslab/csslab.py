from re import S
import flask,psycopg2

app = flask.Flask(__name__)

@app.route('/')
def my_function():
    return render_template("homepage.html")

if __name__ == '__main__':
    my_port = 5128
    app.run(host='0.0.0.0', port = my_port)
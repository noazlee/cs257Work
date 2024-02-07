import flask,psycopg2

app = flask.Flask(__name__)

#
@app.route('/hello')
def my_function():
    return "Hello world!"

@app.route('/display/<word1>/<word2>')
def my_display(word1, word2):
    the_string = "The words are: " + word1 + " and " + word2;
    return the_string

@app.route('/color/<word1>')
def my_color(word1):
    return '<h1 style="color:Red">' + word1 + '</h1>'

@app.route('/add/<num1>/<num2>')
def addition(num1,num2):
    num1 = float(num1)
    num2 = float(num2)
    sum = num1 + num2
    return '<h1 style="font:sans-serif"> The sum is: ' + str(sum) +'</h1>'

@app.route('/area/<abbrev>')
def getArea(abbrev):
    conn = None
    try:
        conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")
        
        cur = conn.cursor()
        sql = '''
        SELECT state_name FROM states WHERE state_id = %s
        '''
        cur.execute(sql, (abbrev, ) )
        row = cur.fetchone()

        if(row):
            ans = '<h1 style="font:sans-serif"> The state area is: ' + row[0] +'</h1>'
        else:
            ans = '<h1 style="font:sans-serif"> Invalid state abbreviation</h1>'

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

    return ans

    

if __name__ == '__main__':
    my_port = 5128
    app.run(host='0.0.0.0', port = my_port)


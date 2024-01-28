import psycopg2

def get_city():
    """ query data from the vendors table """
    conn = None
    try:
        
        conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")
        
        cur = conn.cursor()
        cur.execute("SELECT city_name FROM cities WHERE city_name==Northfield")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

get_city() #northfield is not in the database

def get_city_with_highest_pop():
    """ query data from the vendors table """
    conn = None
    try:
        
        conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")
        
        cur = conn.cursor()
        cur.execute("SELECT city_name FROM cities ORDER BY city_pop DESC LIMIT 1")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

get_city_with_highest_pop() # It is new york

def get_city_in_MN():
    """ query data from the vendors table """
    conn = None
    try:
        
        conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")
        
        cur = conn.cursor()
        cur.execute("""SELECT city_name
        FROM cities
        WHERE state_name=='Minnesota'
        ORDER BY city_pop LIMIT 1""")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        while row is not None:
            print(row)
            row = cur.fetchone()

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

get_city_in_MN()

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
        cur.execute("SELECT city_name FROM cities WHERE city_name LIKE Northfield")
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
        WHERE state_name LIKE 'Minnesota'
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

get_city_in_MN() #shakopee

def get_city_in_N():
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
        cur.execute("""SELECT city_name, state_name
        FROM cities
        ORDER BY city_lat DESC LIMIT 1""")
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

def get_city_in_S():
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
        cur.execute("""SELECT city_name, state_name
        FROM cities
        ORDER BY city_lat LIMIT 1""")
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

def get_city_in_E():
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
        cur.execute("""SELECT city_name, state_name
        FROM cities
        ORDER BY city_lon LIMIT 1""")
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

def get_city_in_W():
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
        cur.execute("""SELECT city_name, state_name
        FROM cities
        ORDER BY city_lon DESC LIMIT 1""")
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



get_city_in_N() #anchorage
get_city_in_S() #honolulu
get_city_in_E() #honolulu
get_city_in_W() #portland, maine

state = input("Enter a US state ")

def get_city_in_USER(state):
    totalpop=0
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

        if(len(state)!=2):
            cur.execute("SELECT city_pop FROM cities WHERE state_name LIKE %s", (state,))
            rows = cur.fetchall()
        else:
            cur.execute("SELECT state_name FROM states WHERE state_id LIKE %s", (state,))
            print("The number of parts: ", cur.rowcount)
            row2 = cur.fetchone()
            state = row2
            
            cur.execute("SELECT city_pop FROM cities WHERE state_name LIKE %s", (state,))
            rows = cur.fetchall()
            

        for row in rows:
                totalpop += row[0]

        print(row)

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

get_city_in_USER(state)

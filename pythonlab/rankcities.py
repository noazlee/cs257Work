import psycopg2


def percPop(cityName, stateName):
    """"GET THE POPULATION OF THE POP WHO LIVES IN THE CITY FROM THE STATE"""
    
    conn = None
    try:

        conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")
        
        cur = conn.cursor()
        cur.execute("""
        CREATE VIEW proportionPop AS
        SELECT (city_pop/pop) AS total FROM cities JOIN statePOP on state_id
        WHERE city_name LIKE""", cityName, """ AND state_name LIKE""", stateName
        )
        #print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        if(row is not None):
            while row is not None:
                print(row)
                row = cur.fetchone()
        else:
            print("No instance found")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


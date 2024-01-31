import psycopg2

def percPop(cityName, stateName):

    #GET THE POPULATION OF THE POP WHO LIVES IN THE CITY FROM THE STATE
    
    conn = None
    try:

        conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")
        
        cur = conn.cursor()

        sql="""
        SELECT (city_pop/pop) AS total FROM cities JOIN statePOP on cities.state_name = statePOP.state_name
        WHERE city_name = %s  AND state_name = %s"""
        
        cur.execute(sql,[city_name, state_name]
        )
        #print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()

        if(row is not None):
            while row is not None:
                print(row)
                row = cur.fetchone()
        else:
            print("No ipernstance found")

        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()

percPop("Cleveland", "Ohio")


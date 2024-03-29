#!/usr/bin/python

import psycopg2
#from config import config

def create_tables():
    """ create tables in the PostgreSQL database"""
    command1 = """CREATE TABLE states ( 
            state_name text NOT NULL,
            state_id text
            ) """
        
    command2 = """CREATE TABLE cities (
                city_name text NOT NULL,
                state_name text NOT NULL,
                city_pop int NOT NULL,
                city_lat real NOT NULL,
                city_lon real NOT NULL
                )"""

    conn = None
    try:
        conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")

        cur = conn.cursor()
        
        # create table one by one
        cur.execute(command1)
        cur.execute(command2)
        # close communication with the PostgreSQL database server
        cur.close()
        # commit the changes
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


if __name__ == '__main__':
    create_tables()
#Tests Connection to Server
def test_connection():

    conn = psycopg2.connect(
        host="localhost",
        port=5432,
        database="leen2",
        user="leen2",
        password="chip574pencil")

    if conn is not None:
        print( "Connection Worked!" )
    else:
        print( "Problem with Connection" )

    return None

#Create a table

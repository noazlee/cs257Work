#!/usr/bin/python

import psycopg2
from config import config

def create_tables():
    """ create tables in the PostgreSQL database"""
    commands = (
        
        CREATE TABLE states (
            state_name VARCHAR(255) NOT NULL,
            state_id SERIAL PRIMARY KEY
        )
        ,
        CREATE TABLE cities (
                city_name VARCHAR(255) NOT NULL,
                state_name VARCHAR(255) NOT NULL,
                city_pop int(255) NOT NULL,
                city_lat real(255) NOT NULL,
                city_lon real(255) NOT NULL
                )
        ,
      )
    conn = None
    try:
        # read the connection parameters
        params = config()
        # connect to the PostgreSQL server
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        # create table one by one
        for command in commands:
            cur.execute(command)
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

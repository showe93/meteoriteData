from table_sort import table_sort, tables
import requests
import sqlite3

""" 
This module establishes a connection, retrieves the information and commits the changes to the table
 """

def db_operation():
    """this function establishes a connection, collects the data,builds the tables and commits any changes"""
    response = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
    json_data = response.json()
    db_connection = None

    try:
        db_name = 'meteorite.db'
        db_connection = sqlite3.connect(db_name)
        db_cursor = db_connection.cursor()
        tables(db_cursor)
        table_sort(json_data, db_cursor)
        db_connection.commit()
        db_cursor.close()
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')
    finally:
        if db_connection:
            db_connection.close()
            print('Database connection closed.')

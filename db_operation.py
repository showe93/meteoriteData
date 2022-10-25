from utility_functions import convert_string_to_numerical
import requests
import sqlite3

""" 
This module establishes a connection, retrieves the information and sorts all the meteorite data
db_operation() is the only function available to outside file
the information is sorted by geolocation and is placed into the appropriate table based on the dictionary found below
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
        _tables(db_cursor)
        _table_sort(json_data, db_cursor)
        db_connection.commit()
        db_cursor.close()
    except sqlite3.Error as db_error:
        print(f'A Database Error has occurred: {db_error}')
    finally:
        if db_connection:
            db_connection.close()
            print('Database connection closed.')
def _tables(db_cursor):
    """Creates the 7 tables for the 7 different locations"""
    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Africa_MiddleEast_Meteorites(
                                       name TEXT,
                                       mass TEXT,
                                       reclat TEXT,
                                       reclong TEXT);''')

    db_cursor.execute('DELETE FROM Africa_MiddleEast_Meteorites')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Europe_Meteorites(
                                               name TEXT,
                                               mass TEXT,
                                               reclat TEXT,
                                               reclong TEXT);''')

    db_cursor.execute('DELETE FROM Europe_Meteorites')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Upper_Asia_Meteorites(
                                               name TEXT,
                                               mass TEXT,
                                               reclat TEXT,
                                               reclong TEXT);''')

    db_cursor.execute('DELETE FROM Upper_Asia_Meteorites')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Lower_Asia_Meteorites(
                                               name TEXT,
                                               mass TEXT,
                                               reclat TEXT,
                                               reclong TEXT);''')

    db_cursor.execute('DELETE FROM Lower_Asia_Meteorites')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS Australia_Meteorites(
                                               name TEXT,
                                               mass TEXT,
                                               reclat TEXT,
                                               reclong TEXT);''')

    db_cursor.execute('DELETE FROM Australia_Meteorites')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS North_America_Meteorites(
                                               name TEXT,
                                               mass TEXT,
                                               reclat TEXT,
                                               reclong TEXT);''')

    db_cursor.execute('DELETE FROM North_America_Meteorites')

    db_cursor.execute('''CREATE TABLE IF NOT EXISTS South_America_Meteorites(
                                               name TEXT,
                                               mass TEXT,
                                               reclat TEXT,
                                               reclong TEXT);''')

    db_cursor.execute('DELETE FROM South_America_Meteorites')
def _table_sort(data, db_cursor):
    """takes the json data, loops through it, and sorts it into the appropriate
    table based on the geolocation(reclat and reclong)"""
    # geolocation bounding box -- (left,bottom,right,top)
    bound_box_dict = {
        'Africa_MiddleEast_Meteorites': (-17.8, -35.2, 62.2, 37.6),
        'Europe_Meteorites': (-24.1, 36, 32, 71.1),
        'Upper_Asia_Meteorites': (32.2, 35.8, 190.4, 72.7),
        'Lower_Asia_Meteorites': (58.2, -9.9, 154, 38.6),
        'Australia_Meteorites': (112.9, -43.8, 154.3, -11.1),
        'North_America_Meteorites': (-168.2, 12.8, -52, 71.5),
        'South_America_Meteorites': (-81.2, -55.8, -34.4, 12.6)
    }
    for record in data:
        reclat = convert_string_to_numerical(record.get('reclat', None))
        reclong = convert_string_to_numerical(record.get('reclong', None))
        if reclat and reclong:
            for location, recvalue in bound_box_dict.items():
                if (recvalue[0] < reclong < recvalue[2]) and (recvalue[1] < reclat < recvalue[3]):
                        executestring = f'INSERT INTO {location} VALUES(?,?,?,?)'
                        db_cursor.execute(executestring,
                                              (record.get('name', None),
                                               record.get('mass', None),
                                               record.get('reclat', None),
                                               record.get('reclong', None)))

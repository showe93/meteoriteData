
"""
This module creates the 7 different tables
"""

def tables(db_cursor):
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

from utility_functions import convert_string_to_numerical

"""
this module sorts all of the incoming json data into the appropriate table based off of
geolocation(reclat and reclong)
"""
def table_sort(data, db_cursor):
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
                if (recvalue[0] <= reclong <= recvalue[2]) and (recvalue[1] <= reclat <= recvalue[3]):
                        executestring = f'INSERT INTO {location} VALUES(?,?,?,?)'
                        db_cursor.execute(executestring,
                                              (record.get('name', None),
                                               record.get('mass', None),
                                               record.get('reclat', None),
                                               record.get('reclong', None)))

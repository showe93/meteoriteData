import requests
"""
This module assists with converting a string to an int or float and checks if theirs an issue completing a GET request.
This is a set of Utility Functions
"""
def _string_is_int(in_string):
    """ returns True if the incoming parameter is an int, returns False otherwise """
    try:
        int(in_string)
        return True
    except TypeError:
        return False
    except ValueError:
        return False

def _string_is_float(in_string):
    """ returns True if the incoming parameter is a float, returns False otherwise """
    try:
        float(in_string)
        return True
    except TypeError:
        return False
    except ValueError:
        return False

def convert_string_to_numerical(in_string):
    """ this function converts a string to a numerical value (to either an int or float)
        'None' is returned if the incoming string is not in the form of an int or float """
    if _string_is_float(in_string):
        return float(in_string)
    elif _string_is_int(in_string):
        return int(in_string)
    return None

def issue_get_request(target_url: str):
    """ This function issues a GET request to the URL passed as its single parameter.
    A response object is returned
    The status code of the request object is also reported"""
    response: requests.Response = requests.get(target_url)
    if response.status_code != 200:
        print(f'The GET request was not successful\n STATUS CODE: {response.status_code}\n please try a new URL')
        exit(1)
    else:
        print(f'the GET request was successful\n STATUS CODE: {response.status_code}')
        return response

def convert_content_to_json(response: requests.Response):
    json_data = None
    try:
        json_data = response.json()
        print(f'Response object content converted to JSON object\n')
    except requests.exceptions.JSONDecodeError as json_decode_error:
        print(f'An error occured while trying to convert the response content to a JSON object:\n'
                f'{json_decode_error}')
    finally:
        return json_data

import utils

START_DATE = '2015-09-07'
STOP_DATE = '2015-09-08'
API_KEY = 'DEMO_KEY'
COUNT_RESULT = 3


def get_url(start=START_DATE, stop=STOP_DATE, key=API_KEY):
    utils.check_date(start, stop)
    return f'https://api.nasa.gov/neo/rest/v1/feed?start_date={start}&end_date={stop}&api_key={key}'



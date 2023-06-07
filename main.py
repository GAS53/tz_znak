import requests

from models import SubjectComposit
from config import get_url


def pars_url(start, stop):
    '''парс api'''
    url = get_url(start, stop)
    response = requests.get(url)
    return response.json()

def run(start, stop, limit):
    '''основная рабочая функция'''
    data = pars_url(start, stop)
    SC = SubjectComposit()
    for date, day_li in data['near_earth_objects'].items():
        for day in day_li:
            SC.add_subject(date, day['neo_reference_id'], day['name'], day['absolute_magnitude_h'], day['is_potentially_hazardous_asteroid'])
    SC.fabric_subjects(is_sort=True, is_preparate=True)
    res = SC.get_strip_subjects(set_count=limit)
    return res


if __name__ == '__main__':
    res = run('2015-09-07', '2015-09-08', 2)
    print(res)



    
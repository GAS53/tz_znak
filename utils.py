import datetime

def check_date(start, stop):
    try:
        a = datetime.date.fromisoformat(start)
    except:
        raise ValueError('неверно задана начальная дата')
    try:
        b = datetime.date.fromisoformat(stop)
    except:
        raise ValueError('неверно задана конечная дата')
    if a < b:
        return True
    raise ValueError('начальная дата должна быть раньше конечной')
    

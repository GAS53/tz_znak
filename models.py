

import config

class Subject():
    '''объект - астероид и т.п.'''
    def __init__(self, neo_reference_id, name, absolute_magnitude_h, is_potentially_hazardous_asteroid):
        self.id = neo_reference_id
        self.name = name
        self.absolute_magnitude_h = absolute_magnitude_h
        self.is_potentially_hazardous_asteroid = is_potentially_hazardous_asteroid

    def get_subject_dict(self):
        '''результирующий словарь объекта'''
        di = {}
        di['name'] = self.name
        di['absolute_magnitude_h'] = self.absolute_magnitude_h
        di['is_potentially_hazardous_asteroid'] = self.is_potentially_hazardous_asteroid
        return di
    

class SubjectComposit():
    def __init__(self):
        self.subjects = {}

    def add_subject(self, date, neo_reference_id, name, absolute_magnitude_h, is_potentially_hazardous_asteroid):
        '''добавляем обьект в хранилище объектов'''
        if self.subjects.get(date):
            self.subjects[date].append(Subject(neo_reference_id, name, absolute_magnitude_h, is_potentially_hazardous_asteroid))
        else:
            day_subjects = []
            day_subjects.append(Subject(neo_reference_id, name, absolute_magnitude_h, is_potentially_hazardous_asteroid))
            self.subjects[date] = day_subjects
    
    def fabric_subjects(self, is_sort=False, is_preparate=False):
        '''сортируем и формируем итоговый словарь'''
        for day, day_li in self.subjects.items():
            if is_sort:
                day_li = sorted(day_li, key=lambda x: x.absolute_magnitude_h, reverse=True)
            if is_preparate:
                day_li = {f'{day} {i.id}': i.get_subject_dict() for i in day_li}
            self.subjects[day] = day_li


    # def get_strip_subjects(self, set_count=config.COUNT_RESULT):
    #     '''решение более лаконичное но по условию тз не допустимо
    #        т.к. импорт только requests и datetime'''
    #     import itertools
    #     return {day: dict(itertools.islice(day_di.items(), set_count)) for day, day_di in self.subjects.items()}

    def get_strip_subjects(self, set_count=config.COUNT_RESULT):
        '''обрезаем резльтаты'''
        res = {}
        for day, day_di in self.subjects.items():
            inner_di = {}
            count = 0
            for key, value in day_di.items():
                inner_di[key] = value
                count += 1
                if count == set_count:
                    break
            res[day] = inner_di

        return res

        
        
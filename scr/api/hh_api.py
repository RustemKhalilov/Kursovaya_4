import requests
from abc import ABC, abstractmethod


class Apihh(ABC):

    @abstractmethod
    def get_vacancies(self):
        pass


class HhunterApi(Apihh):
    def __init__(self):
        self.base_url = "https://api.hh.ru/vacancies"

    def get_vacancies(self, search_job, vacans_cont):
        # params = {"text": search_job, "area": 72}  # Здесь 72 - это код региона Тюмень
        # # Справочник для параметров GET-запроса
        params = {
            'text': search_job,  # Текст фильтра. В имени должно быть слово "Аналитик"
            'area': 95,  # Поиск осуществляется по вакансиям города Тюмень
            'page': 0,  # Индекс страницы поиска на HH
            'per_page': vacans_cont  # Кол-во вакансий на 1 странице
        }
        response = requests.get(self.base_url, params=params)
        return response.json()

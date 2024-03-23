import json
from scr.api.vacanciya import vacanciya
from abc import ABC, abstractmethod


class base_filter(ABC):
    def __str__(self):
        pass

    def __len__(self):
        pass

    def filter_vacanciya_top_salary(self):
        pass

    def safe_json_file(self):
        pass




class FilterVacanciya(base_filter):

    def __init__(self, salary_down, salary_up, vacanciya_display, work_word, data_vacanciya: list):
        self.data_vacanciya = data_vacanciya
        self.salary_up = salary_up
        self.data_down = salary_down
        self.vacanciya_display = int(vacanciya_display)
        self.work_word = work_word

    def filter_vacanciya_top_salary(self):
        def sortvacanciya(item):
            return abs(item.salary_up - int(self.salary_up))

        my_list = self.data_vacanciya
        # Производим сортировку по ближайщей запрошенной зарплате
        # Считаю это корректным, потому что специалист знает как правило сколько предлагают на рынке
        my_list.sort(
            key=sortvacanciya)  # данный участок также можно реализовать посредсво key=lamda abs(x.salary_up -int(self.salary_up))
        my_vacanciya_resume_list = []
        if self.work_word != '':  # Применен фильт по словам
            for item in my_list:
                try:
                    if self.work_word in item.snippet.get('requirement') or self.work_word in item.snippet.get(
                            'responsibility'):
                        my_vacanciya_resume_list.append(item)
                except TypeError:
                    id_error = 1
                # Получаем срез наших вакансий
                self.data_vacanciya = my_vacanciya_resume_list[0:self.vacanciya_display]
                return self.data_vacanciya
        else:  # Нет фильтра по словам
            # Получаем срез наших вакансий
            self.data_vacanciya = my_list[0:self.vacanciya_display]
            return self.data_vacanciya

    def safe_json_file(self):

        with open('vacanciya_info.json', 'w') as write_file:
            my_json = []
            for item in self.data_vacanciya:
                my_json.append(
                    {
                        'наименование вакансии': item.name,
                        'зарплата максимальная': item.salary_up,
                        'минимальная зарплата': item.salary_down,
                        'адрес': item.adress,
                        'электронный адрес': item.alternate_url,
                        'обязанности': item.snippet,
                        'профессиональные навыки': item.professional_roles
                    }
                )
            json.dump(my_json, write_file)

    def __len__(self):
        return len(self.data_vacanciya)

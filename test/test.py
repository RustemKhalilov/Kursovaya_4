import pytest
from scr.api.hh_api import HhunterApi
from scr.api.vacanciya import Vacanciya
from scr.my_func.func import FilterVacanciya


def test_vacanciya():
    job_name = "Проектировщик"
    vacans_cont = 100
    vacans_display = 20
    word_filters = ""
    salary_limit_down = 50000
    salary_limit_up = 150000
    user_dict = {'название работы': job_name,
            'количество запрашиваемых вакансий': vacans_cont,
            'количество отображаемых вакансий': vacans_display,
            'фильтр по работам': word_filters,
            'минимальная зарплата': salary_limit_down,
            'максимальная зарплата': salary_limit_up,
            }
    hh_obj = HhunterApi()  # Создали объект для запроса
    hh_obj_dict = hh_obj.get_vacancies(user_dict['название работы'], user_dict[
        'количество запрашиваемых вакансий'])  # получили ответ от hh.ru в виде json
    data_list = []
    for item in hh_obj_dict['items']:
        my_vacansiya = Vacanciya(item)
        data_list.append(my_vacansiya)
    # создаем класс для фильтра вакансий
    assert len(data_list) == 100
    my_filter = FilterVacanciya(user_dict['минимальная зарплата'], user_dict['максимальная зарплата'],
                                user_dict['количество отображаемых вакансий'], user_dict['фильтр по работам'],
                                data_list)
    my_filter.filter_vacanciya_top_salary()
    assert len(my_filter) == 20
    # Распечатали файл


from scr.api.hh_api import HhunterApi
from scr.api.vacanciya import Vacanciya
from scr.my_func.func import FilterVacanciya


def user_input_data():
    job_name = input("Введите название профессии: ")
    vacans_cont = input("Введите количество запрашиваемых вакансий: ")
    vacans_display = input("Введите количество отображаемых выбранных вакансий: ")
    word_filters = input("Введите слова для фильтра вакансий: (исключить фильтр нажмите Enter) ")
    salary_limit_down = input("Введите нижний лимит зарплат: ")
    salary_limit_up = input("Введите верхний лимит зарплат: ")
    return {'название работы': job_name,
            'количество запрашиваемых вакансий': vacans_cont,
            'количество отображаемых вакансий': vacans_display,
            'фильтр по работам': word_filters,
            'минимальная зарплата': salary_limit_down,
            'максимальная зарплата': salary_limit_up,
            }


if __name__ == "__main__":
    user_dict = user_input_data()
    hh_obj = HhunterApi()  # Создали объект для запроса
    # region_number = hh_obj.get_region()
    hh_obj_dict = hh_obj.get_vacancies(user_dict['название работы'], user_dict[
        'количество запрашиваемых вакансий'])  # получили ответ от hh.ru в виде json
    data_list = []
    for item in hh_obj_dict['items']:
        my_vacansiya = Vacanciya(item)
        data_list.append(my_vacansiya)
    # создаем класс для фильтра вакансий
    my_filter = FilterVacanciya(user_dict['минимальная зарплата'], user_dict['максимальная зарплата'],
                                user_dict['количество отображаемых вакансий'], user_dict['фильтр по работам'],
                                data_list)
    my_filter.filter_vacanciya_top_salary()
    #Распечатали файл
    for index, item in enumerate(my_filter.data_vacanciya):
        print(f'{index + 1}. {item}')
    #Сохранили файл
    my_filter.safe_json_file()

from abc import ABC, abstractmethod


class Base(ABC):

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_salary(self):
        pass

    @abstractmethod
    def get_adress(self):
        pass

    @abstractmethod
    def get_url(self):
        pass

    @abstractmethod
    def snippet(self):
        pass

    @abstractmethod
    def get_professional_roles(self):
        pass


class Vacanciya(Base):
    def __init__(self, vacanc_dict: dict):
        self.name = vacanc_dict.get('name')
        temp_dict = vacanc_dict.get('salary')
        try:
            self.salary_up = temp_dict.get('to')
        except AttributeError:
            self.salary_up = 0
        if self.salary_up == None:
            self.salary_up = 0
        try:
            self.salary_down = temp_dict.get('from')
        except AttributeError:
            self.salary_down = 0
        if self.salary_down == None:
            self.salary_down = 0
        self.adress = vacanc_dict.get('address')
        self.alternate_url = vacanc_dict.get('alternate_url')
        self.snippet = vacanc_dict.get('snippet')
        self.professional_roles = vacanc_dict.get('professional_roles')

    def __str__(self):
        return f'{self.name}. Зарплата :{self.salary_up} руб.'

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary_up

    def get_adress(self):
        return self.adress

    def get_url(self):
        return self.alternate_url

    def snippet(self):
        return self.snippet

    def get_professional_roles(self):
        return self.professional_roles

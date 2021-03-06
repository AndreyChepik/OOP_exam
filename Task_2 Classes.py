"""Класи в пайтон - це об'єкти. Загалом як і все інше)
Успадкування працює по принципу щось є нащадком чогось, тобто можуть бути такі наслідування класів
Тварина-> кіт, будівля-> дім, навчальна_дисципліна->OOP.
Знизу будуть приклади класів."""
class Subject(object):
    """Клас навчальної дисципліни. Всі класси наслідуються від object, тут це явно вказано лише
    щоб про це написати в коментарі. """
    def __init__(self, hours=100, is_exam=False):
        """Ключовою зручністю OOP є те, що дочірній класс наслідує всі атрибути і методи
        батьківського класу. Саме звідси виникло поняття magic methods - це методи классу
        object, а отже і всіх класів як ми зʼясували. """
        self.hours = hours
        self.is_exam = is_exam

    def hours_to_minute(self):
        """Поверне кількість хвилин що є в навчальній дисципліні."""
        return self.hours * 45


class OOP(Subject):
    """Наслідник класу ʼпредметʼ"""
    def __init__(self, practise):
        super().__init__(hours=80, is_exam=True)
        """Про функцію super можно розповісти дуже багато. Головне: вона викликає метод next() класу.
        Виконається функція наступного классу за списком MRO, в нашому випадку це Subject. """
        self.practise = practise
    """В мене на гітхаб є проект grant servise де є ціла купа ООП, наслідування, поліморфізму.
    Можете подивитсь, якщо необхідно)"""


s = Subject(120, False)
o = OOP(True)
print(s)
print(o)
print(o.practise)
print(o.hours_to_minute())
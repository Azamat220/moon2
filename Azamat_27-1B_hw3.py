# 1  класс Computer
class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

#2.  сеттеры и геттеры к существующим атрибутам

    def get_cpu(self):
        return self.__cpu


    def set_cpu(self, cpu):
        self.__cpu = cpu


    def get_memory(self):
        return self.__memory


    def set_memory(self, memory):
        self.__memory = memory

# 3 Добавить в класс Computer метод make_computations
    def make_computations(self):
        print(f"Выполнение вычислений CPU: {self.__cpu} и Memory: {self.__memory}")

    def __str__(self):
        return f"Компьютер с CPU: {self.__cpu} и Memory: {self.__memory}"

    def __eq__(self, other):
        return self.__memory == other.__memory

    def __lt__(self, other):
        return self.__memory < other.__memory

    def __le__(self, other):
        return self.__memory <= other.__memory

    def __gt__(self, other):
        return self.__memory > other.__memory

    def __ge__(self, other):
        return self.__memory >= other.__memory

    def __ne__(self, other):
        return self.__memory != other.__memory

# 4 Создать класс Phone (телефон) с приватным полем sim_cards_list (список симкард)
class Phone:
    def __init__(self, sim_card_list):
        self.__sim_card_list = sim_card_list

# 5.  сеттеры и геттеры к существующему атрибуту.
    def get_sim_cards_list(self):
        return self.__sim_card_list

    def set_sim_cards_list(self, sim_card_list):
        self.__sim_card_list = sim_card_list

# 6. Добавить в класс Phone метод call с входящим параметром
    def call(self, sim_card_number, call_to_number):
        print(f"Звонок с sim-карты-{sim_card_number}: {call_to_number}")

    def __str__(self):
        return f"Sim Cards List: {self.__sim_card_list}"


#  7 8 Создать класс SmartPhone и наследовать его от 2-х классов Computer и Phone. Добавить use_gps

class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)
    def use_gps(self, location):
        print(f"Маршут построен к: {location}")

# 9. В каждом классе переопределить магический метод str
    def __str__(self):
        return f"SmartPhone с CPU: {self.get_cpu()}, "f"Memory: {self.get_memory()}, " \
               f"и Sim Cards: {self.get_sim_cards_list()}"



# 10,11,12. Перезаписать все магические методы сравнения в классе Computer

computer = Computer("Intel Core i9", 256)
print(computer)

phone = Phone(["Beeline", "MegaCom", "O!"])
print(phone)

smartphone1 = SmartPhone("A12", 16, ["Beeline", "MegaCom", "O!"])
print(smartphone1)

smartphone2 = SmartPhone("A13", 21, ["MegaCom", "O!"])
print(smartphone2)
phone.call(1, "+996 555 377 237")
smartphone1.use_gps("Бишкеку")
print(f'У computer CPU лучше, чем у smarphone1: {computer > smartphone1}')










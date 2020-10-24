# вариант запроса Д
# вариант предметной области 7 : Микропроцессор - Компьютер
from operator import itemgetter


class Microprocessor:
    # Класс "Микропроцессор"
    def __init__(self, id, model, price, computer_id):
        self.id = id
        self.model = model
        self.price = price
        self.computer_id = computer_id


class Computer:
    # класс "Компьютер"
    def __init__(self, id, name):
        self.id = id
        self.name = name


class ProcComp:
    # Микропроцессоры компьютера для реализации связи
    # многие-ко-многим
    def __init__(self,  proc_id, comp_id):
        self.proc_id = proc_id
        self.comp_id = comp_id

# компьютеры
Computers = [
    Computer(1, "Laptop 15-bw"),
    Computer(2, "Laptop 53-ch"),
    Computer(3, "Laptop 72-vx"),

    Computer(4, "PC-113531"),
    Computer(5, "PC-223679"),
    Computer(6, "PC-45329")
]

# микропроцессоры
Microprocessors = [
    Microprocessor(1, "amd RX ryzen", 12500, 1),
    Microprocessor(2, "amd SX ryzen", 22500, 1),
    Microprocessor(3, "amd PX ryzen", 45500, 2),
    Microprocessor(4, "core i3", 52500, 2),
    Microprocessor(5, "core i5", 15500, 2),
    Microprocessor(6, "core i7", 145000, 3),
    Microprocessor(7, "core i9", 15400, 3)
]

ProcComps = [
    ProcComp(1, 1),
    ProcComp(2, 2),
    ProcComp(2, 3),
    ProcComp(3, 4),
    ProcComp(3, 5),
    ProcComp(3, 6),
    ProcComp(3, 7),

    ProcComp(4, 1),
    ProcComp(5, 2),
    ProcComp(5, 3),
    ProcComp(6, 4),
    ProcComp(6, 5),
    ProcComp(6, 6),
    ProcComp(6, 7),
]

def main():
    # соединение данных один-ко-многим
    one_to_many = [(c.model, c.price, o.name)
                   for o in Computers
                   for c in Microprocessors
                   if c.computer_id == o.id]

    # соединение данных многие-ко-многим
    many_to_many_temp = [(o.name, co.comp_id, co.proc_id)
                         for o in Computers
                         for co in ProcComps
                         if o.id == co.comp_id]

    many_to_many = [(c.model, c.price, comp_name)
                    for comp_name, comp_id, proc_id in many_to_many_temp
                    for c in Microprocessors if c.id == proc_id]

    print('Задание Д1')
    res1 = []
    for i in one_to_many:
        if i[0][-2:] == "en":
            res1.append(i[0:3:2])
    print(res1)

    print('\nЗадание Д2')
    res2_unsorted = []
    for o in Computers:
        o_proc = list(filter(lambda i: i[2] == o.name, one_to_many))
        if len(o_proc) > 0:
            o_price = [price for _, price, _ in o_proc]
            o_price_sum = sum(o_price)
            o_price_count = len(o_price)
            o_price_average = o_price_sum / o_price_count
            res2_unsorted.append((o.name, int(o_price_average)))
    res2 = sorted(res2_unsorted, key=itemgetter(1), reverse=True)
    print(res2)

    print('\nЗадание Д3')
    res3 = {}
    for o in Computers:
        if o.name[0] == "L":
            o_price = list(filter(lambda i: i[2] == o.name, many_to_many))
            o_price_titles = [x for x, _, _ in o_price]
            res3[o.name] = o_price_titles
    print(res3)


if __name__ == '__main__':
    main()
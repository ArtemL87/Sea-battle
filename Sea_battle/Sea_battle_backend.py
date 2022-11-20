import random

# класс работы с игровым полем
class Board:
    def __init__(self, name):
        self.name = name
        # Первоноальное состояние игрового поля
        self.board = [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0]
        ]
        # корабли игрового поля игрока
        self.list_ship = [

        ]
        # совершеные ходы
        self.list_step = []
        # клетки, в которые нельзя ставить корабли
        self.list_overboard = []
        self.hid = True # разрешение вывода короблей
        self.ship_live = 7 # количество короблей
    # вывод игрового поля в консоль
    def get_board(self):
        n = 1
        print(f'Игровое поле: {self.name}')
        print(end=':) |')
        ([print(f'<{i}>|', end='') for i in range(1, 7)])
        print()
        for i in range(6):
            print(f'<{n}>', end='')
            for j in range(6):
                print(f'| {self.board[i][j]} ', end='')
            print('|', end='\n')
            n += 1
    # выставление короблей на игровое поле
    def set_board(self):
        if self.hid == True:
            for i in self.list_ship:
                for j in i:
                    self.board[j[0]][j[1]] ='#'
    # создание нового списка короблей (работа с классом Ship)
    def set_list_ship(self):
        deck = 3 # палубa
        n = 4 # чтоб корабли не уплывали в соседнее море)))
        number_of_ships = 7
        attempt = 0
        while number_of_ships:
            # проверка на свободные клетки игрового поля
            if attempt > 1000:
                # возврат к исходным настройкам при заполнении игрового поля
                deck = 3
                n = 4
                number_of_ships = 7
                self.list_ship = []
                self.list_overboard = []
                attempt = 0
            else:
                # обращение к классу Ship для постановки корабля на игровое поле
                new_ship = Ship(deck, [random.randrange(n), random.randrange(n)], random.randrange(2))
                new_ship.dots()
                # проверка запрещеных клеток
                if True not in ([_ in self.list_overboard for _ in new_ship.get_ship]):
                    self.list_ship.append(new_ship.get_ship)
                    self.list_overboard.extend(new_ship.get_overboard)
                    if number_of_ships == 7:
                        deck -= 1
                        n += 1
                    if number_of_ships == 5:
                        deck -= 1
                        n += 1
                    number_of_ships -= 1
            attempt += 1
    # возврат списка кораблей
    def get_list_ship(self):
        return print(self.list_ship)
    # возвращает список выстрелов
    def get_list_step(self):
        return self.list_step
    # выстрел
    def set_list_step(self):
        n = 0
        while n == 0:
            try:
                if self.hid == False:
                    print('Введите пересечение чисел игрового поля.')
                    value = [int(input('Число слево: ')) - 1, int(input('Число сверху: ')) - 1]
                else:
                    value = [random.randrange(6), random.randrange(6)]
            except ValueError:
                print('Некоректный ввод!')
            else:
                if all([value not in self.list_step,
                        0 <= value[0] <= 5,
                        0 <= value[1] <= 5]):
                    self.list_step.append(value)
                    n += 1
                else:
                    if self.hid == False:
                        if all([0 <= value[0] <= 5,
                                0 <= value[1] <= 5]):
                            print('Такой ход Вы уже делали. Попробуйте снова.')
                        else:
                            print('Не заплываем за буйки!')

        if True in (value in _ for _ in self.list_ship):
            print('\t\t\t\t  ПОПАЛ!')
            self.board[value[0]][value[1]] = 'X'
            for _ in self.list_ship:
                try:
                    _.remove(value)
                except ValueError:
                    pass
            if [] in self.list_ship:
                self.list_ship.remove([])
                self.ship_live -= 1
                print('\t\tКрысам покинуть корабль! Корабль идет ко дну!')
        else:
            print('\t\t\t\t  ПРОМАХ')
            self.board[value[0]][value[1]] = 'T'
    # возвращает количество оставшихся у игрока короблей
    @property
    def get_ship_live(self):
        return self.ship_live
    # возвращает имя
    @property
    def get_name(self):
        return self.name


# класс создания короблей
class Ship:
    def __init__(self, long, x_y, direction):
        self.long = long
        self.x_y = list(x_y)
        self.direction = direction
        self.live = long
        self.ship = []
        self.overboard = []
    @property
    def get_ship(self):
        return self.ship
    @property
    def get_overboard(self):
        return self.overboard
    # создание одного коробля
    def dots(self):
        x = self.x_y[0]
        y = self.x_y[1]
        for _ in range(self.long):
            self.ship.append([x, y])
            # направление коробля(горизонтально/вертикально)
            if self.direction == 0:
                x += 1
            elif self.direction == 1:
                y += 1
        # создание клеток, куда нельзя ставить корабли
        for i in self.ship:
            x_out = -1
            for _ in range(3):
                y_out = -1
                for _ in range(3):
                    z = []
                    z.append(i[0] + x_out)
                    z.append(i[1] + y_out)
                    if z not in self.overboard:
                        self.overboard.append(z)
                    y_out += 1
                x_out += 1




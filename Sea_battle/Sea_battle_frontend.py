from Sea_battle_backend import Board
import random
class Gamer:
    def __init__(self, player, hid):
        self.player = Board(player)
        self.player.hid = hid
        self.player.set_list_ship()
        self.player.set_board()

class Game:
    def __init__(self, player):
        self.p1 = Gamer(player, True)
        self.p2 = Gamer('Comp', False)
    def __str__(self):
        return f'''
        {self.p1.player.get_name} добро пожаловать в игру Морской бой!!!
            Да прибудет с тобой Посейдон!
        '''
    def game(self):
        step = 1
        while self.p1.player.get_ship_live and self.p2.player.get_ship_live:
            print(f'{step} ХОД.\n')
            # ход игрока
            self.p2.player.get_board()
            print(f'\n\n\t\t\t\tХОДИТ {self.p1.player.get_name.upper()}')
            self.p2.player.set_list_step()
            # ход компа
            print(f'\n\n\t\t\t\tХОДИТ {self.p2.player.get_name.upper()}')
            self.p1.player.set_list_step()
            self.p1.player.get_board()
            # счет
            print(f'\nУ {self.p1.player.get_name} осталось {self.p1.player.get_ship_live} '
                  f'против {self.p2.player.get_ship_live} у {self.p2.player.get_name}\n')
            step += 1
        print(f'Победил {self.p1.player.get_name if self.p2.player.get_ship_live == 0 else self.p2.player.get_name}')
start = Game(input('Введите имя: ').title())
print(start)
start.game()

input()
import random

class TPlayer:
    def strike(self, acting_player, players, player_count):
        if players[acting_player-1].hp > 0:
            
            while (target == acting_player or players[target-1].hp <= 0 or target > player_count or target < 1):
                if target == acting_player:
                    target = int(input('Самобичеванием не здесь заниматься будешь'))
                elif players[target-1].hp <= 0:
                    target = int(input('Некрофилией не здесь заниматься будешь'))
                else:
                    target = int(input('Нет такого игрока'))

            chance = random.randint(1, 10) / 10
            if chance > players[acting_player-1].success_chance:
                print('Мазила')
            else:
                damage = random.randint(10, 30)
                players[target-1].hp -= damage
                print('Игрок', acting_player, 'въебал игроку', target, 'на', damage, 'урона, теперь здоровье игрока', target, 'составляет', players[target-1].hp, '')
            if players[target-1].hp <= 0:
                print('Игрок ', acting_player, ' захуярил игрока ', target, ', помянем\n', sep = '')

    def fireball(self, acting_player, players, player_count):
        if players[acting_player-1].hp > 0:
            
            target = int(input('Кому очко подпалим? Номер игрока вводи\n'))
            while (target == acting_player or players[target-1].hp <= 0 or target > player_count or target < 1):
                if target == acting_player:
                    target = int(input('Самобичеванием не здесь заниматься будешь'))
                elif players[target-1].hp <= 0:
                    target = int(input('Некрофилией не здесь заниматься будешь'))
                else:
                    target = int(input('Нет такого игрока'))
                    
            chance = random.randint(1, 10) / 10
            if chance > players[acting_player-1].success_chance:
                print('Мазила')
            else:
                damage = random.randint(25, 45)
                players[target-1].hp -= damage
                print('Игрок', acting_player, 'вжарил игроку', target, 'на', damage, 'урона, теперь здоровье игрока', target, 'составляет', players[target-1].hp, '')
            if players[target-1].hp <= 0:
                print('Игрок ', acting_player, ' зажарил очко игрока ', target, ', помянем\n', sep = '')

        
            
            
    

class TPlayer_warrior(TPlayer):
    hp = 150
    mana = 3
    success_chance = 0.66
    
class TPlayer_thief(TPlayer):
    hp = 100
    mana = 3
    success_chance = 0.90
    
class TPlayer_mage(TPlayer):
    hp = 100
    mana = 10
    success_chance = 0.66



#---Инициализируем всякое-----------------------------------
random.seed(version=2)

print('Добро пожаловать в героев говна и мочи! Введите количество игроков (2-4):')
player_count = int(input())
while (player_count < 2 or player_count > 4):
    if player_count == 1:
        player_count = int(input('Ебланище, наедине ты можешь подрочить, а это игра для компании\n'))
    elif player_count == 0:
        player_count = int(input('Какой ноль, блять, это игра для компании, вы играть собираетесь?\n'))
    elif player_count < 0:
        player_count = int(input('Ты ебанутый?\n'))
    else:
        player_count = int(input('Чет вас слишком дохуя\n'))
players_alive = player_count
acting_player = 1
players = [TPlayer for i in range(player_count)]
print('Заебись\n\n\nНа данном этапе разработки в игре отсутствует система магии')
#-------------------------------------------------------------

#---Раздаем игровые классы------------------------------------
for i in range(player_count):
    print('\nИгрок ', i + 1,', выбирай класс: 1 - сильный воин, 2 - ловкий вор, 3 - заднеприводный маг:', sep = '')
    class_choice = int(input())
    while class_choice < 1 or class_choice > 3:
        class_choice = int(input('Ты дебил?\n'))
    if class_choice == 1:
        players[i] = TPlayer_warrior()
        print('Игрок ', i + 1, ' выбирает класс воина', sep = '' )
    elif class_choice == 2:
        players[i] = TPlayer_thief()
        print('Игрок ', i + 1, ' выбирает класс вора', sep = '' )
    else:
        players[i] = TPlayer_mage()
        print('Игрок ', i + 1, ' выбирает класс мага', sep = '' )

print('Ну все, приятной игры')
#-----------------------------------------------------------

#---Начинаем ходы-------------------------------------------
while(players_alive > 1):
    print('\nХод игрока номер', acting_player)
    players[acting_player-1].strike(acting_player, players, player_count)
    
    players_alive = 0
    for i in range(player_count):
        if players[i].hp > 0:
            players_alive += 1
        
    if acting_player == player_count:
        acting_player = 1
    else:
        acting_player += 1
#-----------------------------------------------------------

#---Вычисление победителя-------------------------------
acting_player = 0
while players[acting_player].hp <= 0:
    acting_player += 1

print('Выигрывает игрок', acting_player + 1)

import random

#---Получаем с клавы количество игроков-------------------------------------------------------------------
def get_player_count():
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
    print('Заебись, приятной игры')
    return(player_count)
#---------------------------------------------------------------------------------------------------------

#---Ход-удар----------------------------------------------------------------------------------------------
def strike(player_count, acting_player, hp, success_chance):
    if hp[acting_player-1] > 0:
        target = int(input('Ну че, кого пиздим? Номер игрока вводи\n'))
        while (target == acting_player or hp[target-1] <= 0):
            if target == acting_player:
                target = int(input('Самобичеванием не здесь заниматься будешь'))
            else:
                target = int(input('Некрофилией не здесь заниматься будешь'))
        chance = random.randint(1, 10) / 10
        if chance > success_chance[acting_player - 1]:
            print('Мазила')
        else:
            damage = random.randint(10, 30)
            hp[target-1] -= damage
            print('Игрок', acting_player, 'въебал игроку', target, 'на', damage, 'урона, теперь здоровье игрока', target, 'составляет', hp[target - 1], '')
        if hp[target-1] <= 0:
            print('Игрок ', acting_player, ' захуярил игрока ', target, ', помянем\n', sep = '')
#---------------------------------------------------------------------------------------------------------
    
#---Инициализируем всякое-----------------------------------
random.seed(version=2)
player_count = get_player_count()
players_alive = player_count
acting_player = 1
hp = [100 for i in range(player_count)]
success_chance = [0.9 for i in range(player_count)]
#-----------------------------------------------------------

#---Начинаем ходы-------------------------------------------
while(players_alive > 1):
    print('\nХод игрока номер', acting_player)
    strike(player_count, acting_player, hp, success_chance)
    players_alive = 0
    for i in range(player_count):
        if hp[i] > 0:
            players_alive += 1
    if acting_player == player_count:
        acting_player = 1
    else:
        acting_player += 1
#-----------------------------------------------------------
acting_player = 0
while hp[acting_player] <= 0:
    acting_player += 1

print('Выигрывает игрок', acting_player + 1)

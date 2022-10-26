print('"Крестики-нолики"')

field = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def show_filed(field):
    for i, j in enumerate(field):
        if (i+1) % 3 == 0:
            print(f'{j}')
        else:
            print(f'{j} |', end='')

def victory_win(field):
   coord = ((0,1,2), (3,4,5), (6,7,8), (0,3,6), (1,4,7), (2,5,8), (0,4,8), (2,4,6))
   for (x, y, z) in coord:
       if field[x] == field[y] == field[z] and (field[x]== 'X' or field[x] == 'O'):
          return field[x]
   return ''

def player_input(symbol):
   valid = False
   while not valid:
      player = input(f'Поставьте {symbol} - ')
      try:
         player = int(player)
      except:
         print('Некорректный ввод')
         continue
      if player >= 1 and player <= 9:
         if(str(field[player-1]) not in 'XO'):
            field[player-1] = symbol
            valid = True
         else:
            print('Эта клетка занята!')
      else:
        print('Некорректный ввод, введите от 1 до 9.')

def main(field):
    count = 0
    win = False
    while not win:
        show_filed(field)
        if count % 2 == 0:
            player_input('X')
        else:
           player_input('O')
        count += 1
        if count > 4:
           tmp = victory_win(field)
           if tmp:
              print(f'{tmp} выиграл!')
              win = True
              break
        if count == 9:
            print('Ничья!')
            break
    show_filed(field)
main(field)
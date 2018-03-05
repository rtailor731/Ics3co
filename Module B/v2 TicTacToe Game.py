'''Tictactoe game for 2 players
Designed by Rahul Tailor'''

choices = ["   ", "   ", "   ", "   ", "   ", "   ", "   ", "   ", "   "]
choice = None
PlayerOneTurn = True
Winner = False

def PrintBoard():
  print ('-------------')
  print('|' + choices[0] + '|' +choices[1] +'|' + choices[2] + '|')
  print ('-------------')
  print('|' + choices[3] + '|' +choices[4] +'|' + choices[5] + '|')
  print ('-------------')
  print('|' + choices[6] + '|' +choices[7] +'|' + choices[8] + '|')
  print ('-------------')
while True:

  PrintBoard()
    
  if PlayerOneTurn :
    print ('Player 1:')
  else:
    print ('Player 2:')
    
  try: 
    choice = int(input('*>> *:'))
    'break'
  except ValueError:
    print ("please Enter a vaild field...")
    if choices [choice -1] == 'x' or choices [choice -1] == 'o':
      print ("illegal move, please try again")
  
  if PlayerOneTurn :
    choices[choice - 1]= ' x '
  else:
    choices[choice - 1]= ' o '
    
  PlayerOneTurn= not PlayerOneTurn
  

import random as r


print('\n\t\t   HI YOU PLAYED GAME TIC TAC  TOK')

all_steps = [1,2,3,4,5,6,7,8,9]

steps = []


def print_tablo():
	print('      ____________________________')
	print('		|',all_steps[0],'|',all_steps[1],'|',all_steps[2],'|')
	print('      ____________________________')
	print('		|',all_steps[3],'|',all_steps[4],'|',all_steps[5],'|')
	print('      ____________________________')
	print('		|',all_steps[6], '|',all_steps[7] ,'|',all_steps[8],'|')
	print('      ____________________________')



def player():
	while True:
		player_steps = int( input('             WHERE YOU WANT WRITE:'))
		if player_steps not in steps:
			steps.append(player_steps)
			result = player_steps -1
			all_steps[result] = 'x'
			break


def bot():
	while True:
		bot_comp= r.randint(1,9)
		if bot_comp not in steps:
			steps.append(bot_comp)
			print('              comp step',bot_comp)
			result = bot_comp -1
			all_steps[result] = 'O'
			break
while True:	
	print_tablo()
	player()
	print_tablo()
	bot()




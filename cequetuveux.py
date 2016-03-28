from random import randint

dict_brelan = {
		(1, 1, 1) : 7,
		(2, 2, 2) : 2,
		(3, 3, 3) : 3,
		(4, 4, 4) : 4,
		(5, 5, 5) : 5,
		(6, 6, 6) : 6
		}

def roll_dice():
	dices = [randint(1,6), randint(1,6), randint(1,6)]
	print dices
	dices.sort()
	dices = tuple(dices)
	winner = check_brelan(dices)
	if winner == False:
		winner = check_421(dices)
	if winner == False:
		winner = check_double(dices)
	if winner == False:
		winner = check_row(dices)
	if winner == False:
		print 'Try again'

def check_double(dices):
	if dices[0] == dices[1] == 1:
		print ' You win %s points with a double ace' % dices[2]
		return True
	else:
		return False

def check_brelan(dices):
	if dices in dict_brelan:
		print 'You win %s points with a brelan' % dict_brelan[dices]
		return True
	else:
		return False

def check_row(dices):
	if ((dices[0]  + 1) == dices [1]) and ((dices[1]  + 1) == dices [2]):
		print 'You make a row ! It gives you 2 points'
		return True
	else:
		return False
	
def check_421(dices):
	if dices == (1, 2, 4):
		print 'You win 8 points with a 421 !'
		return True
	else:
		return False

roll_dice()
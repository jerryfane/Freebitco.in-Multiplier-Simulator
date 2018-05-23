from random import randint
import logging
logging.basicConfig(filename='log.log',level=logging.DEBUG)


base_bet = 1                 #Modificare qui
base_odd = 2                 #Modificare qui
odd_lose = 2                 #Modificare qui
lose_multiplier = 2          #Modificare qui
win_multiplier = 1           #Modificare qui

rolls_number = 100           #Modificare qui
simulation_number = 30       #Modificare qui

odd = base_odd

results = []
loses = 0
wins = 0
base_bets = []
counts = []

for e in range(0, simulation_number):
    earning = 0
    for i in range(0, rolls_number):
        randomnumber = randint(0, 10000)
        limit = ((10000/odd) - (500/odd))
        if randomnumber < limit:
            earning = earning - base_bet
            earning = earning + base_bet * odd
            odd = base_odd
            base_bet = base_bet * win_multiplier
            logging.warning('random number: '+str(randomnumber)+', limit: '+str(limit)+', you won, base bet: '+str(base_bet))
            wins = wins + 1
        else:
            earning = earning - base_bet
            odd = odd_lose
            base_bet = base_bet * lose_multiplier
            logging.warning('random number: '+str(randomnumber)+', limit: '+str(limit)+', you lose, base bet: '+str(base_bet))
            loses = loses + 1
            base_bets.append(base_bet)
            #print(str(i)+' of '+str(rolls_number))
    print(str(e)+' of '+str(simulation_number))
    if earning > 0:
	    logging.info('event number: '+str(e)+', you won: '+str(earning)+' satoshi')
    else:
	    logging.info('event number: '+str(e)+', you lose: '+str(earning)+' satoshi')
    results.append(earning)
	
total_result = sum(results)

if earning > 0:
    print('you won: ' + str(total_result) + ' satoshi')
else:
    print('you lose: ' + str(total_result) + ' satoshi')	

rolls = loses + wins
losespercentage = loses / rolls * 100
winspercentage = wins / rolls * 100

logging.info('loses percentage: '+str(losespercentage)+'%')
logging.info('wins percentage: '+str(winspercentage)+'%')

print('loses percentage: '+str(losespercentage)+'%')
print('wins percentage: '+str(winspercentage)+'%')

max_bet = max(base_bets)
print('maximum bet: '+str(max_bet))


import math

lose_streak = math.log(max_bet, odd_lose)
print('loses streaks: '+str(lose_streak))
print('total rolls number: '+str(rolls_number*simulation_number))





	
	

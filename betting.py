import matplotlib.pyplot as plt
import numpy as np
from random import random
from statistics import mean, median

# something

def get_br(n, rounds, perc_bet, win_perc):
    """Generates a list of the median bankroll.
    Arguments:
        n - number of sequential bets
        rounds - number of times to perform simulation
        perc_bet - percentage of bankroll to be bet
        win_perc - percentage of time expected to win (binary outcome)
    """

    br_ave = []
    br_list = []
    for k in range(n):
        br_list.append([])

    for j in range(rounds):
        bankroll = 100
        for i in range(n):
            result = random()
            if result >= win_perc:
                bankroll -= bankroll * perc_bet
            else:
                bankroll += bankroll * perc_bet
            br_list[i].append(bankroll)

    for bet_num in br_list:
        br_ave.append(median(bet_num))

    return br_ave

def simple_sim():
    bankroll = 100
    perc_bet = 0.1
    win_perc = .8
    for i in range(100):
        result = random()
        if result >= win_perc:
            bankroll -= bankroll * perc_bet
        else:
            bankroll += bankroll * perc_bet

        print(bankroll)

w50 = get_br(n=100, rounds=1000, win_perc=0.55, perc_bet=0.1)
w55 = get_br(n=100, rounds=1000, win_perc=0.55, perc_bet=0.2)
w60 = get_br(n=100, rounds=1000, win_perc=0.55, perc_bet=0.3)
w65 = get_br(n=100, rounds=1000, win_perc=0.55, perc_bet=0.4)
# simple_sim()

x = np.arange(0, 100)
fig, ax = plt.subplots()
ax.set(title="Median Bankroll After N Bets", xlabel='Bet # (N)', ylabel='Bankroll')
ax.plot(x, w50, label='50')
ax.plot(x, w55, label='55')
ax.plot(x, w60, label='60')
ax.plot(x, w65, label='65')
ax.grid()
ax.legend(title='Win Percentage')
plt.show()
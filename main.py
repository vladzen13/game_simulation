
import random

def game_log(k, days=100):
	balance = 1000
	res = []
	for d in range(days):
		#  play the game on first day
		bet = balance / k

		balance += game_result(bet)	
		
		res.append(balance)

	return res


def game_result(bet):
	return -bet if random.random() < 0.45 else bet


data = []
# data structure - [ ( k - 'caution', [ value of many day1, value of many day2...] - 'days_list') - 'pl_list' ...]
for n in range(10000):
	k = random.randint(1, 100)
	log = game_log(k, days=100)
	item = (k, log)
	data.append(item)

import plotly.express as px


def distr_caution(data):
# распределение кол-ва Сереж по осторожности
    fig = px.histogram([caution for caution, days_list in data])
    fig.show()


def i_pl_list(i, days=100):
# график богатства i-ого Сережи по дням
    fig = px.line(x = list(range(1, days+1)), y = data[i][1])
    fig.show()
    print(f"caution = {data[i][0]}")



def sum_players(data, days=100):
# график богатства всех Сереж вместе по дням

    sum_d_list = [sum(days_list) for days_list in (zip(*[days_list for caution, days_list in data]))]

    fig = px.line(x = list(range(1, days+1)), y = sum_d_list)
    fig.show()



def eq_caution(def_k, data, days=100):
#график богатства всех Сереж c одинаковой осторожностью по дням

    fig = px.line(data, x = list(range(1, days+1)), y = [days_list for caution, days_list in data if caution == def_k])
    fig.show()



def rich_player(data, days=100):
#Сколько заработал самый успешный из Сереж и какая у него была осторожность
    final_value = [days_list[-1] for caution, days_list in data]
    i = final_value.index(max(final_value))
    i_pl_list(i, days=100)


from statistics import *


def median_value(def_k, data):
	median_ = median([days_list[-1] for caution, days_list in data if caution == def_k])
	return median_


def mean_value(def_k, data):
	mean_ = mean([(days_list[-1]) for caution, days_list in data if caution == def_k])
	return mean_

def pstdev_value(def_k, data):
	pstdev_ = pstdev([(days_list[-1]) for caution, days_list in data if caution == def_k])
	return pstdev_


def percent_winners(def_k, data):
    winner = 0
    all_ = 0
    for caution, days_list in data:
        if def_k == caution:
            all_ += 1
            if days_list[-1] > 1000:
                winner += 1
    return (winner/all_)*100


def mean_value_percent(def_k, data):
	return mean_value(def_k, data) * (percent_winners(def_k, data) / 100)


def median_value_percent(def_k, data):
	return median_value(def_k, data) * (percent_winners(def_k, data) / 100)


def drow_bar(data, f):
	fig = px.bar(x = range(1, 101), y = [f(def_k, data) for def_k in range(1, 101)])
	fig.show()
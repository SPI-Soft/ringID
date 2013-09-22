# -*- coding: utf-8 -*-

execfile('stimuli.py')

condition = [1]*100 + [2]*100 + [3]*20 + [4]*20
random.shuffle(condition)

nTrials = len(condition)

# create a sequence of random stimulus onset times
time_list = []
for trial in range(nTrials):
	lag_time = random.randrange(100,150,1)*0.01
	time_list.append(lag_time)


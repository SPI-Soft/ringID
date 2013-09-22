#!/usr/bin/python
# -*- coding: utf-8 -*-

################################
# import the necessary modules #

import VisionEgg
VisionEgg.start_default_logging(); VisionEgg.watch_exceptions()
VisionEgg.config.VISIONEGG_SYNC_SWAP = 1
VisionEgg.config.VISIONEGG_MONITOR_REFRESH_HZ = 100.0
VisionEgg.config.VISIONEGG_SCREEN_W = 1024
VisionEgg.config.VISIONEGG_SCREEN_H = 768
VisionEgg.config.VISIONEGG_HIDE_MOUSE = 1
VisionEgg.config.VISIONEGG_FRAMELESS_WINDOW = 1
VisionEgg.config.VISIONEGG_FULLSCREEN = 1
from VisionEgg.Core import *
from VisionEgg.FlowControl import Presentation
from VisionEgg.Text import *
from VisionEgg.Textures import *
from VisionEgg.MoreStimuli import *
from numpy import *
from pygame import *
import math, random, time
################################

execfile('vp_input.py')

## Screen Parameters
screen = get_default_screen()
screen.parameters.bgcolor = (0.8,0.8,0.8,0.8)
mid_x  = screen.size[0]/2
mid_y  = screen.size[1]/2

## Generate Trials
execfile('functions.py')
execfile('trials.py')
 


## Instructions
start_viewp = Viewport(screen=screen, stimuli=[text1])
screen.clear()
start_viewp.draw()
swap_buffers()
start_keypress()





## define different viewports according to condition
#viewp  = Viewport(screen=screen, stimuli=[])
fix_viewp  = Viewport(screen=screen, stimuli=[fc,text_trials, text_points])
red_viewp = Viewport(screen=screen, stimuli=[fc, red_circ,text_trials, text_points])
blue_viewp = Viewport(screen=screen, stimuli=[fc, blue_circ,text_trials, text_points])
rsp_viewp = Viewport(screen=screen, stimuli=[text3, red_target, blue_target,text_trials, text_points])  
kntrl_viewp = Viewport(screen=screen, stimuli=[text3, red_target, blue_target,text_trials, text_points,text_kontroll])  
nxt_viewp = Viewport(screen=screen, stimuli=[text4,text_trials, text_points])
nxt2_viewp = Viewport(screen=screen, stimuli=[text4,text_trials, text_points, text_kontroll])

##################################
# start the loop over all trials #
##################################

answ = []
rsp_times = []
points = 0

trial = 0
pygame.event.set_allowed(KEYDOWN)



while trial != nTrials:	

	text_trials.parameters.text = u"Katsekord: " + str(trial + 1)

	screen.clear()
        fix_viewp.draw()
        swap_buffers()
	time.sleep(time_list[trial])


        if condition[trial] == 1 or condition[trial] == 3: # red

		screen.clear()
	        red_viewp.draw()
	        swap_buffers()
	        pygame.event.clear()
		start_time = time.time()
		time.sleep(0.1)
			
		
        elif condition[trial] == 2 or condition[trial] == 4: # blue

		screen.clear()
	        blue_viewp.draw()
	        swap_buffers()
	        pygame.event.clear()
		start_time = time.time()
		time.sleep(0.1)

	screen.clear()
        fix_viewp.draw()
        swap_buffers()
	time.sleep(0.4) ### Siin saab defineerida stiimulite ja vastamise vahelise aja

	screen.clear()
        rsp_viewp.draw()
        swap_buffers()

	rsp_keypress()
	answ.append(ans)
	rsp_times.append(rsp)
	#print [condition[trial], lag[trial], ans, rsp_time]		
	pygame.event.clear()
		
	if condition[trial] == 4 and ans == 1:
		points -= 5
	else:
		if ans == 1: points += 1
		elif ans == 0: pass

	f = open('KI_' + str(subj_nr.get()) + '.dat','a')
	L = (str(subj_nr.get()) + '\t' + str(trial + 1) + '\t' + str(condition[trial]) + '\t' + str(ans) + '\t' + str(rsp) + '\t' + str(points) + '\n')
        f.write(L)

	text_points.parameters.text = u"Punktid: " + str(points)

        if condition[trial] == 3 or condition[trial] == 4:
                if condition[trial] == 4 and ans == 1:
                        text_kontroll.parameters.text = u'Kontroll! Vahele jäid!'
                        text_kontroll.parameters.color = (1.0,0.0,0.0)
                        screen.clear()
                        nxt2_viewp.draw()
                        swap_buffers()
                        start_keypress()
                else:
                        text_kontroll.parameters.text = u'Kontroll! Õige!'
                        text_kontroll.parameters.color = (0.0,1.0,0.0)
                        screen.clear()
                        nxt2_viewp.draw()
                        swap_buffers()
                        start_keypress()
        else:
                screen.clear()
                nxt_viewp.draw()
                swap_buffers()
                start_keypress()

        trial += 1

                

screen.close()
#write_data()


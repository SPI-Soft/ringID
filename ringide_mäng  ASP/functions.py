
### different key press functions

def start_keypress():
    pressed = False
    while not pressed:
        for event in pygame.event.get():
            if event.type == pygame.locals.KEYDOWN:
                if event.key == pygame.locals.K_SPACE:
                    pressed = True
                elif event.key == pygame.locals.K_ESCAPE:
		    write_data()
		    exit_exp()


def rsp_keypress():
    global rsp, ans
    pressed = False
    start_time = time.time()
    while not pressed:
    	for event in pygame.event.get():
    		if event.type == pygame.locals.KEYDOWN:
				if event.key == pygame.locals.K_LEFT:
			    		end_time = time.time()
			    		rsp = end_time - start_time
			    		ans = 0
		            		pressed = True
				if event.key == pygame.locals.K_RIGHT:
			    		end_time = time.time()
			    		rsp = end_time - start_time
			    		ans = 1
		            		pressed = True
				if event.key == pygame.locals.K_ESCAPE:
					write_data()
					exit_exp()

def nxt_keypress():
	for event in pygame.event.get():
        	if event.key == pygame.locals.K_ESCAPE:
			write_data()
			exit_exp()
        	if event.key == pygame.locals.K_SPACE:
			return 1
	if not pygame.event.get():
		return 0

### a function that creates the behavioral data file at the end of the experiment

def write_data():

        for trl in range(trial):
            KI   = str(subj_nr.get())
            TRL  = str(trl + 1)
            COND = str(condition[trl])
	    LAG  = str(lag[trl])
            ANS  = str(answ[trl])
	    RSP  = str(rsp_times[trl])
	    if answ[trl] == 1 and condition[trl] == 1 :
            	CORRECT = str(1)
	    elif answ[trl] == 1 and condition[trl] == 3 :
            	CORRECT = str(1)
	    elif answ[trl] == 2 and condition[trl] == 2 :
            	CORRECT = str(1)
	    elif answ[trl] == 2 and condition[trl] == 4 :
            	CORRECT = str(1)
	    else:
		CORRECT = str(0)

            f = open('KI_' + str(subj_nr.get()) + '.dat','a')
            L = (KI + '\t' + TRL + '\t' + COND + '\t' + LAG + '\t' + ANS + '\t' + RSP + '\t' + CORRECT + '\t' + str(time_tar[trl]) + '\t' + str(time_lag[trl]) + 
		'\t' + str(time_mask[trl]) + '\n')
            f.write(L)

def measure_frames():
    frame_timer = VisionEgg.Core.FrameTimer()
    num_frames = 0
    while num_frames != 50000:
        frame_timer.tick()
        num_frames += 1

    frame_timer.log_histogram()

def visual_angle(inches, angle, distance):
	cents = 2.54 * inches
	pix_diag = sqrt(screen.size[0]**2 + screen.size[1]**2)
	ppi = pix_diag / cents
	size_cm = math.tan(math.radians(angle)/2)*2*distance
	size_pix = ceil(ppi*size_cm)
	return size_pix




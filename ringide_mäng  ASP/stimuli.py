# -*- coding: utf-8 -*-

## Fixation cross
fc_size = (15,15,4)
fc_stim = numpy.ones(fc_size, dtype = numpy.float)
fc_stim[:7,:7,3]   -= 1.0
fc_stim[:7,-7:,3]  -= 1.0
fc_stim[-7:,-7:,3] -= 1.0
fc_stim[-7:,:7,3]  -= 1.0
fc_texture = Texture(fc_stim)
fc = TextureStimulus(texture  = fc_texture, 
		     color    = (0.2, 0.2, 0.2),  
		     position = (mid_x, mid_y), 
		     anchor   = 'center', 
		     size     = fc_texture.size, 
		     mipmaps_enabled = 0,
		     internal_format = gl.GL_RGBA)


## circles

red_circ = FilledCircle( color    = (1.0, 0.0, 0.0),  
		       	 position = (mid_x, mid_y * 1.35), 
		         anchor   = 'center', 
		         radius   = 40.0)		# in eye coordinates

blue_circ = FilledCircle( color    = (0.0, 0.0, 1.0),  
		       	 position = (mid_x, mid_y * 1.35), 
		         anchor   = 'center', 
		         radius   = 40.0)

## Targets

red_target  = Target2D(  color    = (1.0, 0.0, 0.0),  
		       	 position = (mid_x*1.15, mid_y), 
		         anchor   = 'center', 
		         size   = (20.0,20.0) )		# in eye coordinates

blue_target = Target2D(  color    = (0.0, 0.0, 1.0),  
		       	 position = (mid_x*0.85, mid_y), 
		         anchor   = 'center', 
		         size   = (20.0,20.0) )

## Texts 

text1 = VisionEgg.Text.Text(text = u"start?",
             position=(mid_x, mid_y), color = (0.2,0.2,0.2),
             anchor = 'center')
text2 = VisionEgg.Text.Text(text = u"SININE      <-        ->      PUNANE",
             position=(mid_x, mid_y), color = (0.2,0.2,0.2),
             anchor = 'center')
text3 = VisionEgg.Text.Text(text = u"?",
             position=(mid_x, mid_y), color = (0.2,0.2,0.2),
             anchor = 'center')
text4 = VisionEgg.Text.Text(text = u"Järgmine?",
             position=(mid_x, mid_y), color = (0.2,0.2,0.2),
             anchor = 'center')
text_trials = VisionEgg.Text.Text(text = u"Katsekord: 1",
             position=(mid_x*1.65, mid_y*1.75), color = (0.2,0.2,0.2),
             anchor = 'left')
text_points = VisionEgg.Text.Text(text = u"Punktid: 0",
             position=(mid_x*1.65, mid_y*1.65), color = (0.2,0.2,0.2),
             anchor = 'left')

text_kontroll = VisionEgg.Text.Text(text = u"Kontroll!",
             	position=(mid_x, mid_y*1.65), color = (0.0,1.0,0.0),
             	anchor = 'center')


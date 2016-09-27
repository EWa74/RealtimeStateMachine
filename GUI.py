from bge import logic
import compz
 
def gui():
	global markerIgnition
	global TimerSpeedTmOut
	global markerIgnitionStartTime
	global txtTimerSpeedTmOut

	cont = logic.getCurrentController()
	o = cont.owner

	if "init" not in o:
	
		markerIgnition = False #HG1
		markerIgnitionStartTime = 0.0
		
		o["C"] = compz.Compz()

		# THEME fuer die GUI:
		btnStyle = compz.Style(name="button", stylesPath=logic.expandPath("//Compz_Theme/default/"))
		panelStyle = compz.Style(name="panel", stylesPath=logic.expandPath("//Compz_Theme/default/"))
		listStyle = compz.Style(name="list", stylesPath=logic.expandPath("//Compz_Theme/default/"))
		entryStyle = compz.Style(name="entry", stylesPath=logic.expandPath("//Compz_Theme/default/"))
		sliderStyle = compz.Style(name="slider", stylesPath=logic.expandPath("//Compz_Theme/default/"))
		cbStyle = compz.Style(name="checkbox", stylesPath=logic.expandPath("//Compz_Theme/default/"))
		radioStyle = compz.Style(name="radio", stylesPath=logic.expandPath("//Compz_Theme/default/"))
		
	# -----------------------
	# FUNCTION 'clickIgnition' - markerIgnition
	# -----------------------	
		def clickIgnition(sender): # , marker = 0
			global markerIgnition #HG1
			global markerIgnitionStartTime #Eric
			
			lst1.selectedIndex=1
		  
			if markerIgnition: 							
				#markerIgnitionStartTime = o['TimerSpeedTmOut']
				logic.getCurrentScene().objects["MeshPhase0"].color = [ 1.0, 0.45, 0.80, 1.0] #color ON
				valueSliderSpdThr.value =0
				btnIgnition.text ='Ignition: OFF'
				markerIgnition = False	  
				
			else:
				o['TimerSpeedTmOut'] = 0.0 #new
				#markerIgnitionStartTime = o['TimerSpeedTmOut']
				logic.getCurrentScene().objects["MeshPhase0"].color = [ 0.55, 0.87, 1.0, 1.0] #color OFF
				valueSliderSpdThr.value =0
				btnIgnition.text ='Ignition: ON'
				markerIgnition = True
				
			markerIgnitionStartTime = o['TimerSpeedTmOut']
			
	# -----------------------
	# FUNCTION 'clickSpeedPlausibility'
	# -----------------------    
		def clickSpeedPlausibility(sender): 
			global  markerSpeedPlausibility
			print('sender: ' + str(sender))
			print("Clicked on button markerSpeedPlausibility " + sender.text)
			print('markerSpeedPlausibility: ' + str(markerSpeedPlausibility))
			
			text.text = sender.text
			
			if markerSpeedPlausibility == 'VALID':
				logic.getCurrentScene().objects["MeshPhase0"].color = [ 1.0, 0.45, 0.80, 1.0] #color ON
				markerSpeedPlausibility ='VINALID'
			   
			elif markerSpeedPlausibility == 'VINALID':
				logic.getCurrentScene().objects["MeshPhase0"].color = [ 0.55, 0.87, 1.0, 1.0] #color OFF
				markerSpeedPlausibility ='VALID'
				
			print('markerSpeedPlausibility nach if: ' + str(markerIgnition))

	# -----------------------
	# FUNCTION 'clickActualClass'
	# -----------------------    

		def clickActualClass(sender): 
			global  markerActualClass

	# -----------------------  
	# FUNCTION 'valueSliderChange' - SpeedThresh
	# -----------------------   
		
		def valueSliderChangeSpeedThresh(sender):
			global intSpeed
			global markerSpeedThresh
			intSpeed = sender.value
			print('.......................  sender: ' + str(sender))
			print("Clicked on button valueSliderChange " + str(sender.value))
			
			txtVehicleSpeed.text = "%.0f" % (intSpeed * 100) + ' km/h'

	# -----------------------  
	# FUNCTION 'valueSliderChange' - SpeedTmOutThresh
	# -----------------------      
		
		def valueSliderChangeSpeedTmOutThresh(sender):
			global intSpeedTmOut
			global markertxtSpeedTmOutThresh
			intSpeedTmOutThresh = sender.value
			print('.......................  sender: ' + str(sender))
			print("Clicked on button valueSliderChange " + str(sender.value))
			
			txtSpeedTmOutThresh.text = "%.0f" % (intSpeedTmOutThresh * 100) + ' seconds'

	# -----------------------  
	# FUNCTION 'valueLst1Index' - ??? --------------------------------------------------------------- ---------------------------------------------------------------
	# -----------------------   
		def valueLst1Index(sender):
			print("Clicked lst1.item " + str(sender.items[2]))
			print("------------------------  sender.selectedIndex: " + str(sender.selectedIndex))

	# ----------------------------------------------------------------
	# linkes Panel - pan -
	# ----------------------------------------------------------------
		
		pan = compz.Panel(panelStyle)
		pan.position = [5, 5]
		pan.width = 150
		pan.height = 335
		o["C"].addComp(pan)

		text = compz.Entry(style=entryStyle)

	# ------------------------------------------------------------------------------------------------------------------------------
	# GUIb Layout block
	# ------------------------------------------------------------------------------------------------------------------------------      
     
		
	# ADD label
		lbl = pan.addComp(compz.Label("Input:"))
		lbl.row = 1
		lbl.textAlignment = compz.TEXT_ALIGN_LEFT

					 
	# ADD Buttons fuer Teile des linkes Panel:
		btnIgnition = compz.Button("Ignition: OFF", btnStyle)
		btnIgnition.events.set(compz.EV_MOUSE_CLICK, clickIgnition)
		btnIgnition.icon = compz.Icon(logic.expandPath("//Compz_Theme/control_play.png"))
		pan.addComp(btnIgnition)



	# ADD Buttons fuer Teile des linkes Panel:     
		cbSpeedPlausibility = compz.CheckBox("SpeedPlausible", cbStyle)
		cbSpeedPlausibility.events.set(compz.EV_CHECK_STATE_CHANGED, clickSpeedPlausibility)
		
		pan.addComp(cbSpeedPlausibility)   
		
		
	# ADD Buttons fuer Teile des linkes Panel:   
		cbActualClass= compz.CheckBox("Occupied", cbStyle)
		cbActualClass.events.set(compz.EV_CHECK_STATE_CHANGED, clickActualClass)
		
		pan.addComp(cbActualClass)
		
				
	# ADD label   
		lbl = pan.addComp(compz.Label("Limit Vehicle Speed:"))
		#lbl.row = 1
		lbl.textAlignment = compz.TEXT_ALIGN_LEFT

	   
	# Textfield:    
		txtVehicleSpeed = compz.Entry(style=entryStyle)
		txtVehicleSpeed.readOnly = True
		pan.addComp(txtVehicleSpeed)   
		
		valueSliderSpdThr = pan.addComp(compz.Slider(style=sliderStyle))
		valueSliderSpdThr.precision = 2
		valueSliderSpdThr.events.set(compz.EV_SLIDER_VALUE_CHANGE, valueSliderChangeSpeedThresh)

		 
	# ADD label
		lbl = pan.addComp(compz.Label("Limit: SpeedTmOut"))
		#lbl.row = 1
		lbl.textAlignment = compz.TEXT_ALIGN_LEFT

		
	# ADD Textfield:    
		txtSpeedTmOutThresh = compz.Entry(style=entryStyle)
		txtSpeedTmOutThresh.readOnly = True
		pan.addComp(txtSpeedTmOutThresh) 
		
		valueSliderSpdTmOutThr = pan.addComp(compz.Slider(style=sliderStyle))
		valueSliderSpdTmOutThr.precision = 2
		valueSliderSpdTmOutThr.events.set(compz.EV_SLIDER_VALUE_CHANGE, valueSliderChangeSpeedTmOutThresh)
			
			
	 
	# ----------------------------------------------------------------
	# rechtes Panel - gpan - :
	# ----------------------------------------------------------------

		gpan = compz.Panel(panelStyle)
		gpan.position = [200, 5] # [1190, 5]
		gpan.width = 160
		gpan.height = 335
		#gpan.layout = compz.GridLayout()
		o["C"].addComp(gpan)

	# ADD label
		lbl0 = gpan.addComp(compz.Label("Output:"))
		#lbl0.row = 0
		lbl0.textAlignment = compz.TEXT_ALIGN_LEFT

	# ADD Label: Textfield - SpeedTmOut:    

		lblO1 = gpan.addComp(compz.Label("TimerSpeedTmOut:"))
		#lbl.row = 4
		lblO1.textAlignment = compz.TEXT_ALIGN_LEFT

	# ADD Textfield - SpeedTmOut:   
		txtTimerSpeedTmOut = compz.Entry(style=entryStyle)
		txtTimerSpeedTmOut.readOnly = True
		gpan.addComp(txtTimerSpeedTmOut)   
		  
	# ADD List
		lbl1 = gpan.addComp(compz.Label("Buffer Phase:"))
		#lbl1.row = 1
		lbl1.textAlignment = compz.TEXT_ALIGN_LEFT
		lst1 = gpan.addComp(compz.List(listStyle))
		#lst1.width = 60
		lst1.height = 60
		#lst1.rowSpan = 9
		#lst1.columnSpan = 20
		#lst1.row = 3
		lst1.items.append("Phase 0")
		lst1.items.append("Phase 1")
		lst1.items.append("Phase 2")
	   
		
		o["init"] = 1
	else:
		o["C"].update()
	if markerIgnition: #HG1
				#txtTimerSpeedTmOut.text = "%3.0f" % (o['TimerSpeedTmOut'] - markerIgnitionStartTime  ) + ' seconds' #HG1
				txtTimerSpeedTmOut.text = "%3.0f" % (o['TimerSpeedTmOut']  ) + ' seconds' #HG1 new
				print('init - else - markerIgnitionStartTime: ' + str(markerIgnitionStartTime))
gui()	
		
	 

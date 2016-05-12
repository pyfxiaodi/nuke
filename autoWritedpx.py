def autoWritedpx():
	import os
	import nuke
	import re
	import nukescripts

	w = nuke.createNode('Write', inpanel = True)

	scriptPath = nuke.root().knob('name').value()
	scriptPathList = re.split('/',scriptPath)

	tempA = scriptPathList[-1]
	tempB = re.split('\.', tempA)

	scriptName = tempB[0]
	showName = scriptPathList[-5]
	shotName = scriptPathList[-3]
	diskStationPath = '/Volumes/VOLT_CENTRAL'
	print showName
	print shotName
	print scriptName

	output_path = diskStationPath +'/'+ showName +'/'+ 'Dailies' +'/'+ shotName +'/'+ scriptName +'/'+ scriptName +'.%04d.dpx'
	w.knob('file').fromScript(output_path)

	try:
		os.makedirs(diskStationPath +'/'+ showName +'/'+ 'Dailies' +'/'+ shotName +'/'+ scriptName)
	except:
		pass


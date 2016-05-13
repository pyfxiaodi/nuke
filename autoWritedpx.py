def autoWritedpx():
	import os
	import nuke
	import re
	import nukescripts

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


	p = nuke.Panel('Any Sub Folder?')

	p.addSingleLineInput('Sub Folder', 'None')
	p.addButton('Nope')
	p.addButton('Yes, mkdir please')

	ret = p.show()
	subFolder = None
	subFolder = p.value('Sub Folder')

	if subFolder == 'None':
		try:
			os.makedirs(diskStationPath +'/'+ showName +'/'+ 'Dailies' +'/'+ shotName +'/'+ scriptName)
		except:
			pass
		w = nuke.createNode('Write', inpanel = True)
		output_path = diskStationPath +'/'+ showName +'/'+ 'Dailies' +'/'+ shotName +'/'+ scriptName +'/'+ scriptName +'.%04d.dpx'
		w.knob('file').fromScript(output_path)

	else:
		try:
			os.makedirs(diskStationPath +'/'+ showName +'/'+ 'Dailies' +'/'+ shotName +'/'+ scriptName + '/' + subFolder)
		except:
			pass
		w = nuke.createNode('Write', inpanel = True)
		output_path = diskStationPath +'/'+ showName +'/'+ 'Dailies' +'/'+ shotName +'/'+ scriptName +'/'+ subFolder + '/' + scriptName +'.%04d.dpx'
		w.knob('file').fromScript(output_path)




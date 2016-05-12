p = nuke.Panel('SAVE THIS SHIT')
dir(p)
jobList = ['Roto CleanUp Comp something']
p.addEnumerationPulldown('Select Your Job:', ''.join(jobList))
nameList = ['Bar Bin Echo July Roy Sora xxx Yry Zly Zcg somebody'] 
p.addEnumerationPulldown('Select Your Name:', ''.join(nameList))
p.addSingleLineInput('Version Number', '01')

p.addButton('Yes, save it please')
p.addButton('No, go fuck yourself')
ret = p.show()

enumVal = p.value("Select Your Job:")
print enumVal
print p.value('Select Your Name:')


p.addSingleLineInput('Path', ('/Volumes/VOLT_CENTRAL/'+enumVal))
print p.value('No, go fuck yourself')
print p.value('Yes, save it please')
savePath = p.value('Path')
nuke.scriptSaveAs(savePath)
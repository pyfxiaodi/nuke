def easySave():
    import os
    import nuke
    import re
    import nukescripts
    scriptPath = nuke.root().knob('name').value()
    if scriptPath == '':
        p = nuke.Panel('Save This Shit')

        p.addEnumerationPulldown('Job', 'Test Roto CleanUp Comp')
        p.addEnumerationPulldown('Name', 'Tester Bar Bin Echo July Roy Sora xxx Yry Zly Zcg')
        p.addSingleLineInput('Version', '001')
        p.addButton('No, go fuck yourself')
        p.addButton('Yes, please save it')

        ret = p.show()

        job = p.value('Job')
        name = p.value('Name')
        version = p.value('Version')
        file = None

        if job == None:
            pass
        else:
            sourceName = nuke.selectedNode().knob('file').value()
            sourceNameList = re.split('/',sourceName)
            print sourceName
            print sourceNameList
            showName = sourceNameList[-5]
            shotName = sourceNameList[-3]
            print showName
            print shotName
            savePath = '/Volumes/NukeDome/' + showName + '/' + 'Conform' + '/' + shotName + '/' + 'Script'
            print savePath
            saveFile = savePath + '/' + shotName + '_' + job + '_' + name + '_' + 'v' + version
            print saveFile
            if nuke.env['nc']:
                file = saveFile + '.nknc'
                nuke.scriptSave(file)
            else:
                file = saveFile + '.nk'
                nuke.scriptSave(file)
            nuke.scriptOpen(file)
        
    else:
        print scriptPath
        scriptPath = nuke.root().knob('name').value()
        scriptPathList = re.split('/',scriptPath)

        print scriptPathList
        tempA = scriptPathList[-1]
        tempB = re.split('\.', tempA)
        tempC = re.split('_',tempB[0])

        print tempB
        print tempC

        job = tempC[-3]
        name = tempC[-2]
        version = tempC[-1][1:]
        count = int(version) + 1
        Fcount = ("%03d" % count)

        print job
        print name
        print version
        print count


        p = nuke.Panel('Save As This Shit')

        p.addEnumerationPulldown('Job', job + ' Test Roto CleanUp Comp')
        p.addEnumerationPulldown('Name', name + ' Tester Bar Bin Echo July Roy Sora xxx Yry Zly Zcg')
        p.addSingleLineInput('Version', Fcount)
        p.addButton('No, go fuck yourself')
        p.addButton('Yes, please save it')

        ret = p.show()

        job = p.value('Job')
        name = p.value('Name')
        version = p.value('Version')

        print job
        print name
        print version

        if job == None:
            pass
        else:
            scriptPathList = re.split('/',scriptPath)
            print scriptPath
            print scriptPathList

            showName = scriptPathList[-5]
            shotName = scriptPathList[-3]
            print showName
            print shotName

            savePath = '/Volumes/NukeDome/' + showName + '/' + 'Conform' + '/' + shotName + '/' + 'Script'
            print savePath
            saveFile = savePath + '/' + shotName + '_' + job + '_' + name + '_' + 'v' + version
            print saveFile

            if nuke.env['nc']:
                file = saveFile + '.nknc'
                nuke.scriptSave(file)
            else:
                file = saveFile + '.nk'
                nuke.scriptSave(file)
            nuke.scriptOpen(file)


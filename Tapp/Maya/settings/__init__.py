import maya.cmds as cmds

import Tapp.utils.yaml as uy

def getSettings():
    
    settingsFile=cmds.internalVar(upd=True)+'Tapp.yml'
    f=open(settingsFile,'r')
    
    settings=uy.load(f)
    
    return settings

def setSettings(data):
    
    settingsFile=cmds.internalVar(upd=True)+'Tapp.yml'
    f=open(settingsFile,'w')
    
    uy.dump(data, f)

def startup():
    
    settings=getSettings()
    
    if settings['launchWindowAtStartup']==True:
        cmds.evalDeferred('import Tapp.Maya.window as win;reload(win);win.show()')
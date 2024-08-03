import maya.cmds as cmds

# Unlocks the basic controls on selected objects
# Translate, rotate, scale, visibility

selectedList = cmds.ls(sl=1, ap=1, tr=1)

for sel in selectedList:
    cmds.setAttr((sel + ".tx"), k=1, l=0)
    cmds.setAttr((sel + ".ty"), k=1, l=0)
    cmds.setAttr((sel + ".tz"), k=1, l=0)
    
    cmds.setAttr((sel + ".rx"), k=1, l=0)
    cmds.setAttr((sel + ".ry"), k=1, l=0)
    cmds.setAttr((sel + ".rz"), k=1, l=0)
    
    cmds.setAttr((sel + ".sx"), k=1, l=0)
    cmds.setAttr((sel + ".sy"), k=1, l=0)
    cmds.setAttr((sel + ".sz"), k=1, l=0)
    
    cmds.setAttr((sel + ".v"), k=1, l=0)
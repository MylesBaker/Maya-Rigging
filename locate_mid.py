import maya.cmds as cmds

# credit to Ben Cheeseman for this script
# Places a locator at the center of your selection

def centreOfPoints():
    selection = cmds.ls(selection=True)
    bBox = cmds.exactWorldBoundingBox(selection)
    centre = ((bBox[3]+bBox[0])/2,(bBox[4]+bBox[1])/2,(bBox[5]+bBox[2])/2)
    cmds.spaceLocator(position = centre)
    cmds.xform(preserve = True, centerPivots = True)
centreOfPoints()
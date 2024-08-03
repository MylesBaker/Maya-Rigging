import maya.cmds as cmds

# Credit to Ben Cheeseman for making this
# Select top of contrainer hierarchy, then constrained hierarchy

def constrainHierarchy():
    #sets up variables
    roots = cmds.ls(selection = True)
    parentChildren = []
    bindChildren = []
    bindStart = [0]
    #Lists all child joints of selected hierarchies
    for i in range(len(roots)-1):
        bindChildren +=(cmds.listRelatives(roots[i],allDescendents= True, type= 'joint'))
        bindStart.append(len(bindChildren))
    
    parentChildren = cmds.listRelatives(roots[len(roots)-1],allDescendents= True, type= 'joint')
    cmds.select(cl = True)    
        
    cmds.parentConstraint(roots)   
    for i in range(len(parentChildren)):
        cmds.select(cl=True)
        for x in range(len(roots)-1):
            cmds.select(bindChildren[(i+bindStart[x])],add = True)
        tempConstraint = cmds.ls(selection = True)
        cmds.parentConstraint(tempConstraint,parentChildren[i])
        cmds.select(cl = True)
constrainHierarchy()
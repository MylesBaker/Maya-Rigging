import maya.cmds as cmds

# points one object at another

selected = cmds.ls(sl=True)

cmds.aimConstraint(selected[0], selected[1])
cmds.aimConstraint(selected[0], selected[1], rm=1)
print(f"Aimed {selected[1]} at {selected[0]}")
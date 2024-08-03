import maya.cmds as cmds

# Makes selected joints visible

selected = cmds.ls(sl=True)

for x in selected:
    cmds.setAttr(f"{x}.drawStyle", 0)
    print(f"Unhidden joint {x}")
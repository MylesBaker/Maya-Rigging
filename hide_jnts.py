import maya.cmds as cmds

# Makes selected joints invisible

selected = cmds.ls(sl=True)

for x in selected:
    cmds.setAttr(f"{x}.drawStyle", 2)
    print(f"Hidden joint {x}")
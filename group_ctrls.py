import maya.cmds as cmds

# select all of your controls that you have positioned and then run this code
# This groups every control into it's own group

ctrls = []
grps = []
ctrls.clear()
grps.clear()

for x in cmds.ls(sl=True):
    cmds.select(d=True)
    ctrls.append(x)
    print(f"added {x}")
print(ctrls)

for x in ctrls:
    cmds.select(d=True)
    cmds.group(em=True, name=f"grp_{x}")
    grps.append(f"grp_{x}")
    print(f"created grp_{x}")
print(grps)

for x,y in zip(ctrls,grps):
    cmds.copyAttr(x,y, values=True, at=["t","r"])
    print(f"copied {x} attributes to {y}")
    cmds.parent(x,y)
    print(f"parented {x} to {y}")
print("attributes copied")
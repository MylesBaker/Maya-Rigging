import maya.cmds as cmds

# Quick FK setup for basic rigs
# Need to include a scaling system at some point

sl = cmds.ls(sl=1)

for x in sl:
    ctrlName = x.replace(x, f"ctrl_{x}")
    ctrl = cmds.circle( nr=(1, 0, 0), r=1,  n=ctrlName)[0]
    group = cmds.group(ctrl, n=ctrl + "_auto")
    offset = cmds.group(group, n=ctrl + "_offset")
    cmds.parentConstraint(x, offset, mo=0)
    cmds.delete(cmds.parentConstraint(x, offset))
    cmds.parentConstraint(ctrl, x, mo=0)
    cmds.select(d=True)
    cmds.select(f"ctrl_{x}")
    cmds.parent(w=1)
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
    cmds.select(d=True)
    cmds.select(f"{x}_offset")
    cmds.delete()
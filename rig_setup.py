import maya.cmds as cmds

# Basic rig folder setup, delete as needed

names = ["geo","locators","joints","rig_joints","IK_joints","FK_joints","IK_ribbons","ribbon_follicles","IK_ribbon_joints","ribbon_ctrl_joints","ribbon_deformers","skin_joints","controls","IK_ctrl","IK_arm_L","IK_leg_L","IK_arm_R","IK_leg_R","FK_ctrl","use_group_script","ctrl_misc","ikHandles"]

cmds.group(em=1, name="asset_NAME")

for x in names:
    print(f"creating grp_{x}")
    cmds.group(em=1, name=f"grp_{x}")

cmds.parent("grp_ribbon_ctrl_joints","grp_IK_ribbon_joints")
cmds.parent("grp_ribbon_follicles","grp_IK_ribbons")
cmds.parent("grp_IK_ribbon_joints","grp_IK_ribbons")
cmds.parent("grp_ribbon_deformers","grp_IK_ribbons")
cmds.parent("grp_IK_arm_L","grp_IK_ctrl")
cmds.parent("grp_IK_leg_L","grp_IK_ctrl")
cmds.parent("grp_IK_arm_R","grp_IK_ctrl")
cmds.parent("grp_IK_leg_R","grp_IK_ctrl")
cmds.parent("grp_use_group_script","grp_FK_ctrl")
cmds.parent("grp_IK_ctrl","grp_controls")
cmds.parent("grp_FK_ctrl","grp_controls")
cmds.parent("grp_ctrl_misc","grp_controls")
cmds.parent("grp_ikHandles","grp_controls")

cmds.parent("grp_rig_joints","grp_joints")
cmds.parent("grp_IK_joints","grp_joints")
cmds.parent("grp_FK_joints","grp_joints")
cmds.parent("grp_IK_ribbons","grp_joints")
cmds.parent("grp_skin_joints","grp_joints")

cmds.parent("grp_geo","asset_NAME")
cmds.parent("grp_locators","asset_NAME")
cmds.parent("grp_joints","asset_NAME")
cmds.parent("grp_controls","asset_NAME")
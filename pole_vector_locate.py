import pymel.core as pm

# credit goes to Lester Banks for this script
# select three objects from root to tip and then run this script
# calculates the pole vector position and places a locator there

def get_pole_vector_position(joint_1, joint_2, joint_3, multiplier=1.0):
    # http://lesterbanks.com/2013/05/calculating-the-position-of-a-pole-vector-in-maya-using-python/
    a = joint_1.getTranslation(space="world")
    b = joint_2.getTranslation(space="world")
    c = joint_3.getTranslation(space="world")

    start_to_end = c - a
    start_to_mid = b - a

    dot = start_to_mid * start_to_end

    projection = float(dot) / float(start_to_end.length())

    start_to_end_normalized = start_to_end.normal()

    projection_vector = start_to_end_normalized * projection

    arrow_vector = start_to_mid - projection_vector
    arrow_vector *= multiplier

    pole_vector_position = arrow_vector + b

    return pole_vector_position

joint_1, joint_2, joint_3 = pm.selected()

locator = pm.spaceLocator()
locator.setTranslation(get_pole_vector_position(joint_1, joint_2, joint_3), space="world")
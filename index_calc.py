
def sm_calc(height):
    sm_height = height/100
    return sm_height;

def met_calc(height):
    sm_height = height*100
    return sm_height;

# Calculation of Body Mass Index
# WARN: Banker's rounding
def calc_bmi(height,weight):
    bmi=round(weight/height**2,2)
    return bmi;


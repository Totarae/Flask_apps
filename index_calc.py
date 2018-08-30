
def sm_calc(height):
    sm_height = height/100
    return sm_height;

def met_calc(height):
    sm_height = height*100
    return sm_height;

# Calculation of Body Mass Index
# WARN: Banker's rounding
def calc_bmi(height,weight):
    try:
        bmi=round(int(weight)/(int(height)/100)**2,2)
        return bmi
    except ZeroDivisionError:
        return 0

def calc_broc(height):
    if (int(height)>150) and (int(height)<170):
        broc=(int(height)-100)+0.1
        return broc
    else:
        return 0

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
# Broc index
# Normal weight depends on height
def calc_broc(height):
    if (int(height)>150) and (int(height)<170):
        broc=(int(height)-100)+0.1
        return broc
    else:
        return 0
# Breight index
# Normal weight depends on height
def calc_breit(height):
    weight=height*0.7-50
    return weight
#Deventrope index
def calc_dave(height,weight):
    dave=round(int(weight)*1000/(int(height))**2,2)
    return dave
#Noord index
# Normal weight depends on height
def calc_noord(height,weight):
    noord=(int(height)*420)/1000
    return noord
#Tatoon index
# Normal weight depends on height
def calc_tatoon(height,weight):
    tatoon=int(height)-(100+(int(height)-100/20))
    return tatoon
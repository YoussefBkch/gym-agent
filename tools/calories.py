


def calculate_calories(weight,height,age,gender,activity_case,goal_case,is_metric=True):
    if not is_metric:
        weight= weight*0.453592
        height=height*2.54
    BMR=0
    if gender.lower() not in ["male","female"]:
        raise ValueError("Gender must be female or male")
    #calculate the BMR first
    if gender.lower() == "male":
        BMR= (weight*10)+(6.25*height)-(5*age)+5
    elif gender.lower()=="female":
        BMR= (weight*10)+(6.25*height)-(5*age)-161
    #Choose the case of activity multipliers and calculate the BMR based on it
    match activity_case.lower():
        case "sedentary":
            BMR=BMR*1.2
        case "lightly active":
            BMR=BMR*1.375
        case "moderately active":
            BMR=BMR*1.55
        case "very Active":
            BMR=BMR*1.725
        case _:
            raise ValueError("Please choose a valid Activity")
    #now to choose either the goal adjustment is loss 
    TDEE=BMR
    match goal_case.lower():
        case "maintenance":
            return TDEE
        case "weight loss":
            return TDEE*0.90
        case "aggressive weight loss":
            return TDEE*0.80
        case "muscle gain":
            return TDEE*1.10
        case _:
            raise ValueError("Please choose a valid goal adjustment")
        

def calculate_macros(weight,TDEE,is_metric=True):
    if not is_metric:
        weight= weight*0.453592
    Protein=1.8*weight#per g
    Fat_in_cal=0.25*TDEE
    Fat=Fat_in_cal/9
    Carbs=(TDEE-Fat_in_cal-(Protein*4))/4
    return round(Protein,2),round(Fat,2),round(Carbs,2)
        

TDEE=calculate_calories(100,180,24,"male","sedentary","maintenance",True)
Pro,fat,car=calculate_macros(100,TDEE,True)
print(f"TDEE = {TDEE} protein={Pro} Fat={fat}  Carbs= {car} ")








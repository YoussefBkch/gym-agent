import json

def search_exercises(muscle_group=None, difficulty=None, equipment=None):
    with open("data/exercises.json","r") as f:
        data =json.load(f)
        if muscle_group and difficulty and equipment :
            all_exercises=[]
            for group in data.values():
                return all_exercises.extend(group)

        groupmus=["chest","back","core","legs","arms","shoulders"]
        diff=["intermediate","advenced","beginner"]
        equi=set()
        for value in data.items():
            for key,val in value.items():
                if key=="equipment":
                    equi.add(val)
        gymequi={item.lower() for item in equi}
        if len(muscle_group)>1 and muscle_group.lower() not in ["chest","back","core","legs","arms","shoulders"]:
            raise ValueError("Please check that the muscle group is in",groupmus)
        if len(difficulty)>1 and difficulty not in diff:
            raise ValueError("Please check that the difficulty is in ",diff)
        if muscle_group.lower() in groupmus and difficulty and equipment:
            muscle_exr=[]
            for key1,val1 in data.items():
                if key1 == muscle_group:
                    return muscle_exr.extend(val1)
        if muscle_group.lower() in groupmus and difficulty in diff and equipment:
            muscle_diff_ex=[]
            for key2,val2 in data.items():
                for key3 in val2.items():
                    if key2==muscle_group and key3==difficulty:
                        return muscle_diff_ex.extend(val2)
        if muscle_group.lower() in groupmus and difficulty in diff and equipment in gymequi:
            all=[]
            for k,v in data.items():
                for kk,
        
        
        
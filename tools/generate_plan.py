from tools.exercises import search_exercises

def generate_plan(goal, fitness_level, days_per_week, available_equipment=None):
    # 1. Input Validation
    valid_goals = ["muscle gain", "fat loss", "strength", "endurance"]
    valid_levels = ["beginner", "intermediate", "advanced"]
    
    clean_goal = goal.lower().strip()
    clean_level = fitness_level.lower().strip()

    if clean_goal not in valid_goals:
        raise ValueError(f"Invalid goal '{goal}'. Must be one of: {', '.join(valid_goals)}")
    
    if clean_level not in valid_levels:
        raise ValueError(f"Invalid fitness level '{fitness_level}'. Must be: {', '.join(valid_levels)}")

    if not (1 <= days_per_week <= 7):
        raise ValueError("Days per week must be between 1 and 7.")

    # THE BUG FIX: Ensure equipment is a list, not a string
    if available_equipment is not None and not isinstance(available_equipment, list):
        raise ValueError(
            f"available_equipment must be a LIST of strings (e.g. ['{available_equipment}']), "
            f"not a single string."
        )

    # 2. Define Volume based on Goal
    prescriptions = {
        "muscle gain": {"sets": 4, "reps": "8-12"},
        "fat loss": {"sets": 3, "reps": "15-20"},
        "strength": {"sets": 5, "reps": "3-5"},
        "endurance": {"sets": 3, "reps": "20+"}
    }
    style = prescriptions[clean_goal]

    # 3. The Split Logic
    all_muscle_groups = ["chest", "back", "legs", "core", "arms", "shoulders"]
    
    # Determine how many groups to hit per day to ensure recovery
    if days_per_week == 1:
        groups_per_day = 6 # Full Body
    elif days_per_week <= 3:
        groups_per_day = 3 # 2-day or 3-day split
    else:
        groups_per_day = 2 # 4+ day split

    weekly_plan = {}

    for i in range(days_per_week):
        day_label = f"Day {i+1}"
        daily_routine = []
        
        # Calculate rotating start index for muscle groups
        start_index = (i * groups_per_day) % len(all_muscle_groups)
        
        todays_groups = [
            all_muscle_groups[(start_index + j) % len(all_muscle_groups)] 
            for j in range(groups_per_day)
        ]

        for muscle in todays_groups:
            # Call our search tool
            pool = search_exercises(muscle_group=muscle, difficulty=clean_level)
            
            # Filter by equipment
            if available_equipment:
                clean_user_equip = [e.lower().strip() for e in available_equipment]
                pool = [
                    ex for ex in pool 
                    if any(eq.lower().strip() in clean_user_equip for eq in ex["equipment"])
                ]
            
            if pool:
                # Pick an exercise, rotating if possible
                selected_ex = pool[i % len(pool)].copy()
                selected_ex["prescribed_sets"] = style["sets"]
                selected_ex["prescribed_reps"] = style["reps"]
                daily_routine.append(selected_ex)

        weekly_plan[day_label] = daily_routine

    return weekly_plan
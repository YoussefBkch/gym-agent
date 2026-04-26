import json
import os

def search_exercises(muscle_group=None, difficulty=None, equipment=None):
    # 1. Setup Path and Load Data
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, "..", "data", "exercises.json")

    with open(file_path, "r") as f:
        data = json.load(f)

    # 2. Validation: Catch invalid inputs before doing any heavy lifting
    valid_difficulties = ["beginner", "intermediate", "advanced"]
    
    if difficulty and difficulty.lower() not in valid_difficulties:
        raise ValueError(f"Invalid difficulty '{difficulty}'. Must be one of: {', '.join(valid_difficulties).title()}")

    if muscle_group and muscle_group.lower() not in data:
        raise ValueError(f"Invalid muscle group '{muscle_group}'. Available: {', '.join(data.keys())}")

    # 3. Handle muscle_group (Mechanic 3: Flattening)
    if muscle_group:
        # Just the list for that specific group
        exercises = data[muscle_group.lower()]
    else:
        # Flatten everything into one giant list
        exercises = []
        for group_list in data.values():
            exercises.extend(group_list)

    # 4. Filter by Difficulty
    if difficulty:
        exercises = [
            ex for ex in exercises 
            if ex["difficulty"].lower() == difficulty.lower()
        ]

    # 5. Filter by Equipment
    if equipment:
        # Normalize the input
        target_eq = equipment.lower().strip()
        # We check if target_eq exists in the list of equipment for that exercise
        exercises = [
            ex for ex in exercises 
            if any(target_eq == eq.lower().strip() for eq in ex["equipment"])
        ]

    return exercises
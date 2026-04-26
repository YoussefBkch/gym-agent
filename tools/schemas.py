calculate_macros_schema = {
    "name": "calculate_macros",
    "description": "Calculates the recommended daily macronutrient breakdown (protein, carbs, fat in grams) given a calorie target and fitness goal. Call this after calculate_calories to give the user a complete nutrition plan.",
    "parameters": {
        "type": "object",
        "properties": {
            "calories": {
                "type": "number",
                "description": "The user's daily calorie target."
            },
            "goal": {
                "type": "string",
                "enum": ["muscle gain", "fat loss", "strength", "endurance"],
                "description": "The user's fitness goal, determines the macro ratio split."
            }
        },
        "required": ["calories", "goal"]
    }
}
calculate_calories_schema = {
  "name": "calculate_calories",
  "description": "Calculates TDEE based on biometrics, activity, and goals.",
  "parameters": {
    "type": "object",
    "properties": {
      "weight": {
        "type": "number",
        "description": "The user's weight; use kilograms if is_metric is True, otherwise use pounds."
      },
      "height": {
        "type": "number",
        "description": "The user's height; use centimeters if is_metric is True, otherwise use inches."
      },
      "age": {
        "type": "integer",
        "description": "The user's age in years."
      },
      "gender": {
        "type": "string", 
        "enum": ["male", "female"],
        "description": "The biological sex used to determine the basal metabolic rate formula."
      },
      "activity_case": {
        "type": "string",
        "enum": ["sedentary", "lightly active", "moderately active", "very active"],
        "description": "The multiplier for daily activity level, ranging from little exercise to heavy activity."
      },
      "goal_case": {
        "type": "string",
        "enum": ["maintenance", "weight loss", "aggressive weight loss", "muscle gain"],
        "description": "The caloric adjustment based on the user's primary fitness objective."
      },
      "is_metric": {
        "type": "boolean",
        "default": True,
        "description": "Set to True for metric units (kg/cm) or False for imperial units (lbs/in)."
      }
    },
    "required": ["weight", "height", "age", "gender", "activity_case", "goal_case"]
  }
}
search_exercises_schema = {
  "name": "search_exercises",
  "description": "Searches the exercise database with optional filters.",
  "parameters": {
    "type": "object",
    "properties": {
      "muscle_group": {
        "type": "string",
        "enum": ["chest", "back", "legs", "core", "arms", "shoulders"]
      },
      "difficulty": {
        "type": "string",
        "enum": ["beginner", "intermediate", "advanced"]
      },
      "equipment": {
        "type": "string",
        "description": "A single piece of equipment (e.g., 'dumbbell')."
      }
    }
  }
}
generate_plan_schema = {
  "name": "generate_plan",
  "description": "Generates a multi-day workout split with sets and reps.",
  "parameters": {
    "type": "object",
    "properties": {
      "goal": {
        "type": "string",
        "enum": ["muscle gain", "fat loss", "strength", "endurance"]
      },
      "fitness_level": {
        "type": "string",
        "enum": ["beginner", "intermediate", "advanced"]
      },
      "days_per_week": {
        "type": "integer",
        "minimum": 1,
        "maximum": 7
      },
      "available_equipment": {
        "type": "array",
        "items": {"type": "string"}
      }
    },
    "required": ["goal", "fitness_level", "days_per_week"]
  }
}
TOOLS = [
    {
        "function_declarations": [
            calculate_calories_schema,
            calculate_macros_schema,
            search_exercises_schema,
            generate_plan_schema
        ]
    }
]
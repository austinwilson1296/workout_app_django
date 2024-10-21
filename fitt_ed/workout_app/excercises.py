import random

gym_equipment = [
    'Treadmill',
    'Stationary Bike',
    'Dumbbells',
    'Barbell',
    'Kettlebell',
    'Leg Press Machine',
    'Rowing Machine',
    'Pull-up Bar',
    'Bench Press',
    'Squat Rack',
    'Smith Machine',
    'Resistance Bands',
    'Elliptical Trainer',
    'Cable Machine',
    'Dip Station',
    'Medicine Ball',
    'Battle Ropes',
    'Jump Rope',
    'Exercise Ball',
    'Plyo Box'
]

warm_ups = [
    "Dynamic Stretching",
    "Arm Circles",
    "Leg Swings",
    "Hip Circles",
    "High Knees",
    "Butt Kicks",
    "Jumping Jacks",
    "Lunges with a Twist",
    "Torso Twists",
    "Ankle Circles",
]
exercises = [
    "Squats",
    "Deadlifts",
    "Bench Press",
    "Overhead Press",
    "Bicep Curls",
    "Tricep Dips",
    "Lunges",
    "Pull-Ups",
    "Plank",
    "Burpees",
]
cooldowns = [
    "Static Stretching",
    "Child's Pose",
    "Seated Forward Bend",
    "Figure Four Stretch",
    "Cat-Cow Stretch",
    "Cobra Stretch",
    "Butterfly Stretch",
    "Pigeon Pose",
    "Hip Flexor Stretch",
    "Deep Breathing Exercises",
]


def generate_workout():
    selected_ex = random.sample(exercises, 6)   # Select 6 unique exercises
    selected_wu = random.sample(warm_ups, 6)     # Select 6 unique warm-ups
    selected_cd = random.sample(cooldowns, 6)  

    # Correctly create the context dictionary with string keys
    context = {
        'selected_ex': selected_ex,
        'selected_wu': selected_wu,
        'selected_cd': selected_cd,
    }
    return context
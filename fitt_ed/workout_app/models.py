from django.db import models

class CategoryLevels(models.TextChoices):
    BEGINNER1 = 'Beginner1', 'Beginner 1'
    BEGINNER2 = 'Beginner2', 'Beginner 2'
    FUNCTIONAL_ENDURANCE1 = 'Functional_Endurance1', 'Functional Endurance 1'
    FUNCTIONAL_ENDURANCE2 = 'Functional_Endurance2', 'Functional Endurance 2'
    FUNCTIONAL_ENDURANCE3 = 'Functional_Endurance3', 'Functional Endurance 3'
    STRENGTH = 'Strength', 'Strength'
    POWER = 'Power', 'Power'
    MED_BALL_CORE = 'Med_ball_core', 'Med Ball Core'
    MED_BALL_POWER = 'Med_ball_power', 'Med Ball Power'
    CORE_HIP_LEGS = 'Core_hip_legs', 'Core Hip/Legs'
    THORACIC_SPINE_MOBILITY = 'Thoracic_spine_mobility', 'Thoracic Spine Mobility'
    SCAPULAR_CLOSED_CHAIN = 'Scapular_closed_chain', 'Scapular Closed Chain'
    SCAPULAR_OPEN_CHAIN = 'Scapular_open_chain', 'Scapular Open Chain'
    SCAPULO_THORACIC = 'Scapulo_thoracic', 'Scapulo Thoracic'
    SCAPULO_THORACIC_HIP = 'Scapulo_thoracic_hip', 'Scapulo Thoracic Hip'
    ACTIVE_WRIST_MOBILIZATION = 'Active_wrist_mobilization', 'Active Wrist Mobilization'
    AGILITY_LADDER = 'Agility_ladder', 'Agility Ladder'
    CONE_DRILLS = 'Cone_drills', 'Cone Drills'
    GENERAL_STRENGTH = 'General_strength', 'General Strength'
    GENERAL_MOBILITY = 'General_mobility', 'General Mobility'
    KETTLEBELL_TRAINING = 'Kettlebell_training', 'Kettlebell Training'
    HOPS_AND_BOUNDS = 'Hops_and_bounds', 'Hops and Bounds'
    LOWER_LEG = 'Lower_leg', 'Lower Leg'
    LEG_STABLE = 'Leg_stable', '1 Leg Stable'
    LEG_STABLE_UNSTABLE = 'Leg_stable_unstable', '1 Leg Stable/2 Leg Unstable'
    LEG_UNSTABLE = 'Leg_unstable', '2 Leg Unstable/1 Leg Unstable'
    STABILIZATION_1 = 'Stabilization_1', 'Stabilization 1'
    STABILIZATION_2 = 'Stabilization_2', 'Stabilization 2'


class ExcerciseCategory(models.Model):
    name = models.CharField(max_length=255, unique=True)
    category = models.CharField(max_length=255, choices=CategoryLevels.choices)
    sub_category = models.CharField(max_length=255, blank=True)

class Excercise(models.Model):
    # Add your fields for exercises here, for example:
    name = models.CharField(max_length=255)
    category = models.ForeignKey(ExcerciseCategory, on_delete=models.CASCADE)

    
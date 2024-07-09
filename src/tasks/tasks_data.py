import json
from src.tasks.task import Task


class TasksData:
    def __init__(self):
        self.load()

    def load(self):
        training_challenges_path = 'resource/arc agi/training/arc-agi_training_challenges.json'
        training_solutions_path = 'resource/arc agi/training/arc-agi_training_solutions.json'

        with open(training_challenges_path, 'r') as f:
            training_challenges_raw = json.load(f)

        with open(training_solutions_path, 'r') as f:
            training_solutions_raw = json.load(f)

        self.training_challenges = []
        for key in training_challenges_raw:
            self.training_challenges.append(Task(training_challenges_raw[key], training_solutions_raw[key]))

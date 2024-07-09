class Task:
    def __init__(self, challenge, solution):
        self.challenge = challenge

        # Training Data
        self.train = []
        self.assign_train()

        # Test Data
        self.test = []
        self.assign_test()

        # Solution
        self.solution = solution

    def assign_test(self):
        for test in self.challenge['test']:
            input_data = test

            self.test.append(input_data)

    def assign_train(self):
        for pair in self.challenge['train']:
            input_data = pair['input']
            output_data = pair['output']

            self.train.append((input_data, output_data))

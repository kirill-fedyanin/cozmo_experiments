import numpy as np

class AlgoDecider:
    threshold = 75
    sum_threshold = 800

    def decide(self, reds):
        print("Max value", np.amax(reds))
        if np.amax(reds) < self.threshold:
            return 1
        else:
            columns = reds.sum(axis=0)
            max_column = np.argmax(columns)
            print("Max column", max_column)
            print("Max column value", np.amax(columns))

            if np.amax(columns) > self.sum_threshold:
                return 0
            elif max_column < 2:
                return 2
            elif max_column > 7:
                return 3
            else:
                return 4
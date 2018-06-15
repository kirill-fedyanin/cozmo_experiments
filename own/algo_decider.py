import numpy as np


class AlgoDecider:
    threshold = 90
    sum_threshold = 800
    max_size = 9

    def decide(self, reds):
        reds = self._extend_points(reds)
        print(reds)
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
            elif max_column < 3:
                return 2
            elif max_column > 7:
                return 3
            else:
                return 4

    def _extend_points(self, reds):
        extended = np.copy(reds)
        for index, element in np.ndenumerate(extended):
            i = index[0]
            j = index[1]
            extended[i, j] = (2 * element
                              + reds[self._bound(i - 1), j]
                              + reds[self._bound(i + 1), j]
                              + reds[i, self._bound(j - 1)]
                              + reds[i, self._bound(j + 1)]) // 6

        return extended

    def _bound(self, i):
        if i < 0:
            return 0
        elif i > self.max_size:
            return self.max_size
        else:
            return i

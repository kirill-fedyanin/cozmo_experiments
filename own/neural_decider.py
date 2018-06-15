import pickle
import numpy as np


class NeuralDecider:
    def __init__(self):
        with open('net.pickle', 'rb') as f:
            self.cgnet = pickle.load(f)

    def decide(self, reds):
        return self._to_num(self.cgnet.predict(reds).round(1))

    def _to_num(self, array_):
        return np.argmax(array_)


if __name__ == '__main__':
    list_ = [1] * 100
    x_test = np.array(list_)
    print(NeuralDecider().decide(x_test))


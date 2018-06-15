import pickle

from neupy import algorithms, layers, plots, environment, storage
from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from neupy.estimators import rmsle

import numpy as np


class Teacher:
    def __init__(self):
        self.datafile = open("action_data.txt", "r")

    def _prepare_target(self, target):
        return [self._flat(int(num)) for num in target]

    def _flat(self, num, size=5):
        base = [0] * size
        base[num] = 1
        return np.array(base)

    def _prepare_data(self, data):
        result = [self._to_int(item.split()) for item in data]
        return np.array(result)

    def _to_int(self, list_):
        return [int(item) for item in list_]


    def go(self):
        raw = self.datafile.read().splitlines()

        data = self._prepare_data(raw[::2])
        target = self._prepare_target(raw[1::2])
        print(len(data))
        print(len(target))

        environment.reproducible()

        x_train, x_test, y_train, y_test = train_test_split(
            data, target, train_size=0.85
        )

        print(x_train[0])

        cgnet = algorithms.ConjugateGradient(
            connection=[
                layers.Input(100),
                layers.Sigmoid(50),
                layers.Sigmoid(5),
            ],
            search_method='golden',
            show_epoch=25,
            verbose=True,
            addons=[algorithms.LinearSearch],
        )


        cgnet.train(x_train, y_train, x_test, y_test, epochs=100)
        plots.error_plot(cgnet)

        y_predict = cgnet.predict(x_test).round(1)
        error = rmsle(y_test, y_predict)
        print(error)

        with open('net.pickle', 'wb') as f:
            pickle.dump(cgnet, f)





if __name__ == '__main__':
    Teacher().go()

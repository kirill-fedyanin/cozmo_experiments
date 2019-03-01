
from neupy import algorithms, layers, plots
from sklearn import datasets, preprocessing
from sklearn.model_selection import train_test_split
from neupy import environment
from neupy.estimators import rmsle


class Teacher:
    def __init__(self):
        pass

    def go(self):
        dataset = datasets.load_boston()
        data, target = dataset.data, dataset.target

        data_scaler = preprocessing.MinMaxScaler()
        target_scaler = preprocessing.MinMaxScaler()

        data = data_scaler.fit_transform(data)
        target = target_scaler.fit_transform(target.reshape(-1, 1))

        environment.reproducible()

        x_train, x_test, y_train, y_test = train_test_split(
            data, target, train_size=0.85
        )

if __name__ == '__main__':
    Teacher().go()

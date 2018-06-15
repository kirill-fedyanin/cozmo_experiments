
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
        print(x_train[0])
        print(type(x_train))

        # cgnet = algorithms.ConjugateGradient(
        #     connection=[
        #         layers.Input(13),
        #         layers.Sigmoid(50),
        #         layers.Sigmoid(1),
        #     ],
        #     search_method='golden',
        #     show_epoch=25,
        #     verbose=True,
        #     addons=[algorithms.LinearSearch],
        # )
        #
        # cgnet.train(x_train, y_train, x_test, y_test, epochs=100)
        # plots.error_plot(cgnet)
        #
        # y_predict = cgnet.predict(x_test).round(1)
        # error = rmsle(target_scaler.inverse_transform(y_test),
        #               target_scaler.inverse_transform(y_predict))
        # print(error)


if __name__ == '__main__':
    Teacher().go()

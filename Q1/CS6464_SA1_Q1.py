import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plotter

data_sa1 = open('/home/prateep/Documents/Courses/CS6464/CS6464/Q1/Q1_data_02.csv', 'rb')
reader = csv.reader(data_sa1)

def format_data(reader_object, size):

    data = [[] for _ in range(size)]
    rownum = 0
    for row in reader_object:
        if rownum == 0:
            header = row
        else:
            colnum = 0
            for col in row:
                if colnum == 0:
                    header = col
                else:
                    data[colnum - 1].append(col)
                colnum += 1
        rownum += 1

    data = np.array(data).astype(np.float)

    return data;

def get_correlation(data):

    dim = len(data)
    correlation = np.ndarray((dim, dim))
    for i in range(dim):
        for j in range(dim):
            corr = np.corrcoef(data[i], data[j])
            # print corr
            correlation[i][j] = corr[0][1]

    return correlation;

def regress(data):
    features = np.transpose(np.asmatrix(data[:len(data) - 1]))
    clf = linear_model.LinearRegression()
    clf.fit(features, data[len(data) - 1])
    mse = np.mean((clf.predict(features) - data[len(data) - 1]) ** 2)
    return [clf, mse];

data = format_data(reader, 4)
correlation = get_correlation(data)
print("\nCorrelation = ")
print correlation
regressor = regress(data)
print("\nCoefficients = ")
print regressor[0].coef_
print("\nMSE = %f" % regressor[1])





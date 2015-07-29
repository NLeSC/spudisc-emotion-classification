#!/usr/bin/python
#
# Splits data into training and test sets by using a randomized search through
# all possible splits with a given training size.

from __future__ import print_function

from glob import glob
from itertools import chain

import numpy as np
from scipy.linalg import norm

from sklearn.cross_validation import ShuffleSplit
from sklearn.preprocessing import MultiLabelBinarizer


data = [ln.rsplit(None, 1)
        for ln in chain.from_iterable(open(f) for f in glob('*.senttag'))]
X, Y = zip(*data)
X = np.asarray(X, dtype=object)

Y = [set(s.split('_')) - {'None'} for s in Y]

# Map disgust-contempt (only six samples!) to anger
for y in Y:
    if 'Disgust-Contempt' in y:
        y.remove('Disgust-Contempt')
        y.add('Anger')

mlb = MultiLabelBinarizer()
Y = mlb.fit_transform(Y)

print("Classes:\n", mlb.classes_)
print("Frequencies:\n", Y.sum(axis=0))
print("Relative:\n", Y.mean(axis=0) * 100)


target = Y.mean(axis=0)

best = None
best_norm = np.inf

for train_ind, test_ind in ShuffleSplit(Y.shape[0], test_size=.2,
                                        n_iter=200000):
    Y_test = Y[test_ind]
    dist_test = norm(Y_test.mean(axis=0) - target)
    if dist_test < best_norm:
        best = train_ind, test_ind
        best_norm = dist_test


print("Test frequencies:\n", Y[test_ind].sum(axis=0))
print("Relative:\n", Y[test_ind].mean(axis=0) * 100)


with open('train.txt', 'w') as f:
    for x, y in zip(X[train_ind], Y[train_ind]):
        print(x,
              '_'.join(mlb.inverse_transform(y.reshape(1, -1))[0]) or 'None',
              file=f)

with open('test.txt', 'w') as f:
    for x, y in zip(X[test_ind], Y[test_ind]):
        print(x,
              '_'.join(mlb.inverse_transform(y.reshape(1, -1))[0]) or 'None',
              file=f)

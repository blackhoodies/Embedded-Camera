import numpy as np
from sklearn import svm
import pickle

normal = np.loadtxt("normal_1.txt")
fall = np.loadtxt("fall_1.txt")

X_train = np.vstack((normal[0:60,:], fall))
Y_train = np.ones((normal[0:60,:].shape[0],1))
Y_train = np.vstack((Y_train, np.zeros((fall.shape[0],1)))).ravel()
#print(normal.shape)
#print(fall.shape)
#print(Y_train.shape)
#print(X_train.shape)
clf = svm.SVC(kernel='linear', gamma='scale',class_weight='balanced')
clf.fit(X_train, Y_train)
pickle.dump(clf, open('model.sav', 'wb'))

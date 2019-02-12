'''
Use this file to generate training models on NCSU's ARC cluster
Note that grid search for finding the optimal hyperparameter configurations is done in the ipython notebook

'''


from osgeo import gdal
import ogr
import numpy as np
import fiona
import xgboost
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neural_network import MLPClassifier
from sklearn.ensemble import AdaBoostClassifier
import pickle

# Set seed
np.random.seed(100)

# Read files 
trainX = np.load('/home/kgadira/data/final-px-tr-6-Xa')
trainY = np.load('/home/kgadira/data/final-px-tr-6-Ya')
testX = np.load('/home/kgadira/data/final-px-te-6-Xa')
testY = np.load('/home/kgadira/data/final-px-te-6-Ya')

trainY = trainY.ravel()
testY = testY.ravel()
print trainX.shape, trainY.shape, testX.shape, testY.shape



#trainX = np.nan_to_num(trainX)
#testX = np.nan_to_num(testX)

xgb = xgboost.XGBClassifier(max_depth=1000, n_estimators=1000, nthread=8, objective='multi:softmax', learning_rate = 0.2 )

xgb.fit(trainX,trainY)
result = xgb.predict(testX)
acc = accuracy_score(testY, result)
cm = confusion_matrix(testY, result)
cr = classification_report(testY,result, target_names=['S1','S2','S3','S4','F','O'])
print 'Overall accuracy = {}\n'.format(acc)
#print 'Slum accuracy = {}\n'.format(cm[0,0]/np.sum(cm[0,:]))
print 'Confusion Matrix \n {}\n'.format(cm)
print 'Classification Report \n {}\n'.format(cr)

fname = './final-L3-xgboost-model.sav'
pickle.dump(xgb, open(fname, 'wb'))


rf = RandomForestClassifier(criterion='entropy',n_estimators=1000,min_samples_split = 2, max_depth = None, n_jobs=-1, bootstrap = False, min_samples_leaf = 1)
rf.fit(trainX,trainY)
result = rf.predict(testX)
acc = accuracy_score(testY, result)
cm = confusion_matrix(testY, result)
cr = classification_report(testY,result, target_names=['S1','S2','S3','S4','F','O'])
print 'Overall accuracy = {}\n'.format(acc)
#print 'Slum accuracy = {}\n'.format(cm[0,0]/np.sum(cm[0,:]))
print 'Confusion Matrix \n {}\n'.format(cm)
print 'Classification Report \n {}\n'.format(cr)

fname = './final-L3-rf-model.sav'
pickle.dump(rf, open(fname, 'wb'))


nb = GaussianNB()
nb.fit(trainX,trainY)
result = nb.predict(testX)
acc = accuracy_score(testY, result)
cm = confusion_matrix(testY, result)
cr = classification_report(testY,result, target_names=['S1','S2','S3','S4','F','O'])
print 'Overall accuracy = {}\n'.format(acc)
print 'Confusion Matrix \n {}\n'.format(cm)
print 'Classification Report \n {}\n'.format(cr)

fname = './final-L3-gnb-model.sav'
pickle.dump(nb, open(fname, 'wb'))


dt = DecisionTreeClassifier(random_state=100)
dt.fit(trainX,trainY)
result = dt.predict(testX)
acc = accuracy_score(testY, result)
cm = confusion_matrix(testY, result)
cr = classification_report(testY,result, target_names=['S1','S2','S3','S4','F','O'])
print 'Overall accuracy = {}\n'.format(acc)
#print 'Slum accuracy = {}\n'.format(cm[0,0]/np.sum(cm[0,:]))
print 'Confusion Matrix \n {}\n'.format(cm)
print 'Classification Report \n {}\n'.format(cr)

fname = './final-L3-dt-model.sav'
pickle.dump(dt, open(fname, 'wb'))

knn = KNeighborsClassifier(10)
knn.fit(trainX, trainY)
result= knn.predict(testX)
acc = accuracy_score(testY, result)
cm = confusion_matrix(testY, result)
cr = classification_report(testY,result, target_names=['S1','S2','S3','S4','F','O'])
print 'Overall accuracy = {}\n'.format(acc)
#print 'Slum accuracy = {}\n'.format(cm[0,0]/np.sum(cm[0,:]))
print 'Confusion Matrix \n {}\n'.format(cm)
print 'Classification Report \n {}\n'.format(cr)

fname = './final-L3-knn-model.sav'
pickle.dump(knn, open(fname, 'wb'))


mlp = MLPClassifier(hidden_layer_sizes = (100,100,100,100,100), activation = 'logistic', learning_rate = 'adaptive', alpha = 0.00001)
mlp.fit(trainX, trainY)
result = mlp.predict(testX)
acc = accuracy_score(testY, result)
cm = confusion_matrix(testY, result)
cr = classification_report(testY,result, target_names=['S1','S2','S3','S4','F','O'])
print 'Overall accuracy = {}\n'.format(acc)
#print 'Slum accuracy = {}\n'.format(cm[0,0]/np.sum(cm[0,:]))
print 'Confusion Matrix \n {}\n'.format(cm)
print 'Classification Report \n {}\n'.format(cr)

fname = './final-L3-mlp-model.sav'
pickle.dump(mlp, open(fname, 'wb'))

adb = AdaBoostClassifier(n_estimators = 100,learning_rate = 0.007)
adb.fit(trainX, trainY)
result = adb.predict(testX)
acc = accuracy_score(testY, result)
cm = confusion_matrix(testY, result)
cr = classification_report(testY,result, target_names=['S1','S2','S3','S4','F','O'])
print 'Overall accuracy = {}\n'.format(acc)
#print 'Slum accuracy = {}\n'.format(cm[0,0]/np.sum(cm[0,:]))
print 'Confusion Matrix \n {}\n'.format(cm)
print 'Classification Report \n {}\n'.format(cr)

fname = './final-L3-adaboost-model.sav'
pickle.dump(adb, open(fname, 'wb'))


from sklearn.datasets import load_breast_cancer
from sklearn.datasets import load_diabetes
from sklearn import svm
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib as plt

dataset_cancer = load_breast_cancer()
print(dataset_cancer.features_names)
print(dataset_cancer.target_names)

dataser_diabets = load_diabetes()
print(dataser_diabets.features_names)
print(dataser_diabets.target_names)

X_train_can, X_test_can, y_train_can, y_test_can = train_test_split(dataset_cancer.data, dataset_cancer.target,stratify=dataset_cancer.target,random_state=42)
X_train_day, X_test_day, y_train_day, y_test_day = train_test_split(dataset_cancer.data, dataset_cancer.target,stratify=dataset_cancer.target,random_state=42)

training_accuracy = []
test_accuracy = []

kernels = ['linear','rbf','sigmoid']
for kernel in kernels:
    svm_model = svm.SVC(kernel=kernel)

    svm_model.fit(X_train_can,y_train_can)
    training_accuracy.append(svm_model.score(X_train_can,y_train_can))
    test_accuracy.append(svm_model.score(X_test_can,y_test_can))

plt.plot(kernels,training_accuracy,label='accuracy in training')
plt.plot(kernels,test_accuracy,label='accuracy in test')
plt.ylabel('accuracy')
plt.xlabel('kernels')
plt.legend()

training_accuracy = []
test_accuracy = []

prof_max = range(1,10)
for md in prof_max:
    tree = DecisionTreeClassifier(max_depth=md,random_state=0)
    tree.fit(X_train_can,y_train_can)
    training_accuracy.append(tree.score(X_train_can,y_train_can))
    test_accuracy.append(tree.score(X_test_can,y_test_can))

plt.plot(prof_max,training_accuracy,label='accuracy in training')
plt.plot(prof_max,test_accuracy,label='accuracy in test')
plt.ylabel('accuracy')
plt.xlabel('Max Deep')
plt.legend()

training_accuracy = []
test_accuracy = []

for interception in [True,False]:
    regr = LinearRegression(fit_intercept=interception)
    regr.fit(X_train_can,y_train_can)
    training_accuracy.append(regr.score(X_train_can,y_train_can))
    test_accuracy.append(regr.score(X_test_can,y_test_can))

plt.plot(['Interc','No Interc'],training_accuracy,label='accuracy in training')
plt.plot(['Interc','No Interc'],test_accuracy,label='accuracy in test')
plt.ylabel('accuracy')
plt.xlabel('Max Deep')
plt.legend()
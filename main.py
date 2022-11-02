"""
deodel - demo

    Module provides examplea of usage for the deodel module.
        Tested with Winpython64-3.10.5.0
"""

# >-----------------------------------------------------------------------------

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def AccuracyEval(x_data, y_target, classifier, iterations = 1, random_seed = None) :

    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    print("- - - - - - - - - ")
    print("- - - Prediction accuracy test")
    print()
    print("- - - - - - classifier:", classifier)
    print("- - - - - - iterations:", iterations)
    print("- - - - - - random_seed:", random_seed)
    print()
    
    test_fraction = 1.0/3
    cumulate_acc = 0

    crt_rand_seed = random_seed
    for crt_idx in range(iterations) :
        if not random_seed == None :
            crt_rand_seed = random_seed + crt_idx
        ret_tuple = train_test_split(x_data, y_target, test_size = test_fraction, random_state = crt_rand_seed)
        x_train, x_test, y_train, y_test = ret_tuple
        classifier.fit(x_train, y_train)
        predictions = classifier.predict(x_test)
        accuracy = accuracy_score(y_test, predictions)
        cumulate_acc += accuracy

    avg_accuracy = (cumulate_acc * 1.0) / iterations
    print("- - - - - - avg_accuracy:", avg_accuracy)
    print()
    return avg_accuracy

# >-----------------------------------------------------------------------------

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Trivial example
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("- - - - - - - - - ")
print("- - - - - - - - - ")
print("- - - Trivial example")
print()

X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
from deodel import DeodataDelangaClassifier
deodel = DeodataDelangaClassifier()
deodel.fit(X, y)
print(deodel.predict([[1.1]]))

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Example of using data formated as list of list tables. 
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("- - - - - - - - - ")
print("- - - - - - - - - ")
print("- - - Usage woth mixed attributes as lists of lists")
print()

import deodel

train_X = [ ['a',   1.01,   'az',   'e' ],
            ['b',   "3.01", 3,      'd' ], 
            ['d',   "4",    5,      'd' ], 
            ['b',   2,      3.0,    None], 
            ['c',   '3.01', 'az',   'e' ]]

train_y = [ 'TA',
            'TB',
            'TB',
            'TC',
            'TA' ]

query_entry = ['a',   0.9,   5.7,    'd']
query_test = [query_entry]

expected_result = ['TB']

classf = deodel.DeodataDelangaClassifier()
classf.fit(train_X, train_y)
query_predict = classf.predict(query_test)

print("- - - - query_predict:", query_predict)
print("- - - - expected_result:", expected_result)

set_eval = ( query_predict == expected_result )

if set_eval :
    print("- - -   test ok")
else :
    print("- - -  test failed")
    print("- - -  invalid test_result")
print()

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Example of using the deodel classifier in a similar way to
#   other sklearn classfiers.
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("- - - - - - - - - ")
print("- - - - - - - - - ")
print("- - - Usage with sklearn facilities")
print()

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn import neighbors
from sklearn import tree

import deodel

print("- - - - - - - - - ")
print()

data_set = datasets.load_wine()

x_data = data_set.data
y_target = data_set.target

x_train, x_test, y_train, y_test = train_test_split(x_data, y_target, test_size=0.5, random_state=42)

###
classifier = neighbors.KNeighborsClassifier()

print("- - - - - - - - - ")
print("- - - classifier:", classifier)
    
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print("- - - accuracy:", accuracy)
print()

###
classifier = tree.DecisionTreeClassifier()

print("- - - - - - - - - ")
print("- - - classifier:", classifier)
    
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print("- - - accuracy:", accuracy)
print()

###
classifier = deodel.DeodataDelangaClassifier()

print("- - - - - - - - - ")
print("- - - classifier:", classifier)
    
classifier.fit(x_train, y_train)
predictions = classifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)

print("- - - accuracy:", accuracy)
print()

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
#   Example for comparing the average accuracy for a set of 
#   classifiers on a toy data set
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("- - - - - - - - - ")
print("- - - - - - - - - ")
print("- - - Average accuracy test")
print()

import random

data_set = datasets.load_breast_cancer()
data_len = len(data_set.target)
print("- - - data_len:", data_len)
print()
x_data = data_set.data
y_target = data_set.target

iter_no = 50
random_seed = 42
random.seed(random_seed)

classifier_lst = [  neighbors.KNeighborsClassifier(),
                    tree.DecisionTreeClassifier(),
                    deodel.DeodataDelangaClassifier() ]

for crt_classif in classifier_lst : 
    accuracy = AccuracyEval(x_data, y_target, crt_classif, iterations=iter_no, random_seed=random_seed)

print("- - - - - - - - - ")

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print("- - - - - - - - - ")
print()

# >-----------------------------------------------------------------------------

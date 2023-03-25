"""
    Compare discretization/binning methods

        Tested with Winpython64-3.10.5.0
"""

#   c4pub@git 2023

import datetime
import random
import deodel
import usap_common

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def AvgAccuracyTest(x_data, y_target, classifier, iterations = 1, random_seed = None) :

    from sklearn.model_selection import train_test_split
    from sklearn.metrics import accuracy_score

    begin_time_ref = datetime.datetime.now()
    crt_time_ref = datetime.datetime.now()
    
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

    new_time_ref = datetime.datetime.now()
    delta = new_time_ref - crt_time_ref
    delta_secs = delta.total_seconds()
    crt_time_ref = new_time_ref

    avg_accuracy = (cumulate_acc * 1.0) / iterations
    return avg_accuracy

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def Run() :

    #""" # comment - begin
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    #   Comparing the average accuracy for a set of 
    #   classifiers on toy data sets
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    from sklearn import datasets
    from sklearn import neighbors
    from sklearn import tree

    data_set_lst = [    
                        datasets.load_iris(),
                        # datasets.load_diabetes(),
                        datasets.load_digits(),
                        # datasets.load_linnerud(),
                        datasets.load_breast_cancer(),
                        datasets.load_wine(),
                    ]

    classifier_lst = [  
                        # neighbors.KNeighborsClassifier(),
                        tree.DecisionTreeClassifier(),

                        deodel.DeodataDelangaClassifier({'split_no': 2, 'split_mode': 'eq_freq'}), 
                        deodel.DeodataDelangaClassifier({'split_no': 2, 'split_mode': 'eq_width'}), 

                        deodel.DeodataDelangaClassifier({'split_no': 3, 'split_mode': 'eq_freq'}), 
                        deodel.DeodataDelangaClassifier({'split_no': 3, 'split_mode': 'eq_width'}), 

                        deodel.DeodataDelangaClassifier({'split_no': 5, 'split_mode': 'eq_freq'}), 
                        deodel.DeodataDelangaClassifier({'split_no': 5, 'split_mode': 'eq_width'}), 

                        deodel.DeodataDelangaClassifier({'split_no': 10, 'split_mode': 'eq_freq'}), 
                        deodel.DeodataDelangaClassifier({'split_no': 10, 'split_mode': 'eq_width'}), 
                    ]

    # iter_no = 10
    iter_no = 50
    random_seed = 42
    random.seed(random_seed)
    print_tab_len = 20

    usap_common.iprnt("- - - - - - - - - ")
    usap_common.iprnt("- - - - - - - - - ")
    usap_common.iprnt("- - - - average accuracy test")
    usap_common.iprnt()
    usap_common.iprnt("- - - - iter_no:", iter_no)
    usap_common.iprnt("- - - - random_seed:", random_seed)
    usap_common.iprnt()

    for crt_data_set in data_set_lst : 
        if 'DESCR' in crt_data_set :
            desc_name = crt_data_set['DESCR']
            desc_name = desc_name[:10]
        else :
            desc_name = 'none'
        usap_common.iprnt()
        usap_common.iprnt("- - - - dataset:", desc_name)
        data_len = len(crt_data_set.target)
        usap_common.iprnt()
        x_data = crt_data_set.data
        y_target = crt_data_set.target
        line_str = usap_common.ListToTabStr(["avg accuracy", "classifier"], print_tab_len)
        usap_common.iprnt (line_str)
        usap_common.iprnt('-'*80)
        for crt_classif in classifier_lst : 
            accuracy = AvgAccuracyTest(x_data, y_target, crt_classif, iterations=iter_no, random_seed=random_seed)
            line_str = usap_common.ListToTabStr([accuracy, crt_classif], print_tab_len)
            usap_common.iprnt (line_str)
        usap_common.iprnt()
    usap_common.iprnt("- - - - - - - - - ")
    usap_common.iprnt("- - - - - - - - - ")
    #""" # comment - end

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

print()
print("- - - - - - - - - ")
print()

Run()

print()
print("- - - - - - - - - ")
print()

# >-----------------------------------------------------------------------------

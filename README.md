
# deodel


## Predictive Algorithm for Very Mixed Data

A predictive algorithm with a unique combination of features:

- supports multi-class target classification
- supports nominal and continuous attributes
- admits missing values in the training and query/test data
- admits mixed types, categorical and numerical, in the same attribute column
- performs classification intermixed with regression
- good accuracy

Deodel started as a python implementation of the "Deodata Delanga" classifier [1]. It has been extended to operate predictions on very heterogenous data. It supports attributes/features that are continuous, categorical, or a mix of both. Furthermore, this applies also to the target values. This means it can do classification, regression, or a mix of both within the context of the same training data. In regression mode, the algorithm implements the technique described in [2].

Its main characteristics are versatility, accuracy, and robustness.

The operation of the module is similar to that of standard classifiers from "sklearn". It accepts as input not only numpy and pandas data but also tables formatted as lists of lists.

The usage of list of lists enables operation with both numerical and categorical attributes. All attributes that are of type "int" or "float" will be categorized as numerical/continuous attributes. If the attribute is "None", it will be interpreted as "missing". All other types are viewed as discrete/nominal multi-valued attributes.
Note that even the mixing of categorical and numerical types for the same attribute is supported.

The target/outcome values can also be of any type, including a mix of categorical and numerical. By default, the module will determine automatically if the numerical values are categorical outcomes or if they represent continuous numerical ones. In the latter case, the entries will be considered for regression instead of classification.


### Very mixed example

To illustrate this "very mixed" ability consider this toy dataset:

              
    #                       ____ _____________ enjoyed party
    #                      /     _____________ age
    #                     /     /    _________ gender
    #                    /     /    /      ___ alcohol conc.
    #                   /     /    /      /      
    party_data = [  #  A  :  B  :  C  :  D       
                    [ 'n',  12,   'm',  'juice'  ],
                    [ 'y',  16,   'f',  'coffee' ],
                    [ 'y',  20,   'm',   0.06    ],
                    [ 'y',  21,   'f',   0.04    ],
                    [ 'n',  29,   'm',   0.39    ],
                 ]

Let's assume that the dataset represents data about a hypothetical party.
Column D, the alcohol concentration of the beverage consumed, is an example of a mix of categorical and numerical values.
If column A is used for prediction, it is a classification problem: did the participant enjoy the party knowing the age, gender, etc.?
If column D is used for prediction, it becomes a mixed regression/classification problem: what is the alcohol concentration of the beverage consumed? It could be a number (e.g., 0.05 for a beer) or could be a category of non-alcoholic beverage.
Deodel will generate a prediction in either case.


### How does deodel deals with mixed attributes?

The "Deodata Delanga" algorithm is a variation of the nearest neighbor type of supervised classifiers. It doesn't seek a fixed number of neighbors, but rather a nearest neighborhood with a variable number of neighbours. Unlike k-NN, that was used on data with continuous numerical attributes, the "Deodata Delanga" algorithm was intended to deal with discrete attributes; much like the ID3 decision tree. The deodel classifier can be viewed as a flattened/collapsed ID3 decision tree. Each branch of the flattened tree corresponds to a unique combination of attribute values, rather than just a single value, as is the case with conventional decision trees.

Deodel starts from a categorical data classiffier and adapts it to continuous/numerical attributes by discretizing them. So, unlike many other algorithms that convert discrete data into numerical ones (like one hot encoding), deodel discretizes the continuous data. Obviously, this entails a loss of information. However, this loss doesn't seem to be severe, and provides surprisingly good results in many settings.

Deodel is essentially non-parametric. However, there are configuration adjustments that can be tuned through an optional dictionary structure specified at initialization. The main adjustment is the number of bins used to discretize numerical attributes. By default, it is set to three. It is also possible to choose the discretization method: "equal-width" vs "equal-frequency". Also, the automatic usage of regression can be overridden.

In terms of accuracy, deodel performs well on datasets with heterogeneous features. On datasets with only categorical/nominal data, the algorithm exhibits accuracy convergence: it approaches the maximum achievable accuracy as more training data is provided.

Occasionally, deodel outperforms more established algorithms like RandomForest, GradientBoostingClassifier, MLPClassifier, etc., in terms of accuracy. An example can be seen [here](https://github.com/c4pub/misc/blob/main/notebooks/deodel_vs_sklearn_on_titanic.ipynb).

Deodel is coded in Python and is compact, fitting in one file/module.


## modules

  * deodel.py
    - It contains all that is needed for the operation of the classifier.

  * main.py
    - Module that serves as a starting point / launchpad for use applications.

  * usap_demo.py
    - Module that contains a demo of the classifier usage.

  * usap_common.py
    - Module that contains common code used by applications.

  * usap_utest.py
    - Module that implements a non-systematic set of sanity/unit tests.

  * usap_cmp_binning.py
    - Module that compares accuracy of the two modes of discretization: eq_freq vs eq_width.
    - Example at: [equal_width_vs_equal_frequency.ipynb](https://github.com/c4pub/misc/blob/main/notebooks/equal_width_vs_equal_frequency.ipynb)

  * usap_csv_eval.py
    - Module that evaluates the predictability of a csv dataset.
    - Example at: : [csv_dataset_eval.ipynb](https://github.com/c4pub/misc/blob/main/notebooks/csv_dataset_eval.ipynb)

---
##### [1] ["Collapsing the Decision Tree: the Concurrent Data Predictor"](https://doi.org/10.13140/RG.2.2.33413.06880)
##### [2] ["From Classification to Regression: A Note on Deodata Predictors"](https://doi.org/10.13140/RG.2.2.21740.03207)
---

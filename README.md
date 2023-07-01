
# deodel 

## Classifier with Good Accuracy and Support for Mixed Attributes

The deodel module provides a Python implementation for the "Deodata Delanga" classifier [1]. Its main characteristics are versatility, accuracy, and robustness.

The operation of the module is similar to standard classifiers from "sklearn". However, deodel accepts as input not only numpy and pandas data but also tables of data formatted as lists of lists.

The usage of list of lists enables operation with both numerical and categorical attributes. All attributes that are of type "int" or "float" will be categorized as numerical/continuous attributes. If the attribute is "None", it will be interpreted as "missing". All other types are viewed as discrete/nominal attributes.
Note that even the mixing of categorical and numerical types for the same attribute is supported.

The target/outcome can also be of any type but will be considered discrete, as deodel does classification and not regression.

The Deodata Delanga algorithm (deodel) is a variation of the nearest neighbor type of supervised classifiers. Unlike the standard k-NN that started as a classifier for data consisting of continuous numerical attributes, the "Deodata Delanga" algorithm was meant to deal with heterogeneous discrete attributes, much like the ID3 decision tree. The deodel classifier can be viewed as a flattened/collapsed ID3 decision tree.

Deodel is almost non-parametric. Obviously, there are configuration adjustments that can be tuned through an optional dictionary structure specified at initialization. The main adjustment is the number of bins used to discretize numerical attributes. By default, it is set to three. It is also possible to choose the discretization method: "equal-width" vs "equal-frequency".

In terms of accuracy, deodel should do well on datsets with heterogeneous features. On categorical/nominal only data, the algorithm exhibits accuracy convergence, it will aproach the maximum achievable accuracy as more training data is provided,

Occasionaly, deodel outdoes, in terms of accuracy, more established algorithms like RandomForest, GradientBoostingClassifier, MLPClassifier, SVC, etc. Such an example is presented in [here](https://github.com/c4pub/misc/blob/main/notebooks/deodel_vs_sklearn_on_titanic.ipynb).

The code is writen in python only. The classifier itself is compact, fits in one file/nodule.


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
---

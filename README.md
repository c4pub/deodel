# deodel 
## classifier with good accuracy and support for mixed attributes

The deodel module provides a Python implementation for the "Deodata Delanga" classifier [1]. Its main characteristics are versatility, accuracy and robustness.

The operation of the module is similar to standard classifiers from "sklearn". However, deodel accepts as input not only numpy data but also tables of data formatted as list of lists.

The usage of list of lists enables operation with both numerical and categorical attributes. All attributes that are of type "int" or "float" will be categorized as numerical/continuous attributes. If the attribute is "None" it will be interpreted as "missing". All other types are viewed as discrete/nominal attributes.
Note that even the mixing of categorical and numerical types for the same attribute is supported.

The target/outcome can also be of any type, but will be considered "discrete" as deodel does classification and not regression.

The Deodata Delanga algorithm (deodel) is a variation of the nearest neighbor type of supervised classifiers. Unlike the standard k-NN that started as a classifier for data consisting of continuous numerical attributes, the "Deodata Delanga" algorithm was meant to deal with heterogeneous discrete attributes; much like the ID3 decision tree. The deodel classifier can be viewed as a flattened/collapsed ID3 decision tree. 

Deodel is almost non-parametric. Obviously, there are configuration adjustments that can be tuned through an optional dictionary structure specified at initialization. The main adjustment is the number of bins used to discretize numerical attributes. There is also By default it is set to three. It is also possible to choose the discretization method: "equal-width" vs "equal-frequency'. 

## modules

    deodel.py
        It contains all it is needed for the operation of the classifier.

    main.py
        Module that serves as starting point / launchpad for use applications.

    usap_demo.py
        Module that contains a demo of the classifier usage.

    usap_common.py
        Module that contains common code used by applications.

    usap_utest.py
        Module that implements a non-systematic set of sanity/unit tests.

    usap_cmp_binning.py
        Module that compares accuracy of the two modes of discretization: eq_freq vs eq_width.

    usap_csv_eval.py
        Module that evaluates the predictability of a csv dataset.

---

##### [1] ["Collapsing the Decision Tree: the Concurrent Data Predictor"](https://doi.org/10.13140/RG.2.2.33413.06880)
 
---

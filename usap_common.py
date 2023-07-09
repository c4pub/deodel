"""
    Misc utility common module

        Tested with Winpython64-3.10.5.0
"""

#   c4pub@git 2023
#
# Latest version available at: https://github.com/c4pub/deodel
#

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def iprnt( *args, **kwargs ) :
    """ Non delayed prints """

    import sys

    ret_item = print( *args, **kwargs )
    sys.stdout.flush()
    sys.stderr.flush()

    return ret_item

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def SepLine ( display_flag = True ) :
    separator_string = ">-" + 78*"-"
    iprnt ( separator_string )

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def CrtTimeStamp(display_flag = True) :
    import datetime

    in_time_stamp = datetime.datetime.now()
    time_str = in_time_stamp.strftime("%Y-%m-%d %H:%M:%S")
    out_str = "time_stamp: %s" % (time_str)
    if display_flag :
        print(out_str)
    return out_str

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def ListToTabStr(in_data_list, in_tab_list = 8) :
    more_char = '>'
    space_char = ' '
    list_len = len(in_data_list)
    if not isinstance(in_tab_list, list) :
        use_tab_list = [in_tab_list] * (list_len)
    else :
        use_tab_list = in_tab_list
    total_str = ""
    for crt_idx in range(list_len - 1) :
        crt_elem = in_data_list[crt_idx]
        crt_tab = use_tab_list[crt_idx]
        data_width = crt_tab - 1
        crt_str = str(crt_elem)
        str_len = len(crt_str)
        if str_len == 0 :
            transf_str = (space_char)*(data_width)
        elif str_len > data_width :
            transf_str = crt_str[:(data_width - 1)] + more_char
        else :
            transf_str = crt_str + space_char * (data_width - str_len)
        total_str += (transf_str + space_char)
    # last column element can be any length
    transf_str = str(in_data_list[-1])
    total_str += (transf_str + space_char)
    return total_str

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def HashString(in_str = "") :
    total_sum = 0
    str_len = len(in_str)
    for crt_idx in range(str_len) :
        crt_elem = in_str[crt_idx]
        total_sum += (ord(crt_elem))
        total_sum ^= (crt_idx + 1)
    return total_sum

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def HashValue(in_param = None) :
    total_sum = 0
    param_str = str(in_param)
    param_str += str(type(in_param))
    hash_num = HashString(param_str)
    return hash_num

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > RandBaselinePredictor - Begin
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class RandBaselinePredictor:
    """Random baseline predictor.

    Randomly chooses a prediction from the training outputs.

    Parameters
    ----------
    aux_param : dict, default=None
        Auxiliary configuration parameters.
        Configuration dictionary keywords:
            'rand_seed' : int, default=None
                Random seed. If "None" no seed initialization

    Attributes
    ----------
    version : float
        Version of algorithm implementation

    Notes
    -----
    Can be used for both classification or regression.

    Examples
    --------
    >>> X = [[0], [1], [2], [3]]
    >>> y = [0.5, 0, 'a', 4.2]
    >>> from randbaseline import RandBaselinePredictor:

    >>> randbaseline = RandBaselinePredictor:
()
    >>> randbaseline.fit(X, y)
    RandBaselinePredictor:
(...)
    >>> print(randbaseline.predict([[1.1]]))
    [4.2]
    """

    def __init__(
        self,
        aux_param = None
    ):
        if aux_param == None :
            self.aux_param = {}
        else :
            self.aux_param = aux_param

    version = 0.01

    def __repr__(self):
        '''Returns representation of the object'''
        return("{}({!r})".format(self.__class__.__name__, self.aux_param))

    def fit(self, X, y):
        """Fit the classifier with the training dataset.

        Parameters
        ----------
        X : array-like matrix of shape (n_samples, n_features)
            This parameter is ignored, present only for compatibility.

        y : array-like matrix of shape (n_samples,)
            Training target values.

        Returns
        -------
        self : RandBaselinePredictor:

            The fitted classifier.
        """

        ret = RandBaselinePredictor.WorkFit( self, X, y )
        return ret

    def predict(self, X):
        """Random prediction.

        Parameters
        ----------
        X : array-like of shape n_queries, n_features
            Test samples.

        Returns
        -------
        y : list of (n_queries,)
            Class labels for each data sample.
        """

        ret = RandBaselinePredictor.WorkPredict( self, X )
        return ret

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def WorkFit(object, in_X, in_y):
        import random

        data_y = in_y.copy()
        aux_param = object.aux_param

        r_state = random.getstate()
        if 'rand_seed' in aux_param :
            rand_seed = aux_param['rand_seed']
            random.seed(rand_seed)
        train_total_no = len(data_y)
        rand_list = random.sample(range(0, train_total_no), train_total_no)
        random.setstate(r_state)

        object.rand_idx_list = rand_list
        object.train_y = data_y

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def WorkPredict(object, in_query):

        query_req = in_query[:]

        train_total_no = len(object.train_y)
        query_len = len(query_req)
        rand_list = object.rand_idx_list
        y_out_lst = [None]*query_len

        for crt_idx in range(query_len) :
            hash_query = HashValue(query_req[crt_idx])
            rand_idx = rand_list[(hash_query + crt_idx) % train_total_no]
            y_out_lst[crt_idx] = object.train_y[rand_idx]

        return y_out_lst

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > RandBaselinePredictor - End
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def AccuracyEval(x_data, y_target, classifier, iterations = 1, train_fraction = 0.5, random_seed = 42, aux_data = None, display_flag = True) :

    import random
    data_rows = len(x_data)
    data_cols = len(x_data[0])

    if display_flag : iprnt("- - - - prediction accuracy test")
    if display_flag : iprnt()
    if display_flag : iprnt("- - - - - - classifier:", classifier)
    if display_flag : iprnt("- - - - - - iterations:", iterations)
    if display_flag : iprnt("- - - - - - train_fraction:", train_fraction)
    if display_flag : iprnt("- - - - - - aux_data:", aux_data)
    if display_flag : iprnt("- - - - - - random_seed:", random_seed)
    if display_flag : iprnt()

    if aux_data == None :
        aux_data = {}

    random.seed(random_seed)

    ret_tuple = AccuracyIterEval(x_data, y_target, classifier, iterations, train_fraction, random_seed, aux_data, True)
    avg_accuracy, rnd_accuracy, delta_secs, sample_test, sample_pred = ret_tuple

    column_limit = 40
    str_limit = 60
    if avg_accuracy == None :
        str_smpl_test = str(list(sample_test))
        str_smpl_pred = str(list(sample_pred))
    else :
        str_smpl_test = str(list(sample_test[:column_limit]))[:str_limit]
        str_smpl_pred = str(list(sample_pred[:column_limit]))[:str_limit]

    if display_flag : iprnt("- - - - - - delta_secs:", delta_secs)
    if display_flag : iprnt("- - - - - - sample_test:", str_smpl_test, "...")
    if display_flag : iprnt("- - - - - - sample_pred:", str_smpl_pred, "...")
    if display_flag : iprnt()
    if display_flag : iprnt("- - - - - - avg_accuracy:", avg_accuracy)
    if display_flag : iprnt("- - - - - - rnd_accuracy:", rnd_accuracy)
    return avg_accuracy, rnd_accuracy

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def AccuracyIterEval(x_data, y_target, classifier, iterations, train_fraction, random_seed, aux_data, valid_target_flag) :
    import datetime
    import random

    from sklearn.model_selection import train_test_split
    fn_ret_tuple = None, None, 0, None, None

    crt_time_ref = datetime.datetime.now()
    test_fraction = 1.0 - train_fraction
    cumulate_clsf_accuracy = 0
    cumulate_rand_accuracy = 0
    crt_rand_seed = random_seed
    if len(x_data) <= 1 :
        return fn_ret_tuple
    if not len(x_data) == len(y_target) :
        return fn_ret_tuple

    for crt_idx in range(iterations) :
        if not random_seed == None :
            crt_rand_seed = random_seed + crt_idx
        fn_ret_tuple = train_test_split(x_data, y_target, test_size = test_fraction, random_state = crt_rand_seed)
        x_train, x_test, y_train, y_test = fn_ret_tuple
        classifier.fit(x_train, y_train)
        y_predict = classifier.predict(x_test)


        # compute accuracy
        test_total_no = len(y_test)
        train_total_no = len(y_train)
        total_clsf_matches = 0
        total_rand_matches = 0
        effective_total = test_total_no
        rand_list = random.sample(range(0, train_total_no), train_total_no)
        for crt_jdx in range(test_total_no) :
            if valid_target_flag and y_test[crt_jdx] == None :
                effective_total -= 1
                continue
            if y_test[crt_jdx] == y_predict[crt_jdx] :
                total_clsf_matches += 1
            rand_idx = rand_list[crt_jdx % train_total_no]
            if y_test[crt_jdx] == y_train[rand_idx] :
                total_rand_matches += 1

        if effective_total > 0 :
            clsf_accuracy = total_clsf_matches / (1.0 * effective_total)
            cumulate_clsf_accuracy += clsf_accuracy
            rand_accuracy = total_rand_matches / (1.0 * effective_total)
            cumulate_rand_accuracy += rand_accuracy

        if crt_idx == 0 :
            sample_test = y_test[:]
            sample_pred = y_predict[:]

    clsf_avg_accuracy = (cumulate_clsf_accuracy * 1.0) / iterations
    rand_avg_accuracy = (cumulate_rand_accuracy * 1.0) / iterations

    new_time_ref = datetime.datetime.now()
    delta = new_time_ref - crt_time_ref
    delta_secs = delta.total_seconds()

    fn_ret_tuple = clsf_avg_accuracy, rand_avg_accuracy, delta_secs, sample_test, sample_pred
    return fn_ret_tuple

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



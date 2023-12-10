"""Deodata Delanga Classification"""

#   c4pub@git 2023
#
# Latest version available at: https://github.com/c4pub/deodel
#

import numpy as np
import warnings
import statistics
import pandas as pd
import numpy as np
import math

class DeodelSecond :
    """Predictor implementing a variant of the Deodata Delanga classifier.

    Read more in the reference document.

    Parameters
    ----------
    aux_param : dict, default=None
        Auxiliary configuration parameters.
        Configuration dictionary keywords:
            'split_no' : int, default=3
                Number of categories, or bins, to split numerical attributes.

            'tbreak_depth' : int, default=0
                Limit to the depth of searching for tie breakers. O means no limit.

    Attributes
    ----------
    version : float
        Version of algorithm implementation

    Notes
    -----
    See online documentation for a discussion of the method.

    https://doi.org/10.13140/RG.2.2.33413.06880

    Examples
    --------
    >>> X = [[0], [1], [2], [3]]
    >>> y = [0, 0, 1, 1]
    >>> from deodel2 import DeodelSecond
    >>> deodel2 = DeodelSecond()
    >>> deodel2.fit(X, y)
    DeodelSecond(...)
    >>> print(deodel2.predict([[1.1]]))
    [0]
    """

    def __init__(
        self,
        aux_param = None
    ):
        default_aux = {
                        'split_no':     0,
                        'split_mode':   'eq_width',
                        'tbreak_depth': None,
                        'predict_mode': 'auto',
                        'score_factor': 2,
                        'back_compat':  False,
                        'int_is_num':   True,
                      }

        if aux_param == None :
            self.aux_param = {}
            self.cfg_param = default_aux
        else :
            self.aux_param = aux_param
            cfg_param = {}
            for crt_elem in default_aux :
                if crt_elem in aux_param :
                    cfg_param[crt_elem] = aux_param[crt_elem]
                else :
                    cfg_param[crt_elem] = default_aux[crt_elem]
            self.cfg_param = cfg_param

    version = 2.13

    def __repr__(self):
        '''Returns representation of the object'''
        return("{}({!r})".format(self.__class__.__name__, self.aux_param))

    def fit(self, X, y):
        """Fit the classifier with the training dataset.

        Parameters
        ----------
        X : array-like matrix of shape (n_samples, n_features)
            Training data.

        y : array-like matrix of shape (n_samples,)
            Target values.

        Returns
        -------
        self : DeodelSecond
            The fitted classifier.
        """

        ret = Working.WorkFit( self, X, y )
        return ret

    def predict(self, X):
        """Predict the class labels for the provided data.

        Parameters
        ----------
        X : array-like of shape n_queries, n_features
            Test samples.

        Returns
        -------
        y : list of (n_queries,)
            Class labels for each data sample.
        """

        ret = Working.WorkPredict( self, X )
        return ret

# >-----------------------------------------------------------------------------

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > Working - Begin
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Working:

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def WorkFit(object, in_X, in_y):

        data_y = CasetDeodel.ListDataConvert(in_y)
        if not data_y == [] :
            if (isinstance(data_y[0], list)) :
                if len(data_y[0]) == 1 :
                    # must be a one column matrix
                    transpose_data = Working.MatrixTranspose(data_y)
                    data_y = transpose_data[0]
                else :
                    data_y = None

        data_X = CasetDeodel.ListDataConvert(in_X)

        split_no = object.cfg_param['split_no']
        split_mode = object.cfg_param['split_mode']
        predict_mode = object.cfg_param['predict_mode']
        score_factor = object.cfg_param['score_factor']
        int_is_num = object.cfg_param['int_is_num']
        back_compat = object.cfg_param['back_compat']

        ret_item = Working.DicretizeTable( data_X, split_no, split_mode, int_is_num )
        (ret_cat_tbl, ret_num_tbl, ret_mask_tbl, ret_attr_num_cfg, ret_attr_dict_list) = ret_item

        object.attr_cat_X = np.array(ret_cat_tbl, dtype='int')
        object.attr_num_X = np.array(ret_num_tbl, dtype='float')
        object.attr_mask_X = np.array(ret_mask_tbl, dtype='int')
        object.attr_num_cfg = ret_attr_num_cfg
        object.attr_dict_list = ret_attr_dict_list
        object.attr_split_no = split_no
        object.attr_split_mode = split_mode
        object.attr_score_factor = score_factor
        object.attr_int_is_num = int_is_num

        object.attr_back_compat = back_compat

        if predict_mode == 'auto' :
            regress_flag = Working.NumParse(data_y, int_is_num)
        elif predict_mode == 'regress' :
            regress_flag = True
        else :
            # 'classif'
            regress_flag = False

        object.regress_flag = regress_flag
        object.targ_y = data_y

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def DicretizeTable(in_tbl, in_split_no, in_split_mode, in_int_is_num):

        data_tbl = in_tbl
        entry_no = len(data_tbl)

        # determine column dimension (for incomplete lists of lists)
        max_col_no = 0
        for crt_row in data_tbl :
            crt_rlen = len(crt_row)
            if crt_rlen > max_col_no :
                max_col_no = crt_rlen
        attr_no = max_col_no

        attr_cat_tbl = []
        attr_num_tbl = []
        attr_mask_tbl = []
        attr_dict_list = []
        attr_num_thresh = []
        split_num = in_split_no

        for crt_idx in range(attr_no) :

            crt_col = Working.GetCol( data_tbl, crt_idx )
            ret_tuple = Working.ProcessVector(crt_col, in_int_is_num)
            (conv_cat, conv_num, conv_mask, shadow_dict, shadrev_dict, numerical_list) = ret_tuple

            # create numerical thresholds if numerical elements are present
            if len(numerical_list) > 0 :
                if in_split_mode == 'eq_width' :
                    ord_num_list = sorted(numerical_list)
                    if ord_num_list[0] == ord_num_list[-1] :
                        crt_attr_thresh = [False, []]
                    else :
                        crt_attr_thresh = [True, [ord_num_list[0], ord_num_list[-1]]]
                elif in_split_mode == 'eq_legacy_width' :
                    crt_attr_thresh = Working.NumSplit(numerical_list, in_split_no, in_split_mode)
                else :
                    crt_attr_thresh = Working.NumSplit(numerical_list, in_split_no, in_split_mode)
            else :
                crt_attr_thresh = [False, []]

            attr_num_thresh.append(crt_attr_thresh)
            attr_dict_list.append(shadow_dict)
            attr_cat_tbl.append(conv_cat)
            attr_num_tbl.append(conv_num)
            attr_mask_tbl.append(conv_mask)

        # Replace numerical values with discretized/processed values
        for crt_idx_1 in range(attr_no) :
            crt_attr_mask_list = attr_mask_tbl[crt_idx_1]
            crt_attr_num_list = attr_num_tbl[crt_idx_1]
            for crt_idx_2 in range(entry_no) :
                crt_mask_elem = crt_attr_mask_list[crt_idx_2]
                crt_num_elem = crt_attr_num_list[crt_idx_2]
                # [crt_flag, crt_thresh_list] = attr_num_thresh[crt_idx_1]
                crt_thresh_list = attr_num_thresh[crt_idx_1]
                if crt_mask_elem == 1 :
                    process_val = Working.DiscretizeAttrVal(crt_num_elem, crt_thresh_list, in_split_mode, in_split_no)
                    new_id = process_val
                    attr_num_tbl[crt_idx_1][crt_idx_2] = new_id

        ret_cat_tbl = Working.MatrixTranspose(attr_cat_tbl)
        ret_num_tbl = Working.MatrixTranspose(attr_num_tbl)
        ret_mask_tbl = Working.MatrixTranspose(attr_mask_tbl)
        ret_attr_num_cfg = attr_num_thresh
        ret_attr_dict_list = attr_dict_list

        ret_tuple = (ret_cat_tbl, ret_num_tbl, ret_mask_tbl, ret_attr_num_cfg, ret_attr_dict_list)
        return ret_tuple

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def WorkPredict(object, in_query):

        query_req = CasetDeodel.ListDataConvert(in_query)

        # attr_no = len(object.attr_X[0])
        # if attr_no != len( object.attr_num_cfg ) :
        #     raise ValueError( "Mismatch in the number of attributes" )

        result_lst = []
        for row in query_req :
            crt_result = Working.PredictOne(object, row)
            result_lst.append(crt_result)
        return result_lst

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def DiscretizeAttrVal(in_cont_value, in_discretize_cfg, in_split_mode, in_split_no) :

        # Discretize a continuous value using threshold list
        crt_num_elem = in_cont_value
        [crt_multi_flag, crt_thresh_list] = in_discretize_cfg

        # start_no_id = len( attr_dict_list[crt_idx_1] ) + 1
        start_no_id = 0.0

        thresh_elem_no = len(crt_thresh_list)
        if thresh_elem_no == 0 :
            new_id = start_no_id
        else :
            if not crt_multi_flag :
                # monocolor attribute
                if in_cont_value == crt_thresh_list[0] :
                    proc_val = start_no_id + 1
                else :
                    proc_val = start_no_id
            else :
                if in_split_mode == 'eq_width' :
                    proc_val = Working.EqualWidthDiscretize(crt_num_elem, crt_thresh_list, in_split_no)
                elif in_split_mode == 'eq_legacy_width' :
                    thresh_div = len(crt_thresh_list)
                    upper_idx = Working.GetElemIdxInOrderList(crt_num_elem, crt_thresh_list)
                    proc_val = upper_idx / (1.0 * thresh_div)
                else :
                    thresh_div = len(crt_thresh_list)
                    upper_idx = Working.GetElemIdxInOrderList(crt_num_elem, crt_thresh_list)
                    proc_val = upper_idx / (1.0 * thresh_div)

            new_id = start_no_id + proc_val

        return new_id

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def TranslateAttrEntry(object, in_attr_list):
        # translate to conforming list
        attr_entry = in_attr_list
        attr_no = len(attr_entry)
        transl_cat_query = []
        transl_mask_query = []
        transl_num_query = []
        int_is_num = object.attr_int_is_num
        for crt_idx in range(attr_no) :
            crt_attr = attr_entry[crt_idx]
            crt_num_cfg = object.attr_num_cfg[crt_idx]
            crt_dict = object.attr_dict_list[crt_idx]
            if crt_attr == None :
                # None is considered to represent missing attribute values, will be ignored.
                new_cat_id = -1
                new_num_id = 0
                new_mask_id = 0
            else :
                ret_tuple = Working.NumericalCheck(crt_attr, int_is_num)
                is_numerical, translate_value = ret_tuple
                if is_numerical :
                    # numerical attribute, discretize with interval
                    process_val = Working.DiscretizeAttrVal(translate_value, crt_num_cfg, object.attr_split_mode, object.attr_split_no)
                    new_num_id = process_val
                    new_mask_id = 1
                    new_cat_id = 0
                else :
                    new_num_id = 0
                    new_mask_id = 0
                    if translate_value in crt_dict :
                        new_cat_id = crt_dict[translate_value]
                    else :
                        new_cat_id = 0
            transl_cat_query.append(int(new_cat_id))
            # transl_num_query.append(int(new_num_id + 0.5))
            transl_num_query.append(float(new_num_id))
            transl_mask_query.append(int(new_mask_id))
        ret_item = (
                        np.array(transl_cat_query, dtype='int'), 
                        np.array(transl_num_query, dtype='float'), 
                        np.array(transl_mask_query, dtype='int'), 
                    )
        return ret_item

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def PredictOne(object, in_query):
        # prediction for one query
        query_len = len(in_query)
        train_len = len(object.attr_cat_X[0])
        int_is_num = object.attr_int_is_num
        if query_len == train_len :
            adjusted_query = in_query[:]
        elif query_len > train_len :
            adjusted_query = in_query[:train_len]
        else :
            # list comprehension
            adjusted_query = in_query + [None for i in range(train_len - query_len)]

        attr_no = query_len
        query_cat_req, query_num_req, query_mask_req = Working.TranslateAttrEntry(object, adjusted_query)

        # list comprehension
        # match_score_list = [[] for i in range(attr_no + 1)]
        match_score_list = [[] for i in range(attr_no * object.attr_score_factor + 1)]
        # shadow_score_list = [[] for i in range(attr_no + 1)]
        shadow_score_list = [[] for i in range(attr_no * object.attr_score_factor + 1)]
    
        attr_rows = len(object.attr_cat_X)
        targ_no = len(object.targ_y)
        train_no = min(attr_rows, targ_no)
        
        for crt_idx in range(train_no) :

            crt_train_cat_attr = object.attr_cat_X[crt_idx]
            compare_cat_vect = (np.equal(crt_train_cat_attr, query_cat_req)).astype(int)
            entry_cat_match_score = int(np.count_nonzero(compare_cat_vect))

            crt_train_mask_attr = object.attr_mask_X[crt_idx]
            crt_train_num_attr = object.attr_num_X[crt_idx]

            # discretize_div = object.attr_split_no - 1
            discretize_div = 1.0
            compare_num_vect = 1.0 - abs((crt_train_num_attr - query_num_req)/(1.0 * discretize_div))
            compare_num_vect *= crt_train_mask_attr
            compare_num_vect *= query_mask_req

            if object.attr_back_compat :
                tmp_vector = compare_num_vect.astype(int)
                compare_num_vect = np.where(tmp_vector == 1, 1, 0)

            entry_num_match_score = sum(compare_num_vect)
            entry_agg_match_score = int( (entry_cat_match_score + entry_num_match_score) * object.attr_score_factor + 0.5 )
            if object.regress_flag :

                crt_targ_elem = object.targ_y[crt_idx]
                ret_tuple = Working.NumericalCheck(crt_targ_elem, int_is_num)
                is_numerical, translate_value = ret_tuple
                if is_numerical :
                    match_score_list[entry_agg_match_score].append((None, 0))
                    shadow_score_list[entry_agg_match_score].append(object.targ_y[crt_idx])
                else :
                    match_score_list[entry_agg_match_score].append(object.targ_y[crt_idx])
            else :
                match_score_list[entry_agg_match_score].append(object.targ_y[crt_idx])

        aux_cfg_data = {'top_first': False}
        if 'tbreak_depth' in object.cfg_param :
            if object.cfg_param['tbreak_depth'] == None :
                pass
            elif object.cfg_param['tbreak_depth'] > 0 :
                aux_cfg_data['eval_limit'] = object.cfg_param['tbreak_depth']
        ret_tuple = CasetDeodel.HelperRecurseTieBreaker(match_score_list, None, aux_cfg_data)
        champ_sel = ret_tuple[2]
        
        if object.regress_flag :
            if champ_sel == (None, 0) :
                # This indicates that the predicted outcome is numerical. 
                # Find top numerical entry.
                # Top score is last non-empty entry
                shadow_len = len(shadow_score_list)
                for crt_idx in range(shadow_len) :
                    complmnt_idx = (shadow_len - 1) - crt_idx
                    crt_list = shadow_score_list[complmnt_idx]
                    if not crt_list == [] :
                        break
                top_score = crt_idx
                top_num_list = crt_list
                vect_mean = statistics.mean(top_num_list)
                champ_sel = vect_mean

        predict_y = champ_sel
        return predict_y

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def GetElemIdxInOrderList( in_elem, in_thresh_list ) :

        ordered_list = in_thresh_list
        new_element = in_elem

        fn_ret_status = False
        fn_ret_insert_idx = None

        # one iteration loop to allow unified return through loop breaks
        for dummy_idx in range(1) :

            no_of_elem = len( ordered_list )
            if no_of_elem == 0 :
                fn_ret_status = True
                fn_ret_insert_idx = 0
                break

            interval_len = no_of_elem
            offset_idx = 0
            while True :
                half_len = int(interval_len/2)
                middle_idx = half_len
                middle_idx += offset_idx
                crt_elem = ordered_list[middle_idx]
                ret_compare = ( new_element < crt_elem )
                if ret_compare :
                    # Correct order
                    interval_len = middle_idx - offset_idx
                else :
                    # Not correct order
                    interval_len = interval_len - ( middle_idx - offset_idx ) - 1
                    offset_idx = middle_idx + 1
                # check break condition
                if interval_len <= 0 :
                    break

            # After iterations completed the appropiate position is in offset_idx
            fn_ret_status = True
            fn_ret_insert_idx = offset_idx

        ret_item = fn_ret_insert_idx
        return(ret_item)

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def EqualWidthDiscretize( in_elem, in_minmax_list, in_split_no ) :

        # list_minmax = sorted(in_minmax_list)
        list_minmax = in_minmax_list
        crt_num_elem = in_elem
        val_span = (list_minmax[-1] - list_minmax[0]) * 1.0
        if val_span > 0 :
            if crt_num_elem < list_minmax[0] :
                crt_num_elem = list_minmax[0]
            if crt_num_elem > list_minmax[-1] :
                crt_num_elem = list_minmax[-1]
            input_offset = (crt_num_elem - list_minmax[0])
            if in_split_no <= 1 :
                # no discretization
                convert_val = input_offset/(1.0 * val_span)
            else :
                unit_width = (val_span * 1.0)/(in_split_no - 1)
                # list comprehension
                # near_discr_offset = int(input_offset/(1.0 * unit_width) + 0.5)
                # near_discr_offset = int(input_offset/(1.0 * unit_width) + 0.0)
                
                interm_val = input_offset/(1.0 * unit_width)
                discr_offset = int(interm_val + 0.5)
                near_scaled_offset = discr_offset / (1.0 * (in_split_no - 1))
                convert_val = near_scaled_offset
        else :
            if crt_num_elem >= list_minmax[0] :
                convert_val = 1
            else :
                convert_val = 0
                # convert_val = 0

        ret_item = convert_val
        return(ret_item)

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def GetCol( in_array, in_col ) :
        ret_item = []
        if not isinstance(in_array, list) :
            ret_item = None
        else :
            row_no = len(in_array)
            if not isinstance(in_array[0], list) :
                ret_item = None
            else :
                ret_item = []
                for crt_idx_row in range(row_no) :
                    crt_row_len = len(in_array[crt_idx_row])
                    if in_col < crt_row_len :
                        ret_item.append((in_array[crt_idx_row][in_col]))
                    else :
                        ret_item.append(None)
        return(ret_item)

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def MatrixTranspose( in_array ) :
        if in_array == [] : return []
        if not isinstance(in_array[0], list) :
            transp_data = list(in_array)
        else :
            transp_data = []
            col_no = len(in_array[0])
            for crt_idx_col in range(col_no) :
                crt_vect = Working.GetCol( in_array, crt_idx_col )
                transp_data.append(crt_vect)
        ret_item = transp_data
        return(ret_item)

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def ProcessVector( in_v, in_int_is_num ) :
        vect_size = len(in_v)
        shadow_id = 1
        shadow_dict = {}
        shadrev_dict = {}
        numerical_list = []
        conv_cat = []
        conv_num = []
        conv_mask = []
        for crt_idx in range(vect_size) :
            crt_elem = in_v[crt_idx]
            is_num_flag, equiv_val = Working.NumericalCheck(crt_elem, in_int_is_num)
            if is_num_flag :
                numerical_list.append(crt_elem)
                conv_num.append(crt_elem)
                conv_cat.append(-2)
                # mask one is used as a marker for numerical values
                conv_mask.append(1)
            else :
                conv_num.append(-1)
                if not equiv_val in shadow_dict :
                   shadow_dict[crt_elem] = shadow_id
                   shadrev_dict[shadow_id] = equiv_val
                   conv_cat.append(shadow_id)
                   shadow_id += 1
                else :
                   conv_cat.append(shadow_dict[equiv_val])
                conv_mask.append(0)

        fn_ret_tuple = (conv_cat, conv_num, conv_mask, shadow_dict, shadrev_dict, numerical_list)
        return fn_ret_tuple

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def NumSplit( in_num_list, in_split_no = 2, in_split_mode = 'eq_width', no_dupl_flag = True ) :
        threshold_list = []
        if in_split_no <= 1 :
            return [False, threshold_list]
        num_len = len(in_num_list)
        if num_len == 0 :
            return [False, threshold_list]
        elif num_len == 1 :
            if no_dupl_flag :
                threshold_list = [in_num_list[0]]
            else :
                # list comprehension
                threshold_list = [in_num_list[0] for i in range(in_split_no - 1)]
            return [True, threshold_list]
        if in_split_mode == 'eq_freq' :
            threshold_list = Working.NumSplitFreq( in_num_list, in_split_no, no_dupl_flag )
        elif in_split_mode == 'eq_width' :
            threshold_list = Working.NumSplitWidth( in_num_list, in_split_no, no_dupl_flag )
        elif in_split_mode == 'eq_legacy_width' :
            threshold_list = Working.NumLegacySplitWidth( in_num_list, in_split_no, no_dupl_flag )
        else :
            # invalid
            return [False, threshold_list]
        return [True, threshold_list]

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def NumSplitFreq( in_num_list, in_split_no = 2, no_dupl_flag = True ) :
        threshold_list = []
        num_len = len(in_num_list)
        if num_len == 0 :
            return threshold_list

        ord_num_list = sorted(in_num_list)
        max_split_factor = 2
        if in_split_no > max_split_factor * num_len :
            split_num = max_split_factor * num_len
        else :
            split_num = int(in_split_no)

        if ord_num_list[0] == ord_num_list[-1] :
            if no_dupl_flag :
                threshold_list = [ord_num_list[0]]
            else :
                # list comprehension
                threshold_list = [ord_num_list[0] for i in range(in_split_no - 1)]
            return threshold_list

        #   |.....|.....|.....|.....|.....|.....|.....
        #   x........x........x........x........x........
        #   .....x........x........x........x........x........

        period_split = 1.0/split_num
        period_ordrd = 1.0/num_len
        sample_point_uscale = -period_ordrd / 2.0
        sample_point_uscale += period_split
        crt_split_len = 0
        thresh_prev = None

        while ((sample_point_uscale < (1 - period_ordrd/4.0))
                and (crt_split_len <= (split_num - 2))) :
            num_near_offset = (sample_point_uscale) / period_ordrd
            num_near_idx = int(num_near_offset)
            if num_near_idx == num_near_offset :
                new_thresh = ord_num_list[num_near_idx]
            else:
                prev_ordrd_uscale = num_near_idx * period_ordrd
                next_ordrd_uscale = (num_near_idx + 1) * period_ordrd
                delta_fract = (sample_point_uscale - prev_ordrd_uscale) / period_ordrd

                # threshold crossed
                #   0.00 0.25 0.50 0.75 1.00
                #         ^
                #   a   (b-a)*0.25         b
                #
                if num_near_idx + 1 < num_len :
                    x_interp = delta_fract
                    y_a = ord_num_list[num_near_idx]
                    y_b = ord_num_list[num_near_idx + 1]
                    y_interp = y_a + (y_b - y_a) * x_interp
                    new_thresh = y_interp
                else :
                    new_thresh = ord_num_list[num_near_idx]

            sampling_add = period_split
            if no_dupl_flag :
                if num_near_idx < num_len - 1 :
                    thresh_next = ord_num_list[num_near_idx + 1]
                    if not thresh_next == new_thresh :
                        threshold_list.append(new_thresh)
                        crt_split_len += 1
                        thresh_prev = new_thresh
                    else :
                        # skip append
                        sample_point_uscale = (num_near_idx + 1) * period_ordrd
                else :
                    if not new_thresh == thresh_prev :
                        threshold_list.append(new_thresh)
                        crt_split_len += 1
                        thresh_prev = new_thresh
                    else :
                        # skip append
                        pass
            else :
                threshold_list.append(new_thresh)
                crt_split_len += 1
                thresh_prev = new_thresh
            sample_point_uscale += sampling_add

        if threshold_list == [] :
            if ord_num_list[0] != ord_num_list[-1] :
                # at least add the last of ordered list
                last_elem = ord_num_list[-1]
                threshold_list = [last_elem]

        return threshold_list

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def NumSplitWidth( in_num_list, in_split_no = 2, no_dupl_flag = True ) :
        threshold_list = []
        num_len = len(in_num_list)
        if num_len == 0 :
            return threshold_list
        ord_num_list = sorted(in_num_list)
        num_min = ord_num_list[0]
        num_max = ord_num_list[-1]
        width = (num_max - num_min)/(in_split_no - 1.0)
        if width == 0 :
            if no_dupl_flag :
                threshold_list = [num_min]
            else :
                # list comprehension
                threshold_list = [in_num_list[0] for i in range(in_split_no - 1)]
        else :
            threshold_list = []
            crt_thresh = num_min + width/2.0
            for crt_idx in range(in_split_no - 1) :
                threshold_list.append(crt_thresh)
                crt_thresh += width
        return threshold_list

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def NumLegacySplitWidth( in_num_list, in_split_no = 2, no_dupl_flag = True ) :
        threshold_list = []
        num_len = len(in_num_list)
        if num_len == 0 :
            return threshold_list
        ord_num_list = sorted(in_num_list)
        num_min = ord_num_list[0]
        num_max = ord_num_list[-1]
        width = (num_max - num_min)/(in_split_no * 1.0)
        if width == 0 :
            if no_dupl_flag :
                threshold_list = [num_min]
            else :
                # list comprehension
                threshold_list = [num_min for i in range(in_split_no - 1)]
        else :
            threshold_list = []
            crt_thresh = num_min
            for crt_idx in range(in_split_no - 1) :
                crt_thresh += width
                threshold_list.append(crt_thresh)
        return threshold_list

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def RevertVector( in_cat_v, shadrev_dict, in_num_v ) :
        vect_size = len(in_cat_v)
        revrt_v = []
        for crt_idx in range(vect_size) :
            crt_elem = in_cat_v[crt_idx]
            if crt_elem == -2 :
                revrt_v.append(in_num_v[crt_idx])
            else :
               tr_elem = shadrev_dict[crt_elem]
               revrt_v.append(tr_elem)

        fn_ret = revrt_v
        return fn_ret

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def NumericalCheck( in_value, int_is_num_flag = True ) :
        """
            Check if numerical. If non regular float, result is false and
            translated value returned
        """
        if not int_is_num_flag :
            if isinstance(in_value, float) :
                float_flag, valid_val = CasetDeodel.ValidateFloat(in_value)
                fn_ret = (float_flag, valid_val)
            else :
                fn_ret = (False, in_value)
        else :
            if isinstance(in_value, float) :
                float_flag, valid_val = CasetDeodel.ValidateFloat(in_value)
                fn_ret = (float_flag, valid_val)
            elif isinstance(in_value, int) :
                fn_ret = (True, in_value)
            else :
                fn_ret = (False, in_value)
        return fn_ret

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def NumParse( in_vect, in_int_is_num) :
        """
            Parse vector and check if vector has valid regress numerical elements.
            Also computes the average of the numerical elements.
            
        """
        regress_flag = False
        num_list = []
        for crt_elem in in_vect :
            is_numerical, translate_value = Working.NumericalCheck(crt_elem, in_int_is_num)
            if is_numerical :
                num_list.append(crt_elem)
        if not num_list == [] :
            # check whether list appears to be made of continuous values
            ret_tuple = CasetDeodel.SummaryFreqCount(num_list)
            crt_types_no, crt_id_list, crt_count_list = ret_tuple
            if crt_types_no > 4 :
                mid_idx = int(crt_types_no/2) - 1
                if crt_count_list[mid_idx] == 1 :
                    # more than half of values are unique
                    regress_flag = True
        return regress_flag

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > Working - End
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > CasetDeodel - Begin
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class CasetDeodel:

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def OrderedFreqCount(in_symbol_sequence_list):
        """
        Returns a list that contains info about the frequency of
        items in parameter input list (in_symbol_sequence_list).
        The list is sorted on no of occurences order

        Params:
            in_symbol_sequence_list
                sequence of symbol occurences

        returns:
            out_list
                The output list has the following structure:
                each row (first level list)  has:
                    first column the element itself from the list
                    second column the no of occurences
                    third column the list of indexes containing the element
        """
        from operator import itemgetter

        in_len = len(in_symbol_sequence_list)
        idx = 0
        out_list = []
        for in_el in in_symbol_sequence_list:
            found_match = 0
            for out_el in out_list:
                if in_el == out_el[0]:
                    out_el[1] = out_el[1] + 1
                    out_el[2].append(idx)
                    found_match = 1
                    break
            if found_match == 0:
                out_list.append([in_el, 1, []])
                # append index into third column
                out_list[-1][2].append(idx)
            idx = idx + 1

        out_list.sort(key=itemgetter(1), reverse=True)
        return out_list

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def SummaryFreqCount(in_symbol_sequence_list):
        """
        Returns a summary about the frequency of
        items in parameter input list (in_symbol_sequence_list).
        The list is sorted on no of occurences order

        Params:
            in_symbol_sequence_list
                sequence of symbol occurences

        returns:
            ret_no_of_distinct_elems
            ret_elem_list
                List of distinct elements
            ret_count_list
                List with counts of each element matching ret_elem_list
        """
        count_data = CasetDeodel.OrderedFreqCount(in_symbol_sequence_list)
        distinct_elem_no, elem_list, count_list = CasetDeodel.CountDataToFreqLists(count_data)

        return distinct_elem_no, elem_list, count_list

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def CountDataToFreqLists(in_freq_count_data):
        """
        Returns a summary of info about the frequency of
        items in parameter input list (in_freq_count_data).
        The lists are sorted on no of occurences order

        Params:
            in_freq_count_data
                sequence of symbol occurences

        returns:
            ret_no_of_distinct_elems
            ret_elem_list
                List of distinct elements
            ret_count_list
                List with counts of each element matching ret_elem_list
        """
        # determine no of distinct elements
        distinct_elem_no = len(in_freq_count_data)

        # Filter out the index lists
        elem_count_pairs = [ elem[:2] for elem in in_freq_count_data ]

        elem_list = [ x[0] for x in elem_count_pairs ]
        count_list = [ x[1] for x in elem_count_pairs ]

        return distinct_elem_no, elem_list, count_list

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def HelperRecurseTieBreaker(in_ordered_outcome_table, in_sel_id_dict = None, aux_data = None) :
        """
        Recursive tie breaker

        Param:
            in_ordered_outcome_table
            in_sel_id_dict
            aux_data
                Auxilliary data

        Return:
            ret_status
            ret_outcome_id
            ret_outcome_count
        """
        fn_ret_status = False
        fn_tbreak_status = False
        fn_ret_outcome_id = None
        fn_ret_outcome_count = None

        # one iteration loop to allow unified return through loop breaks
        for dummy_idx in range(1) :

            if (isinstance (in_sel_id_dict, dict) == False
                    and in_sel_id_dict != None ) :
                break

            if in_ordered_outcome_table == [] :
                # empty list
                fn_ret_status = False
                fn_tbreak_status = False
                fn_ret_outcome_id = None
                fn_ret_outcome_count = 0
                break

            if aux_data == None :
                aux_data = {'top_first': True}
            else :
                if not 'top_first' in aux_data :
                    aux_data['top_first'] = True
            new_aux = dict(aux_data)
            if not new_aux['top_first'] :
                cumulate_outc_list = in_ordered_outcome_table[-1][:]
            else :
                cumulate_outc_list = in_ordered_outcome_table[0][:]

            ret_tuple = CasetDeodel.SummaryFreqCount(cumulate_outc_list)
            crt_types_no, crt_id_list, crt_count_list = ret_tuple

            if not new_aux['top_first'] :
                matchnum_score_list = in_ordered_outcome_table[:-1]
            else :
                matchnum_score_list = in_ordered_outcome_table[1:]

            if 'eval_limit' in new_aux :
                eval_limit = new_aux['eval_limit']
                if eval_limit <= 0 :
                    break

            selectid_dict = in_sel_id_dict

            # look for the first valid outcome type
            crt_max_idx = 0
            crt_sel_idx = 0
            first_match_idx = None
            for max_outc_id in crt_id_list :
                if not selectid_dict == None :
                    if max_outc_id in selectid_dict :
                        # found match
                        first_match_idx = crt_max_idx
                else :
                    # found match
                    first_match_idx = crt_max_idx
                if not first_match_idx == None :
                    break
                crt_max_idx += 1

            if first_match_idx == None :
                # no match found !
                if matchnum_score_list == [] :
                    # No more data
                    fn_ret_status, fn_tbreak_status, fn_ret_outcome_id, fn_ret_outcome_count = False, False, None, 0
                else :
                    # should evaluate rows with less score.
                    new_sel_id_dict = selectid_dict
                    ret_tuple = CasetDeodel.HelperRecurseTieBreaker(matchnum_score_list, new_sel_id_dict, new_aux)
                    fn_ret_status, fn_tbreak_status, fn_ret_outcome_id, fn_ret_outcome_count = ret_tuple
                break
            else :
                # a match has been found
                if 'eval_limit' in new_aux :
                    new_aux['eval_limit'] -= 1

                # Determine how many other valid outcomes have the same count
                first_id_match = crt_id_list[first_match_idx]
                crt_max_idx = 0
                first_match_count = None
                outcome_match_idx_list = []
                for max_outc_id in crt_id_list :
                    if crt_count_list[crt_max_idx] == crt_count_list[first_match_idx] :
                        if not selectid_dict == None :
                            if max_outc_id in selectid_dict :
                                # found match
                                outcome_match_idx_list += [crt_max_idx]
                        else :
                            outcome_match_idx_list += [crt_max_idx]

                    crt_max_idx += 1
                matching_outcome_no = len(outcome_match_idx_list)
                if matching_outcome_no == 1 :
                    # only outcome id matches the maximum score.
                    # Success, recursion is over.
                    fn_ret_status = True
                    fn_tbreak_status = True
                    fn_ret_outcome_id = crt_id_list[first_match_idx]
                    fn_ret_outcome_count = crt_count_list[first_match_idx]
                else :
                    # more than one outcome shares the same count.
                    new_sel_id_dict = {}
                    for crt_idx in outcome_match_idx_list :
                        new_sel_id_dict[crt_id_list[crt_idx]] = True
                    if matchnum_score_list == [] :
                        # No more data
                        fn_ret_status, fn_ret_outcome_id, fn_ret_outcome_count = True, crt_id_list[first_match_idx], crt_count_list[first_match_idx]
                    else :
                        ret_tuple = CasetDeodel.HelperRecurseTieBreaker(matchnum_score_list, new_sel_id_dict, new_aux)
                        fn_ret_status, fn_tbreak_status, fn_ret_outcome_id, fn_ret_outcome_count = ret_tuple
                        if not fn_ret_status :
                            # recursed result is worse
                            fn_ret_status, fn_tbreak_status, fn_ret_outcome_id, fn_ret_outcome_count = True, False, crt_id_list[first_match_idx], crt_count_list[first_match_idx]
                break

        ret_tuple = fn_ret_status, fn_tbreak_status, fn_ret_outcome_id, fn_ret_outcome_count
        return ret_tuple

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def ValidateFloat(in_val) :
        if not isinstance(in_val, float) :
            fn_ret_status = False
            fn_ret_translate = in_val
        elif np.isnan(in_val) :
            fn_ret_status = False
            fn_ret_translate = "nan"
        elif in_val == float('inf') :
            fn_ret_status = False
            fn_ret_translate = "+inf"
        elif in_val == float('-inf') :
            fn_ret_status = False
            fn_ret_translate = "-inf"
        else :
            fn_ret_status = True
            fn_ret_translate = in_val
        ret_tuple = fn_ret_status, fn_ret_translate
        return ret_tuple

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def ListDataConvert(in_data) :

        if (isinstance(in_data, list)) :
            # check whether is a one column array
            lst_data = in_data.copy()
        elif (isinstance(in_data, np.ndarray)) :
            lst_data = in_data.tolist()
        elif (isinstance(in_data, pd.core.arrays.PandasArray)) :
            lst_data = in_data.tolist()
        elif (isinstance(in_data, pd.core.frame.DataFrame)) :
            lst_data = in_data.values.tolist()
        elif (isinstance(in_data, pd.core.series.Series)) :
            lst_data = in_data.values.tolist()
        else :
            lst_data = None

        return lst_data

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > CasetDeodel - End
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

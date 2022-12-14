"""Deodata Delanga Classification"""

# Author: 
#          c4pub@github
#

import numpy as np
import warnings

class DeodataDelangaClassifier:
    """Classifier implementing the Deodata Delanga classifier.

    Read more in the reference document.

    Parameters
    ----------
    aux_param : dict, default=None
        Auxiliary configuration parameters.
        Configuration dictionary keywords:
            'num_split' : int, default=3
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
    >>> from deodel import DeodataDelangaClassifier
    >>> deodel = DeodataDelangaClassifier()
    >>> deodel.fit(X, y)
    DeodataDelangaClassifier(...)
    >>> print(deodel.predict([[1.1]]))
    [0]
    """

    def __init__(
        self,
        aux_param = None
    ):
        if aux_param == None :
            self.aux_param = {}
        else :
            self.aux_param = aux_param

    version = 1.05

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
        self : DeodataDelangaClassifier
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

        if (isinstance(in_y, np.ndarray)) :
            object.data_y = in_y.tolist()
        else :
            object.data_y = in_y.copy()

        if (isinstance(in_X, np.ndarray)) :
            object.data_X = in_X.tolist()
        else :
            object.data_X = in_X.copy()

        entry_no = len(object.data_X)
        attr_no = len(object.data_X[0])

        ret_tuple = Working.ProcessVector(object.data_y, False)
        (conv_v, shadow_dict, shadrev_dict, numerical_list) = ret_tuple

        attr_X = []
        attr_dict_list = []
        attr_num_thresh = []

        if 'split_no' in object.aux_param :
            num_split = object.aux_param['split_no']
        else :
            num_split = 3

        for crt_idx in range(attr_no) :

            crt_col = Working.GetCol( object.data_X, crt_idx )
            ret_tuple = Working.ProcessVector(crt_col)
            (conv_v, shadow_dict, shadrev_dict, numerical_list) = ret_tuple
            
            # process numerical elements if present
            if len(numerical_list) > 0 :
                next_id = len(shadow_dict) + 1
                crt_attr_thresh = Working.NumSplit(numerical_list, num_split)
            else :
                crt_attr_thresh = []

            attr_num_thresh.append(crt_attr_thresh)
            attr_dict_list.append(shadow_dict)
            attr_X.append(conv_v)
        
        # Replace numerical values with threshold
        for crt_idx_1 in range(attr_no) :
            crt_attr_list = attr_X[crt_idx_1]
            for crt_idx_2 in range(entry_no) :
                crt_elem = crt_attr_list[crt_idx_2]
                if isinstance(crt_elem, float) :
                    # entry is a float that needs conversion
                    start_no_id = len( attr_dict_list[crt_idx_1] ) + 1
                    crt_thresh_list = attr_num_thresh[crt_idx_1]
                    if crt_thresh_list == [] :
                        new_id = start_no_id
                    else :
                        upper_idx = Working.GetElemIdxInOrderList(crt_elem, crt_thresh_list)
                        new_id = start_no_id + upper_idx
                    attr_X[crt_idx_1][crt_idx_2] = new_id
                    
        object.attr_X = np.array(attr_X)
        object.attr_X = object.attr_X.transpose()
        object.attr_num_thresh = attr_num_thresh
        object.attr_dict_list = attr_dict_list
        
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def WorkPredict(object, in_query):

        if isinstance(in_query, np.ndarray) :
            query_req = in_query.tolist()
        else :
            query_req = in_query[:]
        
        entry_no = len(object.data_X)
        attr_no = len(object.data_X[0])

        if attr_no != len( object.attr_num_thresh ) :
            raise ValueError( "Mismatch in the number of attributes" )

        result_lst = []
        for row in query_req :
            crt_result = Working.PredictOne(object, row)
            result_lst.append(crt_result)

        return result_lst

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def TranslateAttrEntry(object, in_attr_list):

        attr_entry = in_attr_list
        attr_no = len(attr_entry)
        translated_query = []

        for crt_idx in range(attr_no) :
            
            crt_attr = attr_entry[crt_idx]
            crt_num_interval = object.attr_num_thresh[crt_idx]
            crt_dict = object.attr_dict_list[crt_idx]
            if crt_attr == None :
                # None is considered to represent missing attribute values, will be ignored.
                    new_id = -1
            else :
                if isinstance(crt_attr, (int, float)) :
                    # numerical attribute, discretize with interval
                    upper_idx = Working.GetElemIdxInOrderList(crt_attr, crt_num_interval)
                    dict_len = len(crt_dict)
                    new_id = dict_len + 1 + upper_idx
                else :
                    if crt_attr in crt_dict :
                        new_id = crt_dict[crt_attr]
                    else :
                        new_id = 0
            translated_query.append(new_id)
        ret_item = np.array(translated_query)
        return ret_item

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def PredictOne(object, in_query):

        attr_no = len(in_query)
        query_req = Working.TranslateAttrEntry(object, in_query)
        match_score_list = [[] for i in range(attr_no + 1)]
        train_no = len(object.attr_X)

        for crt_idx in range(train_no) :
            crt_train_attr = object.attr_X[crt_idx]
            compare_vect = ( crt_train_attr == query_req ).astype(int)
            entry_match_score = sum(compare_vect)
            match_score_list[entry_match_score].append(object.data_y[crt_idx])

        aux_data = {'top_first': False}
        if 'tbreak_depth' in object.aux_param :
            if object.aux_param['tbreak_depth'] > 0 :
                aux_data['eval_limit'] = object.aux_param['tbreak_depth']
        ret_tuple = CasetDeodel.HelperRecurseTieBreaker(match_score_list, None, aux_data)
        champ_sel = ret_tuple[2]
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

            # After iterations completed interval is one or zero and the appropiate position is in offset_idx
            fn_ret_status = True
            fn_ret_insert_idx = offset_idx

        ret_item = fn_ret_insert_idx
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
                    ret_item.append((in_array[crt_idx_row][in_col]))

        return(ret_item)

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def MatrixTranspose( in_array ) :
        ret_item = []
        row_no = len(in_array)
        if not isinstance(in_array[0], list) :
            ret_item = in_array.copy()
        else : 
            ret_item = []
            col_no = len(in_array[0])
            for crt_idx_col in range(col_no) :
                crt_vect = Working.GetCol( in_array, crt_idx_col )
                ret_item.append(crt_vect)
        return(ret_item)

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def ProcessVector( in_v, in_num_flag = True ) :
        vect_size = len(in_v)
        shadow_id = 1
        shadow_dict = {}
        shadrev_dict = {}
        numerical_list = []
        conv_v = []
        for crt_idx in range(vect_size) :
            crt_elem = in_v[crt_idx]
            if ( in_num_flag and isinstance(crt_elem, (int, float)) ) :
                numerical_list.append(crt_elem)
                conv_v.append(float(crt_elem))
            else :
                if not crt_elem in shadow_dict :
                   shadow_dict[in_v[crt_idx]] = shadow_id
                   shadrev_dict[shadow_id] = crt_elem
                   conv_v.append(shadow_id)
                   shadow_id += 1
                else :
                   conv_v.append(shadow_dict[crt_elem])

        fn_ret_tuple = (conv_v, shadow_dict, shadrev_dict, numerical_list)
        return fn_ret_tuple

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def NumSplit( in_num_list, in_split_no = 2, no_dupl_flag = True ) :
        threshold_list = []
        num_len = len(in_num_list)
        if num_len <= 1 :
            return []
        ord_num_list = sorted(in_num_list)

        max_split_factor = 2
        if in_split_no > max_split_factor * num_len :
            split_no = max_split_factor * num_len
        else :
            split_no = int(in_split_no)

        #   |.....|.....|.....|.....|.....|.....|.....
        #   x........x........x........x........x........
        #   .....x........x........x........x........x........

        period_split = 1.0/split_no
        period_ordrd = 1.0/num_len
        sample_point_uscale = -period_ordrd / 2.0
        sample_point_uscale += period_split
        crt_split_len = 0
        thresh_prev = None

        while ((sample_point_uscale < (1 - period_ordrd/4.0))
                and (crt_split_len <= (split_no - 2))) :
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
            # at least add the last of ordered list
            last_elem = ord_num_list[-1]
            threshold_list = [last_elem]

        return threshold_list

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def RevertVector( in_v, shadrev_dict ) :
        vect_size = len(in_v)
        revrt_v = []
        for crt_idx in range(vect_size) :
            crt_elem = in_v[crt_idx]
            if ( isinstance(crt_elem, float) ) :
                revrt_v.append(crt_elem)
            else :
               tr_elem = shadrev_dict[crt_elem]
               revrt_v.append(tr_elem)

        fn_ret = revrt_v
        return fn_ret

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
    def StrToFloat(in_str) :
        if not isinstance(in_str, str) :
            return None
        try :
            number = float(in_str)
            return number 
        except ValueError:
            return None

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def StrToSubstr(in_str) :
        import re

        if not isinstance(in_str, str) :
            return None
        substr_flag = False
        sub_str = None
        cpy_instr = in_str
        trim_str = cpy_instr.strip()
        ret_reg = re.search(r"^[\"](?P<tmptag>.*)[\"]$", trim_str)
        if ret_reg != None :
            substr_flag = True
            sub_str = ret_reg.group('tmptag')
        else :
            ret_reg = re.search(r"^[\'](?P<tmptag>.*)[\']$", trim_str)
            if ret_reg != None :
                substr_flag = True
                sub_str = ret_reg.group('tmptag')
        return sub_str

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def PreprocTbl(in_raw_tbl) :
        row_no = len(in_raw_tbl)
        col_no = len(in_raw_tbl[0])
        tbl_csv = []

        # convert fields
        for crt_row_idx in range(row_no) :
            row = in_raw_tbl[crt_row_idx]
            new = []
            for crt_col_idx in range(col_no) :
                crt_elem = in_raw_tbl[crt_row_idx][crt_col_idx]
                if isinstance(crt_elem, float) :
                    new_elem = crt_elem
                elif not isinstance(crt_elem, str) :
                    new_elem = None
                elif crt_elem == '' :
                    new_elem = None
                else :
                    num_elem = CasetDeodel.StrToFloat(crt_elem)
                    if num_elem == None :
                        substr_elem = CasetDeodel.StrToSubstr(crt_elem)
                        if substr_elem == None :
                            new_elem = crt_elem
                        else :
                            new_elem = substr_elem
                    else :
                        new_elem = num_elem
                new.append(new_elem)
            tbl_csv.append(new)
        return tbl_csv

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def ImportCsvToTbl(in_csv_file_path) :
        import csv

        file_d = open(in_csv_file_path, 'r')
        csv_read = csv.reader(file_d)
        list_of_csv = list(csv_read)
        tbl_csv = CasetDeodel.PreprocTbl(list_of_csv)
        return tbl_csv

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > CasetDeodel - End
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

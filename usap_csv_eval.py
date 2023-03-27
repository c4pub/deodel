"""
deodel - csv eval

    Evaluates predictive potential of csv datasets

"""

#   c4pub@git 2023

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > TblUtil - begin
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class TblUtil :

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def StrToNum(in_str) :
        # string to number preserving int or float representation type
        import deodel

        if not isinstance(in_str, str) :
            return None
        try :
            float_number = float(in_str)
            valid_flag, translated_val = deodel.CasetDeodel.ValidateFloat(float_number)
            if not valid_flag :
                return None
            int_number = int(float_number)
            if int_number == float_number :
                # potential integer
                if ('.' in in_str) or ('e' in in_str) or ('E' in in_str) :
                    ret_number = float_number
                else :
                    # preserve integer type
                    ret_number = int_number
            else :
                ret_number = float_number
            return ret_number
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
    @staticmethod
    def CsvTblPrep(in_raw_tbl) :
        # Prepare csv table validating cell content
        import deodel

        row_no = len(in_raw_tbl)
        tbl_csv = []
        # convert fields
        for crt_row_idx in range(row_no) :
            row_crt = in_raw_tbl[crt_row_idx]
            row_new = []
            if not isinstance(row_crt, list) :
                if not row_crt == None :
                    row_new.append(str(row_crt))
            else :
                col_no = len(row_crt)
                for crt_col_idx in range(col_no) :
                    crt_elem = in_raw_tbl[crt_row_idx][crt_col_idx]
                    if isinstance(crt_elem, int) :
                        new_elem = crt_elem
                    elif isinstance(crt_elem, float) :
                        float_flag, translated_val = deodel.CasetDeodel.ValidateFloat(crt_elem)
                        new_elem = translated_val
                    elif not isinstance(crt_elem, str) :
                        if not crt_elem == None :
                            new_elem = str(crt_elem)
                        else :
                            new_elem = None
                    elif crt_elem == '' :
                        new_elem = None
                    else :
                        num_elem = TblUtil.StrToNum(crt_elem)
                        if num_elem == None :
                            substr_elem = TblUtil.StrToSubstr(crt_elem)
                            if substr_elem == None :
                                new_elem = crt_elem
                            else :
                                new_elem = substr_elem
                        else :
                            new_elem = num_elem
                    row_new.append(new_elem)
            tbl_csv.append(row_new)
        return tbl_csv

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def GetFileCsv(in_csv_local) :
        import csv

        fn_ret_status = False
        fn_ret_data = None
        fn_ret_msg = ""

        # one iteration loop to allow unified return through loop breaks
        for dummy_idx in range(1) :
            try :
                file_d = open(in_csv_local, 'r')
                csv_read = csv.reader(file_d)
            except IOError :
                fn_ret_msg = "Error: failed file access !"
                break
            else :
                fn_ret_status = True
                fn_ret_data = csv_read

        fn_ret_tuple = (fn_ret_status, fn_ret_data, fn_ret_msg)
        return fn_ret_tuple

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def CheckIsUrl(in_url) :
        import validators
        url_flag = validators.url(in_url)
        if not url_flag == True :
            return False
        else :
            return True

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def GetUrlCsv(in_csv_url) :
        import csv
        import urllib.request
        from io import StringIO

        fn_ret_status = False
        fn_ret_data = None
        fn_ret_msg = ""

        # one iteration loop to allow unified return through loop breaks
        for dummy_idx in range(1) :
            url_flag = TblUtil.CheckIsUrl(in_csv_url)
            if not url_flag == True :
                fn_ret_msg = "Error: invalid url"
                break
            try :
                response_html = urllib.request.urlopen(in_csv_url)
                response_body = response_html.read()
            except IOError :
                fn_ret_msg = "Error: failed urlopen"
                break
            else :
                response_str = response_body.decode()
                buff_d = StringIO(response_str)
                csv_read = csv.reader(buff_d)
                fn_ret_status = True
                fn_ret_data = csv_read

        fn_ret_tuple = (fn_ret_status, fn_ret_data, fn_ret_msg)
        return fn_ret_tuple

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def GetUrlCsv(in_csv_url) :
        import csv
        import urllib.request
        from io import StringIO

        fn_ret_status = False
        fn_ret_data = None
        fn_ret_msg = ""

        # one iteration loop to allow unified return through loop breaks
        for dummy_idx in range(1) :
            try :
                response_html = urllib.request.urlopen(in_csv_url)
                response_body = response_html.read()
            except IOError :
                fn_ret_msg = "Error: failed urlopen"
                break
            else :
                response_str = response_body.decode()
                buff_d = StringIO(response_str)
                csv_read = csv.reader(buff_d)
                fn_ret_status = True
                fn_ret_data = csv_read

        fn_ret_tuple = (fn_ret_status, fn_ret_data, fn_ret_msg)
        return fn_ret_tuple

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def ImportCsvTbl(in_csv_path) :
        fn_ret_status = False
        fn_ret_data = None
        fn_ret_msg = ""

        # one iteration loop to allow unified return through loop breaks
        for dummy_idx in range(1) :
            csv_read = None
            ret_status = TblUtil.CheckIsUrl(in_csv_path)
            if ret_status :
                ret_info = TblUtil.GetUrlCsv(in_csv_path)
                ret_status, ret_data, ret_msg = ret_info
                if ret_status :
                    csv_read = ret_data
                else :
                    fn_ret_msg = ret_msg
            else :
                ret_info = TblUtil.GetFileCsv(in_csv_path)
                ret_status, ret_data, ret_msg = ret_info
                if ret_status :
                    csv_read = ret_data
                else :
                    fn_ret_msg = ret_msg
            if csv_read == None :
                pass
            else :
                list_csv = list(csv_read)
                fn_ret_status = True
                fn_ret_data = list_csv

        fn_ret_tuple = (fn_ret_status, fn_ret_data, fn_ret_msg)
        return fn_ret_tuple

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def TblPrepProxy(in_csv) :
        ret_status = False
        tbl_csv = None
        ret_msg = ""
        if isinstance(in_csv, str) :
            # input is a url or file path
            ret_status, list_csv, ret_msg = TblUtil.ImportCsvTbl(in_csv)
            if not ret_status :
                return ret_status, tbl_csv, ret_msg
        else :
            # assumes input is a list of lists table
            list_csv = in_csv[:]
            ret_status = True
        if ret_status :
            tbl_csv = TblUtil.CsvTblPrep(list_csv)
        else :
            ret_msg = "Error: csv data could not be accessed !"
        return ret_status, tbl_csv, ret_msg

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def UniformCleanRows(in_raw_tbl) :
        # Weed out empty rows and patch missing columns cells.

        fn_ret_dict = {'status': False, 'proc_tbl': [], 'del_row': [], 'dim':(0, 0)}
        clean_row_tbl = []
        if in_raw_tbl == [] :
            return fn_ret_dict
        row_no = len(in_raw_tbl)
        col_max = len(in_raw_tbl[0])
        col_min = len(in_raw_tbl[0])
        initial_row_no = row_no
        # search the maximum column no and remove empty lines
        for crt_idx in range(row_no) :
            crt_row = in_raw_tbl[crt_idx]
            col_no = len(crt_row)
            if col_no > col_max :
                col_max = col_no
            if col_no < col_min :
                col_min = col_no
            if crt_row == [None]*col_no :
                # skip empty row
                fn_ret_dict['del_row'].append(crt_idx)
            else :
                clean_row_tbl.append(crt_row)
        if col_min != col_max :
            # reparse to adjust rows
            row_no = len(clean_row_tbl)
            clean_tbl = []
            for crt_idx in range(row_no) :
                crt_row = clean_row_tbl[crt_idx]
                col_no = len(crt_row)
                new_row = crt_row[:]
                delta_col = col_max - col_no
                if delta_col > 0 :
                    # append columns
                    append_list = [None]*(delta_col)
                    new_row = crt_row + append_list
                clean_tbl.append(new_row)
        else :
            clean_tbl = clean_row_tbl
        fn_ret_dict['status'] = True
        fn_ret_dict['proc_tbl'] = clean_tbl
        fn_ret_dict['dim'] = (initial_row_no, col_max)
        return fn_ret_dict

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def AccuracyEval(x_data, y_target, classifier, iterations = 1, train_fraction = 0.5, random_seed = 42, display_flag = True) :

        import random
        data_rows = len(x_data)
        data_cols = len(x_data[0])

        if display_flag : print("- - - - prediction accuracy test")
        if display_flag : print()
        if display_flag : print("- - - - - - classifier:", classifier)
        if display_flag : print("- - - - - - iterations:", iterations)
        if display_flag : print("- - - - - - train_fraction:", train_fraction)
        if display_flag : print("- - - - - - random_seed:", random_seed)
        if display_flag : print()

        random.seed(random_seed)

        ret_tuple = TblUtil.AccuracyIterEval(x_data, y_target, classifier, iterations, train_fraction, random_seed, True)
        avg_accuracy, rnd_accuracy, delta_secs, sample_test, sample_pred = ret_tuple

        column_limit = 40
        str_limit = 60
        if avg_accuracy == None :
            str_smpl_test = str(sample_test)
            str_smpl_pred = str(sample_pred)
        else :
            str_smpl_test = str(sample_test[:column_limit])[:str_limit]
            str_smpl_pred = str(sample_pred[:column_limit])[:str_limit]

        if display_flag : print("- - - - - - delta_secs:", delta_secs)
        if display_flag : print("- - - - - - sample_test:", str_smpl_test, "...")
        if display_flag : print("- - - - - - sample_pred:", str_smpl_pred, "...")
        if display_flag : print()
        if display_flag : print("- - - - - - avg_accuracy:", avg_accuracy)
        if display_flag : print("- - - - - - rnd_accuracy:", rnd_accuracy)
        return avg_accuracy, rnd_accuracy

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def AccuracyIterEval(x_data, y_target, classifier, iterations, train_fraction, random_seed, valid_target_flag) :
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
    @staticmethod
    def CleanTargetExtract(in_table, in_targ_idx = None) :
        import deodel

        fn_ret_status = False
        fn_ret_table = []
        fn_ret_col = []
        fn_ret_dim = (0, 0)
        fn_ret_msg = "Error: data extraction failed !"

        crt_tbl = in_table
        # Weed out empty rows and patch missing columns cells.
        ret_info = TblUtil.UniformCleanRows(crt_tbl)
        if not ret_info['status'] :
            fn_ret_tuple = fn_ret_status, fn_ret_table, fn_ret_col, fn_ret_dim, fn_ret_msg
            return fn_ret_tuple
        crt_tbl = ret_info['proc_tbl']
        tbl_dim = ret_info['dim']
        fn_ret_dim = tbl_dim

        # set target col idx
        if in_targ_idx == None :
            # in_targ_idx = -1
            last_column = tbl_dim[1] - 1
            crt_targ_col = last_column
        else :
            crt_targ_col = in_targ_idx

        # Weed out empty columns.
        transpose_tbl = deodel.Working.MatrixTranspose(crt_tbl)
        ret_info = TblUtil.UniformCleanRows(transpose_tbl)
        trans_crt_tbl = ret_info['proc_tbl']

        # adjust target column if required
        adj_list = ret_info['del_row']
        adj_len = len(adj_list)
        adj_idx = 0
        exit_flag = False
        for crt_idx in range(adj_len) :
            old_idx = adj_list[crt_idx]
            if old_idx > crt_targ_col :
                # changes past target column are not relevant
                break
            elif old_idx == crt_targ_col :
                # the chosen target column was a removed empty list
                fn_ret_msg = "Error: empty target column !"
                exit_flag = True
                break
            else :
               adj_idx += 1
        if exit_flag :
            fn_ret_tuple = fn_ret_status, fn_ret_table, fn_ret_col, fn_ret_dim, fn_ret_msg
            return fn_ret_tuple
        new_targ_col = crt_targ_col - adj_idx

        if new_targ_col >= len(trans_crt_tbl) :
            fn_ret_msg = "Error: invalid target index !"
            fn_ret_tuple = fn_ret_status, fn_ret_table, fn_ret_col, fn_ret_dim, fn_ret_msg
            return fn_ret_tuple

        # split table into attributes and target
        target_col = trans_crt_tbl.pop(new_targ_col)
        trans_train_attr = trans_crt_tbl

        # restore train transposed matrix
        train_tbl = deodel.Working.MatrixTranspose(trans_train_attr)

        fn_ret_status = True
        fn_ret_table = train_tbl
        fn_ret_col = target_col
        fn_ret_dim = tbl_dim
        fn_ret_msg = ""
        fn_ret_tuple = fn_ret_status, fn_ret_table, fn_ret_col, fn_ret_dim, fn_ret_msg

        return fn_ret_tuple

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    @staticmethod
    def CvsProcess(in_csv_data, in_targ_idx = -1, in_iter_no = 5, in_rand_seed = 42, aux_data = None, display_flag = False) :
        import deodel

        fn_ret_dict = {'status': False, 'data': (None, None), 'msg':""}

        # one iteration loop to allow unified return through loop breaks
        for dummy_idx in range(1) :

            # Provide default values where needed
            if in_targ_idx == None :
                in_targ_idx = -1
            if in_iter_no == None :
                in_iter_no = 5
            if in_rand_seed == None :
                in_rand_seed = 42
            if display_flag == None :
                display_flag = True

            # Import table from csv and process valid numerical strings
            ret_status, list_csv, ret_msg = TblUtil.TblPrepProxy(in_csv_data)
            if not ret_status :
                fn_ret_dict['status'] = False
                fn_ret_dict['msg'] = ret_msg
                break

            # show data
            str_max_len = 60
            row_max_len = 6
            tbl_sample = list_csv[:row_max_len]
            if display_flag: print ()
            if display_flag: print ("- - - - list_csv:")
            for crt_row in tbl_sample :
                str_row = str(crt_row)[:str_max_len] + " ..."
                if display_flag: print ("- - - - - - - - crt_row:", str_row)
            if display_flag: print ("                ...")

            ret_info = TblUtil.CleanTargetExtract(list_csv, in_targ_idx)
            ret_status, train_tbl, target_col, ret_dim, ret_str = ret_info

            tbl_rows = ret_dim[0]
            tbl_cols = ret_dim[1]
            if display_flag: print ("- - - - - - - - tbl_rows:", tbl_rows)
            if display_flag: print ("- - - - - - - - tbl_cols:", tbl_cols)

            if not ret_status :
                fn_ret_dict['status'] = False
                fn_ret_dict['msg'] = ret_str
                break

            row_max_len = 4
            tbl_sample = train_tbl[:row_max_len]
            if display_flag: print ()
            if display_flag: print ("- - - - train_tbl:")
            for crt_row in tbl_sample :
                str_row = str(crt_row)[:str_max_len] + " ..."
                if display_flag: print ("- - - - - - - - crt_row:", str_row)

            str_row = str(target_col)[:str_max_len] + " ..."
            if display_flag: print ()
            if display_flag: print ("- - - - target_col:", str_row)
            if display_flag: print ()

            # compute averege predict accuracy

            data_digi_x = train_tbl
            data_target_y = target_col

            if display_flag: print("- - - - - - - - - - - - - - - - ")

            crt_classif = deodel.DeodataDelangaClassifier()
            ret_tuple = TblUtil.AccuracyEval(data_digi_x, data_target_y, crt_classif, iterations=in_iter_no, 
                                                random_seed=in_rand_seed, display_flag = display_flag)
            avg_accuracy, rnd_accuracy = ret_tuple
            fn_ret_dict['data'] = avg_accuracy, rnd_accuracy

            if display_flag: print("- - - - - - - - - - - - - - - - ")

            if display_flag: print ()
            if avg_accuracy == None :
                fn_ret_dict['status'] = False
            else :
                fn_ret_dict['status'] = True
        return fn_ret_dict

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# > TblUtil - end
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
@staticmethod
def CvsProcProxy(*in_argv) :
    in_arg_no = len(in_argv)
    new_arg_no = 6
    new_arg_list = [None] * new_arg_no
    min_arg_no = min(in_arg_no, new_arg_no)
    for crt_idx in range(min_arg_no) :
        new_arg_list[crt_idx] = in_argv[crt_idx]
    # set display_flag
    display_flag = True
    new_arg_list[new_arg_no - 1] = display_flag

    ret_info = TblUtil.CvsProcess(*new_arg_list)
    return ret_info

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def PrintHelp(in_module) :
        print()
        print("   Usage:")
        print()
        print("      python %s <path-or-url> [<targ-idx> [<iter-no> [<rnd-seed]]]" % (in_module))
        print()
        print('         <path-or-url>')
        print('            specifies either the file path or the url to')
        print('            the csv dataset')
        print()
        print('         <targ-idx>')
        print('            specifies the target column index')
        print('            starting with zero. If omitted, the last column')
        print('            is used as target')
        print()
        print('         <iter-no>')
        print('            specifies the number of predict iterations')
        print()
        print('         <rnd-seed>')
        print('            random seed for prediction test')
        print()
        return

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
@staticmethod
def Run(*in_argv) :

    import sys
    import os
    import ast

    module_name = os.path.basename(in_argv[0])
    param_list = in_argv[1:]

    print()
    print("- - - - - - - - - - - - - - - - - - - - - - - - ")
    print("   %s" % (str(module_name)))
    print()
    print("      Evaluates the predictive potential of a csv data table.")
    print("- - - - - - - - - - - - - - - - - - - - - - - - ")
    print("   Parans: %s" % (str(param_list)))

    param_no = len(param_list)
    if param_no == 0 :
        print("- - - - - - - - - - - - - - - - - - - - - - - - ")
        PrintHelp(module_name)
        print("- - - - - - - - - - - - - - - - - - - - - - - - ")
        return False

    argv_list = []
    for crt_idx in range(param_no) :
        if crt_idx == 0 :
            path_or_url = param_list[crt_idx]
            argv_list.append(path_or_url)
        elif crt_idx == 1 :
            targ_idx = int(param_list[crt_idx])
            argv_list.append(targ_idx)
        elif crt_idx == 2 :
            iter_no = int(param_list[crt_idx])
            argv_list.append(iter_no)
        elif crt_idx == 3 :
            rnd_seed = int(param_list[crt_idx])
            argv_list.append(rnd_seed)
        elif crt_idx == 4 :
            aux_param = ast.literal_eval(param_list[crt_idx])
            if not isinstance(aux_param, dict) :
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
                PrintHelp(module_name)
                print("- - - - - - - - - - - - - - - - - - - - - - - - ")
                return False
            aux_data = dict(aux_param)
            argv_list.append(aux_data)

    print("- - - - - - - - - - - - - - - - - - - - - - - - ")
    ret_info = CvsProcProxy(*argv_list)
    print("- - - - - - - - - - - - - - - - - - - - - - - - ")

    if ret_info['status'] :
        # normal exit
        return True
    else :
        print("Error:", ret_info['msg'])
        return False

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

if __name__ == "__main__":

    # from usap_common import *
    import sys

    ret_status = Run(*sys.argv)
    if ret_status :
        exit(0)
    else :
        exit(1)

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

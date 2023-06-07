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

"""
    Common utility module

        Tested with Winpython64-3.10.5.0
"""

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
    separator_string = ">-------------------------------------------------------------------------------"
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

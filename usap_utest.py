"""
Deodata Delanga Unit Test

    Module provides an unsystematic/opportunistic collection of tests.

        Tested with Winpython64-3.10.5.0
"""

#   c4pub@git 2023
#
# Latest version available at: https://github.com/c4pub/deodel
#

import usap_common
from usap_common import *

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
def UnitTestDeodel():

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Unit Test Deodel - begin
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    import traceback
    import sys
    import numpy as np
    import pandas as pd

    import deodel

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    utest_fail_counter = 0
    utest_test_no = 0

    sys.stdout.flush()
    sys.stderr.flush()

    test_thresh_list = [1, 2, 3]

    test_elem = -1
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 0
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")
        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)
    #'''#

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 0
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 0
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")
        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 1
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 1
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 1.0
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 1
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 1.5
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 1
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 2
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 2
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 2.1
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 2
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 1.5
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 1
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 2.0
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 2
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 3.0
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 3
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_thresh_list = [3.01, 4.005]
    test_elem = 3
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 0
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_thresh_list = [3.01, 4.005]
    test_elem = 3.01
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 1
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 3.5
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 1
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    test_elem = 5
    test_result = deodel.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

    test_expect = 2
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    tt1 = [['a',    1.01,   2.02,   'e'],
           ['b',    2,      3.01,   'd'],
           ['do',   "4",    5,      'g'],
           ['e',    2,      3.01,   'h'],
           ['cc',   '3.01', 4.01,   'cc']]

    iprnt ("- - - - tt1: ", tt1)

    tt2 = np.array(tt1)
    iprnt ("- - - - tt2: ", tt2)

    tt3 = tt2.tolist()
    iprnt ("- - - - tt3: ", tt3)

    test_result = tt3
    test_expect = [['a', '1.01', '2.02', 'e'],
                    ['b', '2', '3.01', 'd'], ['do', '4', '5', 'g'],
                    ['e', '2', '3.01', 'h'],
                    ['cc', '3.01', '4.01', 'cc']]

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    ty1 = ['one', 2, 3, "one"]
    iprnt ("- - - - ty1: ", ty1)

    iprnt ('- - - - ---')

    iprnt ()
    iprnt ("- - - - tt1: ", tt1)
    tt1b = deodel.Working.MatrixTranspose(tt1)
    iprnt ("- - - - tt1b: ", tt1b)
    tt1c = deodel.Working.MatrixTranspose(tt1b)
    iprnt ("- - - - tt1c: ", tt1c)
    iprnt ()
    iprnt ("- - - - tt1 == tt1c:", tt1 == tt1c)
    iprnt ()

    test_result = tt1c
    test_expect = tt1

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("- - - - ty1: ", ty1)
    ty1b = deodel.Working.MatrixTranspose(ty1)
    iprnt ("- - - - ty1b: ", ty1b)
    ty1c = deodel.Working.MatrixTranspose(ty1b)
    iprnt ("- - - - ty1c: ", ty1c)
    iprnt ()
    iprnt ("- - - - ty1 == ty1c:", ty1 == ty1c)
    iprnt ()

    test_result = ty1
    test_expect = ty1c

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    ttu = [['o']]
    iprnt ()
    iprnt ("- - - - ttu: ", ttu)
    ttub = deodel.Working.MatrixTranspose(ttu)
    iprnt ("- - - - ttub: ", ttub)
    ttuc = deodel.Working.MatrixTranspose(ttub)
    iprnt ("- - - - ttuc: ", ttuc)
    iprnt ()
    iprnt ("- - - - ttu == ttuc:", ttu == ttuc)
    iprnt ()

    test_result = ttu
    test_expect = ttuc

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    ttu = [ ['o'],
            ['b'],
            [1]]
    iprnt ()
    iprnt ("- - - - ttu: ", ttu)
    ttub = deodel.Working.MatrixTranspose(ttu)
    iprnt ("- - - - ttub: ", ttub)
    ttuc = deodel.Working.MatrixTranspose(ttub)
    iprnt ("- - - - ttuc: ", ttuc)
    iprnt ()
    iprnt ("- - - - ttu == ttuc:", ttu == ttuc)
    iprnt ()

    test_result = ttu
    test_expect = ttuc

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    ttu = [ ['o'], [9], ['e']]
    iprnt ()
    iprnt ("- - - - ttu: ", ttu)
    ttub = deodel.Working.MatrixTranspose(ttu)
    iprnt ("- - - - ttub: ", ttub)
    ttuc = deodel.Working.MatrixTranspose(ttub)
    iprnt ("- - - - ttuc: ", ttuc)
    iprnt ()
    iprnt ("- - - - ttu == ttuc:", ttu == ttuc)
    iprnt ()

    test_result = ttu
    test_expect = ttuc

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("ProcessVector and RevertVector test - int is num - 1")

    tv1 = ['e',    1,      3.01,   'h',     11,     None]

    # backup global state
    bkp_opmode_intisnum = deodel.opmode_intisnum
    iprnt ("- - - - bkp_opmode_intisnum:", bkp_opmode_intisnum)
    deodel.opmode_intisnum = True
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)
    iprnt ("- - - - tv1", tv1)
    ret_1 = deodel.Working.ProcessVector(tv1)
    iprnt ("- - - - ret_1", ret_1)
    tv2 = deodel.Working.RevertVector(ret_1[0], ret_1[2])
    iprnt ("- - - - tv2", tv2)

    test_result = tv1
    test_expect = tv2

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("ProcessVector and RevertVector test - int is num - 2")

    ret_1 = deodel.Working.ProcessVector(tv1)
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)
    iprnt ("- - - - ret_1", ret_1)
    tv3 = deodel.Working.RevertVector(ret_1[0], ret_1[2])
    iprnt ("- - - - tv3", tv3)

    test_result = tv1
    test_expect = tv3

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("ProcessVector and RevertVector test - int not num - 3")

    tv1 = ['e',    1,      3.01,   'h',     11,     None]

    deodel.opmode_intisnum = False
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)
    iprnt ("- - - - tv1", tv1)
    ret_1 = deodel.Working.ProcessVector(tv1)
    iprnt ("- - - - ret_1", ret_1)
    tv2 = deodel.Working.RevertVector(ret_1[0], ret_1[2])
    iprnt ("- - - - tv2", tv2)

    test_result = tv1
    test_expect = tv2

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("ProcessVector and RevertVector test - int not num - 4")

    ret_1 = deodel.Working.ProcessVector(tv1)
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)
    iprnt ("- - - - ret_1", ret_1)
    tv3 = deodel.Working.RevertVector(ret_1[0], ret_1[2])
    iprnt ("- - - - tv3", tv3)

    test_result = tv1
    test_expect = tv3

    # restore global state
    deodel.opmode_intisnum = bkp_opmode_intisnum
    iprnt ("- - - - restored deodel.opmode_intisnum:", deodel.opmode_intisnum)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [2.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width', False)
    expect_result = [2.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [1.5, 2.5, 3.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [5, 1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width', False)
    expect_result = [2, 3, 4]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [1.5, 2.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [2.5, 4.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 2, 3, 4, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width', False)
    expect_result = [2, 4]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [3.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [2 - 1.0/6, 3 + 1.0/6]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [1.5, 2.5, 3.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [3.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [2.5, 4.5, 6.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [4, 3, 1, 2, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [2.5, 4.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no)
    expect_result = [4.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 8
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 16
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    #t expect_result = [1.5, 1.5, 2.5, 2.5, 3.5, 3.5, 4.5, 4.5, 5.5, 5.5, 6.5, 6.5, 7.5, 7.5]
    expect_result = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    iprnt ("- - - - tv1", tv1)
    split_no = 5
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [ 2.5, 4.5, 6.5, 8.5 ]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [4, 3, 1, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [2.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [1.5, 2.5, 3.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [3, 3, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [3.0, 3.0, 3.5]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [3, 3, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', True)
    # expect_result = [4]
    expect_result = [3, 4]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [3, 3, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    # expect_result = [4]
    expect_result = [3]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2, -2, -2, -2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no)
    expect_result = [-2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2, -2, -2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = []
    expect_result = [-2, -2, -2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2, -2, -2, -2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width')
    expect_result = [-2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2, -2, -2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width', False)
    expect_result = [-2, -2, -2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [-2, -2, -2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', True)
    expect_result = [-2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width', False)
    expect_result = [-2, -2, -2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [-2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width', True)
    expect_result = [-2]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = []
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', True)
    expect_result = []

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = []
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_width - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_width', True)
    expect_result = []

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [10, 20, 30]
    iprnt ("- - - - tv1", tv1)
    split_no = 7
    iprnt ("- - - - eq_freq - split_no:", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    expect_result = [10, 15, 20, 25, 30]

    test_expect = expect_result
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1.2, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 7
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [1.2, 1.6, 2]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1.2, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [1.2 + 0.4/3, 2 - 0.4/3]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [1.2, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', False)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [1.6]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [3, 5, 3]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [5]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = False)
    iprnt ("- - - - ret_val", ret_val)
    # expect_result = [0]
    expect_result = [1.6653345369377348e-16]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    # expect_result = [1]
    expect_result = [1.6653345369377348e-16]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    # expect_result = [0.6666666666666665]
    expect_result = [1]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    # expect_result = [1]
    expect_result = [0.6666666666666665]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [1]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 5
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [1]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 6
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [0.8333333333333331, 1]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 7
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [0.714285714285714, 1]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 8
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [0.625, 1]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("NumSplit test")

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 9
    iprnt ("- - - - eq_freq - split_no:", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, 'eq_freq', no_dupl_flag = True)
    iprnt ("- - - - ret_val", ret_val)
    expect_result = [0.5555555555555558, 1]

    test_result = ret_val
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("deodel fit test - 1")

    # backup global state
    bkp_opmode_intisnum = deodel.opmode_intisnum
    iprnt ("- - - - bkp_opmode_intisnum:", bkp_opmode_intisnum)

    deodel.opmode_intisnum = True
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)

    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['do',  "4",    5,      'd'],
            ['b',   2,      3.01,   'h'],
            ['cc',  '3.01', 'az',   'e']]

    tt_y = [
            'one',
            2.0,
            3,
            "one",
            2
           ]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ()

    tt_transp_X = deodel.Working.MatrixTranspose(tt_X)
    iprnt ("- - - -        tt_transp_X:", tt_transp_X)

    # o1 = deodel.deodel.DeodataDelangaClassifier()
    tt_o = deodel.DeodataDelangaClassifier({'split_mode': 'eq_freq'})
    tt_o.fit(tt_X, tt_y)
    iprnt ()

    test_result = tt_o.attr_X.tolist()
    test_transp_result = deodel.Working.MatrixTranspose(test_result)

    ref_item = [[1, 2, 3, 2, 4], [3, 1, 2, 5, 1], [1, 2, 3, 2, 1], [1, 2, 2, 3, 1]]

    iprnt ("- - - - test_transp_result:", test_transp_result)
    iprnt ("- - - -           ref_item:", ref_item)
    iprnt ()

    test_expect = deodel.Working.MatrixTranspose(ref_item)

    iprnt ("- - - - tt_o.__dict__ :", tt_o.__dict__ )
    iprnt ()

    iprnt ("- - - - - - - - test_result:", test_result)
    iprnt ("- - - - - - - - test_expect:", test_expect)

    test_result = test_result
    test_expect = test_expect

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("deodel fit test - 2")

    deodel.opmode_intisnum = False
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)

    tt_X = [['a',   101.01,   'az',   'e'],
            [77,    "3.01",   3.01,   'd'],
            ['do',  103.03,   5,      'd'],
            [77,    102.02,   3.01,   'h'],
            [4,     '3.01',   'az',   'e']]

    tt_y = [
            'one',
            2.0,
            3,
            "one",
            2
           ]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ()

    tt_transp_X = deodel.Working.MatrixTranspose(tt_X)
    iprnt ("- - - -        tt_transp_X:", tt_transp_X)

    # o1 = deodel.deodel.DeodataDelangaClassifier()
    tt_o = deodel.DeodataDelangaClassifier({'split_mode': 'eq_freq'})
    tt_o.fit(tt_X, tt_y)
    iprnt ()

    test_result = tt_o.attr_X.tolist()
    test_transp_result = deodel.Working.MatrixTranspose(test_result)

    ref_item = [[1, 2, 3, 2, 4], [2, 1, 4, 3, 1], [1, 4, 2, 4, 1], [1, 2, 2, 3, 1]]

    iprnt ("- - - - test_transp_result:", test_transp_result)
    iprnt ("- - - -           ref_item:", ref_item)
    iprnt ()

    test_expect = deodel.Working.MatrixTranspose(ref_item)

    deodel.opmode_intisnum = bkp_opmode_intisnum
    iprnt ("- - - - restored deodel.opmode_intisnum:", deodel.opmode_intisnum)

    iprnt ("- - - - tt_o.__dict__ :", tt_o.__dict__ )
    iprnt ()

    iprnt ("- - - - - - - - test_result:", test_result)
    iprnt ("- - - - - - - - test_expect:", test_expect)

    test_result = test_result
    test_expect = test_expect

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("predict test")

    tt_test = tt_X[:]
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_y

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("predict test")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2.0,    5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'B',
            'B',
            'C',
            'A',
           ]

    tt_o = deodel.DeodataDelangaClassifier()
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("dealing with missing attributes (None), ignore them")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    None,   'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   None,   'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2.0,    5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'A',
            'B',
            'C',
            'A',
           ]

    tt_o = deodel.DeodataDelangaClassifier()
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("behaviour when no tie break")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2.0,    5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'A',
            'B',
            'C',
            'A',
           ]

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("integer mix in prediction - opmode_intisnum: true")
    iprnt ()

    bkp_opmode_intisnum = deodel.opmode_intisnum
    iprnt ("- - - - bkp_opmode_intisnum:", bkp_opmode_intisnum)
    deodel.opmode_intisnum = True
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)

    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5,      'd'],
            ['b',   2,      3.01,   'h'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'B',
            'B',
            'C',
            'A',
           ]

    tt_o = deodel.DeodataDelangaClassifier()
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("integer mix in prediction - opmode_intisnum: false")
    iprnt ()

    deodel.opmode_intisnum = False
    iprnt ("- - - - deodel.opmode_intisnum:", deodel.opmode_intisnum)

    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'B',
            'B',
            'A',
            'A',
           ]

    tt_o = deodel.DeodataDelangaClassifier()
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("integer mix in dealing with missing attributes - opmode_intisnum: false")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    None,   'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   None,   'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'A',
            'B',
            'B',
            'A',
           ]

    tt_o = deodel.DeodataDelangaClassifier()
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("integer mix in no tie break - opmode_intisnum: false")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'A',
            'B',
            'A',
            'A',
           ]

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    deodel.opmode_intisnum = bkp_opmode_intisnum
    iprnt ("- - - - restored deodel.opmode_intisnum:", deodel.opmode_intisnum)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("behaviour when no tie break")
    iprnt ()

    tt_X = [['a',   None,  'a'],
            ['a',   None,  'b'],
            ['c',   'c',   'c'],
            ['d',   'c',   'c'],
            ['e',   'd',   'd'],
            ['e',   'e',   'd']]

    tt_y = [
            'X',
            'X',
            'Y',
            'Y',
            'Y',
            'Z',
           ]

    tt_test= [
            ['c',   None,  'c'],
            ['a',   'c',   'd']]

    tt_exp = [
            'Y',
            'Y',
           ]

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)
    #'''#

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input - 1")
    iprnt ()

    tt_X = [
            ['a',   None,  'b'],
            ['c',   99.0,   'c'],
            [],
            ['d',   'c'],
            ['e'],
            ['e',   101,   None],
            ]

    iprnt ("- - - - tt_X:", tt_X)

    tt_y = [
            'X',
            'X',
            'Y',
            'Y',
            'Y',
            'Z',
           ]

    iprnt ("- - - - tt_y:", tt_y)

    tt_test= [
            ['c',   None,  'c'],
            ['a',   'c']]

    iprnt ("- - - - tt_test:", tt_test)

    tt_exp = [
            'X',
            'X',
           ]

    iprnt ("- - - - tt_exp:", tt_exp)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input - 2")
    iprnt ()

    tt_X = [['a'],
            ['a',   None,  'b'],
            ['c',   99.0,   'c'],
            ['d',   'c'],
            ['e'],
            ['e',   101,   None]]

    iprnt ("- - - - tt_X:", tt_X)

    tt_y = [
            'X',
            'X',
            'Y',
            'Y',
            'Y',
            'Z',
           ]

    iprnt ("- - - - tt_y:", tt_y)

    tt_test= [
            ['c',   None,  'c'],
            ['a',   'c']]

    iprnt ("- - - - tt_test:", tt_test)

    tt_exp = [
            'Y',
            'X',
           ]

    iprnt ("- - - - tt_exp:", tt_exp)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input - 3")
    iprnt ()

    tt_X = [['a'],
            ['a',   None,  'b'],
            ['c',   99.0,   'c'],
            ['d',   'c'],
            ['e'],
            ['e',   101,   None]]

    iprnt ("- - - - tt_X:", tt_X)

    tt_y = [
            'X',
            'X',
            'Y',
            'Y',
           ]

    iprnt ("- - - - tt_y:", tt_y)

    tt_test= [
            ['c',   None,  'c'],
            ['a',   'c']]

    iprnt ("- - - - tt_test:", tt_test)

    tt_exp = [
            'Y',
            'X',
           ]

    iprnt ("- - - - tt_exp:", tt_exp)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input - 4")
    iprnt ()

    tt_X = [['a'],
            ['a',   None,  'b'],
            ['c',   99.0,   'c'],
            ['d',   'c'],
            ['e'],
            ['e',   101,   None]]

    iprnt ("- - - - tt_X:", tt_X)

    tt_y = [
            'X',
            'X',
            'Y',
            'Y',
            'Y',
            'Z',
            'X',
            'X',
            'Y',
            'Y',
           ]

    iprnt ("- - - - tt_y:", tt_y)

    tt_test= [
            ['c',   None,  'c'],
            ['a',   'c']]

    iprnt ("- - - - tt_test:", tt_test)

    tt_exp = [
            'Y',
            'X',
           ]

    iprnt ("- - - - tt_exp:", tt_exp)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input - 5")
    iprnt ()

    tt_X = [['a'],
            ['a',   None,  'b'],
            ['c',   99.0,   'c'],
            ['d',   'c'],
            ['e'],
            ['e',   101,   None]]

    iprnt ("- - - - tt_X:", tt_X)

    tt_y = [
           ]

    iprnt ("- - - - tt_y:", tt_y)

    tt_test= [
            ['c',   None,  'c'],
            ['a',   'c']]

    iprnt ("- - - - tt_test:", tt_test)

    tt_exp = [
            None,
            None,
           ]

    iprnt ("- - - - tt_exp:", tt_exp)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input - bis 5-a")
    iprnt ()

    tt_X = [['a'],
            ['a',   None,  'b'],
            ['c',   99.0,   'c'],
            ['d',   'c'],
            ['e'],
            ['e',   101,   None]]

    iprnt ("- - - - tt_X:", tt_X)

    tt_y = [
            'X',
            'X',
            'Y',
            'Y',
           ]

    iprnt ("- - - - tt_y:", tt_y)

    tt_test= [
            ['c',   None,  'c', 'zzz', 555],
            ['a',   'c']]

    iprnt ("- - - - tt_test:", tt_test)

    tt_exp = [
            'Y',
            'X',
           ]

    iprnt ("- - - - tt_exp:", tt_exp)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological ref - 6")
    iprnt ()

    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            'C',
            'A',
            'B',
            'B',
            'A',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input - 7")
    iprnt ()

    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    tt_y = [
            ['C'],
            ['A'],
            ['B'],
            ['B'],
            ['A'],
            ['A']
           ]

    tt_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological ref pd - 8")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            'C',
            'A',
            'B',
            'B',
            # 'A',
            102,
            'A'
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    tt_X = pd.array(t1_X)
    tt_y = pd.array(t1_y)
    tt_test = pd.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input pd - 9")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            ['C'],
            ['A'],
            ['B'],
            ['B'],
            # ['A'],
            [102],
            ['A']
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    tt_X = pd.array(t1_X)
    tt_y = pd.array(t1_y)
    tt_test = pd.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input pd - 10")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            'C',
            'A',
            'B',
            'B',
            102,
            'A'
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    tt_y = pd.DataFrame(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input pd - 11")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            ['C'],
            ['A'],
            ['B'],
            ['B'],
            [102],
            ['A']
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    tt_y = pd.DataFrame(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input pd - 12")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            ['C'],
            ['A'],
            ['B'],
            ['B'],
            [102],
            ['A']
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    tt_y = pd.DataFrame(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input pd - 13")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            ['C'],
            ['A'],
            ['B'],
            ['B'],
            [102],
            ['A']
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    # tt_y = pd.DataFrame(t1_y)
    tt_y = pd.Series(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input pd - 14")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,         ],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            'C',
            'A',
            'B',
            'B',
            102,
            'A'
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'C',
            'A',
            'B',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    tt_y = pd.Series(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological ref np - 1")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,      None],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            'C',
            'A',
            'B',
            'B',
            'A',
            'A'
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'A',
            'A',
            'C',
            'C',
           ]

    tt_X = np.array(t1_X)
    tt_y = np.array(t1_y)
    tt_test = np.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pathological input np - 2")
    iprnt ()

    t1_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    5.0,    'd'],
            ['b',    2.0,   3.01,   'h'],
            ['a',    3,     4,      None],
            ['d',    -1.0,  None,   'i'],
            ['c',   '3.01', 'az',   'e']]

    t1_y = [
            ['C'],
            ['A'],
            ['B'],
            ['B'],
            ['A'],
            ['A']
           ]

    t1_test = [
            ['a',   1.01,   5.0,    'd'],
            ['b',   "3.01", 3.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   'e']]

    tt_exp = [
            'A',
            'A',
            'C',
            'C',
           ]

    tt_X = np.array(t1_X)
    tt_y = np.array(t1_y)
    tt_test = np.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("ListDataConvert pd 1")
    iprnt ()

    tin_1 =    [['a',    3,                ],
                ['b',   "3.01", 3.01,   'd'],
                ['b',    2.0,   3.01       ],
                ['d',    -1.0,  None,   'i'],
                ['c',   '3.01', 'az',   'e']]

    tin_2 =    [
                ['C'],
                [],
                ['B'],
                [102],
                ['A']
               ]

    tin_3 =    [
                'C',
                None,
                'B',
                102,
                'A',
               ]

    iprnt ("- - - - tin_1:", tin_1)
    iprnt ("- - - - tin_2:", tin_2)
    iprnt ("- - - - tin_3:", tin_3)

    # tt_in_1 = pd.DataFrame(tin_1)
    tt_in_1 = pd.array(tin_1)
    tt_in_2 = pd.array(tin_2)
    tt_in_3 = pd.array(tin_3)
    
    iprnt ("- - - - tt_in_1:", tt_in_1)
    iprnt ("- - - - tt_in_2:", tt_in_2)
    iprnt ("- - - - tt_in_3:", tt_in_3)

    tout_1 = deodel.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel.CasetDeodel.ListDataConvert(tt_in_3)

    iprnt ("- - - - tout_1:", tout_1)
    iprnt ("- - - - tout_2:", tout_2)
    iprnt ("- - - - tout_3:", tout_3)

    test_result = (tout_1, tout_2, tout_3)
    test_expect = (tin_1, tin_2, tin_3)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("ListDataConvert pd 2")
    iprnt ()

    tin_1 =    [['a',    3,                ],
                ['b',   "3.01", 3.01,   'd'],
                ['b',    2.0,   3.01       ],
                ['d',    -1.0,  None,   'i'],
                ['c',   '3.01', 'az',   'e']]

    tin_2 =    [
                ['C'],
                [],
                ['B'],
                [102],
                ['A']
               ]

    tin_3 =    [
                'C',
                None,
                'B',
                102,
                'A',
               ]

    iprnt ("- - - - tin_1:", tin_1)
    iprnt ("- - - - tin_2:", tin_2)
    iprnt ("- - - - tin_3:", tin_3)

    # tt_in_1 = pd.array(tin_1)
    tt_in_1 = pd.DataFrame(tin_1)
    tt_in_2 = pd.DataFrame(tin_2)
    tt_in_3 = pd.DataFrame(tin_3)
    
    iprnt ("- - - - tt_in_1:", tt_in_1)
    iprnt ("- - - - tt_in_2:", tt_in_2)
    iprnt ("- - - - tt_in_3:", tt_in_3)

    tout_1 = deodel.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel.CasetDeodel.ListDataConvert(tt_in_3)

    iprnt ("- - - - tout_1:", tout_1)
    iprnt ("- - - - tout_2:", tout_2)
    iprnt ("- - - - tout_3:", tout_3)


    texp_1 =    [['a',    3,    None,   None],
                ['b',   "3.01", 3.01,   'd'],
                ['b',    2.0,   3.01,   None],
                ['d',    -1.0,  None,   'i'],
                ['c',   '3.01', 'az',   'e']]

    texp_2 =    [
                ['C'],
                [None],
                ['B'],
                [102],
                ['A']
               ]

    texp_3 =    [
                ['C'],
                [None],
                ['B'],
                [102],
                ['A']
               ]

    test_result = (tout_1, tout_2, tout_3)
    test_expect = (texp_1, texp_2, texp_3)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("ListDataConvert pd 3")
    iprnt ()

    tin_1 =    [['a',    3,                ],
                ['b',   "3.01", 3.01,   'd'],
                ['b',    2.0,   3.01       ],
                ['d',    -1.0,  None,   'i'],
                ['c',   '3.01', 'az',   'e']]

    tin_2 =    [
                ['C'],
                [],
                ['B'],
                [102],
                ['A']
               ]

    tin_3 =    [
                'C',
                None,
                'B',
                102,
                'A',
               ]

    iprnt ("- - - - tin_1:", tin_1)
    iprnt ("- - - - tin_2:", tin_2)
    iprnt ("- - - - tin_3:", tin_3)

    # tt_in_1 = pd.array(tin_1)
    # tt_in_1 = pd.DataFrame(tin_1)
    tt_in_1 = pd.Series(tin_1)
    tt_in_2 = pd.Series(tin_2)
    tt_in_3 = pd.Series(tin_3)
    
    iprnt ("- - - - tt_in_1:", tt_in_1)
    iprnt ("- - - - tt_in_2:", tt_in_2)
    iprnt ("- - - - tt_in_3:", tt_in_3)

    tout_1 = deodel.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel.CasetDeodel.ListDataConvert(tt_in_3)

    iprnt ("- - - - tout_1:", tout_1)
    iprnt ("- - - - tout_2:", tout_2)
    iprnt ("- - - - tout_3:", tout_3)


    texp_1 =    [['a',    3],
                ['b',   "3.01", 3.01,   'd'],
                ['b',    2.0,   3.01],
                ['d',    -1.0,  None,   'i'],
                ['c',   '3.01', 'az',   'e']]

    texp_2 =    [
                ['C'],
                [],
                ['B'],
                [102],
                ['A']
               ]

    texp_3 =    [
                'C',
                None,
                'B',
                102,
                'A'
               ]

    test_result = (tout_1, tout_2, tout_3)
    test_expect = (texp_1, texp_2, texp_3)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("ListDataConvert np 1")
    iprnt ()

    tin_1 =    [['a',    3,                ],
                ['b',   "3.01", 3.01,   'd'],
                ['b',    2.0,   3.01       ],
                ['d',    -1.0,  None,   'i'],
                ['c',   '3.01', 'az',   'e']]

    tin_2 =    [
                ['C'],
                [],
                ['B'],
                [102],
                ['A']
               ]

    tin_3 =    [
                'C',
                None,
                'B',
                102,
                'A',
               ]

    iprnt ("- - - - tin_1:", tin_1)
    iprnt ("- - - - tin_2:", tin_2)
    iprnt ("- - - - tin_3:", tin_3)

    tt_in_1 = np.array(tin_1)
    tt_in_2 = np.array(tin_2)
    tt_in_3 = np.array(tin_3)
    
    iprnt ("- - - - tt_in_1:", tt_in_1)
    iprnt ("- - - - tt_in_2:", tt_in_2)
    iprnt ("- - - - tt_in_3:", tt_in_3)

    tout_1 = deodel.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel.CasetDeodel.ListDataConvert(tt_in_3)

    iprnt ("- - - - tout_1:", tout_1)
    iprnt ("- - - - tout_2:", tout_2)
    iprnt ("- - - - tout_3:", tout_3)

    test_result = (tout_1, tout_2, tout_3)
    test_expect = (tin_1, tin_2, tin_3)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("check version")
    iprnt ()

    test_result = deodel.DeodataDelangaClassifier.version
    # test_expect = 1.51
    # test_expect = 1.65
    # test_expect = 1.75
    # test_expect = 1.77
    test_expect = 2.01

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("pandas data - 1")
    iprnt ()

    tt_X = [['a',   None,  'a'],
            ['a',   None,  'b'],
            ['c',   'c',   'c'],
            ['d',   'c',   'c'],
            ['e',   'd',   'd'],
            ['e',   'e',   'd']]

    tt_y = [
            'X',
            'X',
            'Y',
            'Y',
            'Y',
            'Z',
           ]

    tt_test= [
            ['c',   None,  'c'],
            ['a',   'c',   'd']]

    tt_pd_X = pd.DataFrame(tt_X)
    tt_pd_test = pd.DataFrame(tt_test)
    tt_pd_y = pd.Series(tt_y)
    
    tt_exp = [
            'Y',
            'Y',
           ]

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_pd_X, tt_pd_y)
    tt_predict = tt_o.predict(tt_pd_test)
    iprnt ()

    test_result = tt_predict
    test_expect = tt_exp

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression test 1")
    iprnt ()

    # regr_fn_coeff = [1, -1, 2, -0.5, 3, -2]
    regr_fn_coeff = [1, 0, 1]

    def RegressFn(in_attr_list, in_fn_coeff = None) :
        if in_fn_coeff == None :
            in_fn_coeff = [1.0, 2.0, -0.5]
        coeff_len = len(in_fn_coeff)
        attr_len = len(in_attr_list)
        use_len = min(coeff_len, attr_len)
        ret_val = 0
        for crt_idx in range(use_len) :
            ret_val += in_attr_list[crt_idx] * in_fn_coeff[crt_idx]
        return ret_val

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_col_no = 2
    data_train_row_no = 10
    # data_test_row_no = 2
    data_test_row_no = data_train_row_no
    data_tot_row_no = data_train_row_no + data_test_row_no

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_tbl = []
    data_y_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = []
        for crt_idx_col in range(data_attr_col_no) :
            crt_row.append(((crt_idx_row)/(data_tot_row_no)))
        data_attr_tbl.append(crt_row)
        y_fn = RegressFn(crt_row, regr_fn_coeff)
        data_y_vect.append(y_fn)

    data_attr_train_tbl = []
    data_attr_test_tbl = []
    data_y_train_vect = []
    data_y_test_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = data_attr_tbl[crt_idx_row][:]
        if crt_idx_row % 2 == 0 :
            data_attr_train_tbl.append(crt_row[:])
            data_y_train_vect.append(data_y_vect[crt_idx_row])
        else :
            data_attr_test_tbl.append(crt_row[:])
            data_y_test_vect.append(data_y_vect[crt_idx_row])

    X_train = data_attr_train_tbl
    y_train = data_y_train_vect

    X_test = data_attr_test_tbl
    y_test = data_y_test_vect

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # import deodel
    # deodel_regress = deodel.DeodataDelangaClassifier()
    # deodel_regress = deodel.DeodataDelangaClassifier({'split_no': 5, 'split_mode': 'eq_freq'})
    deodel_regress = deodel.DeodataDelangaClassifier({'split_no': 10, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    # ret_data = deodel_regress.tweak()
    y_pred = deodel_regress.predict(X_test)
    # ret_data = deodel_regress.tweak()
    t_pred = y_pred

    from sklearn import metrics
    t_mae = metrics.mean_absolute_error(y_test, y_pred)
    t_mse = metrics.mean_squared_error(y_test, y_pred)
    t_R2 = metrics.r2_score(y_test, y_pred)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.0, 0.1, 0.2, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9]
    e_mae = 0.04999999999999998
    e_mse = 0.0024999999999999988
    e_R2 = 0.9696969696969697

    test_result = (t_pred, t_mae, t_mse, t_R2)
    test_expect = (e_pred, e_mae, e_mse, e_R2)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression test 2")
    iprnt ()

    # regr_fn_coeff = [1, -1, 2, -0.5, 3, -2]
    regr_fn_coeff = [1, 0, 1]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_col_no = 2
    data_train_row_no = 10
    # data_test_row_no = 2
    data_test_row_no = data_train_row_no
    data_tot_row_no = data_train_row_no + data_test_row_no

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_tbl = []
    data_y_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = []
        for crt_idx_col in range(data_attr_col_no) :
            crt_row.append(((crt_idx_row)/(data_tot_row_no)))
        data_attr_tbl.append(crt_row)
        y_fn = RegressFn(crt_row, regr_fn_coeff)
        data_y_vect.append(y_fn)

    data_attr_train_tbl = []
    data_attr_test_tbl = []
    data_y_train_vect = []
    data_y_test_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = data_attr_tbl[crt_idx_row][:]
        if crt_idx_row % 2 == 0 :
            data_attr_train_tbl.append(crt_row[:])
            data_y_train_vect.append(data_y_vect[crt_idx_row])
        else :
            data_attr_test_tbl.append(crt_row[:])
            data_y_test_vect.append(data_y_vect[crt_idx_row])

    X_train = data_attr_train_tbl
    y_train = data_y_train_vect

    X_test = data_attr_test_tbl
    y_test = data_y_test_vect

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'split_no': 4, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    from sklearn import metrics
    t_mae = metrics.mean_absolute_error(y_test, y_pred)
    t_mse = metrics.mean_squared_error(y_test, y_pred)
    t_R2 = metrics.r2_score(y_test, y_pred)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.1, 0.1, 0.35, 0.35, 0.55, 0.55, 0.55, 0.8, 0.8, 0.8]
    
    e_mae = 0.06499999999999999
    e_mse = 0.006249999999999997
    e_R2 = 0.9242424242424243

    test_result = (t_pred, t_mae, t_mse, t_R2)
    test_expect = (e_pred, e_mae, e_mse, e_R2)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression test 3")
    iprnt ()

    # regr_fn_coeff = [1, -1, 2, -0.5, 3, -2]
    regr_fn_coeff = [1, 0, 1]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_col_no = 2
    data_train_row_no = 10
    # data_test_row_no = 2
    data_test_row_no = data_train_row_no
    data_tot_row_no = data_train_row_no + data_test_row_no

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_tbl = []
    data_y_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = []
        for crt_idx_col in range(data_attr_col_no) :
            crt_row.append(((crt_idx_row)/(data_tot_row_no)))
        data_attr_tbl.append(crt_row)
        y_fn = RegressFn(crt_row, regr_fn_coeff)
        data_y_vect.append(y_fn)

    data_attr_train_tbl = []
    data_attr_test_tbl = []
    data_y_train_vect = []
    data_y_test_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = data_attr_tbl[crt_idx_row][:]
        if crt_idx_row % 2 == 0 :
            data_attr_train_tbl.append(crt_row[:])
            data_y_train_vect.append(data_y_vect[crt_idx_row])
        else :
            data_attr_test_tbl.append(crt_row[:])
            data_y_test_vect.append(data_y_vect[crt_idx_row])

    X_train = data_attr_train_tbl
    y_train = data_y_train_vect

    X_test = data_attr_test_tbl
    y_test = data_y_test_vect

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'predict_mode': 'regress', 'split_no': 4, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    from sklearn import metrics
    t_mae = metrics.mean_absolute_error(y_test, y_pred)
    t_mse = metrics.mean_squared_error(y_test, y_pred)
    t_R2 = metrics.r2_score(y_test, y_pred)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.1, 0.1, 0.35, 0.35, 0.55, 0.55, 0.55, 0.8, 0.8, 0.8]
    
    e_mae = 0.06499999999999999
    e_mse = 0.006249999999999997
    e_R2 = 0.9242424242424243

    test_result = (t_pred, t_mae, t_mse, t_R2)
    test_expect = (e_pred, e_mae, e_mse, e_R2)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression test 4")
    iprnt ()

    # regr_fn_coeff = [1, -1, 2, -0.5, 3, -2]
    regr_fn_coeff = [1, 0, 1]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_col_no = 2
    data_train_row_no = 10
    # data_test_row_no = 2
    data_test_row_no = data_train_row_no
    data_tot_row_no = data_train_row_no + data_test_row_no

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    data_attr_tbl = []
    data_y_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = []
        for crt_idx_col in range(data_attr_col_no) :
            crt_row.append(((crt_idx_row)/(data_tot_row_no)))
        data_attr_tbl.append(crt_row)
        y_fn = RegressFn(crt_row, regr_fn_coeff)
        data_y_vect.append(y_fn)

    data_attr_train_tbl = []
    data_attr_test_tbl = []
    data_y_train_vect = []
    data_y_test_vect = []

    for crt_idx_row in range(data_tot_row_no) :
        crt_row = data_attr_tbl[crt_idx_row][:]
        if crt_idx_row % 2 == 0 :
            data_attr_train_tbl.append(crt_row[:])
            data_y_train_vect.append(data_y_vect[crt_idx_row])
        else :
            data_attr_test_tbl.append(crt_row[:])
            data_y_test_vect.append(data_y_vect[crt_idx_row])

    X_train = data_attr_train_tbl
    y_train = data_y_train_vect

    X_test = data_attr_test_tbl
    y_test = data_y_test_vect

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'predict_mode': 'classif', 'split_no': 4, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    from sklearn import metrics
    t_mae = metrics.mean_absolute_error(y_test, y_pred)
    t_mse = metrics.mean_squared_error(y_test, y_pred)
    t_R2 = metrics.r2_score(y_test, y_pred)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.0, 0.0, 0.3, 0.3, 0.5, 0.5, 0.5, 0.7, 0.7, 0.7]
    
    e_mae = 0.1
    e_mse = 0.014500000000000002
    e_R2 = 0.8242424242424242

    test_result = (t_pred, t_mae, t_mse, t_R2)
    test_expect = (e_pred, e_mae, e_mse, e_R2)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 1")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 0.0, 'a'], [0.1, 0.1, 'a'], [0.2, 0.2, 'a'], [0.3, 0.3, 'a'], [0.4, 0.4, 'a'], 
               [0.5, 0.5, 'a'], [0.6, 0.6, 'a'], [0.7, 0.7, 'a'], [0.8, 0.8, 'a'], [0.9, 0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'y', 'z', 'x']

    X_test = [[0.05, 0.05, 'b'], [0.15, 0.15, 'b'], [0.25, 0.25, 'b'], [0.35, 0.35, 'b'], [0.45, 0.45, 'b'], 
              [0.55, 0.55, 'b'], [0.65, 0.65, 'b'], [0.75, 0.75, 'b'], [0.85, 0.85, 'b'], [0.95, 0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'split_no': 10, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.0, 0.1, 0.2, 0.3, 0.5, 'x', 'y', 'z', 'x', 'x']

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 2")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a'], [0.1, 'a'], [0.2, 'a'], [0.3, 'a'], [0.4, 'a'], 
               [0.5, 'a'], [0.6, 'a'], [0.7, 'a'], [0.8, 'a'], [0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'x', 'y', 'z']

    X_test = [[0.05, 'b'], [0.15, 'b'], [0.25, 'b'], [0.35, 'b'], [0.45, 'b'], 
              [0.55, 'b'], [0.65, 'b'], [0.75, 'b'], [0.85, 'b'], [0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'split_no': 10, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.0, 0.1, 0.2, 0.3, 0.5, 'x', 'x', 'y', 'z', 'z']

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 3")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a', 'g'], [0.1, 'a', 'g'], [0.2, 'a', 'g'], [0.3, 'a', 'g'], [0.4, 'a', 'g'], 
               [0.5, 'a', 'g'], [0.6, 'a', 'g'], [0.7, 'a', 'g'], [0.8, 'a', 'g'], [0.9, 'a', 'g']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 'x', 'x', 'y']

    X_test = [[0.05, 'b', 'h'], [0.15, 'b', 'h'], [0.25, 'b', 'h'], [0.35, 'b', 'h'], [0.45, 'b', 'h'], 
              [0.55, 'b', 'h'], [0.65, 'b', 'h'], [0.75, 'b', 'h'], [0.85, 'b', 'h'], [0.95, 'b', 'h']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'split_no': 2, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.2, 0.2, 0.2, 0.2, 0.55, 0.55, 0.55, 0.55, 0.55, 0.55]

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 4")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a', 'g'], [0.1, 'a', 'g'], [0.2, 'a', 'g'], [0.3, 'a', 'g'], [0.4, 'a', 'g'], 
               [0.5, 'a', 'g'], [0.6, 'a', 'g'], [0.7, 'a', 'g'], [0.8, 'a', 'g'], [0.9, 'a', 'g']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 'x', 'x', 'y']

    X_test = [[0.05, 'b', 'h'], [0.15, 'b', 'h'], [0.25, 'b', 'h'], [0.35, 'b', 'h'], [0.45, 'b', 'h'], 
              [0.55, 'b', 'h'], [0.65, 'b', 'h'], [0.75, 'b', 'h'], [0.85, 'b', 'h'], [0.95, 'b', 'h']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'predict_mode': 'classif', 'split_no': 2, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = [0.0, 0.0, 0.0, 0.0, 'x', 'x', 'x', 'x', 'x', 'x']

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 5")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1'], 
                ['a2', 'b1', 'c2', 'd1', 'e1', 'f1'], 
                ['a3', 'b1', 'c2', 'd2', 'e2', 'f1'], 
                ['a4', 'b2', 'c4', 'd2', 'e2', 'f1'], 
                ['a5', 'b2', 'c2', 'd2', 'e2', 'f1'], 
                ['a6', 'b2', 'c6', 'd2', 'e2', 'f2']
              ]

    y_train = [0.1, 0.2, 0.3, 'x', 'y', 'y']

    X_test =  [
                ['a7', 'b1', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b3', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c4', 'd7', 'e7', 'f7'], 
                ['a6', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c7', 'd7', 'e2', 'f7'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f1'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f7'], 
              ]

    y_expect = [
                0.2, 
                0.2, 
                0.25, 
                'x', 
                0.25,
                'y',
                0.3,
                'y',
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'predict_mode': 'regress', 'split_no': 2, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 6")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['n', 12, 'm'],
                ['y', 16, 'f'],
                ['y', 20, 'm'],
                ['y', 21, 'f'],
                ['n', 29, 'm'],
              ]

    y_train = [
                'juice',
                'coffee',
                0.05,
                0.04,
                0.40,
              ]

    X_test =  [
                ['n', 12, 'm'],
                ['y', 16, 'f'],
                ['y', 20, 'm'],
                ['y', 21, 'f'],
                ['n', 29, 'm'],
                ['y', 18, 'f'],
                ['y', 27, 'f'],
              ]

    y_expect = [
                'juice',
                'coffee',
                0.05,
                0.04,
                0.40,
                'coffee',
                0.04,
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'predict_mode': 'classif', 'split_no': 2, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 7")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['n', 12, 'm'],
                ['y', 16, 'f'],
                ['y', 15, 'f'],
                ['m', 14, 'm'],
                ['y', 20, 'm'],
                ['n', 22, 'm'],
                ['y', 21, 'f'],
                ['n', 31, 'f'],
                ['n', 29, 'm'],
              ]

    y_train = [
                'juice',
                'coffee',
                'juice',
                'coffee',
                0.05,
                0.04,
                0.06,
                0.13,
                0.40,
              ]

    X_test =  [
                ['n', 12, 'm'],
                ['y', 16, 'f'],
                ['y', 20, 'm'],
                ['y', 21, 'f'],
                ['n', 29, 'm'],
                ['y', 18, 'f'],
                ['y', 27, 'f'],
              ]

    y_expect = [
                'juice',
                0.06,
                0.05,
                0.06,
                0.22,
                0.06,
                0.095,
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # deodel_regress = deodel.DeodataDelangaClassifier({'predict_mode': 'regress', 'split_no': 2, 'split_mode': 'eq_width'})
    deodel_regress = deodel.DeodataDelangaClassifier({'split_no': 2, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression mixed test 8")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['n', 12, 'm'],
                ['y', 16, 'f'],
                ['y', 15, 'f'],
                ['m', 14, 'm'],
                ['y', 20, 'm'],
                ['n', 22, 'm'],
                ['y', 21, 'f'],
                ['n', 31, 'f'],
                ['n', 29, 'm'],
              ]

    y_train = [
                'juice',
                'coffee',
                'juice',
                'coffee',
                0.05,
                0.04,
                0.06,
                0.13,
                0.40,
              ]

    X_test =  [
                ['n', 12, 'm'],
                ['y', 16, 'f'],
                ['y', 20, 'm'],
                ['y', 21, 'f'],
                ['n', 29, 'm'],
                ['y', 18, 'f'],
                ['y', 27, 'f'],
              ]

    y_expect = [
                'juice',
                'juice',
                0.05,
                'juice',
                0.04,
                'juice',
                'juice',
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodel_regress = deodel.DeodataDelangaClassifier({'predict_mode': 'classif', 'split_no': 2, 'split_mode': 'eq_width'})

    deodel_regress.fit(X_train,y_train)
    y_pred = deodel_regress.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = (t_pred)
    test_expect = (e_pred)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -






    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression vs classificatiion test 1")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1'], 
                ['a2', 'b1', 'c2', 'd1', 'e1', 'f1'], 
                ['a3', 'b1', 'c2', 'd2', 'e2', 'f1'], 
                ['a4', 'b2', 'c4', 'd2', 'e2', 'f1'], 
                ['a5', 'b2', 'c2', 'd2', 'e2', 'f1'], 
                ['a6', 'b2', 'c6', 'd2', 'e2', 'f2'],
                ['a7', 'b2', 'c6', 'd2', 'e2', 'f2'],
              ]

    y_train = ['x', 1, 2, 3, 4, 'y', 'y', 'y']

    X_test =  [
                ['a7', 'b1', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b3', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c4', 'd7', 'e7', 'f7'], 
                ['a6', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c7', 'd7', 'e2', 'f7'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f1'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f7'], 
              ]

    y_expect = [
                0.2, 
                0.2, 
                0.25, 
                'x', 
                0.25,
                'y',
                0.3,
                'y',
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodelo = deodel.DeodataDelangaClassifier()

    # tst_1 = deodelo.regress_flag
    deodelo.fit(X_train,y_train)
    tst_val = deodelo.regress_flag
    y_pred = deodelo.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = tst_val
    test_expect = False

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression vs classificatiion test 2")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1'], 
                ['a2', 'b1', 'c2', 'd1', 'e1', 'f1'], 
                ['a3', 'b1', 'c2', 'd2', 'e2', 'f1'], 
                ['a4', 'b2', 'c4', 'd2', 'e2', 'f1'], 
                ['a5', 'b2', 'c2', 'd2', 'e2', 'f1'], 
                ['a6', 'b2', 'c6', 'd2', 'e2', 'f2'],
                ['a7', 'b2', 'c6', 'd2', 'e2', 'f2'],
              ]

    y_train = ['x', 1, 2, 3, 4, 5, 'y', 'y']

    X_test =  [
                ['a7', 'b1', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b3', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c4', 'd7', 'e7', 'f7'], 
                ['a6', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c7', 'd7', 'e2', 'f7'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f1'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f7'], 
              ]

    y_expect = [
                0.2, 
                0.2, 
                0.25, 
                'x', 
                0.25,
                'y',
                0.3,
                'y',
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodelo = deodel.DeodataDelangaClassifier()

    # tst_1 = deodelo.regress_flag
    deodelo.fit(X_train,y_train)
    tst_val = deodelo.regress_flag
    y_pred = deodelo.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = tst_val
    test_expect = True

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression vs classificatiion test 3")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1'], 
                ['a2', 'b1', 'c2', 'd1', 'e1', 'f1'], 
                ['a3', 'b1', 'c2', 'd2', 'e2', 'f1'], 
                ['a4', 'b2', 'c4', 'd2', 'e2', 'f1'], 
                ['a5', 'b2', 'c2', 'd2', 'e2', 'f1'], 
                ['a6', 'b2', 'c6', 'd2', 'e2', 'f2'],
                ['a7', 'b2', 'c6', 'd2', 'e2', 'f2'],
              ]

    y_train = ['x', 1, 2, 3, 4, 5, 1, 'y']

    X_test =  [
                ['a7', 'b1', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b3', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c4', 'd7', 'e7', 'f7'], 
                ['a6', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c7', 'd7', 'e2', 'f7'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f1'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f7'], 
              ]

    y_expect = [
                0.2, 
                0.2, 
                0.25, 
                'x', 
                0.25,
                'y',
                0.3,
                'y',
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodelo = deodel.DeodataDelangaClassifier()

    # tst_1 = deodelo.regress_flag
    deodelo.fit(X_train,y_train)
    tst_val = deodelo.regress_flag
    y_pred = deodelo.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = tst_val
    test_expect = True

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression vs classificatiion test 4")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ 
                ['a1', 'b1', 'c1', 'd1', 'e1', 'f1'], 
                ['a2', 'b1', 'c2', 'd1', 'e1', 'f1'], 
                ['a3', 'b1', 'c2', 'd2', 'e2', 'f1'], 
                ['a4', 'b2', 'c4', 'd2', 'e2', 'f1'], 
                ['a5', 'b2', 'c2', 'd2', 'e2', 'f1'], 
                ['a6', 'b2', 'c6', 'd2', 'e2', 'f2'],
                ['a7', 'b2', 'c6', 'd2', 'e2', 'f2'],
              ]

    y_train = ['x', 1, 2, 3, 4, 5, 1, 2]

    X_test =  [
                ['a7', 'b1', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b3', 'c7', 'd7', 'e7', 'f7'], 
                ['a7', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c4', 'd7', 'e7', 'f7'], 
                ['a6', 'b7', 'c2', 'd7', 'e7', 'f7'], 
                ['a7', 'b2', 'c7', 'd7', 'e2', 'f7'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f1'], 
                ['a7', 'b7', 'c7', 'd7', 'e2', 'f7'], 
              ]

    y_expect = [
                0.2, 
                0.2, 
                0.25, 
                'x', 
                0.25,
                'y',
                0.3,
                'y',
               ]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    deodelo = deodel.DeodataDelangaClassifier()

    # tst_1 = deodelo.regress_flag
    deodelo.fit(X_train,y_train)
    tst_val = deodelo.regress_flag
    y_pred = deodelo.predict(X_test)
    t_pred = y_pred

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - - - X_train:", X_train)
    iprnt ("- - - - X_test:", X_test)
    iprnt ()
    iprnt ("- - - - y_train:", y_train)
    iprnt ("- - - - y_test:", y_test)
    iprnt ()

    e_pred = y_expect

    test_result = tst_val
    test_expect = False

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -







    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - -
    SepLine()
    iprnt ("- - - UnitTestDeodel results")
    iprnt ("- - -   utest_fail_counter:", utest_fail_counter)
    SepLine()
    # >- - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    return utest_fail_counter

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Unit Test Deodel - end
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -



# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def UnitTestUseApp():

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Unit Test Usap - begin
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    import traceback
    import sys

    import usap_csv_eval

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    utest_fail_counter = 0
    utest_test_no = 0

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CsvTblPrep ok")
    iprnt ()

    test_csv_lst =  [
                        ['', '', '', '', ''],
                        ['', 'a', '   1.01', '   az', ''],
                        ['', 'b', '3.051', "  ' 3.051' ", ' '],
                        ['', 'd', '4', '   5 ', ' '],
                        ['', 'b', '   2', '      3.01', ' '],
                        ['', 'c', "33", ' az', ''],
                        ['', 'a', '   ', '    az  z ', ''],
                        ['', 'b', '2.01', 7.01, ''],
                        ['', 'd', '-4e-2', '-5', ''],
                        ['', 'b', '   2', "      33.013 '", ''],
                        ['', 'c', '3.098', " az ' sd", ''],
                        ['', 'a', '   1.01', '   az \' "gd" \'uiou uo\' ds', ''],
                        ['', 'b', '', '22 qqw  9.03', '', -4, ' -75'],
                        ['', 'd', {1, 2, 1, 3}, "6'    5", '', 8.333],
                        ['', 'b', '   2.2424', '      44.017', ''],
                        ['', 'c', '  "53.07"  ', '77 " az" 2\' sd 89', ''],
                        ['', 'd', '', "''", '8', -0],
                        ['', 'e', ' ', '``', '9', -0.0],
                        ['', 'a', '-inf', '+inf', 'nan'],
                        ['', 'b', "-inf", "inf", "nan"],
                        ['', 'c', float('-inf'), float('+inf'), float('nan')],
                        ['', 'd', float('-inf'), float('inf'), None],
                        ['', '', None, "", '']
                    ]

    iprnt ("- - - - test_csv_lst:", test_csv_lst)

    expect_result = [
                        [None, None, None, None, None],
                        [None, 'a', 1.01, '   az', None],
                        [None, 'b', 3.051, ' 3.051', ' '],
                        [None, 'd', 4, 5.0, ' '],
                        [None, 'b', 2, 3.01, ' '],
                        [None, 'c', 33, ' az', None],
                        [None, 'a', '   ', '    az  z ', None],
                        [None, 'b', 2.01, 7.01, None],
                        [None, 'd', -4e-2, -5, None],
                        [None, 'b', 2, "      33.013 '", None],
                        [None, 'c', 3.098, " az ' sd", None],
                        [None, 'a', 1.01, '   az \' "gd" \'uiou uo\' ds', None],
                        [None, 'b', None, '22 qqw  9.03', None, -4, -75],
                        [None, 'd', "{1, 2, 3}", "6'    5", None, 8.333],
                        [None, 'b', 2.2424, 44.017, None],
                        [None, 'c', "53.07", '77 " az" 2\' sd 89', None],
                        [None, 'd', None, '', 8, 0],
                        [None, 'e', ' ', '``', 9, 0.0],
                        [None, "a", "-inf", "+inf", "nan"],
                        [None, 'b', '-inf', 'inf', 'nan'],
                        [None, 'c', '-inf', '+inf', 'nan'],
                        [None, 'd', '-inf', '+inf', None],
                        [None, None, None, None, None]
                    ]

    iprnt ("- - - - CsvTblPrep - begin")
    proc_tbl = usap_csv_eval.TblUtil.CsvTblPrep(test_csv_lst)
    iprnt ("- - - - CsvTblPrep - end")

    test_result = proc_tbl
    test_expect = expect_result

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test TblPrepProxy ok")
    iprnt ()

    t_csv = [
                None,
                [" 'a aa' ",     None,   " -15e-2 ",       '',         'Y' ],
                ['  "a bb" ',  "None",            2, " '65' ",        "'N'"],
                ['b aa',      {'a':1},  "  '3e-1' ",     '""', float('nan')],
                {}
            ]

    ret_tuple = usap_csv_eval.TblUtil.TblPrepProxy(t_csv)
    ret_status, ret_list_csv, ret_msg = ret_tuple

    e_csv = [
                [None],
                ['a aa',      None,     -0.15,      None,     'Y' ],
                ['a bb',      "None",       2,      '65',     'N' ],
                ['b aa',  "{'a': 1}",  '3e-1',        '',   'nan' ],
                ['{}']
            ]

    test_result = ret_tuple
    test_expect = True, e_csv, ""

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract ok")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = -1

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = True
    e_train = [
                [  'a',        101  ],
                [  'b',        23.4 ],
            ]
    e_targ = [ 'Y', 'N' ]
    e_dim = (5, 5)
    e_str = ""
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract ok")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 4

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = True
    e_train = [
                [  'a',        101  ],
                [  'b',        23.4 ],
            ]
    e_targ = [ 'Y', 'N' ]
    e_dim = (5, 5)
    e_str = ""
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract ok")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 0

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = True
    e_train = [
                [ 101,    'Y' ],
                [ 23.4,   'N' ],
            ]
    e_targ = [ 'a', 'b' ]
    e_dim = (5, 5)
    e_str = ""
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract ok")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 2

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = True
    e_train = [
                [ 'a',    'Y' ],
                [ 'b',    'N' ],
            ]
    e_targ = [ 101, 23.4 ]
    e_dim = (5, 5)
    e_str = ""
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract ok")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  None, 'a', None,  101,   None, 'Y' ],
                [  None, 'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 1

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    e_status = True
    e_train = [
                [ 101,    'Y' ],
                [ 23.4,   'N' ],
            ]
    e_targ = [ 'a', 'b' ]
    e_dim = (5, 6)
    e_str = ""
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract idx wrong")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  None, 'a', None,  101,   None, 'Y' ],
                [  None, 'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 0

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = False
    e_train = []
    e_targ = []
    e_dim = (5, 6)
    e_str = "Error: empty target column !"
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract idx wrong")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 10

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = False
    e_train = []
    e_targ = []
    e_dim = (5, 5)
    e_str = "Error: invalid target index !"
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract idx wrong")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 3

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = False
    e_train = []
    e_targ = []
    e_dim = (5, 5)
    e_str = "Error: empty target column !"
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CheckIsUrl ok")
    iprnt ()

    t_url = "https://unexistent.just.for.test.site.org"

    r_status = usap_csv_eval.TblUtil.CheckIsUrl(t_url)

    e_status = True

    test_result = r_status
    test_expect = e_status

    iprnt ("- - - - t_url:", t_url)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CheckIsUrl wrong")
    iprnt ()

    t_url = "gggggghttps://unexistent.just.for.test.site.org"

    r_status = usap_csv_eval.TblUtil.CheckIsUrl(t_url)

    e_status = False

    test_result = r_status
    test_expect = e_status

    iprnt ("- - - - t_url:", t_url)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test ImportCsvTbl wrong")
    iprnt ()

    t_url = "gggggghttps://unexistent.just.for.test.site.org"

    r_tuple = usap_csv_eval.TblUtil.ImportCsvTbl(t_url)

    e_status = False
    e_csv = None
    e_str = "Error: failed file access !"
    e_tuple = e_status, e_csv, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_url:", t_url)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test ImportCsvTbl wrong")
    iprnt ()

    t_url = "https://unexistent.just.for.test.site.org"

    r_tuple = usap_csv_eval.TblUtil.ImportCsvTbl(t_url)

    e_status = False
    e_csv = None
    e_str = "Error: failed urlopen"
    e_tuple = e_status, e_csv, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_url:", t_url)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test TblPrepProxy wrong")
    iprnt ()

    t_url = "gggggghttps://unexistent.just.for.test.site.org"

    r_tuple = usap_csv_eval.TblUtil.TblPrepProxy(t_url)

    e_status = False
    e_csv = None
    e_str = "Error: failed file access !"
    e_tuple = e_status, e_csv, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_url:", t_url)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CleanTargetExtract ok")
    iprnt ()

    t_csv = [
                [None, None],
                [],
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
                []
            ]
    t_targ_idx = 0

    r_tuple = usap_csv_eval.TblUtil.CleanTargetExtract(t_csv, t_targ_idx)
    r_status, r_train, r_targ, r_dim, r_str = r_tuple

    e_status = True
    e_train = [
                [ 101,    'Y' ],
                [ 23.4,   'N' ],
            ]
    e_targ = [ 'a', 'b' ]
    e_dim = (5, 5)
    e_str = ""
    e_tuple = e_status, e_train, e_targ, e_dim, e_str

    test_result = r_tuple
    test_expect = e_tuple

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess ok")
    iprnt ()

    t_csv = [
                [  'a', None,  101,   None, 'Y' ],
                [  'b', None,  23.4,  None, 'N' ],
            ]

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv)

    e_dict = {}
    e_dict['status'] = True
    e_dict['data'] = (0, 0)
    e_dict['msg'] = ""

    test_result = r_dict
    test_expect = e_dict

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess wrong")
    iprnt ()

    t_csv = [
                [  'a', None,  101,   None, 'Y' ],
                # [  'b', None,  23.4,  None, 'N' ],
            ]

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv)

    e_dict = {}
    e_dict['status'] = False
    e_dict['data'] = (None, None)
    e_dict['msg'] = ""

    test_result = r_dict
    test_expect = e_dict

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess wrong")
    iprnt ()

    t_csv = [
                # [  'a', None,  101,   None, 'Y' ],
                # [  'b', None,  23.4,  None, 'N' ],
            ]

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv)

    e_dict = {}
    e_dict['status'] = False
    e_dict['data'] = (None, None)
    e_dict['msg'] = "Error: data extraction failed !"

    test_result = r_dict
    test_expect = e_dict

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - -
    SepLine()
    iprnt ("- - - UnitTestUseApp results")
    iprnt ("- - -   utest_fail_counter:", utest_fail_counter)
    SepLine()
    # >- - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess rand param")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'b1',  'e2', 'n3', 'N' ],
                [ 'b1',  'e2', 'n3', 'N' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 42, aux_data = None, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 1.0

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess rand param")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'b1',  'e2', 'n3', 'N' ],
                [ 'b1',  'e2', 'n3', 'N' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 44, aux_data = None, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 0.0

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess rand param")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'b1',  'e2', 'n3', 'N' ],
                # [ 'b1',  'e2', 'n3', 'N' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 43, aux_data = None, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 0.5

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess tie ref")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'b1',  'e2', 'n3', 'N' ],
                [ 'b1',  'e2', 'm3', 'N' ],
                [ 'a1',  'e2', 'n3', 'Y' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 45, aux_data = None, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 0.5

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess aux param")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'b1',  'e2', 'n3', 'N' ],
                [ 'b1',  'e2', 'm3', 'N' ],
                [ 'a1',  'e2', 'n3', 'Y' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 45, aux_data = {'exc':{2}}, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 1.0

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess none target")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', None ],
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'b1',  'e2', 'n3', 'N' ],
                # [ 'b1',  'e2', 'n3', 'N' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 43, aux_data = None, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 0.0

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess none target")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'a1',  'e2', 'm3', None ],
                [ 'b1',  'e2', 'n3', 'N' ],
                # [ 'b1',  'e2', 'n3', 'N' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 43, aux_data = None, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 0.0

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test CvsProcess none target")
    iprnt ()

    t_csv = [
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'a1',  'e2', 'm3', 'Y' ],
                [ 'b1',  'e2', 'n3', None ],
                # [ 'b1',  'e2', 'n3', 'N' ],
            ]
    t_targ_idx = -1
    t_itern_no = 1

    r_dict = usap_csv_eval.TblUtil.CvsProcess(t_csv, in_targ_idx = -1, in_iter_no = 1, in_rand_seed = 43, aux_data = None, display_flag = True)
    r_status = r_dict['status']
    r_accuracy = r_dict['data'][0]

    e_status = True
    e_accuracy = 1.0

    test_result = (r_status, r_accuracy)
    test_expect = (e_status, e_accuracy)

    iprnt ("- - - - t_csv:", t_csv)
    iprnt ("- - - - t_targ_idx:", t_targ_idx)
    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test HashValue")
    iprnt ()

    tt_list_var = ["", 22, {}, [], None, "None", "caramba", [1, 2, 4], [1,2,3], [3, 1, 2]]
    tt_out_list = []

    for crt_elem in tt_list_var :
        var = crt_elem
        hash = usap_common.HashValue(var)
        tt_out_list.append(hash)

    ee_out_list = [1114, 1179, 1428, 1436, 2009, 1480, 1780, 1733, 1692, 1732]

    iprnt ("- - - - tt_list_var:", tt_list_var)

    test_result = (tt_out_list)
    test_expect = (ee_out_list)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test RandBaselinePredictor 1")
    iprnt ()

    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['do',  "4",    5,      'd'],
            ['b',   2,      3.01,   'h'],
            ['cc',  '3.01', 'az',   'e']]

    tt_y = [
            'one',
            2.0,
            3,
            "one",
            2
           ]

    tt_T = [['a',   2.0,     'az',   'd'],
            ['dp',  "3.01",  3.01,   'd'],
            ['a',   None,    None,   'e'],
            ['dp',  None,    'za',   'h'],
            ['b',  "5",      3.02,   'e'],
            ['cc',  1.01,    'az',   'h'],
            ['e',  '3.01',   'az',   'i']]


    tt_o = usap_common.RandBaselinePredictor({'rand_seed': 42})
    tt_o.fit(tt_X, tt_y)
    rr_predict = tt_o.predict(tt_T)

    ee_y = ['one', 'one', 'one', 3, 2.0, 'one', 2]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_T:", tt_T)

    test_result = (rr_predict)
    test_expect = (ee_y)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1")
    iprnt ()

    import deodel
    from sklearn import datasets

    data_set = datasets.load_wine()
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    crt_classif = deodel.DeodataDelangaClassifier()
    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9400749063670412, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 2")
    iprnt ()

    import deodel
    from sklearn import datasets

    data_set = datasets.load_wine()
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 10
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    crt_classif = usap_common.RandBaselinePredictor({'rand_seed': in_rand_seed})
    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.3382022471910112, 0.3146067415730337)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    return utest_fail_counter

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Unit Test Usap - end
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
def UnitTest():

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ( "*** unit test begin ***" )
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    utest_fail_counter = 0

    ret_data = UnitTestDeodel()
    utest_fail_counter += ret_data
    iprnt ("- - - ")

    ret_data = UnitTestUseApp()
    utest_fail_counter += ret_data
    iprnt ("- - - ")

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - -
    SepLine()
    iprnt ("- - - Aggregate results")
    iprnt ("- - -   utest_fail_counter:", utest_fail_counter)
    if utest_fail_counter == 0:
        iprnt ("- - -   UnitTest succes")
    else:
        iprnt ("- - -   UnitTest failed !")
        iprnt ("- - -       errors:", utest_fail_counter)
    SepLine()
    # >- - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ( "*** unit test end ***" )
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    return utest_fail_counter

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -





# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# if __name__ == "__main__":
if True :
    print()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    CrtTimeStamp()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print()
    print("- - - - - - - - - ")

    ret_data = UnitTest()

    print()
    print("- - - - - - - - - ")
    print("- - - - ret_data:", ret_data)
    print("- - - - - - - - - ")
    print()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    CrtTimeStamp()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    print()

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

"""
Deodata Delanga Unit Test

    Module provides an unsystematic/opportunistic collection of tests.

        Tested with Winpython64-3.10.5.0
"""

#   c4pub@git 2023
#
# Latest version available at: https://github.com/c4pub/deodel
#

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
    ret_1 = deodel.Working.ProcessVector(tv1, True)
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

    ret_1 = deodel.Working.ProcessVector(tv1, False)
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
    ret_1 = deodel.Working.ProcessVector(tv1, True)
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

    ret_1 = deodel.Working.ProcessVector(tv1, False)
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

    iprnt ("- - - - tt_o.__dict__ :", tt_o.__dict__ )
    iprnt ()


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

    iprnt ("- - - - tt_o.__dict__ :", tt_o.__dict__ )
    iprnt ()



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

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("check version")
    iprnt ()

    aux_param = {'tbreak_depth': 1}
    tt_o = deodel.DeodataDelangaClassifier(aux_param)
    tt_o.fit(tt_X, tt_y)
    tt_predict = tt_o.predict(tt_test)
    iprnt ()

    test_result = deodel.DeodataDelangaClassifier.version
    # test_expect = 1.51
    # test_expect = 1.65
    test_expect = 1.75

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

    import pandas as pd

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
                [],
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

    iprnt ("test CleanTargetExtract idx fail")
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

    iprnt ("test CleanTargetExtract idx fail")
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

    iprnt ("test CleanTargetExtract idx fail")
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

    iprnt ("test CheckIsUrl fail")
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

    iprnt ("test ImportCsvTbl fail")
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

    iprnt ("test ImportCsvTbl fail")
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

    iprnt ("test TblPrepProxy fail")
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

    iprnt ("test CvsProcess fail")
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

    iprnt ("test CvsProcess fail")
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
    print("- - - - - - - - - ")

    ret_data = UnitTest()

    print()
    print("- - - - - - - - - ")
    print("- - - - ret_data:", ret_data)
    print("- - - - - - - - - ")
    print()

# >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

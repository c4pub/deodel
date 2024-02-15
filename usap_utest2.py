"""
Deodata Delanga Unit Test

    Module provides an unsystematic/opportunistic collection of tests.

        Tested with Winpython64-3.10.5.0
"""

#   c4pub@git 2023 - 2024
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

    import deodel2


    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("test GetElemIdxInOrderList - 001")

    utest_fail_counter = 0
    utest_test_no = 0

    sys.stdout.flush()
    sys.stderr.flush()

    test_thresh_list = [1, 2, 3]

    test_elem = -1
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 002")

    test_elem = 0
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 003")

    test_elem = 1
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 004")

    test_elem = 1.0
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 005")

    test_elem = 1.5
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 006")

    test_elem = 2
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 007")

    test_elem = 2.1
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 008")

    test_elem = 1.5
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 009")

    test_elem = 2.0
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 010")

    test_elem = 3.0
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 011")

    test_thresh_list = [3.01, 4.005]
    test_elem = 3
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 012")

    test_thresh_list = [3.01, 4.005]
    test_elem = 3.01
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 013")

    test_elem = 3.5
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 014")

    test_elem = 5
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 016")

    test_thresh_list = [3]
    test_elem = 3
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 017")

    test_thresh_list = [3]
    test_elem = 4
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test GetElemIdxInOrderList - 018")

    test_thresh_list = [3]
    test_elem = 2
    test_result = deodel2.Working.GetElemIdxInOrderList(test_elem, test_thresh_list)

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
    iprnt ("test list convert")

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
    iprnt ("test MatrixTranspose - 1")

    ty1 = ['one', 2, 3, "one"]
    iprnt ("- - - - ty1: ", ty1)

    iprnt ('- - - - ---')

    iprnt ()
    iprnt ("- - - - tt1: ", tt1)
    tt1b = deodel2.Working.MatrixTranspose(tt1)
    iprnt ("- - - - tt1b: ", tt1b)
    tt1c = deodel2.Working.MatrixTranspose(tt1b)
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
    iprnt ("test MatrixTranspose - 2")

    iprnt ("- - - - ty1: ", ty1)
    ty1b = deodel2.Working.MatrixTranspose(ty1)
    iprnt ("- - - - ty1b: ", ty1b)
    ty1c = deodel2.Working.MatrixTranspose(ty1b)
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
    iprnt ("test MatrixTranspose - 3")

    ttu = [['o']]
    iprnt ()
    iprnt ("- - - - ttu: ", ttu)
    ttub = deodel2.Working.MatrixTranspose(ttu)
    iprnt ("- - - - ttub: ", ttub)
    ttuc = deodel2.Working.MatrixTranspose(ttub)
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
    iprnt ("test MatrixTranspose - 4")

    ttu = [ ['o'],
            ['b'],
            [1]]
    iprnt ()
    iprnt ("- - - - ttu: ", ttu)
    ttub = deodel2.Working.MatrixTranspose(ttu)
    iprnt ("- - - - ttub: ", ttub)
    ttuc = deodel2.Working.MatrixTranspose(ttub)
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
    iprnt ("test MatrixTranspose - 5")

    ttu = [ ['o'], [9], ['e']]
    iprnt ()
    iprnt ("- - - - ttu: ", ttu)
    ttub = deodel2.Working.MatrixTranspose(ttu)
    iprnt ("- - - - ttub: ", ttub)
    ttuc = deodel2.Working.MatrixTranspose(ttub)
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
    iprnt ("test RegressParse - 1")

    ttu1 = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 20 ]
    ttu2 = [ 0 ] * 10 + [ 1 ] *  2
    tt_in = ttu1 + ttu2
    int_is_num = True

    iprnt ()
    iprnt ("- - - - tt_in:", tt_in)
    iprnt ("- - - - int_is_num:", int_is_num)
    iprnt ()

    regress_flag = deodel2.Working.RegressParse(tt_in, int_is_num)

    iprnt ("- - - - regress_flag:", regress_flag)

    test_result = regress_flag
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
    iprnt ("test RegressParse - 2")

    ttu1 = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 20 ]
    ttu2 = ttu1[:]
    tt_in = ttu1 + ttu2
    int_is_num = True

    iprnt ()
    iprnt ("- - - - tt_in:", tt_in)
    iprnt ("- - - - int_is_num:", int_is_num)
    iprnt ()

    regress_flag = deodel2.Working.RegressParse(tt_in, int_is_num)

    iprnt ("- - - - regress_flag:", regress_flag)

    test_result = regress_flag
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
    iprnt ("test RegressParse - 3")

    ttu1 = [ 10, 20, 30, 40, 50, 60, 70, 80, 90, 20 ]
    ttu2 = [ 0 ] * 9
    tt_in = ttu1 + ttu2
    int_is_num = True

    iprnt ()
    iprnt ("- - - - tt_in:", tt_in)
    iprnt ("- - - - int_is_num:", int_is_num)
    iprnt ()

    regress_flag = deodel2.Working.RegressParse(tt_in, int_is_num)

    iprnt ("- - - - regress_flag:", regress_flag)

    test_result = regress_flag
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
    iprnt ("test RegressParse - 4")

    ttu1 = [0, 0, 0, 2, 0, 1, 0, 0, 5, 12, 12, 9, 0, 0, 0, 0, 5, 0, 0, 0, 0, 0, 5]
    tt_in = ttu1
    int_is_num = True

    iprnt ()
    iprnt ("- - - - tt_in:", tt_in)
    iprnt ("- - - - int_is_num:", int_is_num)
    iprnt ()

    regress_flag = deodel2.Working.RegressParse(tt_in, int_is_num)

    iprnt ("- - - - regress_flag:", regress_flag)

    test_result = regress_flag
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
    iprnt ("test RegressParse - 5")

    ttu1 = [0, 6, 1, 0, 0, 0, 0, 12, 1, 0, 9, 0, 0, 0, 0, 10, 0, 0, 8, 0, 0, 1, 5]
    tt_in = ttu1
    int_is_num = True

    iprnt ()
    iprnt ("- - - - tt_in:", tt_in)
    iprnt ("- - - - int_is_num:", int_is_num)
    iprnt ()

    regress_flag = deodel2.Working.RegressParse(tt_in, int_is_num)

    iprnt ("- - - - regress_flag:", regress_flag)

    test_result = regress_flag
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
    iprnt ("ProcessVector and RevertVector test - int is num - 1")

    tv1 = ['e',    1,      3.01,   'h',     11,     None]

    int_isnum = False
    iprnt ("- - - - int_isnum:", int_isnum)
    iprnt ("- - - - tv1", tv1)
    ret_1 = deodel2.Working.ProcessVector(tv1, int_isnum)
    iprnt ("- - - - ret_1", ret_1)
    tv2 = deodel2.Working.RevertVector(ret_1[0], ret_1[4], ret_1[1])
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

    int_isnum = True
    iprnt ("- - - - int_isnum:", int_isnum)
    iprnt ("- - - - tv1", tv1)
    ret_1 = deodel2.Working.ProcessVector(tv1, int_isnum)
    iprnt ("- - - - ret_1", ret_1)
    tv3 = deodel2.Working.RevertVector(ret_1[0], ret_1[4], ret_1[1])
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

    int_isnum = True
    iprnt ("- - - - int_isnum:", int_isnum)
    iprnt ("- - - - tv1", tv1)
    ret_1 = deodel2.Working.ProcessVector(tv1, int_isnum)
    iprnt ("- - - - ret_1", ret_1)
    tv2 = deodel2.Working.RevertVector(ret_1[0], ret_1[4], ret_1[1])
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

    int_isnum = True
    iprnt ("- - - - int_isnum:", int_isnum)
    iprnt ("- - - - tv1", tv1)
    ret_1 = deodel2.Working.ProcessVector(tv1, int_isnum)
    iprnt ("- - - - ret_1", ret_1)
    tv3 = deodel2.Working.RevertVector(ret_1[0], ret_1[4], ret_1[1])
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

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    #'''#

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    def ApproxSplitList(in_num_list, in_split_no) :
        if in_num_list == [] :
            return []
        ordered_list = sorted(in_num_list)
        resolution = 10000
        interval_width = ordered_list[-1] - ordered_list[0]
        if interval_width == 0 :
            return [ordered_list[0]]
        step_interval = interval_width/(resolution)
        crt_offset = ordered_list[0] - step_interval
        crt_conv = 0.0
        split_list = []
        for crt_idx in range(resolution + 2) :
            proc_val = deodel2.Working.EqualWidthDiscretize(crt_offset, in_num_list, in_split_no)
            if proc_val > crt_conv :
                split_list.append(crt_offset)
                crt_conv = proc_val
            crt_offset += step_interval
        return split_list

    iprnt ("test number list discretization")
    iprnt ()
    tt_split_list = [
                    #      tag       split_mode  split noduplic multi   num_list  expect_thresh   
                    # ----------------------------------------------------------
                        [ 'tag_001',   ('eq_freq',  2,  False,  True,  [1, 2, 3, 4], [2.5])],
                        [ 'tag_002',   ('eq_width', 2,  False,  True,  [1, 2, 3, 4], [2.5])],
                        [ 'tag_003',   ('eq_freq',  4,  False,  True,  [1, 2, 3, 4], [1.5, 2.5, 3.5])],
                        [ 'tag_004',   ('eq_freq',  5,  False,  True,  [5, 1, 2, 3, 4], [1.5, 2.5, 3.5, 4.499999999999999])],
                        [ 'tag_005',   ('eq_width', 5,  False,  True,  [5, 1, 2, 3, 4], [1.5, 2.5, 3.5, 4.5])],
                        [ 'tag_006',   ('eq_freq',  3,  False,  True,  [1, 2, 3], [1.5, 2.5])],
                        [ 'tag_007',   ('eq_freq',  3,  False,  True,  [1, 2, 3, 4, 5, 6], [2.5, 4.5])],
                        [ 'tag_008',   ('eq_width', 3,  False,  True,  [0, 2, 3, 4, 5, 6], [1.5, 4.5])],
                        [ 'tag_009',   ('eq_freq',  2,  False,  True,  [1, 2, 3, 4, 5, 6], [3.5])],
                        [ 'tag_010',   ('eq_freq',  3,  False,  True,  [1, 2, 3, 4], [2 - 1.0/6, 3 + 1.0/6])],
                        [ 'tag_011',   ('eq_freq',  4,  False,  True,  [1, 2, 3, 4], [1.5, 2.5, 3.5])],
                        [ 'tag_012',   ('eq_freq',  2,  False,  True,  [1, 2, 3, 4, 5, 6], [3.5])],
                        [ 'tag_013',   ('eq_freq',  4,  False,  True,  [4, 3, 1, 2, 8, 5, 7, 6], [2.5, 4.5, 6.5])],
                        [ 'tag_014',   ('eq_freq',  3,  False,  True,  [4, 3, 1, 2, 5, 6], [2.5, 4.5])],
                        [ 'tag_015',   ('eq_freq',  2,  False,  True,  [4, 3, 1, 2, 8, 5, 7, 6], [4.5])],
                        [ 'tag_016',   ('eq_freq',  8,  False,  True,  [4, 3, 1, 2, 8, 5, 7, 6], [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5])],
                        [ 'tag_017',   ('eq_freq',  16, False,  True,  [4, 3, 1, 2, 8, 5, 7, 6], [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8])],
                        [ 'tag_018',   ('eq_freq',  5,  False,  True,  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [ 2.5, 4.5, 6.5, 8.5 ])],
                        [ 'tag_019',   ('eq_freq',  2,  False,  True,  [4, 3, 1, 2], [2.5])],
                        [ 'tag_020',   ('eq_freq',  4,  False,  True,  [1, 2, 3, 4], [1.5, 2.5, 3.5])],
                        [ 'tag_021',   ('eq_freq',  4,  False,  True,  [3, 3, 3, 4], [3.0, 3.0, 3.5])],
                        [ 'tag_022',   ('eq_freq',  4,  True,   True,  [3, 3, 3, 4], [3, 4])],
                        [ 'tag_023',   ('eq_freq',  2,  False,  True,  [3, 3, 3, 4], [3])],
                        [ 'tag_024',   ('eq_width', 4,  True,   True,  [-2, -2, -2, -2], [-2])],
                        [ 'tag_025',   ('eq_freq',  4,  False,  True,  [-2, -2, -2], [-2, -2, -2])],
                        [ 'tag_026',   ('eq_width', 5,  True,   True,  [-2, -2, -2, -2], [-2])],
                        [ 'tag_027',   ('eq_width', 4,  False,  True,  [-2, -2, -2], [-2, -2, -2])],
                        [ 'tag_028',   ('eq_freq',  4,  False,  True,  [-2], [-2, -2, -2])],
                        [ 'tag_029',   ('eq_freq',  4,  True,   True,  [-2], [-2])],
                        [ 'tag_030',   ('eq_width', 4,  False,  True,  [-2], [-2, -2, -2])],
                        [ 'tag_031',   ('eq_width', 4,  True,   True,  [-2], [-2])],
                        [ 'tag_032',   ('eq_freq',  4,  True,   True,  [], [])],
                        [ 'tag_033',   ('eq_width', 4,  True,   True,  [], [])],
                        [ 'tag_034',   ('eq_freq',  7,  False,  True,  [10, 20, 30], [10, 15, 20, 25, 30])],
                        [ 'tag_035',   ('eq_freq',  7,  False,  True,  [1.2, 2], [1.2, 1.6, 2])],
                        [ 'tag_036',   ('eq_freq',  3,  False,  True,  [1.2, 2], [1.2 + 0.4/3, 2 - 0.4/3])],
                        [ 'tag_037',   ('eq_freq',  2,  False,  True,  [1.2, 2], [1.6])],
                        [ 'tag_038',   ('eq_freq',  3,  True,   True,  [3, 5, 3], [5])],
                        [ 'tag_039',   ('eq_freq',  2,  False,  True,  [0, 0, 1], [1.6653345369377348e-16])],
                        [ 'tag_040',   ('eq_freq',  2,  True,   True,  [0, 0, 1], [1.6653345369377348e-16])],
                        [ 'tag_041',   ('eq_freq',  2,  True,   True,  [0, 0, 0, 0, 1], [1])],
                        [ 'tag_042',   ('eq_freq',  3,  True,   True,  [0, 0, 0, 0, 1], [0.6666666666666665])],
                        [ 'tag_043',   ('eq_freq',  4,  True,   True,  [0, 0, 0, 0, 1], [1])],
                        [ 'tag_044',   ('eq_freq',  5,  True,   True,  [0, 0, 0, 0, 1], [1])],
                        [ 'tag_045',   ('eq_freq',  6,  True,   True,  [0, 0, 0, 0, 1], [0.8333333333333331, 1])],
                        [ 'tag_046',   ('eq_freq',  7,  True,   True,  [0, 0, 0, 0, 1], [0.714285714285714, 1])],
                        [ 'tag_047',   ('eq_freq',  8,  True,   True,  [0, 0, 0, 0, 1], [0.625, 1])],
                        [ 'tag_048',   ('eq_freq',  9,  True,   True,  [0, 0, 0, 0, 1], [0.5555555555555558, 1])],
                        [ 'tag_049',   ('eq_width', 11,  True,  True,  [100, 200], [105, 115, 125, 135, 145, 155, 165, 175, 185, 195])],
                    # ----------------------------------------------------------
                        [ 'tag_101-a', ('eq_freq',  4,  False,  True,  [-5, -5, -5], [-5, -5, -5])],
                        [ 'tag_101-b', ('eq_freq',  4,  True,   True,  [-5, -5, -5], [-5])],
                        [ 'tag_101-c', ('eq_width', 4,  False,  True,  [-5, -5, -5], [-5, -5, -5])],
                        [ 'tag_101-d', ('eq_width', 4,  True,   True,  [-5, -5, -5], [-5])],
                        [ 'tag_102-a', ('eq_freq',  4,  False,  True,  [-5], [-5, -5, -5])],
                        [ 'tag_102-b', ('eq_freq',  4,  True,   True,  [-5], [-5])],
                        [ 'tag_102-c', ('eq_width', 4,  False,  True,  [-5], [-5, -5, -5])],
                        [ 'tag_102-d', ('eq_width', 4,  True,   True,  [-5], [-5])],
                        [ 'tag_103-a', ('eq_freq',  4,  False,  True,  [], [])],
                        [ 'tag_103-b', ('eq_freq',  4,  True,   True,  [], [])],
                        [ 'tag_103-c', ('eq_width', 4,  False,  True,  [], [])],
                        [ 'tag_103-d', ('eq_width', 4,  True,   True,  [], [])],

                        [ 'tag_104-a', ('eq_freq',  4,  False,  True,  [10, 20, 30, 40, 50, 60, 65, 70], [25.0, 45.0, 62.5])],
                        [ 'tag_104-b', ('eq_freq',  4,  True,   True,  [10, 20, 30, 40, 50, 60, 65, 70], [25.0, 45.0, 62.5])],
                        [ 'tag_104-c', ('eq_width', 4,  False,  True,  [10, 20, 30, 40, 50, 60, 65, 70], [20.0, 40.0, 60.0])],
                        [ 'tag_104-d', ('eq_width', 4,  True,   True,  [10, 20, 30, 40, 50, 60, 65, 70], [20.0, 40.0, 60.0])],

                    # ----------------------------------------------------------

                        [ 'tag_111-a', ('eq_freq',  4,  False,  False, [-5, -5, -5], [-5, -5, -5])],
                        [ 'tag_111-b', ('eq_freq',  4,  True,   False, [-5, -5, -5], [-5])],
                        [ 'tag_111-c', ('eq_width', 4,  False,  False, [-5, -5, -5], [-5, -5, -5])],
                        [ 'tag_111-d', ('eq_width', 4,  True,   False, [-5, -5, -5], [-5])],
                        [ 'tag_112-a', ('eq_freq',  4,  False,  False, [-5], [-5, -5, -5])],
                        [ 'tag_112-b', ('eq_freq',  4,  True,   False, [-5], [-5])],
                        [ 'tag_112-c', ('eq_width', 4,  False,  False, [-5], [-5, -5, -5])],
                        [ 'tag_112-d', ('eq_width', 4,  True,   False, [-5], [-5])],
                        [ 'tag_113-a', ('eq_freq',  4,  False,  False, [], [])],
                        [ 'tag_113-b', ('eq_freq',  4,  True,   False, [], [])],
                        [ 'tag_113-c', ('eq_width', 4,  False,  False, [], [])],
                        [ 'tag_113-d', ('eq_width', 4,  True,   False, [], [])],

                    # ----------------------------------------------------------
                        [ 'tag_114-a', ('eq_freq',  1,  False,  True,  [100, 200], [])],
                        [ 'tag_114-b', ('eq_freq',  1,  True,   True,  [100, 200], [])],
                        [ 'tag_114-c', ('eq_width', 1,  False,  True,  [100, 200], [])],
                        [ 'tag_114-d', ('eq_width', 1,  True,   True,  [100, 200], [])],
 
                        [ 'tag_114-e', ('eq_freq',  1,  False,  False, [100, 200], [])],
                        [ 'tag_114-f', ('eq_freq',  1,  True,   False, [100, 200], [])],
                        [ 'tag_114-g', ('eq_width', 1,  False,  False, [100, 200], [])],
                        [ 'tag_114-h', ('eq_width', 1,  True,   False, [100, 200], [])],
                    # ----------------------------------------------------------
                        [ 'tag_114-i', ('eq_freq',  5,  False,  True,  [100, 200], [100, 150.0, 200])],
                        [ 'tag_114-j', ('eq_freq',  5,  True,   True,  [100, 200], [100, 150.0, 200])],
                        [ 'tag_114-k', ('eq_width', 5,  False,  True,  [100, 200], [112.5, 137.5, 162.5, 187.5])],
                        [ 'tag_114-l', ('eq_width', 5,  True,   True,  [100, 200], [112.5, 137.5, 162.5, 187.5])],
 
                        [ 'tag_114-m', ('eq_freq',  5,  False,  False, [100, 200], [100, 150.0, 200])],
                        [ 'tag_114-n', ('eq_freq',  5,  True,   False, [100, 200], [100, 150.0, 200])],
                        [ 'tag_114-o', ('eq_width', 5,  False,  False, [100, 200], [112.5, 137.5, 162.5, 187.5])],
                        [ 'tag_114-p', ('eq_width', 5,  True,   False, [100, 200], [112.5, 137.5, 162.5, 187.5])],
                    # ----------------------------------------------------------
                        [ 'tag_115',   ('eq_width', 2,  False,  True,  [100, 200], [150])],
                        [ 'tag_116',   ('eq_width', 3,  False,  True,  [100, 200], [125.0, 175.0])],
                        [ 'tag_117',   ('eq_width', 4,  False,  True,  [100, 200], [116.666666666666668, 150.0, 183.33333333333334])],
                        [ 'tag_118',   ('eq_width', 5,  False,  True,  [100, 200], [112.5, 137.5, 162.5, 187.5])],
                        [ 'tag_119',   ('eq_width', 6,  False,  True,  [100, 200], [110.0, 130.0, 150.0, 170.0, 190.0])],
                        [ 'tag_120',   ('eq_width', 7,  False,  True,  [100, 200], [108.33333333333333, 125.0, 141.66666666666666, 158.33333333333331, 174.99999999999997, 191.66666666666663])],
                        [ 'tag_121',   ('eq_width', 8,  False,  True,  [100, 200], [107.14285714285714, 121.42857142857143, 135.71428571428572, 150.0, 164.28571428571428, 178.57142857142856, 192.85714285714283])],
                        [ 'tag_122',   ('eq_width', 2,  False,  True,  [2, 4], [3])],
                        [ 'tag_123',   ('eq_width', 3,  False,  True,  [2, 4], [2.5, 3.5])],
                        [ 'tag_124',   ('eq_width', 4,  False,  True,  [2, 4], [2.3333333333333335, 3.0, 3.6666666666666665])],
                        [ 'tag_125',   ('eq_width', 5,  False,  True,  [2, 4], [2.25, 2.75, 3.25, 3.75])],
                        [ 'tag_126',   ('eq_width', 6,  False,  True,  [2, 4], [2.2, 2.6, 3.0, 3.4, 3.8])],
                        [ 'tag_127',   ('eq_width', 7,  False,  True,  [2, 4], [2.1666666666666665, 2.5, 2.8333333333333335, 3.166666666666667, 3.5000000000000004, 3.833333333333334])],
                        [ 'tag_128',   ('eq_width', 8,  False,  True,  [2, 4], [2.142857142857143, 2.4285714285714284, 2.714285714285714, 2.9999999999999996, 3.285714285714285, 3.5714285714285707, 3.8571428571428563])],
                    # ----------------------------------------------------------
                        [ 'tag_131-a', ('eq_freq',  2,  False,  True,  [3, 4, 2], [3])],
                        [ 'tag_131-b', ('eq_freq',  2,  True,   True,  [3, 4, 2], [3])],
                        [ 'tag_131-c', ('eq_width', 2,  False,  True,  [3, 4, 2], [3])],
                        [ 'tag_131-d', ('eq_width', 2,  True,   True,  [3, 4, 2], [3])],

                        [ 'tag_132-a', ('eq_freq',  2,  False,  False, [3, 4, 2], [3])],
                        [ 'tag_132-b', ('eq_freq',  2,  True,   False, [3, 4, 2], [3])],
                        [ 'tag_132-c', ('eq_width', 2,  False,  False, [3, 4, 2], [3])],
                        [ 'tag_132-d', ('eq_width', 2,  True,   False, [3, 4, 2], [3])],
                    # ----------------------------------------------------------
                    ]
    show_max_elem = 50
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - Test - part A")
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    iprnt ("")

    list_len = len(tt_split_list)
    iprnt ("- - - - list_len:", list_len)
    error_flag = False
    error_count = 0
    error_i_idx = None

    for crt_i_idx in range(list_len) :
        crt_tag = tt_split_list[crt_i_idx][0]
        crt_elem = tt_split_list[crt_i_idx][1]

        ( in_split_mode, in_split_no, no_dupl_flag, multi_flag, in_num_list, expect_thresh ) = crt_elem
        crt_param = ( in_num_list, in_split_no, in_split_mode, no_dupl_flag )
        iprnt ("- - - - crt_i_idx:", crt_i_idx)
        iprnt ("- - - - crt_tag:", crt_tag)
        iprnt ("- - - - - - crt_elem:", crt_elem)
        [crt_type, crt_attr_thresh] = deodel2.Working.NumSplit(*crt_param)
        iprnt ("- - - - - - crt_attr_thresh:", crt_attr_thresh)
        iprnt ("- - - - - - expect_thresh:  ", expect_thresh)
        approx_width_split = ApproxSplitList(in_num_list, in_split_no)
        iprnt ("- - - - - - approx_width_split:  ", approx_width_split[:show_max_elem])

        if not crt_attr_thresh == expect_thresh :
            error_flag = True
            error_i_idx = crt_i_idx
            error_count += 1
            iprnt ("- - - - - - - - mismatch")
            iprnt ("- - - - - - - - crt_i_idx:", crt_i_idx)
            # break

        if error_flag :
            # break
            pass
            
    iprnt ("- - - - error_flag:", error_flag)
    iprnt ("- - - - error_count:", error_count)
    iprnt ("- - - - error_i_idx:", error_i_idx)
    iprnt ("")
    test_result_a = error_count

    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("- - Test - part B")
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    iprnt ("")

    small_factor = 0.000001
    list_len = len(tt_split_list)
    iprnt ("- - - - list_len:", list_len)
    error_flag = False
    error_count = 0
    error_i_idx = None
    error_j_idx = None

    for crt_i_idx in range(list_len) :
        crt_tag = tt_split_list[crt_i_idx][0]
        crt_elem = tt_split_list[crt_i_idx][1]

        ( in_split_mode, in_split_no, no_dupl_flag, multi_flag, in_num_list, expect_thresh ) = crt_elem
        # crt_param = ( in_split_mode, in_split_no, no_dupl_flag, in_num_list )
        crt_param = ( in_num_list, in_split_no, in_split_mode, no_dupl_flag )

        iprnt ("- - - - crt_i_idx:", crt_i_idx)
        iprnt ("- - - - crt_tag:", crt_tag)
        iprnt ("- - - - - - crt_elem:", crt_elem)
        iprnt ("- - - - - - expect_thresh:", expect_thresh)
        approx_width_split = ApproxSplitList(in_num_list, in_split_no)
        iprnt ("- - - - - - approx_width_split:  ", approx_width_split[:show_max_elem])

        ordered_list = sorted(in_num_list)
        len_ordered = len(ordered_list)

        expect_len = len(expect_thresh)
        exp_proc_thresh = sorted(list(set(expect_thresh)))

        if len_ordered == 1 :
            crt_attr_thresh = [ordered_list[0]]
        else :
            if not multi_flag and expect_len > 0 :
                # exp_proc_thresh = exp_proc_thresh[:1]
                exp_proc_thresh = []
                crt_attr_thresh = ordered_list
            elif in_split_mode == 'eq_width' :
                crt_attr_thresh = ordered_list
            else :
                [crt_type, crt_attr_thresh] = deodel2.Working.NumSplit(*crt_param)

        iprnt ("- - - - - - crt_attr_thresh:  ", crt_attr_thresh)
        len_crt_thresh = len(crt_attr_thresh)

        iprnt ("- - - - - - exp_proc_thresh:", exp_proc_thresh)
        exp_proc_len = len(exp_proc_thresh)

        if in_split_mode == 'eq_width' :
            idx_factor = in_split_no - 1
        else :
            idx_factor = expect_len
        iprnt ("- - - - - - idx_factor: ", idx_factor)

        if exp_proc_len == 0 :
            # empty expected threshold
            if len_ordered > 0 :
                ref_elem = ordered_list[0]
            else :
                ref_elem = 0
            error_empty_flag = False

            crt_elem = ref_elem
            nz_delta = 100
            left_elem = crt_elem - nz_delta
            middle_elem = crt_elem
            right_elem = crt_elem + nz_delta

            val_left = deodel2.Working.DiscretizeAttrVal(left_elem, [multi_flag, crt_attr_thresh], in_split_mode, in_split_no)
            idx_left = int(val_left * (idx_factor))

            val_middle = deodel2.Working.DiscretizeAttrVal(middle_elem, [multi_flag, crt_attr_thresh], in_split_mode, in_split_no)
            idx_middle = int(val_middle * (idx_factor))

            val_right = deodel2.Working.DiscretizeAttrVal(right_elem, [multi_flag, crt_attr_thresh], in_split_mode, in_split_no)
            idx_right = int(val_right * (idx_factor))

            if in_split_no <= 1 :
                # no discretization
                if multi_flag:
                    if (
                        val_middle > val_right
                        or val_left > val_middle 
                        ) :
                        iprnt ("- - - - - - - - error - 01")
                        error_empty_flag = True
                else :
                    if len_crt_thresh > 0 :
                        if (
                            val_left != 0
                            or val_middle != 1
                            or val_right != 0
                            ) :
                            iprnt ("- - - - - - - - error - 02a")
                            error_empty_flag = True
                    else:
                        if (
                            val_left != 0
                            or val_middle != 0
                            or val_right != 0
                            ) :
                            iprnt ("- - - - - - - - error - 02b")
                            error_empty_flag = True
            else :
                # in_split_no > 1
                if len_ordered > 0 :
                    # non-empty threshold 
                    if multi_flag :
                        if (
                            val_left != 0
                            or val_middle != 1
                            or val_right != 1
                            ) :
                            iprnt ("- - - - - - - - error - 03")
                            error_empty_flag = True
                    else :
                        if (
                            val_left != 0
                            or val_middle != 1
                            or val_right != 0
                            ) :
                            iprnt ("- - - - - - - - error - 04")
                            error_empty_flag = True
                else :
                    # empty threshold
                    if (
                        val_left != 0
                        or val_middle != 0
                        or val_right != 0
                        ) :
                        iprnt ("- - - - - - - - error - 05")
                        error_empty_flag = True

            if error_empty_flag :
                error_flag = True
                error_i_idx = crt_i_idx
                error_j_idx = -1
                error_count += 1
                iprnt ("- - - - - - - - mismatch")
                iprnt ("- - - - - - - - on empty thresh")
                iprnt ("- - - - - - - - - - len_ordered:", len_ordered)
                iprnt ("- - - - - - - - - - ref_elem:", ref_elem)
                iprnt ("- - - - - - - - - - left_elem:", left_elem)
                iprnt ("- - - - - - - - - - val_left:", val_left)
                iprnt ("- - - - - - - - - - middle_elem:", middle_elem)
                iprnt ("- - - - - - - - - - val_middle:", val_middle)
                iprnt ("- - - - - - - - - - right_elem:", right_elem)
                iprnt ("- - - - - - - - - - val_right:", val_right)
                # break
        else :
            # multiple element expected threshold
            error_nonempty_flag = False
            for crt_j_idx in range(exp_proc_len) :
                crt_elem = exp_proc_thresh[crt_j_idx]
                nz_delta = (abs(crt_elem) + small_factor) * small_factor
                left_elem = crt_elem - nz_delta
                middle_elem = crt_elem
                right_elem = crt_elem + nz_delta

                val_left = deodel2.Working.DiscretizeAttrVal(left_elem, [multi_flag, crt_attr_thresh], in_split_mode, in_split_no)
                idx_left = int(val_left * (idx_factor))

                val_middle = deodel2.Working.DiscretizeAttrVal(middle_elem, [multi_flag, crt_attr_thresh], in_split_mode, in_split_no)
                idx_middle = int(val_middle * (idx_factor))

                val_right = deodel2.Working.DiscretizeAttrVal(right_elem, [multi_flag, crt_attr_thresh], in_split_mode, in_split_no)
                idx_right = int(val_right * (idx_factor))

                if not multi_flag:
                    # it is not multi_flag, same attribute value
                    if (
                        val_left != 0
                        or val_middle != 1
                        or val_right != 0
                        ) :
                        iprnt ("- - - - - - - - error - 06")
                        error_nonempty_flag = True
                else :
                    # it is multi_flag, several attribute values
                    # condition to skip duplicates
                    if ((crt_j_idx > 0)
                          and (exp_proc_thresh[crt_j_idx] == exp_proc_thresh[crt_j_idx - 1])) :
                        # skip expected duplicate entry
                        iprnt ("- - - - - - - - - - skipping")
                        iprnt ("- - - - - - - - - - - - expect_len:", expect_len)
                        iprnt ("- - - - - - - - - - - - crt_j_idx:", crt_j_idx)
                        iprnt ("- - - - - - - - - - - - exp_proc_thresh[crt_j_idx]:", exp_proc_thresh[crt_j_idx])
                        iprnt ("- - - - - - - - - - - - exp_proc_thresh[crt_j_idx-1]:", exp_proc_thresh[crt_j_idx - 1])
                        pass

                    else :
                        # non duplicate entry or first entry
                        if in_split_no <= 1 :
                            # no discretization
                            if (
                                val_middle > val_right
                                or val_left > val_middle 
                                ) :
                                iprnt ("- - - - - - - - error - 07")
                                error_nonempty_flag = True
                        else :
                            # in_split_no > 1
                            if (
                                idx_middle > idx_right
                                or idx_left >= idx_right
                                ):
                                iprnt ("- - - - - - - - error - 08")
                                error_nonempty_flag = True

                if error_nonempty_flag :
                    # a mismatch
                    error_flag = True
                    error_i_idx = crt_i_idx
                    error_j_idx = crt_j_idx
                    error_count += 1
                    iprnt ("- - - - - - - - mismatch")
                    iprnt ("- - - - - - - - crt_j_idx:", crt_j_idx)

                    iprnt ("- - - - - - - - - - left_elem:", left_elem)
                    iprnt ("- - - - - - - - - - val_left:", val_left)
                    iprnt ("- - - - - - - - - - idx_left:", idx_left)
                    iprnt ("- - - - - - - - - - middle_elem:", middle_elem)
                    iprnt ("- - - - - - - - - - val_middle:", val_middle)
                    iprnt ("- - - - - - - - - - idx_middle:", idx_middle)
                    iprnt ("- - - - - - - - - - right_elem:", right_elem)
                    iprnt ("- - - - - - - - - - val_right:", val_right)
                    iprnt ("- - - - - - - - - - idx_right:", idx_right)
                    # break
                else :
                    # entry conforms
                    pass
        if error_flag :
            # break
            pass
            
    iprnt ("- - - - error_flag:", error_flag)
    iprnt ("- - - - error_count:", error_count)
    iprnt ("- - - - error_i_idx:", error_i_idx)
    iprnt ("- - - - error_j_idx:", error_j_idx)
    test_result_b = error_count

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    test_result = (test_result_a, test_result_b)
    test_expect = (0, 0)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += (test_result_a + test_result_b)
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    #'''#

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    iprnt ("deodel fit test - 1")

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

    tt_transp_X = deodel2.Working.MatrixTranspose(tt_X)
    iprnt ("- - - -        tt_transp_X:", tt_transp_X)


    aux_param = {'split_mode': 'eq_freq', 'split_no': 10, 'legacy_match': False, 'int_is_num': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
    tt_o.fit(tt_X, tt_y)
    iprnt ()

    test_result = tt_o.attr_cat_X.tolist()
    test_transp_result = deodel2.Working.MatrixTranspose(test_result)

    # ref_item = [[1, 2, 3, 2, 4], [ 3, 1, 2,  5, 1], [1, 2,  3,  2,  1], [1, 2, 2, 3, 1]]
    ref_item =   [[1, 2, 3, 2, 4], [-2, 1, 2, -2, 1], [1, -2, -2, -2, 1], [1, 2, 2, 3, 1]]

    iprnt ("- - - - test_transp_result:", test_transp_result)
    iprnt ("- - - -           ref_item:", ref_item)
    iprnt ()

    test_expect = deodel2.Working.MatrixTranspose(ref_item)

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

    tt_transp_X = deodel2.Working.MatrixTranspose(tt_X)
    iprnt ("- - - -        tt_transp_X:", tt_transp_X)

    aux_param = {'split_mode': 'eq_freq', 'split_no': 10, 'legacy_match': False, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
    tt_o.fit(tt_X, tt_y)
    iprnt ()

    test_result = tt_o.attr_cat_X.tolist()
    test_transp_result = deodel2.Working.MatrixTranspose(test_result)

    # ref_item = [[1, 2, 3, 2, 4], [ 2, 1,  4,  3, 1], [1,  4, 2,  4, 1], [1, 2, 2, 3, 1]]
    ref_item =   [[1, 2, 3, 2, 4], [-2, 1, -2, -2, 1], [1, -2, 2, -2, 1], [1, 2, 2, 3, 1]]

    iprnt ("- - - - test_transp_result:", test_transp_result)
    iprnt ("- - - -           ref_item:", ref_item)
    iprnt ()

    test_expect = deodel2.Working.MatrixTranspose(ref_item)

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
    iprnt ("predict test - 1 (continuation)")

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
    iprnt ("predict test - 2")
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

    aux_param = {'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("dealing with missing attributes (None), ignore them - a")
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

    aux_param = {'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("dealing with missing attributes (None), ignore them - b")
    iprnt ()
    tt_X = [['a',   None,   'az',   'e'],
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
            'B',
            'B',
            'C',
            'A',
           ]

    aux_param = {'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("behaviour when no tie break - 1")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
    tt_o.fit(tt_X, tt_y)

    iprnt ("- - - - tt_o.cfg_param:", tt_o.cfg_param)
    iprnt ()

    tt_predict = tt_o.predict(tt_test)

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
    iprnt ("integer mix in prediction - int_is_num: true - 1")
    iprnt ()

    iprnt ()
    tt_X = [
            ['a',   4.9,   ],
            ['b',   5.0,   ],
            ['c',   5.1,   ],
            ['d',   5,     ],
            ['e',   5,     ],
            ['f',   3.01,  ],
            ['g',   'z',   ],
           ]

    tt_y = [
            'A',
            'A',
            'A',
            'B',
            'B',
            'C',
            'C',
           ]

    tt_test = [
            ['x',   4.9,   ],
            ['x',   5.0,   ],
            ['x',   5.1,   ],
            ['x',   5,     ],
            ['x',   5,     ],
            ['x',   3.5,   ],
            ['x',   'z',   ],
            ]

    tt_exp = ['A', 'A', 'A', 'A', 'A', 'C', 'C']

    aux_param = {'split_no': 10, 'legacy_match': False, 'int_is_num': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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
    iprnt ("integer mix in prediction - int_is_num: false - 2")
    iprnt ()

    tt_X = [
            ['a',   4.9,   ],
            ['b',   5.0,   ],
            ['c',   5.1,   ],
            ['d',   5,     ],
            ['e',   5,     ],
            ['f',   3.01,  ],
            ['g',   'z',   ],
           ]

    tt_y = [
            'A',
            'A',
            'A',
            'B',
            'B',
            'C',
            'C',
           ]

    tt_test = [
            ['x',   4.9,   ],
            ['x',   5.0,   ],
            ['x',   5.1,   ],
            ['x',   5,     ],
            ['x',   5,     ],
            ['x',   3.5,   ],
            ['x',   'z',   ],
            ]

    tt_exp = ['A', 'A', 'A', 'B', 'B', 'C', 'C']

    aux_param = {'split_no': 10, 'legacy_match': False, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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
    iprnt ("integer mix in prediction - int_is_num: false - 3")
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

    aux_param = {'split_no': 10, 'legacy_match': False, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("integer mix in dealing with missing attributes - int_is_num: false - a")
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

    aux_param = {'split_no': 10, 'legacy_match': False, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("integer mix in dealing with missing attributes - int_is_num: false - b")
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

    aux_param = {'split_no': 10, 'legacy_match': True, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("integer mix in dealing with missing attributes - int_is_num: false - c")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    None,   'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   None]]

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

    aux_param = {'split_no': 10, 'legacy_match': True, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("integer mix in dealing with missing attributes - int_is_num: false - d")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    None,   'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   None]]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   None,   'd'],
            ['b',   "3.01", 2.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   None]]

    tt_exp = [
            'A',
            'B',
            'B',
            'B',
           ]

    aux_param = {'split_no': 10, 'legacy_match': True, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("integer mix in dealing with missing attributes - int_is_num: false - e")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'],
            ['d',   "4",    None,   'd'],
            ['b',   2.0,    3.01,   'h'],
            ['c',   '3.01', 'az',   None]]

    tt_y = [
            'A',
            'B',
            'B',
            'C',
            'A'
           ]

    tt_test = [
            ['a',   1.01,   None,   'd'],
            ['b',   "3.01", 2.01,   'e'],
            ['b',   2,      5.0,    'e'],
            ['a',   "4",    3.01,   None]]

    tt_exp = [
            'A',
            'B',
            'B',
            'B',
           ]

    aux_param = {'split_no': 10, 'legacy_match': False, 'int_is_num': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("integer mix in no tie break - int_is_num: false")
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

    int_isnum = False
    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False, 'int_is_num': int_isnum}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("behaviour when no tie break - 2")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological ref - 6-a")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input - 7-a")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological ref pd - 8-a")
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

    # tt_X = pd.array(t1_X)
    tt_X = pd.array(t1_X, dtype=object)
    tt_y = pd.array(t1_y)
    tt_test = pd.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 9-a")
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

    # tt_X = pd.array(t1_X)
    tt_X = pd.array(t1_X, dtype=object)
    tt_y = pd.array(t1_y)
    tt_test = pd.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 10-a")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 11-a")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 12-a")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 13-a")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 14-a")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological ref - 6-b")
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
            'C',
            'C',
           ]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input - 7-b")
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
            'C',
            'C',
           ]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological ref pd - 8-b")
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
            'C',
            'C',
           ]

    # tt_X = pd.array(t1_X)
    tt_X = pd.array(t1_X, dtype=object)
    tt_y = pd.array(t1_y)
    tt_test = pd.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 9-b")
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
            'C',
            'C',
           ]

    # tt_X = pd.array(t1_X)
    tt_X = pd.array(t1_X, dtype=object)
    tt_y = pd.array(t1_y)
    tt_test = pd.array(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 10-b")
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
            'C',
            'C',
           ]

    # tt_X = pd.DataFrame(t1_X)
    tt_X = pd.array(t1_X, dtype=object)
    tt_y = pd.DataFrame(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 11-b")
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
            'C',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    tt_y = pd.DataFrame(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 12-b")
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
            'C',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    tt_y = pd.DataFrame(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 13-b")
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
            'C',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    # tt_y = pd.DataFrame(t1_y)
    tt_y = pd.Series(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("pathological input pd - 14-b")
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
            'C',
            'C',
           ]

    tt_X = pd.DataFrame(t1_X)
    tt_y = pd.Series(t1_y)
    tt_test = pd.DataFrame(t1_test)

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    t1_X = [['a',   1.01,   4.01,   2.7],
            ['b',   "3.01", 4.01,   2.7],
            ['d',   "4",    4.01,   2.7],
            ['b',    2.0,   4.01,   2.7],
            ['a',    3,     4.01,   2.7],
            [None,   -1.0,  3.02,   2.7],
            ['c',   '3.01', 4.01,   2.7]]

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
            ['b',   2,      5.0,    3.3],
            ['a',   "4",    3.01,   2.7]]

    tt_exp = [
            'C',
            'A',
            'B',
            'A',
           ]

    tt_X = t1_X
    tt_y = t1_y
    tt_test = t1_test

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ("- - - - tt_y:", tt_y)
    iprnt ("- - - - tt_test:", tt_test)

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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
    # tt_in_1 = pd.array(tin_1)
    tt_in_1 = pd.array(tin_1, dtype=object)
    # tt_in_2 = pd.array(tin_2)
    tt_in_2 = pd.array(tin_2, dtype=object)
    tt_in_3 = pd.array(tin_3)
    
    iprnt ("- - - - tt_in_1:", tt_in_1)
    iprnt ("- - - - tt_in_2:", tt_in_2)
    iprnt ("- - - - tt_in_3:", tt_in_3)

    tout_1 = deodel2.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel2.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel2.CasetDeodel.ListDataConvert(tt_in_3)

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

    tout_1 = deodel2.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel2.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel2.CasetDeodel.ListDataConvert(tt_in_3)

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

    tout_1 = deodel2.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel2.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel2.CasetDeodel.ListDataConvert(tt_in_3)

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

    # tt_in_1 = np.array(tin_1)
    tt_in_1 = np.array(tin_1, dtype=object)
    # tt_in_2 = np.array(tin_2)
    tt_in_2 = np.array(tin_2, dtype=object)
    tt_in_3 = np.array(tin_3)
    
    iprnt ("- - - - tt_in_1:", tt_in_1)
    iprnt ("- - - - tt_in_2:", tt_in_2)
    iprnt ("- - - - tt_in_3:", tt_in_3)

    tout_1 = deodel2.CasetDeodel.ListDataConvert(tt_in_1)
    tout_2 = deodel2.CasetDeodel.ListDataConvert(tt_in_2)
    tout_3 = deodel2.CasetDeodel.ListDataConvert(tt_in_3)

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

    iprnt ("ListDataConvert numeric")
    iprnt ()

    tin_1 =    [
                [101,   102.5,  103  ],
                [201.7, 202.8,  203.9],
                [301,   302,    303  ],
               ]

    tin_2 = np.array(tin_1)

    tin_3 = []
    for crt_row in tin_1 :
        new_row = np.array(crt_row)
        tin_3.append(new_row)

    iprnt ("- - - - tin_1:", tin_1)
    iprnt ("- - - - tin_2:", tin_2)
    iprnt ("- - - - tin_3:", tin_3)

    tout_1 = deodel2.CasetDeodel.ListDataConvert(tin_1)
    tout_2 = deodel2.CasetDeodel.ListDataConvert(tin_2)
    tout_3 = deodel2.CasetDeodel.ListDataConvert(tin_3)

    iprnt ("- - - - tout_1:", tout_1)
    iprnt ("- - - - tout_2:", tout_2)
    iprnt ("- - - - tout_3:", tout_3)

    test_result = (tout_1, tout_2, tout_3)
    test_expect = (tin_1, tin_1, tin_1)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    test_result = deodel2.DeodelSecond.version
    # test_expect = 1.51
    # test_expect = 1.65
    # test_expect = 1.75
    # test_expect = 1.77
    # test_expect = 2.01
    # test_expect = 2.11
    test_expect = 2.17

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("default config")
    iprnt ()

    tt_X = [['a',   7702],
            ['b',   7703]]

    tt_y = [
            'X',
            'Y',
           ]

    tt_test= [
            ['a',   None],
            ['b',   7705]]

    tt_wrk_X = tt_X
    tt_wrk_test = tt_test
    tt_wrk_y = tt_y
    
    tt_exp = [
            'X',
            'Y',
           ]

    tt_o = deodel2.DeodelSecond()
    tt_o.fit(tt_wrk_X, tt_wrk_y)
    tt_predict = tt_o.predict(tt_wrk_test)

    iprnt ("- - - - tt_o.__dict__ :", tt_o.__dict__ )

    test_result = tt_o.cfg_param 
    test_expect = {
                    'split_no':     0,
                    'split_mode':   'eq_width',
                    'tbreak_depth': None,
                    'predict_mode': 'auto',
                    'score_factor': 2,
                    'legacy_match':  False,
                    'int_is_num':   True,
                  }

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("internal state")
    iprnt ()

    tt_X = [
            ['a',   7702,   8102],
            ['b',   7803,   8203],
            ['c',   7904,   None],
            ['d',   7904,   'm'],
           ]

    iprnt ("- - - - tt_X:", tt_X)
    iprnt ()

    tt_y = [
            'V',
            'X',
            'Y',
            'Z',
           ]

    iprnt ("- - - - tt_y:", tt_y)
    iprnt ()

    tt_wrk_X = tt_X
    tt_wrk_test = tt_test
    tt_wrk_y = tt_y
    
    tt_exp = [
            'X',
            'Y',
           ]

    aux_param = {'split_no': 3, 'legacy_match': False}
    # aux_param = {'split_no': 0, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)

    tt_o.fit(tt_wrk_X, tt_wrk_y)
    tt_internal = tt_o.__dict__

    tt_expect = {
        'aux_param': {'split_no': 3, 'legacy_match': False}, 
        'cfg_param': {'split_no': 3, 'split_mode': 'eq_width', 'tbreak_depth': None, 
        'predict_mode': 'auto', 'score_factor': 2, 'legacy_match': False, 'int_is_num': True}, 
        'attr_cat_X': np.array([[ 1, -2, -2],
        [ 2, -2, -2],
        [ 3, -2,  1],
        [ 4, -2,  2]]), 'attr_num_X': np.array([[-1. ,  0. ,  0. ],
        [-1. ,  0.5,  1. ],
        [-1. ,  1. , -1. ],
        [-1. ,  1. , -1. ]]), 'attr_mask_X': np.array([[0, 1, 1],
        [0, 1, 1],
        [0, 1, 0],
        [0, 1, 0]]), 'attr_num_cfg': [[False, []], [True, [7702, 7904]], [True, [8102, 8203]]], 'attr_dict_list': [{'a': 1, 'b': 2,
        'c': 3, 'd': 4}, {}, {None: 1, 'm': 2}], 'attr_split_no': 3,
        'attr_split_mode': 'eq_width', 'attr_score_factor': 2, 'attr_int_is_num': True, 'attr_legacy_match': False, 'regress_flag': False, 'targ_y': ['V', 'X', 'Y', 'Z']
    }

    test_result = tt_internal
    test_expect = tt_expect

    iprnt ("- - - - test_result:", test_result)
    iprnt ()
    iprnt ("- - - - test_expect:", test_expect)
    iprnt ()

    # set_eval = ( test_result == test_expect )
    set_eval = ( str(test_result) == str(test_expect) )

    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    aux_param = {'tbreak_depth': 1, 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
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

    iprnt ("classification test - 1")
    iprnt ()

    X_train = [ 
                ['a00', 200, 'f'],
                ['a01', 210, 'f'],
                ['a02', 220, 'f'],
                ['a03', 230, 'f'],
                ['a04', 240, 'f'],
                ['a05', 250, 'f'],
                ['a06', 260, 'f'],
                ['a07', 270, 'f'],
                ['a08', 280, 'f'],
                ['a09', 290, 'f'],
                ['a10', 300, 'f'],
              ]

    iprnt ("- - - - X_train:", X_train)
    iprnt ()

    y_train = ['y00','y01','y02','y03','y04','y05','y06','y07','y08','y09','y10']

    iprnt ("- - - - y_train:", y_train)
    iprnt ()

    X_test =  [
                ['b00', 203, 'f'],
                ['b00', 207, 'f'],
                ['b01', 213, 'f'],
                ['b01', 217, 'f'],
                ['b02', 223, 'f'],
                ['b02', 227, 'f'],
                ['b03', 233, 'f'],
                ['b03', 237, 'f'],
                ['b04', 243, 'f'],
                ['b04', 247, 'f'],
                ['b05', 253, 'f'],
                ['b05', 257, 'f'],
                ['b06', 263, 'f'],
                ['b06', 267, 'f'],
                ['b07', 273, 'f'],
                ['b07', 277, 'f'],
                ['b08', 283, 'f'],
                ['b08', 287, 'f'],
                ['b09', 293, 'f'],
                ['b09', 297, 'f'],
                ['b10', 303, 'f'],
                ['b10', 307, 'f'],
              ]

    iprnt ("- - - - X_test:", X_test)
    iprnt ()

    y_expect = ['y00', 'y01', 'y01', 'y02', 'y02', 'y03', 'y03', 'y04', 'y04', 'y05', 'y05', 'y06', 'y06', 'y07', 'y07', 'y08', 'y08', 'y09', 'y09', 'y10', 'y10', 'y10']

    aux_param = {'split_no': 11, 'score_factor': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
    tt_o.fit(X_train, y_train)
    tt_predict = tt_o.predict(X_test)

    test_result = tt_predict
    test_expect = y_expect

    iprnt ()
    iprnt ("- - - - test_result:", test_result)
    iprnt ()
    iprnt ("- - - - test_expect:", test_expect)
    iprnt ()

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("classification test - 2")
    iprnt ()

    X_train = [ 
                ['a00', 200, 'f'],
                ['a01', 210, 'f'],
                ['a02', 220, 'f'],
                ['a03', 230, 'f'],
                ['a04', 240, 'f'],
                ['a05', 250, 'f'],
                ['a06', 260, 'f'],
                ['a07', 270, 'f'],
                ['a08', 280, 'f'],
                ['a09', 290, 'f'],
                ['a10', 300, 'f'],
              ]

    iprnt ("- - - - X_train:", X_train)
    iprnt ()

    y_train = ['y00','y01','y02','y03','y04','y05','y06','y07','y08','y09','y10']

    iprnt ("- - - - y_train:", y_train)
    iprnt ()

    X_test =  [
                ['b00', 203, 'f'],
                ['b00', 207, 'f'],
                ['b01', 213, 'f'],
                ['b01', 217, 'f'],
                ['b02', 223, 'f'],
                ['b02', 227, 'f'],
                ['b03', 233, 'f'],
                ['b03', 237, 'f'],
                ['b04', 243, 'f'],
                ['b04', 247, 'f'],
                ['b05', 253, 'f'],
                ['b05', 257, 'f'],
                ['b06', 263, 'f'],
                ['b06', 267, 'f'],
                ['b07', 273, 'f'],
                ['b07', 277, 'f'],
                ['b08', 283, 'f'],
                ['b08', 287, 'f'],
                ['b09', 293, 'f'],
                ['b09', 297, 'f'],
                ['b10', 303, 'f'],
                ['b10', 307, 'f'],
              ]

    iprnt ("- - - - X_test:", X_test)
    iprnt ()

    # y_expect = ['y00', 'y01', 'y01', 'y02', 'y02', 'y03', 'y03', 'y04', 'y04', 'y05', 'y05', 'y06', 'y06', 'y07', 'y07', 'y08', 'y08', 'y09', 'y09', 'y10', 'y10', 'y10']
    y_expect =   ['y00', 'y00', 'y01', 'y01', 'y01', 'y01', 'y03', 'y03', 'y03', 'y03', 'y05', 'y05', 'y05', 'y05', 'y07', 'y07', 'y07', 'y07', 'y09', 'y09', 'y09', 'y09']

    # aux_param = {'split_no': 11, 'score_factor': 10, 'legacy_match': False}
    aux_param = {'split_no': 6, 'score_factor': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
    tt_o.fit(X_train, y_train)
    tt_predict = tt_o.predict(X_test)

    test_result = tt_predict
    test_expect = y_expect

    iprnt ()
    iprnt ("- - - - test_result:", test_result)
    iprnt ()
    iprnt ("- - - - test_expect:", test_expect)
    iprnt ()

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("classification test - 3")
    iprnt ()

    X_train = [ 
                ['a00', 200, 'f'],
                ['a01', 210, 'f'],
                ['a02', 220, 'f'],
                ['a03', 230, 'f'],
                ['a04', 240, 'f'],
                ['a05', 250, 'f'],
                ['a06', 260, 'f'],
                ['a07', 270, 'f'],
                ['a08', 280, 'f'],
                ['a09', 290, 'f'],
                ['a10', 300, 'f'],
              ]

    iprnt ("- - - - X_train:", X_train)
    iprnt ()

    y_train = ['y00','y01','y02','y03','y04','y05','y06','y07','y08','y09','y10']

    iprnt ("- - - - y_train:", y_train)
    iprnt ()

    X_test =  [
                ['b00', 203, 'f'],
                ['b00', 207, 'f'],
                ['b01', 213, 'f'],
                ['b01', 217, 'f'],
                ['b02', 223, 'f'],
                ['b02', 227, 'f'],
                ['b03', 233, 'f'],
                ['b03', 237, 'f'],
                ['b04', 243, 'f'],
                ['b04', 247, 'f'],
                ['b05', 253, 'f'],
                ['b05', 257, 'f'],
                ['b06', 263, 'f'],
                ['b06', 267, 'f'],
                ['b07', 273, 'f'],
                ['b07', 277, 'f'],
                ['b08', 283, 'f'],
                ['b08', 287, 'f'],
                ['b09', 293, 'f'],
                ['b09', 297, 'f'],
                ['b10', 303, 'f'],
                ['b10', 307, 'f'],
              ]

    iprnt ("- - - - X_test:", X_test)
    iprnt ()

    y_expect = ['y00', 'y01', 'y01', 'y02', 'y02', 'y03', 'y03', 'y04', 'y04', 'y05', 'y05', 'y06', 'y06', 'y07', 'y07', 'y08', 'y08', 'y09', 'y09', 'y10', 'y10', 'y10']

    aux_param = {'split_no': 0, 'score_factor': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    tt_o = deodel2.DeodelSecond(aux_param)
    tt_o.fit(X_train, y_train)
    tt_predict = tt_o.predict(X_test)

    test_result = tt_predict
    test_expect = y_expect

    iprnt ()
    iprnt ("- - - - test_result:", test_result)
    iprnt ()
    iprnt ("- - - - test_expect:", test_expect)
    iprnt ()

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("regression test 1-a")
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
    # deodel_regress = deodel2.DeodelSecond()
    # deodel_regress = deodel2.DeodelSecond({'split_no': 5, 'split_mode': 'eq_freq'})

    aux_param = {'split_mode': 'eq_width', 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.1, 0.1, 0.3, 0.3, 0.5, 0.6, 0.7, 0.8, 0.9, 0.9]
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

    iprnt ("regression test 1-b")
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
    # deodel_regress = deodel2.DeodelSecond()
    # deodel_regress = deodel2.DeodelSecond({'split_no': 5, 'split_mode': 'eq_freq'})

    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.1, 0.1, 0.3, 0.3, 0.5, 0.6, 0.7, 0.8, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.04999999999999998
    e_mse = 0.002999999999999996
    e_R2 = 0.9636363636363636

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

    iprnt ("regression test 1-c")
    iprnt ()

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

    aux_param = {'split_mode': 'eq_width', 'split_no': 100, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.05, 0.15000000000000002, 0.25, 0.35, 0.45, 0.55, 0.6499999999999999, 0.75, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.010000000000000012
    e_mse = 0.0009999999999999974
    e_R2 = 0.9878787878787879

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

    iprnt ("regression test 1-d")
    iprnt ()

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

    aux_param = {'split_mode': 'eq_width', 'split_no': 0, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.05, 0.15000000000000002, 0.25, 0.35, 0.45, 0.55, 0.6499999999999999, 0.75, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.010000000000000012
    e_mse = 0.0009999999999999974
    e_R2 = 0.9878787878787879


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

    iprnt ("regression test 1-e")
    iprnt ()

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

    aux_param = {'split_mode': 'eq_width', 'split_no': 5, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.05, 0.25, 0.25, 0.45, 0.45, 0.45, 0.6499999999999999, 0.6499999999999999, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.050000000000000024
    e_mse = 0.005000000000000001
    e_R2 = 0.9393939393939393

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

    iprnt ("regression test 1-f")
    iprnt ()

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

    aux_param = {'split_mode': 'eq_legacy_width', 'split_no': 5, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.05, 0.05, 0.25, 0.25, 0.45, 0.6499999999999999, 0.6499999999999999, 0.8500000000000001, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.05
    e_mse = 0.004999999999999996
    e_R2 = 0.9393939393939394

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

    iprnt ("regression test 1-g")
    iprnt ()

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

    aux_param = {'split_mode': 'eq_freq', 'split_no': 5, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.05, 0.05, 0.25, 0.45, 0.45, 0.6499999999999999, 0.6499999999999999, 0.8500000000000001, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.05
    e_mse = 0.004999999999999997
    e_R2 = 0.9393939393939394


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

    aux_param = {'split_mode': 'eq_width', 'split_no': 4, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.05, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.8500000000000001, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.06999999999999999
    e_mse = 0.007499999999999998
    e_R2 = 0.9090909090909091

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

    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 4, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)


    deodel_regress = deodel2.DeodelSecond({'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 4, 'legacy_match': False})

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

    e_pred = [0.05, 0.3, 0.3, 0.3, 0.6, 0.6, 0.6, 0.8500000000000001, 0.8500000000000001, 0.8500000000000001]
    e_mae = 0.06999999999999999
    e_mse = 0.007499999999999998
    e_R2 = 0.9090909090909091

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

    aux_param = {'predict_mode': 'classif', 'split_mode': 'eq_width', 'split_no': 4, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

    deodel_regress = deodel2.DeodelSecond({'predict_mode': 'classif', 'split_mode': 'eq_width', 'split_no': 4, 'legacy_match': False})

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

    e_pred = [0.0, 0.2, 0.2, 0.2, 0.5, 0.5, 0.5, 0.8, 0.8, 0.8]
    
    e_mae = 0.07999999999999999
    e_mse = 0.008499999999999997
    e_R2 = 0.896969696969697

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

    iprnt ("regression mixed test 1-a")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [ [0.0, 0.0, 'a'],
                [0.1, 0.1, 'a'], 
                [0.2, 0.2, 'a'], 
                [0.3, 0.3, 'a'], 
                [0.4, 0.4, 'a'], 
                [0.5, 0.5, 'a'], 
                [0.6, 0.6, 'a'], 
                [0.7, 0.7, 'a'], 
                [0.8, 0.8, 'a'], 
                [0.9, 0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'y', 'z', 'x']

    X_test = [  [0.05, 0.05, 'b'], 
                [0.15, 0.15, 'b'], 
                [0.25, 0.25, 'b'], 
                [0.35, 0.35, 'b'], 
                [0.45, 0.45, 'b'], 
                [0.55, 0.55, 'b'], 
                [0.65, 0.65, 'b'], 
                [0.75, 0.75, 'b'], 
                [0.85, 0.85, 'b'], 
                [0.95, 0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    aux_param = {'split_mode': 'eq_width', 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.1, 0.1, 0.3, 0.3, 0.5, 'x', 'y', 'z', 'x', 'x']

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

    iprnt ("regression mixed test 1-b")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 0.0, 'a'], [0.1, 0.1, 'a'], [0.2, 0.2, 'a'], [0.3, 0.3, 'a'], [0.4, 0.4, 'a'], 
               [0.5, 0.5, 'a'], [0.6, 0.6, 'a'], [0.7, 0.7, 'a'], [0.8, 0.8, 'a'], [0.9, 0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'y', 'z', 'x']

    X_test = [[0.05, 0.05, 'b'], [0.15, 0.15, 'b'], [0.25, 0.25, 'b'], [0.35, 0.35, 'b'], [0.45, 0.45, 'b'], 
              [0.55, 0.55, 'b'], [0.65, 0.65, 'b'], [0.75, 0.75, 'b'], [0.85, 0.85, 'b'], [0.95, 0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.1, 0.1, 0.3, 0.3, 0.45, 0.5, 'x', 'x', 'x', 'x']

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

    iprnt ("regression mixed test 2-a")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a'], [0.1, 'a'], [0.2, 'a'], [0.3, 'a'], [0.4, 'a'], 
               [0.5, 'a'], [0.6, 'a'], [0.7, 'a'], [0.8, 'a'], [0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'x', 'y', 'z']

    X_test = [[0.05, 'b'], [0.15, 'b'], [0.25, 'b'], [0.35, 'b'], [0.45, 'b'], 
              [0.55, 'b'], [0.65, 'b'], [0.75, 'b'], [0.85, 'b'], [0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    aux_param = {'split_mode': 'eq_width', 'split_no': 10, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.1, 0.1, 0.3, 0.3, 0.5, 'x', 'x', 'y', 'z', 'z']

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

    iprnt ("regression mixed test 2-b")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a'], [0.1, 'a'], [0.2, 'a'], [0.3, 'a'], [0.4, 'a'], 
               [0.5, 'a'], [0.6, 'a'], [0.7, 'a'], [0.8, 'a'], [0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'x', 'y', 'z']

    X_test = [[0.05, 'b'], [0.15, 'b'], [0.25, 'b'], [0.35, 'b'], [0.45, 'b'], 
              [0.55, 'b'], [0.65, 'b'], [0.75, 'b'], [0.85, 'b'], [0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 5, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    # e_pred = [0.0, 0.1, 0.2, 0.3, 0.5, 'x', 'x', 'y', 'z', 'z']
    # e_pred = [0.05, 0.1, 0.2, 0.3, 0.45, 'x', 'x', 'x', 'y', 'y']
    e_pred = [0.15, 0.25, 0.25, 0.35, 0.35, 0.35, 0.45, 0.45, 'x', 'x']

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

    iprnt ("regression mixed test 2-c")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a'], [0.1, 'a'], [0.2, 'a'], [0.3, 'a'], [0.4, 'a'], 
               [0.5, 'a'], [0.6, 'a'], [0.7, 'a'], [0.8, 'a'], [0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'x', 'y', 'z']

    X_test = [[0.05, 'b'], [0.15, 'b'], [0.25, 'b'], [0.35, 'b'], [0.45, 'b'], 
              [0.55, 'b'], [0.65, 'b'], [0.75, 'b'], [0.85, 'b'], [0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.15, 0.15, 0.3, 0.3, 0.4, 0.45, 'x', 'x', 'x', 'x']

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

    iprnt ("regression mixed test 2-d")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a'], [0.1, 'a'], [0.2, 'a'], [0.3, 'a'], [0.4, 'a'], 
               [0.5, 'a'], [0.6, 'a'], [0.7, 'a'], [0.8, 'a'], [0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'x', 'y', 'z']

    X_test = [[0.05, 'b'], [0.15, 'b'], [0.25, 'b'], [0.35, 'b'], [0.45, 'b'], 
              [0.55, 'b'], [0.65, 'b'], [0.75, 'b'], [0.85, 'b'], [0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 0, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    # e_pred = [0.0, 0.1, 0.2, 0.3, 0.5, 'x', 'x', 'y', 'z', 'z']
    # e_pred = [0.05, 0.1, 0.2, 0.3, 0.45, 'x', 'x', 'x', 'y', 'y']
    e_pred = [0.1, 0.15, 0.25, 0.35, 0.4, 0.45, 'x', 'x', 'x', 'x']

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

    iprnt ("regression mixed test 2-e")
    iprnt ()

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    X_train = [[0.0, 'a'], [0.1, 'a'], [0.2, 'a'], [0.3, 'a'], [0.4, 'a'], 
               [0.5, 'a'], [0.6, 'a'], [0.7, 'a'], [0.8, 'a'], [0.9, 'a']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 'x', 'y', 'z', 'w']

    X_test = [[0.05, 'b'], [0.15, 'b'], [0.25, 'b'], [0.35, 'b'], [0.45, 'b'], 
              [0.55, 'b'], [0.65, 'b'], [0.75, 'b'], [0.85, 'b'], [0.95, 'b']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    e_pred = [0.15, 0.15, 0.3, 0.3, 0.4, 0.45, 0.5, 'x', 'y', 'y']

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

    X_train = [ [0.0, 'a', 'g'], 
                [0.1, 'a', 'g'], 
                [0.2, 'a', 'g'], 
                [0.3, 'a', 'g'], 
                [0.4, 'a', 'g'], 
                [0.5, 'a', 'g'], 
                [0.6, 'a', 'g'], 
                [0.7, 'a', 'g'], 
                [0.8, 'a', 'g'], 
                [0.9, 'a', 'g']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 'x', 'x', 'y']

    X_test = [  [0.05, 'b', 'h'], 
                [0.15, 'b', 'h'], 
                [0.25, 'b', 'h'], 
                [0.35, 'b', 'h'], 
                [0.45, 'b', 'h'], 
                [0.55, 'b', 'h'], 
                [0.65, 'b', 'h'], 
                [0.75, 'b', 'h'], 
                [0.85, 'b', 'h'], 
                [0.95, 'b', 'h']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 2, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    X_train = [ [0.0, 'a', 'g'], 
                [0.1, 'a', 'g'], 
                [0.2, 'a', 'g'], 
                [0.3, 'a', 'g'], 
                [0.4, 'a', 'g'], 
                [0.5, 'a', 'g'], 
                [0.6, 'a', 'g'], 
                [0.7, 'a', 'g'], 
                [0.8, 'a', 'g'], 
                [0.9, 'a', 'g']]

    y_train = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 'x', 'x', 'y']

    X_test = [  [0.05, 'b', 'h'], 
                [0.15, 'b', 'h'], 
                [0.25, 'b', 'h'], 
                [0.35, 'b', 'h'], 
                [0.45, 'b', 'h'], 
                [0.55, 'b', 'h'], 
                [0.65, 'b', 'h'], 
                [0.75, 'b', 'h'], 
                [0.85, 'b', 'h'], 
                [0.95, 'b', 'h']]

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    aux_param = {'predict_mode': 'classif', 'split_mode': 'eq_width', 'split_no': 2, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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
    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 2, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    aux_param = {'predict_mode': 'classif', 'split_mode': 'eq_width', 'split_no': 2, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    aux_param = {'predict_mode': 'regress', 'split_mode': 'eq_width', 'split_no': 2, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    aux_param = {'predict_mode': 'classif', 'split_mode': 'eq_width', 'split_no': 2, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodel_regress = deodel2.DeodelSecond(aux_param)

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

    iprnt ("regression vs classification test 1")
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

    aux_param = {'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodelo = deodel2.DeodelSecond(aux_param)

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

    iprnt ("regression vs classification test 2")
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

    aux_param = {'predict_mode': 'regress', 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodelo = deodel2.DeodelSecond(aux_param)

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

    iprnt ("regression vs classification test 3")
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

    aux_param = {'predict_mode': 'regress', 'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodelo = deodel2.DeodelSecond(aux_param)

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

    iprnt ("regression vs classification test 4")
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

    aux_param = {'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    deodelo = deodel2.DeodelSecond(aux_param)

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
    import deodel2

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

    from sklearn import datasets

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


    iprnt ("test sklearn dataset 1-a")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 3, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    # test_expect = (0.9400749063670412, 0.250936329588015)
    test_expect = (0.9063670411985019, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1-b")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 3, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    # test_expect = (0.9063670411985019, 0.250936329588015)
    test_expect = (0.895131086142322, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1-c")
    iprnt ()

    data_set = datasets.load_iris()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_no': 6, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    # test_expect = (0.9775280898876405, 0.250936329588015)
    # test_expect = (0.9662921348314607, 0.250936329588015)
    test_expect = (0.9511111111111111, 0.3333333333333333)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1-d")
    iprnt ()

    data_set = datasets.load_iris()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_no': 6, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    # test_expect = (0.9511111111111111, 0.3333333333333333)
    test_expect = (0.9466666666666667, 0.3333333333333333)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1-e")
    iprnt ()

    data_set = datasets.load_iris()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_legacy_width', 'split_no': 6, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9555555555555556, 0.3333333333333333)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1-f")
    iprnt ()

    data_set = datasets.load_iris()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_legacy_width', 'split_no': 6, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    # test_expect = (0.9555555555555556, 0.3333333333333333)
    test_expect = (0.9511111111111111, 0.3333333333333333)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1-g")
    iprnt ()

    data_set = datasets.load_iris()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 6}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9466666666666667, 0.3333333333333333)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 1-h")
    iprnt ()

    data_set = datasets.load_iris()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 6, 'legacy_match': True}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9511111111111111, 0.3333333333333333)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
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

    iprnt ("test sklearn dataset 3")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_no': 10, 'legacy_match': False}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    # test_expect = (0.9775280898876405, 0.250936329588015)
    test_expect = (0.9662921348314607, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-a")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_freq', 'split_no': 7}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9325842696629213, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-b")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_freq', 'split_no': 7, 'legacy_match': True, 'score_factor': 1}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)
    iprnt ("- - - - aux_param:", aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9325842696629213, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-c")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_freq', 'split_no': 7, 'legacy_match': True, 'score_factor': 5}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9325842696629213, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-d")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_freq', 'split_no': 7, 'legacy_match': False, 'score_factor': 5}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9250936329588014, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
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

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-e")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 7}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9737827715355806, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-f")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_legacy_width', 'split_no': 7, 'legacy_match': True, 'score_factor': 1}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)
    iprnt ("- - - - aux_param:", aux_param)

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

    iprnt ("test sklearn dataset 4-g")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_legacy_width', 'split_no': 7, 'legacy_match': True, 'score_factor': 5}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

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

    iprnt ("test sklearn dataset 4-h")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 7, 'legacy_match': True, 'score_factor': 5}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9213483146067415, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-i")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 7, 'legacy_match': True, 'score_factor': 1}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9213483146067415, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-j")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 7, 'legacy_match': False, 'score_factor': 1}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9700374531835205, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test sklearn dataset 4-k")
    iprnt ()

    data_set = datasets.load_wine()
    iprnt ("- - - - data_set:", data_set['DESCR'][:19])
    display_flag = True

    data_digi_x = data_set.data
    data_target_y = data_set.target
    train_ratio = 0.5
    in_iter_no = 3
    in_rand_seed = 42
    aux_data = None

    if display_flag: print("- - - - - - - - - - - - - - - - ")

    aux_param = {'split_mode': 'eq_width', 'split_no': 7, 'legacy_match': False, 'score_factor': 5}

    iprnt ("- - - - aux_param:", aux_param)
    iprnt ()

    crt_classif = deodel2.DeodelSecond(aux_param)

    ret_tuple = usap_common.AccuracyEval(data_digi_x, data_target_y, crt_classif, 
                                        in_iter_no, train_ratio, 
                                        in_rand_seed, aux_data, 
                                        display_flag = display_flag)

    avg_accuracy, rnd_accuracy = ret_tuple

    test_result = (avg_accuracy, rnd_accuracy)
    test_expect = (0.9700374531835205, 0.250936329588015)

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    #'''#
    
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

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    ret_data = UnitTestDeodel()
    utest_fail_counter += ret_data
    iprnt ("- - - ")

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
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

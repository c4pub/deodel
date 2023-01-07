"""
Deodata Delanga Unit Test

    Module provides an unsystematic/opportunistic collection of tests.
        Tested with Winpython64-3.10.5.0
"""

# >-----------------------------------------------------------------------------

def iprnt( *args, **kwargs ) :
    """ Non delayed prints """

    import sys

    ret_item = print( *args, **kwargs )
    sys.stdout.flush()
    sys.stderr.flush()

    return ret_item

# >-----------------------------------------------------------------------------

def SepLine ( display_flag = True ) :
    separator_string = ">-------------------------------------------------------------------------------"
    iprnt ( separator_string )

# >-----------------------------------------------------------------------------

def UnitTest():

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Unit Tests - begin
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    import traceback
    import sys
    import numpy as np

    # catmp from .deodel import deodel
    import deodel

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ( "*** unit test begin ***" )

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

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
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

    tv1 = ['e',    1,      3.01,   'h',     11,     None]

    iprnt ("- - - - tv1", tv1)
    ret_1 = deodel.Working.ProcessVector(tv1, True)
    iprnt ("- - - - ret_1", ret_1)
    tv2 = deodel.Working.RevertVector(ret_1[0], ret_1[2])
    iprnt ("- - - - tv2", tv2)

    test_result = tv1
    test_expect = tv2

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    ret_1 = deodel.Working.ProcessVector(tv1, False)
    iprnt ("- - - - ret_1", ret_1)
    tv3 = deodel.Working.RevertVector(ret_1[0], ret_1[2])
    iprnt ("- - - - tv3", tv3)

    test_result = tv1
    test_expect = tv3

    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [4, 3, 1, 2, 5, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

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

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 8
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [4, 3, 1, 2, 8, 5, 7, 6]
    iprnt ("- - - - tv1", tv1)
    split_no = 16
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    iprnt ("- - - - tv1", tv1)
    split_no = 5
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [4, 3, 1, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1, 2, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [3, 3, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [3, 3, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, True)
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

    tv1 = [3, 3, 3, 4]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [-2, -2, -2, -2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

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

    tv1 = [-2, -2, -2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [-2]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = []
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, True)
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

    tv1 = [10, 20, 30]
    iprnt ("- - - - tv1", tv1)
    split_no = 7
    iprnt ("- - - - split_no", split_no)

    test_result = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1.2, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 7
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [1.2, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, True)
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

    tv1 = [1.2, 2]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, False)
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

    tv1 = [3, 5, 3]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, True)
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

    tv1 = [0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = False)
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

    tv1 = [0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 2
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 3
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 4
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 5
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 6
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 7
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 8
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    tv1 = [0, 0, 0, 0, 1]
    iprnt ("- - - - tv1", tv1)
    split_no = 9
    iprnt ("- - - - split_no", split_no)

    ret_val = deodel.Working.NumSplit(tv1, split_no, no_dupl_flag = True)
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

    # o1 = deodel.deodel.DeodataDelangaClassifier()
    tt_o = deodel.DeodataDelangaClassifier()
    tt_o.fit(tt_X, tt_y)
    iprnt ()

    test_result = tt_o.attr_X.tolist()

    ref_item = [[1, 2, 3, 2, 4], [3, 1, 2, 5, 1], [1, 2, 3, 2, 1], [1, 2, 2, 3, 1]]

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

    iprnt ("dealing with missing attributes (None), ignore them")
    iprnt ()
    tt_X = [['a',   1.01,   'az',   'e'],
            ['b',   "3.01", 3.01,   'd'], 
            ['d',   "4",    None,   'd'], 
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
            ['a',   1.01,   None,   'd'],
            ['b',   "3.01", 3.01,   'e'], 
            ['b',   2,      5.0,    'e'],
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
    test_expect = 1.05

    iprnt ("- - - - test_result:", test_result)
    iprnt ("- - - - test_expect:", test_expect)
    
    set_eval = ( test_result == test_expect )
    iprnt ("- - - utest_test_no:", utest_test_no)
    utest_test_no += 1
    if set_eval :
        iprnt ("- - -   test ok")
    else :
        iprnt ("- - -  test failed")
        utest_fail_counter += 1
        iprnt ("- - -  invalid test_result")

        iprnt ("Unit test failure !")
        traceback.print_stack(file=sys.stdout)

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ("test PreprocTbl")
    iprnt ()

    test_csv_lst =  [
                        ['', '', '', '', ''],
                        ['', 'a', '   1.01', '   az', ''],
                        ['', 'b', '3.01', "  ' 3.01' ", ' '],
                        ['', 'd', '4', '    5', ' '],
                        ['', 'b', '   2', '      3.01', ' '],
                        ['', 'c', '33', ' az', ''],
                        ['', 'a', '   ', '    az  z ', ''],
                        ['', 'b', '2.01', 7.01, ''],
                        ['', 'd', '4', '5', ''],
                        ['', 'b', '   2', "      33.013 '", ''],
                        ['', 'c', '3.01', " az ' sd", ''],
                        ['', 'a', '   1.01', '   az \' "gd" \'uiou uo\' ds', ''],
                        ['', 'b', '', '22 qqw  9.03', ''],
                        ['', 'd', {1, 2, 1}, "6'    5", ''],
                        ['', 'b', '   2.2424', '      44.013', ''],
                        ['', 'c', '  "53.01"  ', '77 " az" 2\' sd 89', ''],
                        ['', 'd', '', "''", '8'],
                        ['', 'e', ' ', '``', '9'],
                        ['', '', None, "", '']
                    ]

    iprnt ("- - - - test_csv_lst:", test_csv_lst)

    expect_result = [
                        [None, None, None, None, None],
                        [None, 'a', 1.01, '   az', None],
                        [None, 'b', 3.01, ' 3.01', ' '],
                        [None, 'd', 4, 5, ' '],
                        [None, 'b', 2, 3.01, ' '],
                        [None, 'c', 33, ' az', None],
                        [None, 'a', '   ', '    az  z ', None],
                        [None, 'b', 2.01, 7.01, None],
                        [None, 'd', 4, 5, None],
                        [None, 'b', 2, "      33.013 '", None],
                        [None, 'c', 3.01, " az ' sd", None],
                        [None, 'a', 1.01, '   az \' "gd" \'uiou uo\' ds', None],
                        [None, 'b', None, '22 qqw  9.03', None],
                        [None, 'd', None, "6'    5", None],
                        [None, 'b', 2.2424, 44.013, None],
                        [None, 'c', "53.01", '77 " az" 2\' sd 89', None],
                        [None, 'd', None, '', 8],
                        [None, 'e', ' ', '``', 9],
                        [None, None, None, None, None]
                    ]

    iprnt ("- - - - PreprocTbl - begin")
    proc_tbl = deodel.CasetDeodel.PreprocTbl(test_csv_lst)
    iprnt ("- - - - PreprocTbl - end")

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

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    # >- - - - - - - - - - -
    SepLine()
    iprnt ("- - - utest_fail_counter:", utest_fail_counter)
    if utest_fail_counter == 0:
        iprnt ("- - -   UnitTest succes")
    else:
        iprnt ("- - -   UnitTest failed !")
        iprnt ("- - -       errorrs:", utest_fail_counter)
    SepLine()
    # >- - - - - - - - - - -

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    iprnt ( "*** unit test end ***" )

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    SepLine()
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

    return utest_fail_counter

    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
    # Unit Tests - end
    # >- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# >-----------------------------------------------------------------------------

if __name__ == "__main__":   

    print()
    print("- - - - - - - - - ")

    ret_data = UnitTest()

    print()
    print("- - - - - - - - - ")
    print("- - - - ret_data:", ret_data)
    print("- - - - - - - - - ")
    print()

# >-----------------------------------------------------------------------------

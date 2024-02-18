import src.nw as align

def test_nw_1():
    """Identical sequences, match=5, mismatch=-4, gap=-10
    """
    seq1 = 'ACGT'
    seq2 = 'ACGT'
    score, aligned_seq1, aligned_seq2 = align.needleman_wunsch(seq1, 
                                                 seq2, 
                                                 score_fun=lambda x, y: 5 if x == y else -4, 
                                                 gap_penalty=-10)
    assert score == 20
    assert aligned_seq1 == 'ACGT'
    assert aligned_seq2 == 'ACGT'

def test_nw_2():
    '''
    обязательное дозаполнение 
    '''
    diff = 7
    l = 10
    seq1 = '*'*l
    seq2 = '*'*(l-diff)
    score, aligned_seq1, aligned_seq2 = align.needleman_wunsch(seq1, 
                                                 seq2, 
                                                 # опытным (и долгим) путем понял, что 
                                                 # тут должна быть нормальная функция
                                                 score_fun=lambda x, y: 0 if x == y else -4,
                                                 gap_penalty=-10)

    assert aligned_seq1 == seq1
    assert aligned_seq2 == '-'*diff + seq2
    assert score == -10*diff


def test_nw_3():
    '''
    ну и симметричный тест
    '''
    diff = 7
    l = 10
    seq1 = '*'*l
    seq2 = '*'*(l-diff)
    score, aligned_seq2, aligned_seq1 = align.needleman_wunsch(seq2, 
                                                 seq1, 
                                                 # опытным (и долгим) путем понял, что 
                                                 # тут должна быть нормальная функция
                                                 score_fun=lambda x, y: 0 if x == y else -4,
                                                 gap_penalty=-10)

    assert aligned_seq1 == seq1
    assert aligned_seq2 == '-'*diff + seq2
    assert score == -10*diff


def test_nw_4():
    '''
    совпадают по длинне, разные символы
    выгоднее ошибаться
    '''
    seq1 = '*'*10
    seq2 = '+'*10
    score, aligned_seq2, aligned_seq1 = align.needleman_wunsch(seq2, 
                                                 seq1, 
                                                 # опытным (и долгим) путем понял, что 
                                                 # тут должна быть нормальная функция
                                                 score_fun=lambda x, y: 0 if x == y else -4,
                                                 gap_penalty=-10)

    assert aligned_seq1 == seq1
    assert aligned_seq2 == seq2
    assert score == -40

def test_nw_5():
    '''
    совпадают по длинне, разные символы
    выгоднее добавлять пробел
    '''
    seq1 = '*'*10
    seq2 = '+'*10
    score, aligned_seq2, aligned_seq1 = align.needleman_wunsch(seq2, 
                                                 seq1, 
                                                 # опытным (и долгим) путем понял, что 
                                                 # тут должна быть нормальная функция
                                                 score_fun=lambda x, y: 0 if x == y else -4,
                                                 gap_penalty=-1)

    assert aligned_seq1 == seq1 + '-'*10
    assert aligned_seq2 == '-'*10 + seq2
    assert score == -20

def test_nw_6():
    '''
    совпадают по длинне, разные символы
    выгоднее мисмачить буквы
    '''
    seq1 = '*'*10
    seq2 = '+'*10
    score, aligned_seq2, aligned_seq1 = align.needleman_wunsch(seq2, 
                                                 seq1, 
                                                 # опытным (и долгим) путем понял, что 
                                                 # тут должна быть нормальная функция
                                                 score_fun=lambda x, y: 0 if x == y else -1,
                                                 gap_penalty=-4)

    assert aligned_seq1 == seq1
    assert aligned_seq2 == seq2
    assert score == -10

def test_nw_7():
    '''
    вырожденный случай
    '''
    seq1 = ''
    seq2 = '+'*10
    score, aligned_seq2, aligned_seq1 = align.needleman_wunsch(seq2, 
                                                 seq1, 
                                                 # опытным (и долгим) путем понял, что 
                                                 # тут должна быть нормальная функция
                                                 score_fun=lambda x, y: 0 if x == y else -1,
                                                 gap_penalty=-10)

    assert aligned_seq1 == '-'*10
    assert aligned_seq2 == seq2
    assert score == -100

def test_nw_8():
    '''
    симметричный вырожденный случай
    '''
    seq1 = ''
    seq2 = '+'*10
    score, aligned_seq1, aligned_seq2 = align.needleman_wunsch(seq1, 
                                                 seq2, 
                                                 # опытным (и долгим) путем понял, что 
                                                 # тут должна быть нормальная функция
                                                 score_fun=lambda x, y: 0 if x == y else -1,
                                                 gap_penalty=-10)

    assert aligned_seq2 == seq2
    assert aligned_seq1 == '-'*10
    assert score == -100


if __name__ == "__main__":
    test_nw_1()
    print('test1 passed')
    test_nw_2()
    print('test2 passed')
    test_nw_3()
    print('test3 passed')
    test_nw_4()
    print('test4 passed')
    test_nw_5()
    print('test5 passed')
    test_nw_6()
    print('test6 passed')
    test_nw_7()
    print('test7 passed')
    test_nw_8()
    print('test8 passed')

import sys
sys.path.append(sys.path[0] +'/..')
import src.nw as align
from collections import namedtuple
from pprint import pprint as pp

def test_nw_1():
    """Identical sequences, match=5, mismatch=-4, gap=-10
    """
    seq1 = 'ACGT'
    seq2 = 'ACGT'
    score, aligned_seq1, aligned_seq2 = align.needleman_wunsch(seq1, 
                                                 seq2, 
                                                 score_fun=lambda x, y: 5 if x == y else -4, 
                                                 gap_penalty=-10, k =10)
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
    print(aligned_seq2, aligned_seq1)
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


def run_legacy_tests():
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


Test = namedtuple('Test', ['inp', 'outp', 'descr'])
TestInputs = namedtuple('TestInputs', ['seq1', 'seq2', 'match', 'mismatch', 'gp', 'k'])
TestOutputs = namedtuple('TestOutputs', ['seq1', 'seq2', 'score'])

def run_test(test: Test):
    testin = test.inp
    
    score, aligned_seq1, aligned_seq2 = align.needleman_wunsch(
        seq1=testin.seq1, seq2=testin.seq2, 
        score_fun = lambda x, y: testin.match if x == y else testin.mismatch,
        gap_penalty = testin.gp,
        k = testin.k
    )

    outs = TestOutputs(aligned_seq1, aligned_seq2, score)
    assert aligned_seq1 == test.outp.seq1
    assert aligned_seq1 == test.outp.seq1
    assert score == test.outp.score
    print(testin)
    print(outs)
    print(test.descr)
    print('PASSED!')
                             
                                               
if __name__ == "__main__":
    # прогоним старые тесты
    run_legacy_tests()

    tests_list = [
        Test (
            TestInputs(seq1='ACGT', seq2='ACGT', match=5, mismatch=-4, gp=-10, k=100), 
            TestOutputs(seq1='ACGT', seq2='ACGT', score=20), 
            "базовый тест"
        ),

        Test (
            TestInputs(seq1='ACGT', seq2='ACGT', match=5, mismatch=-4, gp=-10, k=1), 
            TestOutputs(seq1='ACGT', seq2='ACGT', score=20), 
            "базовый тест, но двигаться можно только по диагонали"
        ),

        Test (
            TestInputs(seq1='**********', seq2='*******', match=1, mismatch=-4, gp=-1, k=1), 
            TestOutputs(seq1='**********', seq2='-*******--', score=4), 
            "k не хватает"

        ),
        Test (
            TestInputs(seq1='**********', seq2='*******', match=1, mismatch=-4, gp=-1, k=2), 
            TestOutputs(seq1='**********', seq2='--******-*', score=4), 
            "k не хватает"
        ),
        Test (
            TestInputs(seq1='**********', seq2='*******', match=1, mismatch=-4, gp=-1, k=3), 
            TestOutputs(seq1='**********', seq2='---*******', score=4), 
            "k=3 хватает, чтобы заполнить все за раз - успевает выйти на нормальную диагональ"
        ),
        Test (
            TestInputs(seq1='LMLLLL', seq2='RRRRMR', match=100, mismatch=-4, gp=-1, k=4), 
            TestOutputs(seq1='----LM-LLLL', seq2='RRRR-MR----', score=90), 
            "один матч точно сделает - слишком уж выгодно"
        ),
        Test (
            TestInputs(seq1='LMLLLL', seq2='RRRRMR', match=100, mismatch=-4, gp=-1, k=2), 
            TestOutputs(seq1='---LM-L-L-LL', seq2='RRR--R-M-R--', score=-12), 
            "матча не будет - k слишком мал"
        ),
        Test (
            TestInputs(seq1='ABCDEF', seq2='FEDCBA', match=1, mismatch=-4, gp=-1, k=4), 
            TestOutputs(seq1='----AB-CDEF', seq2='FEDC-BA----', score=-9),
            "делать гэп сильно дешевле"
        ),
        Test (
            TestInputs(seq1='ABCDEF', seq2='FEDCBA', match=1, mismatch=-1, gp=-4, k=3), 
            TestOutputs(seq1='ABCDEF', seq2='FEDCBA', score=-6),
            "мисматчиться дешевле"
        ),
        Test (
            TestInputs(seq1='NNNNNN', seq2='FFFFFF', match=1, mismatch=-1, gp=-4, k=100), 
            TestOutputs(seq1='NNNNNN', seq2='FFFFFF', score=-6), 
            "недиагональные стрелочки в пред. тестах возникают из-за скоринга"
        ),


    ]

    for i, test in enumerate(tests_list):
        print('-'*40)
        print(f'#TEST {i+1}:')
        run_test(test)
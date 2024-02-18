from typing import Callable, Tuple
import argparse
import sys
import math


PRINT_MAX_LINE_LENGTH = 80
DEBUG = True

UP = '↑' 
LEFT = '←'
DIAG = '↖'

def score_fun(a: str, 
              b: str,
              match_score: int = 5, 
              mismatch_score: int = -4) -> int:
    return match_score if a == b else mismatch_score

def needleman_wunsch(seq1: str,
                     seq2: str,
                     score_fun: Callable[[str, str], int] = score_fun,
                     gap_penalty: int = -10,
                     k: int = 99999999) -> Tuple[int, str, str]:

    """Given two sequences, aligns them using the Needleman-Wunsch algorithm.

    This function takes two sequences and optionally a scoring function and a
    gap penalty value as arguments. 
    The function returns a tuple containing the optimal alignment score and the
    aligned sequences, e.g. (10, 'ACCGT', 'AC-GT').

    Args:
        seq1: The first sequence, e.g. 'ACCGT'
        seq2: The second sequence, e.g. 'ACGT'
        score_fun: The scoring function, e.g. score_fun('A', 'A') returns 5
        gap_penalty: The gap penalty value, e.g. -10

    Returns:
        score: The optimal alignment score, e.g. 10
        aligned_seq1: The first aligned sequence, e.g. 'ACCGT'
        aligned_seq2: The second aligned sequence, e.g. 'AC-GT'
    """ 
    assert k >= 1

    # ставим seq2 > seq1
    swapped = False
    if len(seq2) < len(seq1):
        seq1, seq2 = seq2, seq1
        swapped = True

    # инициализируем матрицу
    nrow = len(seq1)+1
    ncol = len(seq2)+1
    # поставим крайне меленький скор, чтобы не было елания туда сворачивать :)
    score_matrix = [[-9999999 for _ in range(ncol)] for _ in range(nrow)]
    score_matrix[0][0] = 0
    pointer_matrix = [[' ' for _ in range(ncol)] for _ in range(nrow)]
    index_matrix = [[str((i,j)) for j in range(ncol)] for i in range(nrow)]
    
    # заполняем нулевые строку и столбец
    for i in range(1,ncol):
        score_matrix[0][i] = gap_penalty*i
        pointer_matrix[0][i] = LEFT
    for i in range(1,nrow):
        score_matrix[i][0] = gap_penalty*i
        pointer_matrix[i][0] = UP

    # НОВОЕ
    # будем считать, что гэп идет вдоль главной диагонали, 
    # на примере k = 3

    # @ @ @ @ @ @ @ @ @ @
    # @ 1 2 3 4
    # @ 2 3 4 5 6
    # @ 3 4 5 6 7 8 9 1 2 
    # @   5 6 7 8 9 1 2 3
    # @     7 8 9 1 2 3 4

    # k = 4
    # @ @ @ @ @ @ @ @ @ @
    # @ 1 2 3 4 5
    # @ 2 3 4 5 6 7 8 9 1
    # @ 3 4 5 6 7 8 9 1 2 
    # @ 4 5 6 7 8 9 1 2 3
    # @   6 7 8 9 1 2 3 4

    # последовательно проходимся по диагоналям матрицы
    for diag_num in range(2, ncol+nrow-1):
        # не считаем для крайних элементов матрицы

        # поставили в левый нижний элемент диагонали
        i = min(nrow-1, diag_num-1)
        j = max(1, diag_num - i)
        
        # если мы на главной диагонали, то, возможно, надо сдвинуть
        if diag_num < 2*nrow+1:
            # побочная диагональ имеет центральный элемент
            diag_odd = diag_num % 2 == 0
            # k нечентное
            k_odd = k %2 == 1

            # вычислим номер строки центрального элемента
            icenter = math.floor(diag_num/2)
            ibandmin = -1
            match diag_odd, k_odd:
                # "четности" совпали - тут все симметрично
                case (True, True) | (False, False):
                    # сдвигаемся на k/2 вниз по стоке
                    ibandmin = icenter + k//2 
                # на диагонале есть центральный элемент
                # но k - четный
                case True, False:
                    # тогда смещаемся на 0.5 вверх и вправо
                    # левый от центра элемент band`a будет 
                    ibandmin = icenter + (k//2 - 1)
                # нет центрального элемента
                # но k - нечетный
                case False, True:
                    ibandmin = icenter + ((k-1)//2)
                case _:
                    raise RuntimeError('тут быть не должны мы')
                

            # если band не помещается на диагональ
            if i > ibandmin:
                i, j = ibandmin, diag_num - ibandmin


        ki = 0
        while (j < ncol) and (i > 0) and (ki < k):
            # вычисляем значения в случаях UP, LEFT и DIAG
            diag = (score_matrix[i-1][j-1] + score_fun(seq1[i-1], seq2[j-1]), DIAG) 
            up = (score_matrix[i-1][j] + gap_penalty, UP) 
            left = (score_matrix[i][j-1] + gap_penalty, LEFT) 
            # при прочих равных diag приоритетнее 
            m = diag
            if m[0] < up[0]:
                m = up
            if m[0] < left[0]:
                m = left
            score_matrix[i][j], pointer_matrix[i][j] = m

            i -= 1
            j +=1
            ki +=1


    if DEBUG:
        # print_array(score_matrix)
        print_array(pointer_matrix)

    # выравниваем
    aligned_seq1 = ''
    aligned_seq2 = ''

    i,j = nrow-1, ncol-1
    # движемся куда-то, пока не наткнемся на начало
    while i + j > 0:
        match pointer_matrix[i][j]:
            case '↑':
                aligned_seq1 += seq1[i-1]
                aligned_seq2 += '-'
                i-=1
            case '←':
                aligned_seq2 += seq2[j-1]
                aligned_seq1 += '-'
                j-=1
            case '↖':
                aligned_seq1 += seq1[i-1]
                aligned_seq2 += seq2[j-1]
                j-=1
                i-=1
            case _:
                raise RuntimeError(f'код написан некорректно - не все стрелочки заполнены')

    if swapped:
        aligned_seq1, aligned_seq2 = aligned_seq2, aligned_seq1

    return score_matrix[-1][-1], aligned_seq1[::-1], aligned_seq2[::-1]

def print_array(matrix: list):
    for row in matrix:
        for element in row:
            print(f"{element:5}", end="")
        print()

def print_results(seq1: str, seq2: str, score: int, file = None):
    """Prints the results of the Needleman-Wunsch algorithm.

    This function takes two aligned sequences and the optimal alignment score
    as arguments. It prints the sequences and the score to the standard output
    or to a file.

    Args:
        seq1: The first aligned sequence, e.g. 'ACCGT'
        seq2: The second aligned sequence, e.g. 'AC-GT'
        score: The optimal alignment score, e.g. 10
        file: The file to print to. If None, prints to the standard output.

    Returns:
        None
    """
    if file is None:
        file = sys.stdout

    def print_subseq(i, n, s):
        print("%s: %s" % (n, s[i: i + PRINT_MAX_LINE_LENGTH]), file=file)

    print("Pairwise alignment:", file=file)
    for i in range(0, len(seq1), PRINT_MAX_LINE_LENGTH):
        print_subseq(i, 'seq1', seq1)
        print_subseq(i, 'seq2', seq2)
        print(file=file)
    print("Score: %s" % score, file=file)

def main():
    parser = argparse.ArgumentParser(description='Needleman-Wunsch algorithm')
    parser.add_argument('seq1', help='first sequence')
    parser.add_argument('seq2', help='second sequence')
    parser.add_argument('--match', type=int, help='match score')
    parser.add_argument('--mismatch', type=int, help='mismatch score')
    parser.add_argument('--gap', type=int, default=-10, help='gap penalty')
    parser.add_argument('--debug', action='store_true', help='debug mode')
    args = parser.parse_args()

    global DEBUG
    DEBUG = args.debug
    print(args.match, args.mismatch, args.gap)
    
    if args.match and args.mismatch:
        score, aln1, aln2 = needleman_wunsch(args.seq1, 
                                             args.seq2, 
                                             score_fun=lambda x, y: args.match if x == y else args.mismatch, 
                                             gap_penalty=args.gap)
    else:
        assert not args.match and not args.mismatch, "match and mismatch must be specified together"
        score, aln1, aln2 = needleman_wunsch(args.seq1, 
                                             args.seq2, 
                                             score_fun=score_fun,
                                             gap_penalty=args.gap)
    print_results(aln1, aln2, score)

    return score, aln1, aln2

if __name__ == '__main__':
    main()
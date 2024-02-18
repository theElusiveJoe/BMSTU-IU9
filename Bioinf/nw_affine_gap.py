from typing import Callable, Tuple
import numpy as np

DEBUG = False


def score_fun(a: str,
              b: str,
              match_score: int = 5,
              mismatch_score: int = -4) -> int:
    return match_score if a == b else mismatch_score


def needleman_wunsch_affine(seq1: str,
                            seq2: str,
                            score_fun: Callable = score_fun,
                            gap_open: int = -10,
                            gap_extend: int = -1) -> Tuple[str, str, int]:
    '''
    matrix_inputs:
    seq1 - first sequence
    seq2 - second sequence
    score_fun - function that takes two characters and returns score
    gap_open - gap open penalty
    gap_extend - gap extend penalty
    Outputs:
    aln1 - first aligned sequence
    aln2 - second aligned sequence
    score - score of the alignment
    '''

    infinity = float('-inf')

    n = len(seq1)
    m = len(seq2)
    matrix_m = np.zeros((n+1, m+1))
    matrix_d = np.zeros((n+1, m+1))
    matrix_i = np.zeros((n+1, m+1))

    matrix_d[0, 0] = infinity
    matrix_i[0, 0] = infinity

    for i in range(1, n+1):
        matrix_m[i][0] = infinity
        matrix_i[i][0] = gap_open + (i-1) * gap_extend
        matrix_d[i][0] = infinity
    for j in range(1, m+1):
        matrix_m[0][j] = infinity
        matrix_i[0][j] = infinity
        matrix_d[0][j] = gap_open + (j-1) * gap_extend

    for i in range(1, n+1):
        for j in range(1, m+1):
            matrix_m[i][j] = max(
                matrix_m[i-1, j-1]+score_fun(seq1[i-1], seq2[j-1]),
                matrix_i[i-1, j-1]+score_fun(seq1[i-1], seq2[j-1]),
                matrix_d[i-1, j-1]+score_fun(seq1[i-1], seq2[j-1]),
            )
            matrix_i[i][j] = max(
                matrix_i[i][j-1] + gap_extend,
                matrix_m[i][j-1] + gap_open,
            )
            matrix_d[i][j] = max(
                matrix_d[i-1][j] + gap_extend,
                matrix_m[i-1][j] + gap_open,
            )

    aln1 = ''
    aln2 = ''
    i = len(seq1)
    j = len(seq2)
    m = np.maximum(matrix_m, np.maximum(matrix_i, matrix_d))
    print(m)
    while i > 0 or j > 0:
        mx = max(matrix_m[i, j], matrix_i[i, j], matrix_d[i, j])

        if i == 0 or j > 0 and (
            mx == matrix_m[i, j-1] + gap_open
            or mx == matrix_i[i, j-1] + gap_extend
        ):
            aln1 += '-'
            aln2 += seq2[j-1]
            j -= 1
            continue

        if j == 0 or i > 0 and (
            mx == matrix_m[i-1, j] + gap_open
            or mx == matrix_d[i-1, j] + gap_extend
        ):
            aln1 += seq1[i-1]
            aln2 += '-'
            i -= 1
            continue

        if i > 0 and j > 0 and (
            mx == matrix_m[i-1, j-1] + score_fun(seq1[i-1], seq2[j-1])
            or mx == matrix_d[i-1, j-1] + score_fun(seq1[i-1], seq2[j-1])
            or mx == matrix_i[i-1, j-1] + score_fun(seq1[i-1], seq2[j-1])
        ):
            aln1 += seq1[i-1]
            aln2 += seq2[j-1]
            i -= 1
            j -= 1
            continue

        raise RuntimeError

    score = max(matrix_m[-1, -1], matrix_i[-1, -1], matrix_d[-1, -1])
    if score == infinity:
        score = 0

    return aln1[::-1], aln2[::-1], score


def print_array(matrix: list):
    for row in matrix:
        for element in row:
            print(f"{element:6}", end="")
        print()


def main():
    aln1, aln2, score = needleman_wunsch_affine("ACG", "ACGT")
    assert len(aln1) == len(aln2)
    assert aln1 == "ACG-"
    assert aln2 == "ACGT"
    assert score == 5


if __name__ == "__main__":
    main()

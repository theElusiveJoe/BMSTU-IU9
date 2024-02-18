from typing import Callable, Tuple
from copy import deepcopy as dc


DEBUG = False


def score_fun(a: str, 
              b: str,
              match_score: int = 5, 
              mismatch_score: int = -4) -> int:
    return match_score if a == b else mismatch_score


def hirschberg(seq1: str, 
               seq2: str, 
               score_fun: Callable = score_fun, 
               gap_score: int = -5) -> Tuple[str, str, int]:
    '''
    Inputs:
    seq1 - first sequence
    seq2 - second sequence
    score_fun - function that returns score for two symbols
    gap_score - score for gap in final alignment

    Outputs:
    aln1 - first sequence in alignment
    aln2 - second sequence in alignment
    score - score of alignment
    '''
    l1, l2 = len(seq1), len(seq2)

    if l1 <= 1 or l2 <= 1:
        return needleman_wunsch(seq1, seq2, score_fun, gap_score)

    m1 = l1//2
    s1, s2 = nw_last_line(seq1[:m1], seq2, score_fun, gap_score), \
            nw_last_line(seq1[m1:][::-1], seq2[::-1], score_fun, gap_score)
    s = list([x+y for x, y in zip(s1, s2[::-1])])
    m2 = s.index(max(s))

    al1_l, al2_l, s_l = hirschberg(seq1[:m1], seq2[:m2], score_fun, gap_score)
    al1_r, al2_r, s_r = hirschberg(seq1[m1:], seq2[m2:], score_fun, gap_score)
    return al1_l+al1_r, al2_l+al2_r, s_l+s_r


def nw_last_line(seq1:str, seq2:str, score_fun=score_fun, gap_score=-5):
    # берем код из nw))))
    m, n = len(seq1) + 1, len(seq2) + 1

    matrix = [[0] * n for _ in range(2)]
    
    for j in range(n):
        matrix[0][j] = j * gap_score

    for i in range(1, m):
        matrix[1][0] = i * gap_score
        for j in range(1, n):
            matrix[1][j] = max(matrix[0][j - 1] + score_fun(seq1[i - 1], seq2[j - 1]), 
                                matrix[0][j] + gap_score, 
                                matrix[1][j - 1] + gap_score)
        matrix[0] = matrix[1]
        matrix[1] = [0] * n
        
    return(matrix[0])


def needleman_wunsch(seq1: str, seq2: str, score_fun: Callable = score_fun, gap_score: int = -5):

    m, n = len(seq1) + 1, len(seq2) + 1

    matrix = [[0] * n for _ in range(m)]
    
    for i in range(m):
        matrix[i][0]  = i * gap_score
    for j in range(n):
        matrix[0][j] = j * gap_score
    
    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = max(matrix[i - 1][j - 1] + score_fun(seq1[i - 1], seq2[j - 1]), 
                               matrix[i - 1][j] + gap_score, 
                               matrix[i][j - 1] + gap_score)
    if DEBUG:
        print_array(matrix)

    score = matrix[-1][-1]
    i, j = m - 1, n - 1
    aln1 = ""
    aln2 = ""
    while i > 0 or j > 0:
        a, b = '-', '-'
        # (A, B)
        if i > 0 and j > 0 and matrix[i][j] == matrix[i-1][j-1] + score_fun(seq1[i - 1], seq2[j - 1]):
            a = seq1[i - 1]
            b = seq2[j - 1]
            i -= 1
            j -= 1

        # (A, -)
        elif i > 0 and matrix[i][j] == matrix[i - 1][j] + gap_score:
            a = seq1[i - 1]
            i -= 1

        # (-, A)
        elif j > 0 and matrix[i][j] == matrix[i][j - 1] + gap_score:
            b = seq2[j - 1]
            j -= 1     
        
        aln1 += a
        aln2 += b
    return aln1[::-1], aln2[::-1], score


def print_array(matrix: list):
    for row in matrix:
        for element in row:
            print(f"{element:6}", end="")
        print()



if __name__ == "__main__":    
    #aln1, aln2, score = hirschberg("ATCT", "ACT", gap_score=-5)
    aln1, aln2, score = needleman_wunsch("ATCT", "ACT", gap_score=-5)
    
    assert len(aln1) == len(aln2)
    print(aln1)
    print(aln2)
    print(score)

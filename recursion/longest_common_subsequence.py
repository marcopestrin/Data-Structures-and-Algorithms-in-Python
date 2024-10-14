from jovian.pythondsa import evaluate_test_cases
from mock_tests import tests

# longest common subsequence
def lcs_recursive(seq1, seq2, idx1=0, idx2=0):
    if idx1 == len(seq1) or idx2 == len(seq2):
        return 0
    elif seq1[idx1] == seq2[idx2]:
        # found a match
        # increment both indexes --> step forward
        print('seq1:', seq1, '(', seq1[idx1], ')', ' seq2:', seq2, '(', seq2[idx2], ')')
        # when 2 elements match we resolved 2 problems in 1 recursive call
        return 1 + lcs_recursive(seq1, seq2, idx1+1, idx2+1)
    else:
        # check next index
        # increase the indixes separately and take the longest match
        # worst scenario --> complexity: O(2^m+n) --> exponential numbers of subproblems
        print('seq1:', seq1, '(', seq1[idx1], ')', ' seq2:', seq2, '(', seq2[idx2], ')')
        option1 = lcs_recursive(seq1, seq2, idx1+1, idx2)
        option2 = lcs_recursive(seq1, seq2, idx1, idx2+1)
        return max(option1, option2)


def lcs_memo(seq1, seq2):
    # use this solution when the same problem been call again again and again
    # save the result into a dictionary
    memo = {}

    def recurse(idx1=0, idx2=0):
        print('--> ',memo)
        key = (idx1, idx2)
        if key in memo:
            return memo[key]
        elif idx1 == len(seq1) or idx2 == len(seq2):
            # end of the string. nothing to compare
            memo[key] = 0
        elif seq1[idx1] == seq2[idx2]:
            # case when both chars are same
            # found a match. increment both indexes --> step forward
            memo[key] = 1 + recurse(idx1+1, idx2+1)
        else:
            # two elememnts no equal. We have 2 options (worst scenario)
            memo[key] = max(recurse(idx1+1, idx2), recurse(idx1, idx2+1))
        return memo[key]
    return recurse(0,0)


evaluate_test_cases(lcs_memo, tests)

#longest common subsequence
'''
A subsequence is a part of a string where characters appear in the same order, but not necessarily next to each other.
For example, in the string ABCDEFG, ABEF is a subsequence but BAD isn’t.
The LCS problem requires us to find the length of the longest subsequence that exists in both strings.
'''
def longest_common_subsequence ( str1 : str , str2 : str ) -> str :
    """
    Given two strings str1 and str2, return the longest common subsequence (LCS) of the two strings.
    If there are multiple LCSs, return any one of them.
    
    :param str1: First string
    :param str2: Second string
    :return: Longest common subsequence of str1 and str2
    """
    # Length of both strings
    n = len( str1 )
    m = len( str2 )

    # Initialize a 2D array ( table ) of size (n +1) x (m +1) with zeros
    dp = [[0 for _ in range ( m + 1) ] for _ in range ( n + 1) ]
    ## YOUR CODE GOES HERE
    for i in range(1,n+1):
        for j in range(1,m+1):
            if str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]

            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])

    print("length: ",dp[n][m])

    i,j=n,m
    lcs=[]
    while i>0 and j>0:
        if str1[i-1]==str2[j-1]:
            lcs.append(str1[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    lcs.reverse()
    lcs="".join(lcs)
    return lcs


print(longest_common_subsequence ("abc", "ab"))

#O(N*M) time complexity and O(N*M) space complexity.    

'''
Frequency Counting of Words / Top N words in a document.
 
Given N terms, your task is to find the k most frequent terms from given N terms.
 
Input format :
 
First line of input contains N, denoting the number of terms to add.
In each of the next N lines, each contains a term.
Next line contains k, most frequent terms.
 
Output format :
 
Print the k most frequent terms in descending order of their frequency. If two terms have same frequency print them in lexicographical order.
 
Sample input :
 
14
Fee
Fi
Fo
Fum
Fee
Fo
Fee 
Fee
Fo
Fi
Fi
Fo
Fum
Fee
3
 
Sample output :
 
Fee
Fo
Fi
 
Constraint :
0 < N < 300000 
0 < term length < 25.
'''


def main():

    word_vs_freq = {}
    freq_vs_word = {}

    num_of_inputs = int(raw_input())
    for i in range(num_of_inputs):
        try:
            word = raw_input()
            word_vs_freq[word.strip()] += 1
        except KeyError:
            word_vs_freq[word.strip()] = 1

    k_most_freq = int(raw_input())

    #O(n) operation
    for k,v in word_vs_freq.items():
        try:
            freq_vs_word[v].append(k)
        except KeyError:
            freq_vs_word[v] = [k]

    counts = freq_vs_word.keys()
    #get it in descending order
    counts.sort()
    counts.reverse()

    it = 0
    while k_most_freq > 0:
        sorted_words = freq_vs_word[counts[it]]
        if len(sorted_words) > 1:
            sorted_words.sort()
        for ele in sorted_words:
            if k_most_freq > 0:
                print ele
                k_most_freq -= 1
            else:
                break
        it += 1

if __name__ == '__main__':
    main()


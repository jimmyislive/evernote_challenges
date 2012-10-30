'''
Given an unordered list of N elements, write a function to find the top four elements of the given list. Make sure your function runs in linear time O(N).
 
Input format :
 
First line of input contains N , number of elements in list.
Next N line , each contains a element.
 
Output format :
 
Print the top four elements of list.
 
Sample input :
 
8
6930886
-1692777
4636915
7747793
-4238335
9885386
9760492
6516649
 
Sample ouput :
 
9885386
9760492
7747793
6930886
 
Constraint :
 
N < 1000000.
all numbers will fit  in 32-bit integer.
'''

from Queue import Queue

#To do this on O(n), use radix sort

def radix_sort(array, max_len):

    bucket = {}
    bucket[0] = Queue()
    bucket[1] = Queue()
    bucket[2] = Queue()
    bucket[3] = Queue()
    bucket[4] = Queue()
    bucket[5] = Queue()
    bucket[6] = Queue()
    bucket[7] = Queue()
    bucket[8] = Queue()
    bucket[9] = Queue()

    divisor = 1

    while max_len:

        for num in array:
            digit = int(num)/divisor % 10
            bucket[digit].put(num)

        new_array = []
        for i in range(10):
            while not bucket[i].empty():
                new_array.append(bucket[i].get())

        max_len -= 1
        divisor *= 10

        array = new_array

    return array



def main():

    negative_nums = []
    positive_nums = []

    negative_nums_processed = []
    positive_nums_processed = []

    max_len_negative = 0
    max_len_positive = 0

    num_of_inputs = int(raw_input())
    for i in range(num_of_inputs):
        num = int(raw_input())

        if num < 0:
            if len(str(abs(num))) > max_len_negative:
                max_len_negative = len(str(abs(num)))

            negative_nums.append(abs(num))
        else:
            if len(str(num)) > max_len_positive:
                max_len_positive = len(str(num))

            positive_nums.append(num)

    #make all the numbers of the same length
    for num in negative_nums:
        negative_nums_processed.append('0'*(max_len_negative - len(str(num))) + str(num))
    for num in positive_nums:
        positive_nums_processed.append('0'*(max_len_positive - len(str(num))) + str(num))


    sorted_negative = radix_sort(negative_nums_processed, max_len_negative)
    sorted_positive = radix_sort(positive_nums_processed, max_len_positive)

    sorted_negative = map(lambda s: '-' + s, sorted_negative)

    sorted_negative.extend(sorted_positive)

    print int(sorted_negative[-1])
    print int(sorted_negative[-2])
    print int(sorted_negative[-3])
    print int(sorted_negative[-4])

if __name__ == '__main__':
    main()

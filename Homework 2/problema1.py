def largest_sum_subarray(arr: list[int]) -> int:

    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]

    max_sums = {}

    def get_max_sum(index):

        if index == 0:
            return arr[0]

        if index in max_sums:
            return max_sums[index]

        max_sums[index] = max( arr[index], get_max_sum(index-1) + arr[index] )
        return max_sums[index]

    for i in range(n):
        get_max_sum(i)

    return max( max_sums.values() )

def test_func(array, result): # funzione per il testing
    sum = largest_sum_subarray(array)
    if sum == result:
        return True, sum
    else:
        return False, sum   

if __name__ == '__main__':

    array_test0 = [-1, -3, 4, 2]
    array_test1 = [-1, 2, -5, 7]
    array_test2 = []
    array_test3 = [-10, ]

    print('\n')

    print('[TEST CASE 0] Testing array: ' + str(array_test0))
    success, sum = test_func(array_test0, 6)
    if success:
        print('Result: ' + str(sum) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(sum) + ' -> FAILURE.')

    print('\n[TEST CASE 1] Testing array: ' + str(array_test1))
    success, sum = test_func(array_test1, 7)
    if success:
        print('Result: ' + str(sum) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(sum) + ' -> FAILURE.')

    print('\n[TEST CASE 2] Testing array: ' + str(array_test2))
    success, sum = test_func(array_test2, 0)
    if success:
        print('Result: ' + str(sum) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(sum) + ' -> FAILURE.')

    print('\n[TEST CASE 3] Testing array: ' + str(array_test3))
    success, sum = test_func(array_test3, -10)
    if success:
        print('Result: ' + str(sum) + ' -> SUCCESS.')
    else:
        print('Result: ' + str(sum) + ' -> FAILURE.')

    print('\n')    

def largest_sum_subarray(arr: list[int]) -> int:

    n = len(arr)
    if n == 0:
        return 0

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

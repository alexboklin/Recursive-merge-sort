nums = [ int(x) for x in input().split() ]

def merge_sort(array):
    return merge(merge_sort(array[0:len(array)//2]), merge_sort(array[len(array)//2:])) if len(array) > 1 else array

def merge(left, right):
    def merge_help(left, right, result):
        if len(left) == 0: return result + right
        if len(right) == 0: return result+left
        return merge_help(left[1:], right, result+[left[0]]) if left[0]<=right[0] \
            else merge_help(left, right[1:], result+[right[0]] )
    return merge_help(left, right, [])	



output = merge_sort(nums)
print(output)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # create a set of nums list
        numSet = set(nums)

        # init longest sequence
        longest = 0

        # loop through numSet
        for num in numSet:

            # if num-1 in numSet, then it's not the start of a sequence -> skip
            if num-1 in numSet:
                continue

            # otherwise, continue adding 1 to num while num in numSet
            else:
                length = 1
                while num+length in numSet:
                    length += 1

                # replace longest with length if longer than longest
                if length > longest:
                    longest = length

        return longest
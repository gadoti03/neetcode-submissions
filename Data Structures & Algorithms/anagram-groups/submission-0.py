class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []

        d_output = {} # word : position in the list
        max_index = 0

        for s in strs:
            sorted_s = "".join(sorted(s))
            if sorted_s in d_output:
                index = d_output[sorted_s]
                output[index].append(s)
            else:
                d_output[sorted_s] = max_index
                max_index += 1

                output.append([s])
        return output
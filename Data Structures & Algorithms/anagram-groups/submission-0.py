class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grams = {}

        for str in strs:
            sortedStr = "".join(sorted(str))

            if sortedStr in grams:
                grams[sortedStr].append(str)
            else:
                grams[sortedStr] = [str]

        return list(grams.values())
        

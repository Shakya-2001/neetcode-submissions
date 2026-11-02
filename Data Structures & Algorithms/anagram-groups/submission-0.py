class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myhash = {}
        for i in range(len(strs)):
            x = "".join(sorted(strs[i]))
            if x in myhash:
                myhash[x].append(strs[i])
            else:
                myhash[x]=[(strs[i])]
            

        return list(myhash.values())
        
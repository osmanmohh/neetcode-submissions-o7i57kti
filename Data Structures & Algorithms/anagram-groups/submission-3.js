class Solution {
    /**
     * @param {string[]} strs
     * @return {string[][]}
     */
    groupAnagrams(strs) {
        let res = new Map()
        for(const s of strs){
            const sortedS = s.split('').sort().join('');

            if(!res.has(sortedS)){
                res.set(sortedS, [])
            }

            res.get(sortedS).push(s)

        }
        return Array.from(res.values());

    }
    
}


/**
 * 
 res = collections.defaultdict(list)
 for s in strs:
    res[tuple(Counter(s))].append(s)
return list(res.values())
 */
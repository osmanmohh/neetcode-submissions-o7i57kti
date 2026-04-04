class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    isAnagram(s, t) {
        if (s.length !== t.length){
            return false
        }
        let sMap = {}
        let tMap = {}
        for (const c of s){
            sMap[c] = (sMap[c] || 0) + 1
        }
        for (const c of t){
            tMap[c] = (tMap[c] || 0) + 1
        }
        for (const key in sMap){
            if (sMap[key] !== tMap[key]){
                return false
            }
        }
        return true

    }
    
}

class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        // s is the string we are checking
        // p is the anagram string
        vector<int> ans;
        //26 is alphabet size
        //represents freqs of current substring of s
        vector<int> hash(26, 0);
        //represents freqs of string p
        vector<int> phash(26, 0);
        //if string s is 'abcde' then the hashes look like
        //idx 0 has freq of a, idx 1 has freq of b etc
        int window = p.size();
        int len = s.size();
        
        //returns empty vector if s is smaller than p
        if(len < window) {
            return ans;
        }
        //window boundaries
        int left = 0,right = 0;
        while(right < window) {
            phash[p[right] - 'a'] += 1;
            hash[s[right] - 'a'] += 1;
            right++;
        }
        right -=1;
        //go thru whole string s => O(n) where n is length of s
        //right will end at s.length()-1
        while(right < len) {
            if(phash == hash) {
                ans.push_back(left);
            }
            right+=1;
            if(right != len) {
                hash[s[right] - 'a'] += 1;
            }
            hash[s[left] - 'a'] -=1 ;
            left += 1;
        }
        return ans;
    }
};

class Solution {
  public:
    int count(string& s) {
        vector<int> freq(26, 0);
        for (char c : s) {
            freq[c - 'a']++;
        }

        int evenCount = 0;

        // count characters with even frequency
        for (int f : freq) {
            if (f > 0 && f % 2 == 0) {
                evenCount++;
            }
        }

        return evenCount;
    }
};

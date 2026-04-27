class Solution {
  public:
    int substrWithVowels(string &s1, string &s2) {
        unordered_set<char> required(s1.begin(), s1.end());
        unordered_map<char, int> window;

        int requiredCount = required.size();
        int formed = 0;

        int left = 0;
        int minLen = INT_MAX;

        for (int right = 0; right < s2.size(); right++) {
            char c = s2[right];

            if (required.count(c)) {
                window[c]++;
                if (window[c] == 1) {
                    formed++;
                }
            }
            while (formed == requiredCount) {
                minLen = min(minLen, right - left + 1);

                char leftChar = s2[left];
                if (required.count(leftChar)) {
                    window[leftChar]--;
                    if (window[leftChar] == 0) {
                        formed--;
                    }
                }
                left++;
            }
        }

        return (minLen == INT_MAX) ? -1 : minLen;
    }
};

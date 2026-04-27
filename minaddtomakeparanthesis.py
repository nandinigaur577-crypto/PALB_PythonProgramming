class Solution {
  public:
    int minParentheses(string& s) {
        int open = 0;        // unmatched '('
        int insertions = 0;  // needed '('

        for (char c : s) {
            if (c == '(') {
                open++;
            } else { // c == ')'
                if (open > 0) {
                    open--;  // match with '('
                } else {
                    insertions++; // need to insert '('
                }
            }
        }

        // remaining '(' need ')'
        return insertions + open;
    }
};

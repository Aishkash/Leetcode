class Solution {
    public String convert(String s, int numRows) {
        if (numRows == 1 || s.length() <= numRows) {
            return s;
        }

        // create an array of Strings instead of StringBuilder
        String[] rows = new String[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = "";
        }

        int row = 0;
        boolean goingDown = true;

        for (char ch : s.toCharArray()) {
            rows[row] = rows[row] + ch; // string concatenation

            if (row == numRows - 1) {
                goingDown = false;
            } else if (row == 0) {
                goingDown = true;
            }

            row += goingDown ? 1 : -1;
        }

        // join strings
        String result = "";
        for (String r : rows) {
            result = result + r;
        }

        return result;
    }
}
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.List;

public class _2870_math_homework {
    static List<String> nums;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        String line;
        nums = new ArrayList<>();
        for (int i=0; i<n; i++) {
            find(br.readLine());
        }
        Collections.sort(nums, new Comparator<String>() {
            @Override
            public int compare(String o1, String o2) {
                if (o1.length() == o2.length()) {
                    return o1.compareTo(o2);
                }
                return o1.length() - o2.length();
            }
        });
        StringBuilder sb = new StringBuilder();
        for (String num : nums) {
            sb.append(num);
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    private static void find(String line) {
        StringBuilder sb = new StringBuilder();
        boolean isNum = false;
        for (char c : line.toCharArray()) {
            if (c >= '0' && c <= '9') {
                isNum = true;
                sb.append(c);
            } else {
                isNum = false;
            }
            if (isNum == false) {
                if (sb.length() != 0) {
                    nums.add(noZero(sb.toString()));
                    sb = new StringBuilder();
                }
            }
        }
        if (sb.length() != 0) {
            nums.add(noZero(sb.toString()));
        }
    }

    private static String noZero(String num) {
        if (num.length() == 1) {
            return num;
        }
        int idx = -1;
        for (int i=0; i<num.length(); i++) {
            if (num.charAt(i) == '0') {
                idx = i;
            } else {
                break;
            }
        }
        if (idx == num.length()-1) {
            return "0";
        }
        if (idx != -1) {
            return num.substring(idx+1);
        }
        return num;
    }
}
/*
1
009223372036854775807
-----------
9223372036854775807
 */

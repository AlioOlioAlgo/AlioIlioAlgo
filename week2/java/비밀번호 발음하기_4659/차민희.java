import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class _4659_pronounce_pw {
    static String T = "<%s> is acceptable.";
    static String F = "<%s> is not acceptable.";
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        List<String> results = new ArrayList<>();
        String line;
        StringBuilder sb = new StringBuilder();
        while ((line = br.readLine()) != null && !line.isEmpty()) {
            results.add(check(line));
        }
        for (int i=0; i<results.size()-1; i++) {
            sb.append(results.get(i));
            sb.append("\n");
        }
        System.out.println(sb.toString());
    }

    private static String check(String line) {
        boolean hasConsonant = false; // 1. 모음 하나 이상 포함
        boolean isContinue3 = false; // 2. 모음 3개 연속 또는 자음 3개 연속 (x)
        boolean isContinue2 = false; // 3. 같은 글자가 연속 두번 (ee, oo는 제외) (x)
        int cnt = 1;
        boolean isConsonant = !consonant[line.charAt(0)-'a'];
        char pre = ' ';
        for (char c : line.toCharArray()) {
            int idx = c-'a';
            //1.
            if (!hasConsonant && consonant[idx]) {
                hasConsonant = true;
            }
            //2.
            boolean nIsConsonant = consonant[idx];
            if (!isContinue3) {
                if (isConsonant == nIsConsonant) {
                    cnt++;
                    if (cnt == 3) {
                        isContinue3 = true;
                    }
                } else {
                    cnt = 1;
                }
                isConsonant = nIsConsonant;
            }
            //3.
            if (!isContinue2
                    && !allow[idx]
                    && pre == c) {
                isContinue2 = true;
            }
            pre = c;
        }
//        System.out.println(hasConsonant + ", " + !isContinue3 + ", " + !isContinue2);
        if (hasConsonant && !isContinue3 && !isContinue2) {
            return String.format(T, line);
        } else {
            return String.format(F, line);
        }
    }

    static boolean[] allow = {false, false, false, false, true, false, false, false, false, false, false, false, false, false, true, false, false, false, false, false, false, false, false, false, false, false};
    static boolean[] consonant = {true, false, false, false, true, false, false, false, true, false, false, false, false, false, true, false, false, false, false, false, true, false, false, false, false, false};
}

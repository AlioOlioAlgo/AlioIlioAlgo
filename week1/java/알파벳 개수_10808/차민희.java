import java.io.*;

public class _10808_number_of_alphabets {
    static final Integer ALPHABET_TOTAL = 26;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int[] count = new int[ALPHABET_TOTAL];
        for (char c : br.readLine().toCharArray()) {
            count[c-'a'] += 1;
        }
        for (int i=0; i<ALPHABET_TOTAL; i++) {
            bw.write(String.valueOf(count[i]));
            if (i != ALPHABET_TOTAL-1) {
                bw.write(" ");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }
}

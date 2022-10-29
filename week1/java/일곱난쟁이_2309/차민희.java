import java.io.*;
import java.util.Arrays;

public class _2309_seven_dwarfs {
    static int sum = 0;
    static int[] statures = new int[9];
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i=0; i<9; i++) {
            statures[i] = Integer.parseInt(br.readLine());
            sum += statures[i];
        }
        markNoDwarf();
        Arrays.sort(statures);
        for (int i=0; i<7; i++) {
            bw.write(String.valueOf(statures[i]));
            if (i != 6) {
                bw.write("\n");
            }
        }
        bw.flush();
        bw.close();
        br.close();
    }

    public static void markNoDwarf() {
        for (int i=0; i<9; i++) {
            for (int j=i+1; j<9; j++) {
                if (sum - statures[i] - statures[j] == 100) {
                    statures[i] = statures[j] = 100;
                    return;
                }
            }
        }
    }
}

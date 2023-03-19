package allper.functions;

import java.io.*;

/**
 * packageName    : allper.functions
 * fileName       : fiveStars
 * author         : ipeac
 * date           : 2023-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-19        ipeac       최초 생성
 */
public class FiveStars {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 10; j++) {
                bw.write("*");
            }
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }

}





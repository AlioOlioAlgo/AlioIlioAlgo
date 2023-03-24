package allper.implement.ZOAC_16719;

import java.io.*;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

/**
 * packageName    : allper.implement.ZOAC_16719
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-24
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-24        ipeac       최초 생성
 */
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

    public static void main(String[] args) throws IOException {
        String[] word = br.readLine().split("");
        System.out.println("word = " + Arrays.toString(word));
        List<String> makeArr = new ArrayList<>();
        makeWord(new ArrayList<>(Arrays.asList(word)), makeArr);
        br.close();
        bw.flush();
        bw.close();
    }

    public static void makeWord(List<String> leftWord, List<String> makeArr) throws IOException {
        if (leftWord.size() == 0) {
            for (String s : makeArr) {
                bw.write(s + "\n");
            }
            System.exit(0);
        }
        for (int i = 0; i < leftWord.size(); i++) {
            String remove = leftWord.remove(i);
            makeArr.add(remove);
            if (checkArr(makeArr)) {
                makeWord(leftWord, makeArr);
            }
            makeArr.remove(makeArr.size() - 1);
            leftWord.add(i, remove);
        }

        return;
    }

    private static boolean checkArr(List<String> makeArr) {
        if (makeArr.size() == 1) {
            return true;
        }
        for (int i = 0; i < makeArr.size() - 1; i++) {
            if ((int) makeArr.get(makeArr.size() - 2).charAt(i) < (int) makeArr.get(makeArr.size() - 1).charAt(i)) {
                return true;
            }
        }
        return false;
    }

    // 2차원 List 출력 메소드
    public static void print2DList(List<List<Integer>> twoDList) throws IOException {
        bw.write("[ ");
        for (List<Integer> row : twoDList) {
            for (Integer value : row) {
                bw.write(value + " ");
            }
            bw.newLine();
        }
    }
}

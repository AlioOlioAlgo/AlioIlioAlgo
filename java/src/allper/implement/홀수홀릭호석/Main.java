package allper.implement.홀수홀릭호석;

import java.io.*;
import java.util.List;

/**
 * packageName    : allper.implement
 * fileName       : OddHolicHosuk_20164
 * author         : ipeac
 * date           : 2023-03-22
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-22        ipeac       최초 생성
 */
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    static int n;
    static int MIN = Integer.MAX_VALUE, MAX = Integer.MIN_VALUE;
    
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        
        cutWord(String.valueOf(n), countOdd(String.valueOf(n)));
        
        
        bw.write(MIN + " " + MAX);
        br.close();
        bw.flush();
        bw.close();
    }
    
    
    public static void cutWord(String word, int total) throws IOException {
        bw.write("===========================================\n");
        
        String[] words = word.split("");
        int value = 0;
        bw.write("word" + word);
        bw.newLine();
        if (word.length() == 1) {
            MAX = Math.max(MAX, total);
            MIN = Math.min(MIN, total);
            bw.write("MAX" + MAX);
            bw.newLine();
            
            bw.write("MIN" + MIN);
            bw.newLine();
        } else if (word.length() == 2) {
            for (String s : words) {
                value += Integer.parseInt(s);
            }
            
            cutWord(String.valueOf(value), total + countOdd(String.valueOf(value)));
            
        } else if (word.length() >= 3) {
            for (int i = 0; i <= word.length() - 3; i++) {
                for (int j = i + 1; j <= word.length() - 2; j++) {
                    String s1 = word.substring(0, i + 1);
                    String s2 = word.substring(i + 1, j + 1);
                    String s3 = word.substring(j + 1);
                    bw.write(s1 + "\n");
                    bw.write(s2 + "\n");
                    bw.write(s3 + "\n");
                    int sum = Integer.parseInt(s1) + Integer.parseInt(s2) + Integer.parseInt(s3);
                    
                    cutWord(String.valueOf(sum), total + countOdd(String.valueOf(sum)));
                }
            }
        }
    }
    
    /*
     * 해당 단어의 홀수의 갯수를 센다.
     * */
    public static int countOdd(String word) throws IOException {
        String[] wordArr = word.split("");
        int oddCount = 0;
        for (String s : wordArr) {
            if (Integer.parseInt(s) % 2 != 0) {
                oddCount++;
            }
        }
        return oddCount;
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

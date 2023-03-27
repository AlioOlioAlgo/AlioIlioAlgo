package allper.implement.단어맞추기_9081;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/**
 * packageName    : allper.implement.단어맞추기_9081
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-27        ipeac       최초 생성
 */
public class Main {
    static int T;
    static StringBuilder sb = new StringBuilder();
    
    static int first = -1;
    
    
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        T = rd.nextInt();
        
        for (int i = 0; i < T; i++) {
            System.out.println("=====================");
            String word = rd.next();
            System.out.println("word = " + word);
            checkAsc(word.toCharArray());
            
            sb.append(word).append("\n");
            
            System.out.println(sb);
        }
    }
    
    public static void checkAsc(char[] word) {
        //마지막 문자보다 작은 값을 탐색한다
        for (int i = word.length - 1; i > -1; i--) {
            char curChar = word[i];
            for (int j = i - 1; j > -1; j--) {
                if (curChar > word[j]) {
                    char changedWord = word[j];
                    char tmp = word[i];
                    word[i] = word[j];
                    word[j] = tmp;
                    first = j;
                    break;
                }
            }
        }
        System.out.println("word = " + Arrays.toString(word));
        //변환합니다.
        // 이후 주소를 오름차순으로 변경
        for (int i = first + 1; i < word.length - 1; i++) {
            for (int j = i + 1; j < word.length; j++) {
                if (word[i] > word[j]) {
                    char tmp = word[i];
                    word[i] = word[j];
                    word[j] = tmp;
                }
            }
        }
        
        System.out.println("word = " + Arrays.toString(word));
    }
    
    static class FastReader {
        BufferedReader br;
        StringTokenizer st;
        
        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }
        
        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        
        int nextInt() {
            return Integer.parseInt(next());
        }
        
        long nextLong() {
            return Long.parseLong(next());
        }
        
        String nextLine() {
            String str = "";
            try {
                str = br.readLine();
            } catch (IOException e) {
                e.printStackTrace();
            }
            return str;
        }
    }
}

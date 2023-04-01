package com.allper.implement.단어맞추기_9081;

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
    
    
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        T = rd.nextInt();
        
        for (int i = 0; i < T; i++) {
            String word = rd.next();
            char[] returnedChar = checkAsc(word.toCharArray());
            System.out.println(String.valueOf(returnedChar));
        }
    }
    
    public static char[] checkAsc(char[] word) {
        boolean wordChanged = false;
        //마지막 문자보다 작은 값을 탐색한다 -> 다만 인덱스는 그 후보중에 최댓값이여한다.
        int curIndex = 0;
        int first = -1;
        for (int i = word.length - 1; i > -1; i--) {
            char curChar = word[i];
            for (int j = i - 1; j > -1; j--) {
                if (curChar > word[j] && j > first) {
                    first = j;
                    curIndex = i;
                    wordChanged = true;
                }
            }
        }
        if (wordChanged) {
            //maxIndex와 curIndex 자리 바꿈
            char tmp = word[curIndex];
            word[curIndex] = word[first];
            word[first] = tmp;
            //변환합니다.
            // 이후 주소를 오름차순으로 변경
            Arrays.sort(word, first + 1, word.length);
        }
        
        return word;
        
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

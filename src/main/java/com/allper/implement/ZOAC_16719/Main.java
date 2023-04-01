package com.allper.implement.ZOAC_16719;

import java.io.*;

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
    
    static char[] result;
    
    public static void main(String[] args) throws IOException {
        String s = br.readLine();
        result = new char[s.length()];
        zoac(s, 0, s.length());
        
    }
    
    private static void zoac(String inputWord, int startIndex, int endIndex) throws IOException {
        if (startIndex >= endIndex) {
            return;
        }
        int minIndex = Integer.MAX_VALUE;
        char minChar = 'z' + 1;
        for (int i = startIndex; i < endIndex; i++) {
            char curChar = inputWord.charAt(i);
            if (minChar > curChar) {
                minChar = curChar;
                minIndex = i;
            }
        }
        result[minIndex] = minChar;
        String sb = removeEmpty(result);
        bw.write(sb + "\n");
        if (sb.length() == inputWord.length()) {
            br.close();
            bw.flush();
            bw.close();
            System.exit(0);
        }
        
        zoac(inputWord, minIndex + 1, endIndex);
        zoac(inputWord, startIndex, minIndex);
    }
    
    private static String removeEmpty(char[] chars) {
        StringBuilder sb = new StringBuilder();
        for (char aChar : chars) {
            if (aChar != '\0') {
                sb.append(aChar);
                
            }
        }
        return sb.toString();
    }
    
    
}

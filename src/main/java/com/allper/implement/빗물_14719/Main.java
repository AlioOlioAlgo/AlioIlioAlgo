package com.allper.implement.빗물_14719;

import java.io.*;
import java.util.List;
import java.util.StringTokenizer;

/**
 * packageName    : allper.implement.빗물_14719
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-23
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-23        ipeac       최초 생성
 */
public class Main {
    
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    
    static int h, w, ans;
    static int[] intArr;
    
    public static void main(String[] args) throws IOException {
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        h = Integer.parseInt(st.nextToken());
        w = Integer.parseInt(st.nextToken());
        
        intArr = new int[w];
        st = new StringTokenizer(br.readLine(), " ");
        for (int i = 0; i < w; i++) {
            intArr[i] = Integer.parseInt(st.nextToken());
        }
        
        for (int i = 1; i < w - 1; i++) {
            int curHeight = intArr[i];
            int left = 0;
            int right = 0;
            
            for (int j = i - 1; j > -1; j--) {
                left = Math.max(intArr[j], left);
            }
            for (int j = i + 1; j < w; j++) {
                right = Math.max(intArr[j], right);
            }
            if (curHeight < left && curHeight < right) {
                int min = Math.min(left, right);
                ans += min - curHeight;
            }
        }
        bw.write(String.valueOf(ans));
        br.close();
        
        bw.flush();
        bw.close();
    }
    
    public static int plusArea(int maxX, int curX, int curHeight, int exHeight) {
        return (curX - maxX - 1) * (curHeight - exHeight);
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

package com.allper.functions.단축키지정_1283;

import java.io.*;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.StringTokenizer;

/**
 * packageName    : com.allper.functions.단축키지정_1283
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-04-01
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-04-01        ipeac       최초 생성
 */
public class Main {
    static Map<String, int[]> check;
    
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        check = new LinkedHashMap<>();
        int n = rd.nextInt();
        for (int i = 0; i < n; i++) {
            String word = rd.nextLine();
            StringTokenizer st = new StringTokenizer(word, " ");
            boolean flag = false;
            for (int j = 0; j < st.countTokens(); j++) {
                String wo = st.nextToken();
                if (!check.containsKey(wo.substring(0, 1)
                                               .toLowerCase())) { // 첫글자들이 단축키에 등록이 안되어있다면 단축키 등록함.
                    check.put(wo.substring(0, 1)
                                      .toLowerCase(), new int[]{j, i, 0}); // i번째 단어중에 j 단어 앞글자가 대문자임
                    flag = true;
                    break;
                }
            }
            bw.newLine();
            if (!flag) {
                StringTokenizer st2 = new StringTokenizer(word, " ");
                loop1:
                for (int j = 0; j < st2.countTokens(); j++) {
                    String innerWord = st2.nextToken();
                    for (int k = 0; k < innerWord.length(); k++) {
                        String key = innerWord.substring(k, k + 1)
                                             .toLowerCase();
                        if (!check.containsKey(key)) {
                            
                            check.put(key, new int[]{j, i, k});
                            break loop1;
                        }
                    }
                }
            }
        }
        for (Map.Entry<String, int[]> stringEntry : check.entrySet()) {
            
        }
        System.out.println("check = " + check);
        
        
        bw.close();
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

package com.allper.backtracking.가르침_1062;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;
import java.util.StringTokenizer;

/**
 * packageName    : com.allper.backtracking.가르침_1062
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-04-02
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-04-02        ipeac       최초 생성
 */
public class Main {
    
    static Set<Character> alpha = new HashSet<>();
    static int k;
    
    static String[] words;
    static int maxCnt = Integer.MIN_VALUE;
    
    
    public static void main(String[] args) throws IOException {
        Set<Character> removeSet = new HashSet<>(Arrays.asList('a', 'n', 't', 'i', 'c'));
        FastReader rd = new FastReader();
        
        for (int i = 97; i < 123; i++) {
            alpha.add((char) i);
        }
        alpha.removeAll(removeSet);
        System.out.println("alpha = " + alpha);
        int n = rd.nextInt();
        k = rd.nextInt();
        if (k < 5) {
            System.out.println("0");
            return;
        }
        if (k == 26) {
            System.out.println(n);
            return;
        }
        int canLearn = k - 5;
        
        words = new String[n];
        for (int i = 0; i < n; i++) {
            words[i] = rd.next();
            words[i] = words[i].substring(4, words[i].length() - 4);
        }
        System.out.println("words = " + Arrays.toString(words));
        
        setWord(0, canLearn, 'a');
        System.out.println(maxCnt);
    }
    
    static void setWord(int cnt, int canLearn, char start) {
        if (cnt == canLearn) {
            counting(words);
            return;
        }
        for (char i = start; i <= 'z'; i++) {
            if (alpha.contains(i)) {
                alpha.remove(i);
                setWord(cnt + 1, canLearn, (char) (i + 1));
                alpha.add(i);
            }
        }
    }
    
    private static void counting(String[] words) {
        int cnt = 0;
//        System.out.println("alpha = " + alpha);
//        System.out.println("words = " + Arrays.toString(words));
        for (String word : words) {
            boolean flag = false;
            for (int i = 0; i < word.length(); i++) {
                if (alpha.contains(word.charAt(i))) {
                    flag = true;
                    break;
                }
            }
            if (!flag) {
                cnt++;
            }
        }
        maxCnt = Math.max(maxCnt, cnt);
//        System.out.println("maxCnt = " + maxCnt);
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

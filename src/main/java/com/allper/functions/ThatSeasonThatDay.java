package com.allper.functions;

import java.io.*;
import java.time.DateTimeException;
import java.time.LocalDate;
import java.util.StringTokenizer;

/**
 * packageName    : allper.functions
 * fileName       : ThatSeasonThatDay
 * author         : ipeac
 * date           : 2023-03-19
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-19        ipeac       최초 생성
 */
public class ThatSeasonThatDay {
    public static boolean isValidate(int year, int month, int day) {
        try {
            LocalDate date = LocalDate.of(year, month, day);
            return true;
        } catch (DateTimeException e) {
            return false;
        }
    }
    
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(bf.readLine(), " ");
        
        int year = Integer.parseInt(st.nextToken());
        int month = Integer.parseInt(st.nextToken());
        int day = Integer.parseInt(st.nextToken());
        
        if (isValidate(year, month, day)) {
            if (month >= 3 && month <= 5) {
                bw.write("Spring");
            } else if (month >= 6 && month <= 8) {
                bw.write("Summer");
            } else if (month >= 9 && month <= 11) {
                bw.write("Fall");
            } else {
                bw.write("Winter");
            }
        } else {
            bw.write(String.valueOf(-1));
        }
        
        bf.close();
        bw.flush();
        bw.close();
    }
}

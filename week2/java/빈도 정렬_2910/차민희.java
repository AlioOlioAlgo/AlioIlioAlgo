import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class _2910_frequency_sort {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int limit = Integer.parseInt(st.nextToken());
        List<Num> nums = new ArrayList<>();
        Map<Integer, Num> map = new HashMap<>();
        int sn;
        for (String s : br.readLine().split(" ")) {
            sn = Integer.parseInt(s);
            Num num = map.get(sn);
            if (num != null) {
                num.freq += 1;
            } else {
                Num nNum = new Num(sn, 1);
                nums.add(nNum);
                map.put(sn, nNum);
            }
        }
        Collections.sort(nums);
        StringBuilder sb = new StringBuilder();
        for (Num num : nums) {
            for (int i=0; i<num.freq; i++) {
                sb.append(num.num);
                sb.append(" ");
            }
        }
        System.out.println(sb.toString());
    }

    static class Num implements Comparable<Num> {
        int num;
        int freq;

        Num (int num, int freq) {
            this.num = num;
            this.freq = freq;
        }

        @Override
        public int compareTo(Num o) {
            return o.freq - freq;
        }
    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;
import java.util.stream.Stream;

public class _2979_parking_truck {
    static enum IO {
        I, O;
    }

    static class Data implements Comparable<Data> {
        int time;
        IO io;
        public Data(int time, IO io) {
            this.time = time;
            this.io = io;
        }

        @Override
        public int compareTo(Data o) {
            return this.time - o.time;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] fee;
        Data[] datas = new Data[6];
        fee = Stream.of(br.readLine().split(" ")).mapToInt(Integer::parseInt).toArray();

        StringTokenizer st;
        for (int i=0; i<3; i++) {
            st = new StringTokenizer(br.readLine());
            datas[2*i] = new Data(Integer.parseInt(st.nextToken()), IO.I);
            datas[2*i+1] = new Data(Integer.parseInt(st.nextToken()), IO.O);
        }

        Arrays.sort(datas);
        int cnt = 0;
        int start = 0;
        int total = 0;
        for (int i=0; i<datas.length; i++){
            if (cnt == 0) {
                start = datas[i].time;
                cnt++;
                continue;
            }
            total += (datas[i].time - start) * cnt * fee[cnt-1];
            start = datas[i].time;
            if (datas[i].io == IO.I) {
                cnt++;
            }else {
                cnt--;
            }
        }
        System.out.println(total);
    }
}

/*
[case]
INPUT
5 3 1
1 2
2 8
3 5
OUPUT
37
 */
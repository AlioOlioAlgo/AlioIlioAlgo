import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class _1620_im_poketmon_master {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        String[] name = new String[n+1];
        Map<String, Integer> nameToNum = new HashMap<>();
        for (int i=1; i<=n; i++) {
            name[i] = br.readLine();
            nameToNum.put(name[i], i);
        }
        StringBuilder sb = new StringBuilder();
        String str;
        char c;
        for (int i=0; i<m; i++) {
            str = br.readLine();
            c = str.charAt(0);
            if (c >= '0' && c <= '9') {
                sb.append(name[Integer.parseInt(str)]);
            } else {
                sb.append(nameToNum.get(str));
            }
            sb.append("\n");
        }
        System.out.printf(sb.toString());
    }
}

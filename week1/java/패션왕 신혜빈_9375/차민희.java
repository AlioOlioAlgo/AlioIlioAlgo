import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class _9375_fashion_king {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        Map<String, Integer> typeToNum;
        int t = Integer.parseInt(br.readLine());
        int n;
        StringTokenizer st;
        String type;
        int cnt;
        StringBuilder sb = new StringBuilder();
        for (int i=0; i<t; i++) {
            n = Integer.parseInt(br.readLine());
            cnt = 1;
            typeToNum = new HashMap<>();
            for (int j=0; j<n; j++) {
                st = new StringTokenizer(br.readLine());
                st.nextToken();
                type = st.nextToken();
                typeToNum.put(type, typeToNum.getOrDefault(type, 0)+1);
            }
            for (Map.Entry<String, Integer> e : typeToNum.entrySet()) {
                cnt *= e.getValue() + 1;
            }
            sb.append(cnt-1).append("\n");
        }
        System.out.printf(sb.toString());
    }
}

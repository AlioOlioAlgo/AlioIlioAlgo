import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.Map;
import java.util.StringTokenizer;

public class _1940_jumong {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());
        Map<Integer, Boolean> armorMap = new HashMap<>();
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            int armor = Integer.parseInt(st.nextToken());
            armorMap.put(armor, true);
        }
        int sum = 0;
        for (int armor : armorMap.keySet()) {
            int armor2 = m-armor;
            if (armor > armor2 && armorMap.get(armor2) != null) {
                sum++;
            }
        }
        System.out.println(sum);
    }
}

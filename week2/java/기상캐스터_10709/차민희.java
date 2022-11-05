import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _10709_weather_caster {
    static StringBuilder sb = new StringBuilder();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int h = Integer.parseInt(st.nextToken());
        int w = Integer.parseInt(st.nextToken());
        for (int i=0; i<h; i++) {
            cloud(br.readLine());
        }
        System.out.println(sb.toString());
    }

    private static void cloud(String line) {
        char c;
        boolean hasCloud = false;
        int min = -1;
        for (int i=0; i<line.length(); i++) {
            c = line.charAt(i);
            if (c == 'c') {
                min = 0;
                hasCloud = true;
            } else if (hasCloud) {
                min++;
            }
            sb.append(min);
            if (i < line.length()-1) {
                sb.append(" ");
            }
        }
        sb.append("\n");
    }
}

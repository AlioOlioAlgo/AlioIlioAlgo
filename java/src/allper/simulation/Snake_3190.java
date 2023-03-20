package allper.simulation;

import java.io.*;
import java.util.*;

/**
 * packageName    : allper.simulation
 * fileName       : Snake_3190
 * author         : ipeac
 * date           : 2023-03-20
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-20        ipeac       최초 생성
 */
public class Snake_3190 {

    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n, k, l;
    static List<List<Integer>> appleLocation = new ArrayList<>();
    static List<List<String>> snakesDir = new ArrayList<>();

    static List<List<Integer>> graph = new ArrayList<>();
    static List<Integer> tailLocation = new ArrayList<>();

    static int ans; // 정답

    static int[][] move = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}}; // 북 동 남 서

    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        k = Integer.parseInt(br.readLine());
        for (int i = 0; i < k; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            List<Integer> newArr = new ArrayList<>();
            newArr.add(Integer.valueOf(st.nextToken()));
            newArr.add(Integer.valueOf(st.nextToken()));
            appleLocation.add(newArr);
        }
        print2DList(appleLocation, "appleLocation");

        l = Integer.parseInt(br.readLine());

        for (int i = 0; i < l; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            List<String> newArr = new ArrayList<>(List.of(new String[]{st.nextToken(), st.nextToken()}));
            snakesDir.add(newArr);
        }
        print2DList(snakesDir, "snakeDir");

        for (int i = 0; i < n; i++) {
            List<Integer> rows = new ArrayList<>(Collections.nCopies(n, 0));
            graph.add(rows);
        }

        //그래프에 사과위치 표시하기
        for (List<Integer> integers : appleLocation) {
            graph.get(integers.get(0) - 1).set(integers.get(1), 1);
        }
        print2DList(graph, "graph");

        br.close();
        bw.flush();
        bw.close();
    }

    public static void moveSnake() {
        tailLocation = new ArrayList<>(Arrays.asList(0, 0));
        int x = 0, y = 0;
        int dir = 1; // 동쪽으로 움직여야함
        while (true) {
            if (graph.get(x).get(y) == 2 || !inRange(x, y)) { // 벽이나 자기 몸을 만나면 break합니다.
                break;
            }
        }

    }

    public static boolean inRange(int x, int y) {
        return 0 <= x && x < n && 0 <= y && y < n;
    }

    // 2차원 List 출력 메소드
    public static <T> void print2DList(List<List<T>> twoDList, String varName) throws IOException {
        bw.write("\n[  -> " + varName);
        bw.newLine();
        for (List<T> row : twoDList) {
            for (T value : row) {
                bw.write(value + " ");
            }
            bw.newLine();
        }
        bw.write(" ]\n");

    }
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

public class _1068_tree {
    static int cnt = 0;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        Queue<Integer> queue = new LinkedList<>();
        List<Integer>[] edges = new List[n];
        for (int i=0; i<n; i++) {
            edges[i] = new ArrayList<>();
        }
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0; i<n; i++) {
            int parent = Integer.parseInt(st.nextToken());
            if (parent == -1) {
                queue.offer(i);
            } else {
                edges[parent].add(i);
            }
        }
        int rvNum = Integer.parseInt(br.readLine());
        edges[rvNum] = null;
        for (List<Integer> edge : edges) {
            if (edge != null && edge.contains(rvNum)) {
                edge.remove(Integer.valueOf(rvNum));
            }
        }
        count(queue, edges);
        System.out.println(cnt);
    }

    private static void count(Queue<Integer> queue, List<Integer>[] edges) {
        while (!queue.isEmpty()) {
            int num = queue.poll();
            if (edges[num] == null) {
                continue;
            }
            if (edges[num].size() == 0) {
                cnt++;
            } else {
                for (int i=0; i<edges[num].size(); i++) {
                    queue.offer(edges[num].get(i));
                }
            }
        }
    }
    /*
2
-1 0
1
-----
1
     */
}

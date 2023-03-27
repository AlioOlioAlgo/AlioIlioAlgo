package allper.implement.트리순회;

import java.io.*;
import java.util.List;
import java.util.StringTokenizer;

/**
 * packageName    : allper.implement.트리순회
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-27
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-27        ipeac       최초 생성
 */
public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n, ans, end;
    static Node[] nodes;
    static boolean[] visited;
    
    public static void main(String[] args) throws IOException {
        FastReader rd = new FastReader();
        n = rd.nextInt();
        nodes = new Node[n + 10];
        visited = new boolean[n + 10];
        
        for (int i = 1; i <= n; i++) {
            nodes[i] = new Node();
        }
        for (int i = 1; i <= n; i++) {
            int cur = rd.nextInt();
            int left = rd.nextInt();
            int right = rd.nextInt();
            nodes[cur].setChildren(left, right);
            if (left != -1) {
                nodes[left].setParent(cur);
            }
            if (right != -1) {
                nodes[right].setParent(cur);
            }
        }
        checkEnd(1);// 노드의 오른쪽으로 쭉쭉타서 마지막 value 값을 기억합니다. end가 그 끝값입니다.
        
        
    }
    
    public static void checkEnd(int cur) {
        end = cur;
        if (nodes[end].right != -1) {
            checkEnd(end);
        } else {
            return;
        }
    }
    
    // 2차원 List 출력 메소드
    public static void print2DList(List<List<Integer>> twoDList) throws IOException {
        bw.write("[ ");
        for (List<Integer> row : twoDList) {
            for (Integer value : row) {
                bw.write(value + " ");
            }
            bw.newLine();
        }
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

class Node {
    int left, right, parent;
    
    public Node() {
        this.left = -1;
        this.right = -1;
        this.parent = -1;
    }
    
    void setChildren(int left, int right) {
        this.left = left;
        this.right = right;
    }
    
    void setParent(int parent) {
        this.parent = parent;
    }
}

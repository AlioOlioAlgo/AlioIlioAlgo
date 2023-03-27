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
    static int n, ans;
    static Node[] nodes;
    static boolean[] visited;
    
    public static void main(String[] args) throws IOException {
        
        n = Integer.parseInt(br.readLine());
        nodes = new Node[n + 1];
        visited = new boolean[n + 1];
        
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine(), " ");
            int a = Integer.parseInt(st.nextToken());
            int b = Integer.parseInt(st.nextToken());
            int c = Integer.parseInt(st.nextToken());
            Node node;
            if (nodes[a] == null) {
                node = new Node(a);
                nodes[a] = node;
            } else {
                node = nodes[a]; // 이미존재하는 노드의 경우 해당 노드를 불러와서 left right 설정
            }
            
            if (b != -1) {
                if (nodes[b] == null) {
                    Node leftNode = new Node(b);
                    nodes[b] = leftNode;
                    node.left = leftNode;
                } else {
                    node.left = nodes[b];
                }
            }
            
            if (c != -1) {
                if (nodes[c] == null) {
                    Node rightNode = new Node(c);
                    nodes[c] = rightNode;
                    node.right = rightNode;
                } else {
                    node.right = nodes[c];
                }
            }
        }
        inorderTraversal(nodes[1]);
        br.close();
        bw.flush();
        bw.close();
    }
    
    public static boolean allTrue(boolean[] arr) {
        for (boolean b : arr) {
            if (!b) {
                return false;
            }
        }
        return true;
    }
    
    public static void inorderTraversal(Node curNode) {
        if (allTrue(visited)) {
            return;
        }
        if (curNode == null) {
            return;
        }
        
        inorderTraversal(curNode.left);
        
        inorderTraversal(curNode.right);
        
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
}

class Node {
    int value;
    Node left, right;
    
    public Node(int value) {
        this.value = value;
    }
}

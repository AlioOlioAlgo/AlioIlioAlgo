package com.allper.implement.트리순회_22856;

import java.io.*;

/**
 * packageName    : allper.implement.트리순회_22856
 * fileName       : Main
 * author         : ipeac
 * date           : 2023-03-26
 * description    :
 * ===========================================================
 * DATE              AUTHOR             NOTE
 * -----------------------------------------------------------
 * 2023-03-26        ipeac       최초 생성
 */
class Node {
    int value;
    Node left, right;
    
    public Node(int value) {
        this.value = value;
    }
}

public class Main {
    static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
    static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
    static int n;
    
    static Node[] nodeList;
    static int ans;
    
    static boolean[] visited;
    
    
    public static void main(String[] args) throws IOException {
        n = Integer.parseInt(br.readLine());
        nodeList = new Node[n + 1];
        visited = new boolean[n + 1];
        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            String[] arr = line.split(" ");
            int value = Integer.parseInt(arr[0]), left = Integer.parseInt(arr[1]), right = Integer.parseInt(arr[2]);
            
            Node node;
            
            if (nodeList[value] == null) {
                node = new Node(value);
                nodeList[value] = node;
            } else {
                node = nodeList[value]; // 이미 존재한다면 해당 value 를 가진 node 를 불러옵니다.
            }
            
            if (left != -1) {
                Node leftNode;
                if (nodeList[left] == null) {
                    leftNode = new Node(left);
                    nodeList[left] = leftNode;
                } else {
                    leftNode = nodeList[left];
                }
                node.left = leftNode;
            }
            
            if (right != -1) {
                Node rightNode;
                if (nodeList[right] == null) {
                    rightNode = new Node(right);
                    nodeList[right] = rightNode;
                } else {
                    rightNode = nodeList[right];
                }
                node.right = rightNode;
            }
        }
        inorderTraversal(nodeList[1]);
        
        bw.write(String.valueOf(ans));
        
        br.close();
        bw.flush();
        bw.close();
    }
    
    public static void inorderTraversal(Node node) {
        if (node == null) {
            return;
        }
        inorderTraversal(node.left);
        if (node.left != null) {
            ans++;
            System.out.println("node.left = " + node.left.value);
        }
        inorderTraversal(node.right);
        if (node.right != null) {
            ans++;
            System.out.println("node.right = " + node.right.value);
        }
    }
    
}

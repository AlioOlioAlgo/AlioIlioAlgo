import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class _1992_quad_tree {
    static char[][] video;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        video = new char[n][n];
        //영상내용 video 배열에 저장
        for (int i=0; i<n; i++){
            video[i] = br.readLine().toCharArray();
        }
        StringBuilder sb = new StringBuilder();
        //quadTree 작업 시작(recursive 하게 작업)
        quadTree(sb, 0, 0, n);
        System.out.println(sb.toString());
    }

    /**
     * (x, y) 는 사각형 영역의 왼쪽 위 꼭지점
     * l 은 영역의 길이
     * @param sb
     * @param x
     * @param y
     * @param l
     */
    private static void quadTree(StringBuilder sb, int x, int y, int l) {
        //num: 압축할 숫자
        char num = video[x][y];
        //영역 내부가 모두 같은 숫자인지 확인되면 압축
        if (canCompress(num, x, y, l)) {
            sb.append(num);
            return;
        }
        //영역 내부에 다른 숫자가 있는 경우, 4분위로 나누어 quadTree 과정을 밟음
        sb.append("(");
        int nl = l/2;
        int nx = x+nl;
        int ny = y+nl;
        quadTree(sb, x, y, nl);
        quadTree(sb, x, ny, nl);
        quadTree(sb, nx, y, nl);
        quadTree(sb, nx, ny, nl);
        sb.append(")");
    }

    private static boolean canCompress(char num, int x, int y, int l) {
        for (int i=x; i<x+l; i++) {
            for (int j=y; j<y+l; j++) {
                if (num != video[i][j]) {
                    return false;
                }
            }
        }
        return true;
    }
/*
[case]
2
11
11
-------
1
 */
}

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class _14502_lab {
	static int max = 0;
	static int n, m;
	static int[][] map;
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());
		n = Integer.parseInt(st.nextToken());
		m = Integer.parseInt(st.nextToken());
		map = new int[n][m];
		for (int i=0; i<n; i++) {
			st = new StringTokenizer(br.readLine());
			for (int j=0; j<m; j++) {
				map[i][j] = Integer.parseInt(st.nextToken());
			}
		}
		pickWall();
		System.out.println(max);
	}

	private static void pickWall() {
		int totalArea = n*m;
		for (int i=0; i<totalArea-2; i++) {
			if (map[i/m][i%m] == 0) {
				map[i/m][i%m] = 1;
			} else {
				continue;
			}
			for (int j=i+1; j<totalArea-1; j++) {
				if (map[j/m][j%m] == 0) {
					map[j/m][j%m] = 1;
				} else {
					continue;
				}
				for (int k=j+1; k<totalArea; k++) {
					if (map[k/m][k%m] == 0) {
						map[k/m][k%m] = 1;
					} else {
						continue;
					}
					spreadAndCount();
					map[k/m][k%m] = 0;
				}
				map[j/m][j%m] = 0;
			}
			map[i/m][i%m] = 0;
		}
	}

	private static void spreadAndCount() {
		int ni, nj;
		for (int i=0; i<n*m; i++) {
			ni = i / m;
			nj = i % m;
			if (map[ni][nj] == 2) {
				spread(ni, nj);
			}
		}
		int cnt = count();
		if (max < cnt) {
			max = cnt;
		}
	}
	
	static int[] dx = {1, -1, 0, 0};
	static int[] dy = {0, 0, 1, -1};
	private static void spread(int x, int y) {
		int nx, ny;
		for (int i=0; i<4; i++) {
			nx = x + dx[i];
			ny = y + dy[i];
			if (nx >= 0 && nx < n && ny >= 0 && ny < m
					&& map[nx][ny] == 0) {
				map[nx][ny] = 3;
				spread(nx, ny);
			}
		}
	}

	private static int count() {
		int cnt = 0;
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				if (map[i][j] == 0) {
					cnt++;
				} else if (map[i][j] == 3) {
					map[i][j] = 0;
				}
			}
		}
		return cnt;
	}
	
	private static void print(int[][] map) {
		for (int i=0; i<n; i++) {
			for (int j=0; j<m; j++) {
				System.out.print(map[i][j]);
				System.out.print(" ");
			}
			System.out.println();
		}
		System.out.println();
	}
}

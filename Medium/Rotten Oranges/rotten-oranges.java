//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            String[] s = br.readLine().trim().split(" ");
            int n = Integer.parseInt(s[0]);
            int m = Integer.parseInt(s[1]);
            int[][] grid = new int[n][m];
            for(int i = 0; i < n; i++){
                String[] S = br.readLine().trim().split(" ");
                for(int j = 0; j < m; j++){
                    grid[i][j] = Integer.parseInt(S[j]);
                }
            }
            Solution obj = new Solution();
            int ans = obj.orangesRotting(grid);
            System.out.println(ans);
        }
    }
}
// } Driver Code Ends


class Pair{
    int x;
    int y;
    int time;
    public Pair(int x, int y, int time){
        this.x = x;
        this.y = y;
        this.time = time;
    }
}
class Solution
{
    //Function to find minimum time required to rot all oranges. 
    public int orangesRotting(int[][] grid)
    {
        int n = grid.length;
        int m = grid[0].length;
        int cntFresh = 0, cnt = 0;
        boolean vis[][] = new boolean[n][m];
        Queue<Pair> queue = new LinkedList<>();
        for(int i=0;i<n;i++){
            for(int j=0;j<m;j++){
                if(grid[i][j]==2){
                    queue.offer(new Pair(i,j,0));
                    vis[i][j] = true;
                }
                if(grid[i][j]==1){
                    cntFresh++;
                }
            }
        }
        int tm = 0;
        int dcol[] = {-1,0,1,0};
        int drow[] = {0,-1,0,1};
        while(!queue.isEmpty()){
            Pair pair = queue.poll();
            int r = pair.x;
            int c = pair.y;
            int t = pair.time;
            tm = Math.max(t,tm);
            for(int i=0;i<4;i++){
                int nrow = r + drow[i];
                int ncol = c + dcol[i];
                if(nrow>=0 && nrow<n && ncol>=0 && ncol<m && !vis[nrow][ncol] && grid[nrow][ncol] == 1){
                    queue.offer(new Pair(nrow,ncol,t+1));
                    vis[nrow][ncol] = true;
                    cnt++;
                }
            }
        }
        if(cnt!=cntFresh) return -1;
        return tm;
    }
}
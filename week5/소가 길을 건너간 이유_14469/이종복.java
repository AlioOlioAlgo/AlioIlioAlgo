import java.util.*; 


class Pair implements Comparable<Pair>{
    
    int arrive;
    int time;
    
    public Pair(int arrive, int time){
        this.arrive = arrive;
        this.time = time; 
    }
    
    @Override
    public int compareTo(Pair cmp){
        
        if(this.arrive == cmp.arrive){
            return this.time-cmp.time;
        }
     
        return this.arrive-cmp.arrive;
        
    }
    
}


public class Main {
    
    public static boolean[] check; 
    
    
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      int N = sc.nextInt();
      ArrayList<Pair> arr = new ArrayList<>(); 
      check = new boolean[N+10];
      
      
      for(int i=1; i<=N; i++){
          
          int arrive = sc.nextInt();
          int time = sc.nextInt(); 
          
          arr.add(new Pair(arrive, time));
          
      }
      
      
      Collections.sort(arr); 
      
      
      
      int time = 0; 
      int cnt = 0; 
      
      
      while(true){
          
          if(cnt == N){
              break; 
          }
          
          int minTime = Integer.MAX_VALUE;
          int minPos = 0; 
          boolean isExist = false;
          
          for(int i=0; i<arr.size(); i++){
              if(check[i] == false && time >= arr.get(i).arrive){
                  if(minTime >= arr.get(i).time){
                      isExist = true;
                      minTime = Math.min(minTime, arr.get(i).time);
                      minPos = i; 
                      // System.out.println("minTime, minPos는?" + minTime+ " " + minPos);
                  }
              }
          }
          
          if(isExist == true){
              check[minPos] = true;
              time += minTime;
              cnt++;
          }else{
              time++;
          }
          
          
          // System.out.println("time은?" + time);
          
          
          
          
          
      }
      
      
      System.out.println(time);
      
      
      
      
    }
}

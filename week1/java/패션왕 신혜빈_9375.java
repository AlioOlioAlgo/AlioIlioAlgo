import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Main K = new Main();
      Scanner sc = new Scanner(System.in);
      
      
      int T = sc.nextInt();
      
      
      for(int i=1; i<=T; i++){
          
          int answer = 1;
          
          HashMap<String, Integer> map = new HashMap<>();
          int n = sc.nextInt();
          
          for(int j=1; j<=n; j++){
              
              String name = sc.next();
              String type = sc.next();
              
              if(map.containsKey(type)){
                  map.put(type, map.get(type)+1);
              }else{
                  map.put(type, 1);
              }
              
             
              
              
          }
          
          
              
              if(map.size() == 1){
                  
              for(String key: map.keySet()){
                  answer *= map.get(key); 
              }
              }else{
               
              for(String key: map.keySet()){
                  answer *= (map.get(key)+1); 
              }   
              answer -= 1;
              }
              
          
          System.out.println(answer); 
          
          
          
          
          
      }
      
      
      
      
      
      
    }
}

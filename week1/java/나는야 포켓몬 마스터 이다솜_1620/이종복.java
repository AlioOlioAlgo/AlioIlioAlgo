import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Scanner sc = new Scanner(System.in);
      
      int N = sc.nextInt();
      int M = sc.nextInt();
      
      HashMap<Integer, String> map1 = new HashMap<>(); 
      HashMap<String, Integer> map2 = new HashMap<>();
      
      String[] arr = new String[N+10];
      
      for(int i=1; i<=N; i++){
          String str = sc.next();
          map1.put(i, str);
          map2.put(str, i);
      }
      
      
      for(int i=1; i<=M; i++){
          
          String input = sc.next(); 
          if('A'<= input.charAt(0) && input.charAt(0) <= 'Z'){
              
              System.out.println(map2.get(input));
              
          }else{
              int num = Integer.parseInt(input);
              
              System.out.println(map1.get(num));
          }
          
          
      }
      
      
      
      
    }
}

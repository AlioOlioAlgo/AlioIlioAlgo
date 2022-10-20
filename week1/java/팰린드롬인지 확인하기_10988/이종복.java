import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      String str = sc.next();
      StringBuilder sb = new StringBuilder();
      
      for(int i=0; i<str.length(); i++){
          sb.append(str.charAt(i));
      }
      
      String reversed = sb.reverse().toString();
      
      if(str.equals(reversed)){
          System.out.println(1);
      }else{
          System.out.println(0); 
      }
      
      
      
      
      
      
    }
}

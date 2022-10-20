import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      int N = sc.nextInt();
      int[] arr = new int[30];
      
      for(int i=1; i<=N ;i++){
          String str = sc.next();
          int pos = str.charAt(0)-97;
          arr[pos] += 1;
      }
      
      boolean isExist = false;
      
      for(int i=0; i<26; i++){
          if(arr[i] >= 5){
              isExist = true;
              System.out.print((char)(i+97));
          }
      }
      
      if(isExist == false){
         System.out.println("PREDAJA");
      }
      
      
      
      
    }
}

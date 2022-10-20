import java.util.*; 

public class Main {
    
    public static int[] arr;
    
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      String str = sc.next();
      int[] arr = new int[30];
      
      for(int i=0; i<str.length(); i++){
          int pos = str.charAt(i)-97;
          arr[pos] += 1;
      }
      
      for(int i=0; i<26; i++){
          System.out.print(arr[i]+ " ");
      }
      
      
      
    }
}

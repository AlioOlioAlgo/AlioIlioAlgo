import java.util.*; 

public class Main {
    public static void main(String args[]) {
      Main T = new Main();
      Scanner sc = new Scanner(System.in);
      
      int N = sc.nextInt();
      
      
      String pattern = sc.next();
      int idx = pattern.indexOf("*");
      String strA = pattern.substring(0, idx);
      String strB = pattern.substring(idx+1);
      
      int lenA = strA.length();
      int lenB = strB.length(); 
      int len = pattern.length()-1;
      
      for(int i=1; i<=N; i++){
          String str = sc.next();
          int strLen = str.length(); 
         
          if(strLen < len){
              System.out.println("NE");
              continue; 
          }
         
          String a = str.substring(0, idx);
          String b = str.substring(strLen-lenB);
          
          if(strA.equals(a) && strB.equals(b)){
              System.out.println("DA");
              continue;
          }else{
              System.out.println("NE");
          }
         
         
       
          
          
      }
      
      
      
      
      
    }
}

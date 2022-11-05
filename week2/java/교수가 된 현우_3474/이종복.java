import java.util.*; 

public class Main {
    public static void main(String args[]) {
     
       Scanner sc = new Scanner(System.in);
       
       int T = sc.nextInt();
       
       for(int i=1; i<=T; i++){
           
           int N = sc.nextInt();
           int j= 1; 
           int answer = 0; 
           
           while(true){
               
               int num = (int)Math.pow(5, j++);
               
               if(N >= num){
                   answer += (N/num);
               }else{
                   break; 
               }
              
           }
           
           
           System.out.println(answer);
           
           
           
           
       }
       
       
     
     
    }
}

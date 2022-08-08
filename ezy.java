import java.util.Scanner;

class ezy{
  public static void main(String args[]){
     Scanner sc = new Scanner(System.in);
     int n, N;
     System.out.println("Enter the number: ");
     n = sc.nextInt();
     N = n;
     for(int i = n; i != 0; i--, n--){
         System.out.print("\n");
         for(int j = N - n; j !=0; j--){
             System.out.print("  ");
         }
         for(int j = i; j != 0; j--){
             System.out.print("* ");
         }
         for(int j = i - 1; j != 0; j--){
             System.out.print("* ");
         }
     }
     n = N;
     for(int i = 1; i <= n; i++){
         System.out.print("\n");
         for(int j = n - i; j != 0; j--){
             System.out.print("  ");
         }
         for(int j = i; j != 0; j--){
             System.out.print("* ");
         }
         for(int j = i - 1; j != 0; j--){
             System.out.print("* ");
         }
     }
  }
}
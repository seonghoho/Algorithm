import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();
        int n = sc.nextInt();
        System.out.println(str.repeat(n));
        // for문 사용
        // for (int i=0; i<n;i++) {
        // System.out.print(str);
        // }
        
    }
}
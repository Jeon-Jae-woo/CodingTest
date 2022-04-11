package intellijBaekjoon;


import java.util.Scanner;
import java.util.Stack;

//제로
//스택
public class B10773 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int k = sc.nextInt();
        Stack<Integer> stack = new Stack<Integer>();

        for(int i=0;i<k;i++){
            int n = sc.nextInt();
            if(n==0){
                stack.pop();
            }else{
                stack.push(n);
            }
        }

        int sum = 0;
        for(int n : stack){
            sum += n;
        }
        System.out.println(sum);
    }

}

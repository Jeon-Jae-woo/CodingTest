package intellijBaekjoon;

import java.util.Scanner;

public class B1817 {

    //짐 챙기는 숌
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int[] book = new int[n];
        for(int i=0;i<n;i++){
            book[i] = sc.nextInt();
        }

        int box = 0;
        int temp = 0;
        for(int i=0;i<n;i++){
            if(temp+book[i] < m){
                temp += book[i];
            }else if(temp+book[i] > m){
                box++;
                temp = temp-temp + book[i];
            }else{
                box++;
                temp = 0;
            }
        }
        if(temp !=0){
            box++;
        }
        System.out.println(box);
    }
}

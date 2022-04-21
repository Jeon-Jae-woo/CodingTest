package intellijBaekjoon;

import java.util.Scanner;

public class B1292 {

    //쉽게 푸는 문제
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();

        //1 ~ m 까지의 수열을 만든다
        int[] numbers = new int[m+1];
        //1 2 2 3 3 3 4 4 4 5 5 5 6 6 6 7 7 7
        int count = 1;
        for(int i=1;i<m+1;i++){
            for(int j=0;j<i;j++){
                if(count == m+1){
                    break;
                }
                numbers[count] = i;
                count++;
            }
        }

        int sum = 0;
        //n ~ m 까지의 합
        for(int i=n;i<=m;i++){
            sum += numbers[i];
        }

        System.out.println(sum);
    }
}

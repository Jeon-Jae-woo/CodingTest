package intellijBaekjoon;

import java.util.Scanner;

public class B14646 {

    public static void main(String[] args){
        //메뉴 N개
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int[] arr = new int[100001];

        int count = 0;
        int result = 0;
        for(int i=0;i<n*2;i++){
            int temp = sc.nextInt();
            arr[temp]++;
            if(arr[temp] == 1){
                count++;
            }else{
                count--;
            }

            if(count > result){
                result = count;
            }

        }

        System.out.println(result);

    }
}

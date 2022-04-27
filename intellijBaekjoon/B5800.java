package intellijBaekjoon;

import java.util.Arrays;
import java.util.Scanner;

public class B5800 {

    //성적 통계
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        StringBuilder sb = new StringBuilder();

        for(int i=0;i<n;i++){
            int gap = 0;
            int m = sc.nextInt();
            int[] score = new int[m];
            for(int j=0;j<m;j++){
                score[j] = sc.nextInt();
            }
            Arrays.sort(score);

            for(int x=m-1;x>0;x--){
                int temp = score[x] - score[x - 1];
                if(temp > gap){
                    gap = temp;
                }
            }

            sb.append("Class " + (i+1) + "\n" + "Max " + score[m-1] + ", Min " + score[0] +", Largest gap " + gap + "\n");

        }

        System.out.println(sb.toString());
    }
}

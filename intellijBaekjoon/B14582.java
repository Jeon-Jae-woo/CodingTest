package intellijBaekjoon;

import java.util.Scanner;

public class B14582 {

    public static void main(String[] args) {
        String result = "No";

        Scanner sc = new Scanner(System.in);
        int[] team1 = new int[9];
        int[] team2 = new int[9];

        for(int i=0;i<9;i++){
            team1[i] = sc.nextInt();
        }
        for(int i=0;i<9;i++){
            team2[i] = sc.nextInt();
        }

        int score1 = 0;
        int score2 = 0;
        for(int i=0;i<9;i++){
            score1 += team1[i];
            if(score1 > score2) {
                result = "Yes";
                break;
            }
            score2 += team2[i];
        }

        System.out.println(result);
    }
}

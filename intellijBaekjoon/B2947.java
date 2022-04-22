package intellijBaekjoon;

import java.util.Scanner;

public class B2947 {

    //나무 조각
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] number = new int[5];

        for(int i=0;i<5;i++){
            number[i] = sc.nextInt();
        }

        int index = 0;
        int temp;
        while (true){
            if(index == 4){
                index = 0;
            }
            if(number[index] > number[index+1]){
                temp = number[index];
                number[index] = number[index+1];
                number[index+1] = temp;
                System.out.println(number[0] + " " + number[1] + " " + number[2] + " " + number[3] + " " + number[4]);
                if(number[0]==1 && number[1]==2 && number[2]==3 && number[3]==4 && number[4]==5){
                    break;
                }
            }
            index++;
        }
    }
}

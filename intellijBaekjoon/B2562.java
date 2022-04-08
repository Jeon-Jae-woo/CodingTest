package intellijBaekjoon;

import java.util.Scanner;

//최대값
public class B2562 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int max = 0;
        int index = 1;
        int number = 0;
        for(int i=0;i<9;i++){
            number = sc.nextInt();
            if(number > max){
                max = number;
                index = i+1;
            }
        }

        System.out.println(max);
        System.out.println(index);
    }
}

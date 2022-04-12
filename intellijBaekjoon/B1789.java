package intellijBaekjoon;

import java.util.Scanner;

public class B1789 {
    //수들의 합
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        long s = sc.nextLong();

        long temp = 0;
        long count = 0;
        int i = 1;
        while(true){
            temp += i;
            i++;
            count++;
            if(temp > s){
                break;
            }

        }

        System.out.println(count-1);
    }
}

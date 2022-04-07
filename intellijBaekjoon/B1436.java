package intellijBaekjoon;

import java.util.Scanner;

public class B1436 {
    public static void main(String[] args) {
        //영화감독 숌
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int count = 0;
        int movie = 666;

        boolean result;
        while(true){
            result = sixCount(movie);
            if (result){
                count++;
            }
            if(n==count){
                break;
            }
            movie++;
        }
        System.out.println(movie);
    }

    //666
    public static boolean sixCount(int movie){
        String movieStr = String.valueOf(movie);
        if(movieStr.contains("666")){
            return true;
        }else{
            return false;
        }

    }
}

package intellijBaekjoon;

import java.util.Scanner;

public class B14912 {

    //숫자 빈도수
    public static void main(String[] args) {

        //2중 for문
        // 1 ~ 해당 숫자까지 반복
        // 문자열로 만들어 해당 문자의 길이만큼 반복하며 해당 숫자가 있는지 체크
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int digit = sc.nextInt();

        String num = "";
        int count = 0;
        for(int i=1;i<=n;i++){
            num = String.valueOf(i);
            for(int j=0;j<num.length();j++){
                if(digit == num.charAt(j)-'0'){
                    count++;
                }
            }
        }

        System.out.println(count);
    }
}

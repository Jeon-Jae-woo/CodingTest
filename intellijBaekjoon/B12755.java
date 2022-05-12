package intellijBaekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B12755 {
    //수면 장애
    public static void main(String[] args) throws IOException {
        //N번째 숫자가 무엇인가
        //1 ~ NUM 까지 반복
        //숫자가 증가할 때 마다 N을 - 시켜서 해당 숫자를 찾는 방식
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        int num = 0;
        String temp = "";
        String result = "";
        while (n > 0){
            num++;
            temp = String.valueOf(num);
            n -= temp.length();

            if(n <= 0){
                result = String.valueOf(temp.charAt(temp.length()-1 + n)); //해당 숫자에서 index를 찾아 출력
                break;
            }
        }
        System.out.println(result);
    }
}

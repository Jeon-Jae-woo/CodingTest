package intellijBaekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class B1475 {

    //방 번호
    public static void main(String[] args) throws IOException {
        //6, 9 는 같이 사용이 가능 --> 1팩에 6 9, 66, 99 사용 가능

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine().toString();

        int[] num = new int[10];
        for(int i=0;i<str.length();i++){
            int temp = str.charAt(i) - '0';
            if(temp==9){
                num[6] +=1;
            }else{
                num[temp] +=1;
            }
        }
        if(num[6]%2 == 1){
            num[6] = (num[6]/2)+1;
        }else{
            num[6] = num[6]/2;
        }

        Arrays.sort(num);
        System.out.println(num[9]);

    }

}

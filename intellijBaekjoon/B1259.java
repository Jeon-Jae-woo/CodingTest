package intellijBaekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B1259 {

    //팰린드롬수
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String number = "";
        boolean check;
        while(true){
            check = true;
            number = br.readLine();
            if(number.equals("0")){
                break;
            }

            for(int i=0;i<number.length()/2;i++){
                if(number.charAt(i) != number.charAt(number.length()-1-i)){
                    check = false;
                }
            }

            if(check){
                System.out.println("yes");
            }else{
                System.out.println("no");
            }



        }



    }
}

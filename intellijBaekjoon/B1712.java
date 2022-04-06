package intellijBaekjoon;

import java.util.Scanner;

public class B1712 {
    public static void main(String[] args) {
        //손익분기점

        //임대료, 재산세, 보험료, 급여 등 A만원의 고정 비용 -- 매년
        //재료비, 인건비 -- 노트북 1대
        // A=1000 , B=70 --> 1070만원  -> 10대 1700만원
        //노트북 가격 C만원 - 170

        Scanner sc = new Scanner(System.in);
        int A = sc.nextInt();
        int B = sc.nextInt();
        int C = sc.nextInt();

        //간단 수식
            // count 구하기 -> count = (A/(C-B))+1

        if(B >= C){
            System.out.println("-1");
        }else{
            System.out.println((A/(C-B))+1);
        }
    }
}

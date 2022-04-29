package intellijBaekjoon;

import java.util.HashMap;
import java.util.Scanner;

public class B14467 {

    //소가 길을 건너는 이유 1
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        //hashMap 사용 -> 없는 경우에 추가, 존재한다면 값이 같은지 아닌지 비교 -> 다르면 해당 값으로 갱신, count++
        HashMap<Integer, Integer> cows = new HashMap<Integer,Integer>();
        int n = sc.nextInt();

        int count = 0;
        for(int i=0;i<n;i++){
            int cNum = sc.nextInt();
            int move = sc.nextInt();

            if(!cows.containsKey(cNum)){
                cows.put(cNum, move);
            }
            //이동했다면
            else if(cows.get(cNum).intValue() != move){
                cows.put(cNum,move);
                count++;
            }

        }

        System.out.println(count);

    }
}

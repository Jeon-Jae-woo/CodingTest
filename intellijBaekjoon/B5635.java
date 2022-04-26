package intellijBaekjoon;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class B5635 {

    //생일
    public static void main(String[] args){
        //나이가 가장 많은 사람, 적은 사람

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[][] person = new String[n][4];
        for(int i=0;i<n;i++){
            person[i][0] = sc.next();
            person[i][1] = sc.next();
            person[i][2] = sc.next();
            person[i][3] = sc.next();
        }

        Arrays.sort(person, new Comparator<String[]>() {
            //return 양수면 교체
            @Override
            public int compare(String[] o1, String[] o2) {
                //오름차순
                //year, month, day 같은 경우에 처리할 조건
                if(o1[3].equals(o2[3])){
                    if(o1[2].equals(o2[2])){
                        return Integer.parseInt(o1[1]) - Integer.parseInt(o2[1]);
                    }else{
                        return Integer.parseInt(o1[2]) - Integer.parseInt(o2[2]);
                    }
                }else{
                    return Integer.parseInt(o1[3]) - Integer.parseInt(o2[3]);
                }
            }
        });

        //나이가 적은, 많은
        System.out.println(person[n-1][0]);
        System.out.println(person[0][0]);



    }
}

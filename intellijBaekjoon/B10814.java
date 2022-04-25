package intellijBaekjoon;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class B10814 {

    //나이순 정렬
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        String[][] users = new String[n][2];

        for(int i=0;i<n;i++){
            users[i][0] = sc.next();
            users[i][1] = sc.next();
        }

        //나이만 바꾸고 이름은 그대로
        Arrays.sort(users, new Comparator<String[]>() {
            @Override
            public int compare(String[] o1, String[] o2) {
                if(Integer.parseInt(o1[0]) > Integer.parseInt(o2[0])){
                    return 1;
                }else if(Integer.parseInt(o1[0]) < Integer.parseInt(o2[0])){
                    return -1;
                }else{
                    return 0;
                }
            }
        });

        for(int i=0;i<n;i++){
            System.out.println(users[i][0] + " " + users[i][1]);
        }

    }
}

package intellijBaekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;

public class B1764 {

    //듣보잡
    public static void main(String[] args) throws IOException {

        //듣도 보도 못한 명단을 구하는 프로그램
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        int m = Integer.parseInt(input[1]);

        HashSet<String> str = new HashSet<String>();
        ArrayList<String> result = new ArrayList<String>();
        for(int i=0;i<n;i++){
            str.add(br.readLine());
        }

        String temp = "";
        for(int i=0;i<m;i++){
            temp = br.readLine();
            if(str.contains(temp)){
                result.add(temp);
            }
        }
        Collections.sort(result);
        System.out.println(result.size());
        for(String st : result){
            System.out.println(st);
        }
    }
}

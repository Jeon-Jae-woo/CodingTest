package intellijBaekjoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashMap;

public class B1302 {
    //베스트셀러
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        HashMap<String, Integer> hs = new HashMap<>();
        for(int i=0;i<n;i++){
            String book = br.readLine();
            hs.put(book, hs.getOrDefault(book, 0) +1 );
        }

        int max = 0;
        for(String key : hs.keySet()){
            max = Math.max(max, hs.get(key));
        }

        ArrayList<String> al = new ArrayList<>(hs.keySet());
        Collections.sort(al);
        for(String key : al){
            if(max == hs.get(key)){
                System.out.println(key);
                break;
            }

        }

    }
}

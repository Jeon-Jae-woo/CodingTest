package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B10809 {
	//¾ËÆÄºª Ã£±â
	public static void main(String[] args) throws IOException {
		//baekjoon
		//1 0 -1 -1 2 -1 -1 -1 -1 4 3 -1 -1 7 5 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1 -1
		
		int[] count = {-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1};
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String str = br.readLine().toString();
		
		for(int i=0;i<str.length();i++) {
			char c = str.charAt(i);
			if(count[(int)c-97] == -1) {
				count[(int)c-97] = i;
			}	
		}
		
		for(int num : count) {
			System.out.print(num + " ");
		}
		
	}
	
	
	
	
}

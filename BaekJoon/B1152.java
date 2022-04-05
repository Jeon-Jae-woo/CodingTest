package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B1152 {
	//단어의 개수
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		String str = br.readLine();
		String[] result = str.trim().split(" ");
		
		int num;
		if(result[0].equals("")) {
			num = 0;
		}else {
			num = result.length;
		}
		
		System.out.println(num);
		
	}

}

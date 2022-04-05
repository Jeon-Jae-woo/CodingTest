package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B2675 {
	
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int r = Integer.parseInt(br.readLine());
		
		String inputStr;
		String str;
		int n;
		String[] result = new String[r];
		for(int x=0;x<r;x++) {
			inputStr = br.readLine();
			str = inputStr.split(" ")[1];
			n = Integer.parseInt(inputStr.split(" ")[0]);

			for(int i=0;i<str.length();i++) {
				char c = str.charAt(i);
				for(int j=0;j<n;j++) {
					if(result[x] == null) {
						result[x] = String.valueOf(c);
					}else {
						result[x] += c;
					}
				
				}
			}
		}

		for(int i=0;i<result.length;i++) {
			System.out.println(result[i]);
		}
		
	}
	
	
}

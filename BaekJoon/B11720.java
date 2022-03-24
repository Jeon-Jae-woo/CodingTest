package BaekJoon;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class B11720 {
	//������ ��
	public static void main(String[] args) throws IOException {
		
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		String[] number = br.readLine().split("");
		
		if(n != number.length) {
			return;
		}
		
		int sum = 0;
		for(int i=0;i<number.length;i++) {
			sum += Integer.parseInt(number[i]);
		}
		
		System.out.println(sum);
	}
}

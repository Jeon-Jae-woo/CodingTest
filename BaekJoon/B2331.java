package BaekJoon;

import java.util.Scanner;

public class B2331 {
	
	//분해합
	public static void main(String[] args) {
		//n까지 , 이중반복  

		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int result = 0;
		
		int temp;
		int sum;
		for(int i=1;i<=n;i++) {
			temp = i;
			sum = i;
			while(temp!=0) {
				sum += temp%10;
				temp /= 10;
			}
			if(sum==n) {
				result = i;
				break;
			}
		}
		
		System.out.println(result);
		
	}
}

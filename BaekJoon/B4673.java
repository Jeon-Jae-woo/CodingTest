package BaekJoon;

public class B4673 {

	public static void main(String[] args) {
		//셀프넘버
		
		//33 --> 33 + 3 + 3 --> 39
		//1부터 10000까지 생성자를 만들고 ? --> 10000까지 true 배열? --> 생성자의 위치를 true 변경
		boolean[] selfCheck = new boolean[10001];
		
		int sum;
		int temp;
		for(int i=1;i<100001;i++) {
			//계산값이 10000이 넘어간다면, 종료
			sum = i;
			temp = i;
			while(temp != 0) {
				sum += temp%10;
				temp = temp/10;
			}
			
			if(sum > 10000) {
				continue;
			}else {
				selfCheck[sum] = true;
			}
			
		}
		
		for(int i=1;i<selfCheck.length;i++) {
			if(!selfCheck[i]) {
				System.out.println(i);
			}
		}
		
	}

}

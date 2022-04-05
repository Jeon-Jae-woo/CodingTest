package BaekJoon;

public class B4673 {

	public static void main(String[] args) {
		//�����ѹ�
		
		//33 --> 33 + 3 + 3 --> 39
		//1���� 10000���� �����ڸ� ����� ? --> 10000���� true �迭? --> �������� ��ġ�� true ����
		boolean[] selfCheck = new boolean[10001];
		
		int sum;
		int temp;
		for(int i=1;i<100001;i++) {
			//��갪�� 10000�� �Ѿ�ٸ�, ����
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


public class Main {
	
	public static void main(String[] args) {
		
		/* ��Ʈ ����
		DartGame dt = new DartGame();
		String dartResult = "1D2S0T";
		int result = dt.solution(dartResult);
		*/
		
		/* ��Ŭ��
		NEmoney nm = new NEmoney();
		long result = nm.solution(3, 20, 4);
		*/
		
		/* �������
		SecretMap sm = new SecretMap();
		int[] arr1 = {9, 20, 28, 18, 11};
		int[] arr2 = {30, 1, 21, 17, 28};
		String[] result = sm.solution(5, arr1, arr2);
		
		for(String re : result) {
			System.out.println(re);
		}
		*/
		
		/*
		//�������� 1�� �Ǵ� �� ã��
		RestOne ro = new RestOne();
		int result = ro.solution(12);
		System.out.println(result);
		*/
		
		/*
		//�ּ����簢��
		MiniRectangle mr = new MiniRectangle();
		int[][] sizes = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
		int result = mr.solution(sizes);
		System.out.println(result);
		*/
		
		/*
		//�� �� �̾Ƽ� ���ϱ�
		TwoAdd ta = new TwoAdd();
		int[] numbers = {5,0,2,7};
		int[] result = ta.solution(numbers);
		*/
		
		//����
		Budget bg = new Budget();
		int[] d = {1,3,2,5,4};
		int budget = 9;
		System.out.println(bg.solution(d, budget));
		
		
		
		
		
	}
}

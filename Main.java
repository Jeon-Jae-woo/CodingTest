
public class Main {
	
	public static void main(String[] args) {
		
		/* 다트 게임
		DartGame dt = new DartGame();
		String dartResult = "1D2S0T";
		int result = dt.solution(dartResult);
		*/
		
		/* 위클리
		NEmoney nm = new NEmoney();
		long result = nm.solution(3, 20, 4);
		*/
		
		/* 비밀지도
		SecretMap sm = new SecretMap();
		int[] arr1 = {9, 20, 28, 18, 11};
		int[] arr2 = {30, 1, 21, 17, 28};
		String[] result = sm.solution(5, arr1, arr2);
		
		for(String re : result) {
			System.out.println(re);
		}
		*/
		
		/*
		//나머지가 1이 되는 수 찾기
		RestOne ro = new RestOne();
		int result = ro.solution(12);
		System.out.println(result);
		*/
		
		/*
		//최소직사각형
		MiniRectangle mr = new MiniRectangle();
		int[][] sizes = {{60, 50}, {30, 70}, {60, 30}, {80, 40}};
		int result = mr.solution(sizes);
		System.out.println(result);
		*/
		
		/*
		//두 개 뽑아서 더하기
		TwoAdd ta = new TwoAdd();
		int[] numbers = {5,0,2,7};
		int[] result = ta.solution(numbers);
		*/
		
		//예산
		Budget bg = new Budget();
		int[] d = {1,3,2,5,4};
		int budget = 9;
		System.out.println(bg.solution(d, budget));
		
		
		
		
		
	}
}

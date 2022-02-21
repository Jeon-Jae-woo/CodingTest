
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
		
		/*
		//예산
		Budget bg = new Budget();
		int[] d = {1,3,2,5,4};
		int budget = 9;
		System.out.println(bg.solution(d, budget));
		*/
		
		/*
		//삼진법
		ThreeM tm = new ThreeM();
		System.out.println(tm.solution(45));
		*/
		
		/*
		//완주하지 못한 선수
		FinishRace fr = new FinishRace();
		String[] par = {"mislav", "stanko", "mislav", "ana"};
		String[] com = {"mislav", "stanko", "ana"};
		System.out.println(fr.solution(par, com));
		*/
		
		/*
		//숫자의표현
		ExpNumber en = new ExpNumber();
		System.out.println(en.solution(15));
		*/
		
		/*
		//기능개발
		FunctionDev fd = new FunctionDev();
		int[] progresses = {95, 90, 99, 99, 80, 99};
		int[] speeds = {1, 1, 1, 1, 1, 1};
		System.out.println(fd.solution(progresses, speeds));
		*/
		
		/*
		//최대값과 최소값
		MaxAndMin mm = new MaxAndMin();
		System.out.println(mm.solution("-1 -1"));
		*/
		
		/*
		//피보나치
		Fibonacci fc = new Fibonacci();
		System.out.println(fc.solution(15));
		*/
		
		/*
		//JadenCase
		JadenCase jc = new JadenCase();
		System.out.println(jc.solution("3people unFollowed me"));
		*/
		
		/*
		//로또의 최고 순위와 최저 순위
		Lottos lt = new Lottos();
		int[] lottos = {45, 4, 35, 20, 3, 9};
		int[] win_nums = {20, 9, 3, 45, 4, 35};
		int[] result = lt.solution(lottos, win_nums);
		System.out.println(result[0] + " ," + result[1]);
		*/
		
		/*
		//숫자 문자열과 영단어
		NumberEng ne = new NumberEng();
		System.out.println(ne.solution("one4seveneight"));
		*/
		
		/*
		//음 양 더하기
		YinAndYang yy = new YinAndYang();
		int[] absolutes = {4,7,12};
		boolean[] signs = {true,false,true};
		System.out.println(yy.solution(absolutes, signs));
		*/
		
		/*
		//신규 아이디 추천
		NewId ni = new NewId();
		System.out.println(ni.solution("...!@BaT#*..y.abcdefghijklm"));
		*/
		
		/*
		//최솟값 만들기
		MinValue min = new MinValue();
		int[] A = {1,2};
		int[] B = {3,4};
		System.out.println(min.solution(A, B));
		*/
		
		//올바른괄호
		CorParen cp = new CorParen();
		System.out.println(cp.solution("(()("));
		
		
	}
}


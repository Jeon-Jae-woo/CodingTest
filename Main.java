
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
		
		/*
		//����
		Budget bg = new Budget();
		int[] d = {1,3,2,5,4};
		int budget = 9;
		System.out.println(bg.solution(d, budget));
		*/
		
		/*
		//������
		ThreeM tm = new ThreeM();
		System.out.println(tm.solution(45));
		*/
		
		/*
		//�������� ���� ����
		FinishRace fr = new FinishRace();
		String[] par = {"mislav", "stanko", "mislav", "ana"};
		String[] com = {"mislav", "stanko", "ana"};
		System.out.println(fr.solution(par, com));
		*/
		
		/*
		//������ǥ��
		ExpNumber en = new ExpNumber();
		System.out.println(en.solution(15));
		*/
		
		/*
		//��ɰ���
		FunctionDev fd = new FunctionDev();
		int[] progresses = {95, 90, 99, 99, 80, 99};
		int[] speeds = {1, 1, 1, 1, 1, 1};
		System.out.println(fd.solution(progresses, speeds));
		*/
		
		/*
		//�ִ밪�� �ּҰ�
		MaxAndMin mm = new MaxAndMin();
		System.out.println(mm.solution("-1 -1"));
		*/
		
		/*
		//�Ǻ���ġ
		Fibonacci fc = new Fibonacci();
		System.out.println(fc.solution(15));
		*/
		
		/*
		//JadenCase
		JadenCase jc = new JadenCase();
		System.out.println(jc.solution("3people unFollowed me"));
		*/
		
		/*
		//�ζ��� �ְ� ������ ���� ����
		Lottos lt = new Lottos();
		int[] lottos = {45, 4, 35, 20, 3, 9};
		int[] win_nums = {20, 9, 3, 45, 4, 35};
		int[] result = lt.solution(lottos, win_nums);
		System.out.println(result[0] + " ," + result[1]);
		*/
		
		/*
		//���� ���ڿ��� ���ܾ�
		NumberEng ne = new NumberEng();
		System.out.println(ne.solution("one4seveneight"));
		*/
		
		/*
		//�� �� ���ϱ�
		YinAndYang yy = new YinAndYang();
		int[] absolutes = {4,7,12};
		boolean[] signs = {true,false,true};
		System.out.println(yy.solution(absolutes, signs));
		*/
		
		/*
		//�ű� ���̵� ��õ
		NewId ni = new NewId();
		System.out.println(ni.solution("...!@BaT#*..y.abcdefghijklm"));
		*/
		
		/*
		//�ּڰ� �����
		MinValue min = new MinValue();
		int[] A = {1,2};
		int[] B = {3,4};
		System.out.println(min.solution(A, B));
		*/
		
		/*
		//�ùٸ���ȣ
		CorParen cp = new CorParen();
		System.out.println(cp.solution("(()("));
		*/
		
		/*
		//�ֽİ���
		StockPrice sp = new StockPrice();
		int[] prices = {1, 2, 3, 2, 3};
		int[] result = sp.solution(prices);
		for(int re : result) {
			System.out.println(re);
		}
		*/
		
		/*
		//����Ʈ 
		Lifeboat lb = new Lifeboat();
		int[] people = {30, 30,0,100,200};
		int limit = 100;
		System.out.println(lb.solution(people, limit));
		*/
		
		/*
		//���� ���� ���ϱ�
		AddNumbersEx ax = new AddNumbersEx();
		int[] numbers = {5,8,4,0,6,7,9};
		System.out.println(ax.solution(numbers));
		*/
		
		/*
		//����
		Inner in = new Inner();
		int[] a = {1,2,3,4};
		int[] b = {-3,-1,0,2};
		System.out.println(in.solution(a, b));
		*/
		
		/*
		//�Ҽ� �����
		MakeDecimal md = new MakeDecimal();
		int[] nums = {1,2,3};
		System.out.println(md.solution(nums));
		*/
		
		/*
		//H-Index
		HIndex h = new HIndex();
		int[] citations = {3, 0, 6, 1, 5};
		System.out.println(h.solution(citations));
		*/
		
		/*
		//ū �� �����
		MakeBigNumber mbn = new MakeBigNumber();
		String number = "4177252841";
		int k = 4;
		System.out.println(mbn.solution(number, k));
		*/
		
		/*
		//��ȭ��ȣ ���
		PhoneNumberList pnl = new PhoneNumberList();
		String[] phone_book = {"123","456","789"};
		System.out.println(pnl.solution(phone_book));
		*/

		/*
		//���� ������ �Ǻ� 
		SquareRoot sr = new SquareRoot();
		System.out.println(sr.solution(121));
		*/
		
		/*
		//����
		Camouflage cf = new Camouflage();
		String[][] clothes = {{"yellowhat", "headgear"}, 
				{"bluesunglasses", "eyewear"}, {"green_turban", "headgear"}};
		System.out.println(cf.solution(clothes));
		*/
		
		/*
		//�ٸ��� ������ Ʈ��
		TruckBridge tb = new TruckBridge();
		int bridge_length = 100;
		int weight = 100;
		int[] truck_weights = {10,10,10,10,10,10,10,10,10,10};
		System.out.println(tb.solution(bridge_length, weight, truck_weights));
		*/
		
		/*
		//�Ű� ��� �ޱ�
		ReportResult rr = new ReportResult();
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int k = 2;
		System.out.println(rr.solution(id_list, report, k));
		*/
		
		
		//Ű�е� ������
		Keypad kp = new Keypad();
		int[] numbers = {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2};
		String hand = "left";
		System.out.println(kp.solution(numbers, hand));
		
		
		
		
		
		
	}
}


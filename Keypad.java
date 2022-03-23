
public class Keypad {
	
	
	//Ű�е� ������
    public String solution(int[] numbers, String hand) {
        //1,4,7 -> Left
    	//3,6,8 -> Right
    	//2,5,8,0 -> Left OR Right
    	
    	// �ش� ��ǥ
    	/*
    	 * [ 1 2 3 ]	 [ 0,0  0,1  0,2]
    	 * [ 4 5 6 ]	 [ 1,0  1,1  1,2]
    	 * [ 7 8 9 ]	 [ 2,0  2,1  2,2]
    	 * [ * 0 # ]	 [ 3,0  3,1  3,2]
    	 *  ��������  10 , 11 , 12�� �ٲ� --> �Ÿ� ����� ���ؼ� �ӽ÷� ����     
    	 */ 
    	StringBuffer sb = new StringBuffer();
    	int[][] coodi = { {0,0},{0,1},{0,2},
    					  {1,0},{1,1},{1,2},
    					  {2,0},{2,1},{2,2},
    					  {3,0},{3,1},{3,2}
				  		};
    	int left = 10;
    	int right = 12;
    	
    	//�Ÿ��� -> ���밪 ( Ű�е� ��ġ - ���� ��ġ )  ( Ű�е� ��ġ - ������ ��ġ ) --> �� ���� ���� ����
    	for(int i=0;i<numbers.length;i++) {
    		if(numbers[i]==1 || numbers[i]==4 || numbers[i]==7) {
    			left = numbers[i];
    			sb.append("L");
    		}else if(numbers[i]==3 || numbers[i]==6 || numbers[i] == 9) {
    			right = numbers[i];
    			sb.append("R");
    		}else {
    			if(numbers[i]==0) {
    				numbers[i] = 11;
    			}
    			
    			//left �Ÿ� (���õ� ������ ��ǥ��, ���� ��ġ�� ��ǥ�� �Ÿ��� ����Ͽ� �Ÿ��� ���Ѵ�)
    			int left_dis = Math.abs(coodi[left-1][0]-coodi[numbers[i]-1][0])
    							+ Math.abs(coodi[left-1][1]-coodi[numbers[i]-1][1]);
    			//right �Ÿ�
    			int right_dis = Math.abs(coodi[right-1][0]-coodi[numbers[i]-1][0])
    							+ Math.abs(coodi[right-1][1]-coodi[numbers[i]-1][1]);
    			
    			//�� ����
    			if(left_dis < right_dis) {
    				left = numbers[i];
    				sb.append("L");
    				
    			}else if(left_dis > right_dis){
    				right = numbers[i];
    				sb.append("R");
    				
    			}else{
    				if(hand.equals("left")) {
    					left = numbers[i];
    					sb.append("L");
    				}else {
    					right = numbers[i];
    					sb.append("R");
    				}
    				
    			}

    		 }
    	}
    	
    	
    	String answer = sb.toString();
        return answer;
    }
	
    
    	
}

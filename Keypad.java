
public class Keypad {
	
	
	//키패드 누르기
    public String solution(int[] numbers, String hand) {
        //1,4,7 -> Left
    	//3,6,8 -> Right
    	//2,5,8,0 -> Left OR Right
    	
    	// 해당 좌표
    	/*
    	 * [ 1 2 3 ]	 [ 0,0  0,1  0,2]
    	 * [ 4 5 6 ]	 [ 1,0  1,1  1,2]
    	 * [ 7 8 9 ]	 [ 2,0  2,1  2,2]
    	 * [ * 0 # ]	 [ 3,0  3,1  3,2]
    	 *  마지막은  10 , 11 , 12로 바꿈 --> 거리 계산을 위해서 임시로 변경     
    	 */ 
    	StringBuffer sb = new StringBuffer();
    	int[][] coodi = { {0,0},{0,1},{0,2},
    					  {1,0},{1,1},{1,2},
    					  {2,0},{2,1},{2,2},
    					  {3,0},{3,1},{3,2}
				  		};
    	int left = 10;
    	int right = 12;
    	
    	//거리는 -> 절대값 ( 키패드 위치 - 왼쪽 위치 )  ( 키패드 위치 - 오른쪽 위치 ) --> 더 작은 값을 넣음
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
    			
    			//left 거리 (선택된 숫자의 좌표와, 손이 위치한 좌표의 거리를 계산하여 거리를 구한다)
    			int left_dis = Math.abs(coodi[left-1][0]-coodi[numbers[i]-1][0])
    							+ Math.abs(coodi[left-1][1]-coodi[numbers[i]-1][1]);
    			//right 거리
    			int right_dis = Math.abs(coodi[right-1][0]-coodi[numbers[i]-1][0])
    							+ Math.abs(coodi[right-1][1]-coodi[numbers[i]-1][1]);
    			
    			//손 선택
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

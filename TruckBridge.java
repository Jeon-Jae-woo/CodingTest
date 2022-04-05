import java.util.LinkedList;
import java.util.Queue;

public class TruckBridge {
	//다리를 지나는 트럭
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int t_index = 0;
        int b_weight = 0;
        // 다리 길이만큼 1초에 하나씩 이동 
        // queue 길이를 다리 길이만큼 ( 0으로 채움 )
        //while(){
        	// 적재량을 넘은 경우 -> queue에 0을 넣음
        	// 적재량을 넘지 않은 경우 -> 트럭을 넣음 ( t_index )
        	// b_weight에 값을 더하고 뻄
        //마지막 트럭이면서, 적재량을 넘지 않은 경우 ------> 반복문을 종료시키고 다리 길이만큼 시간을 더함  
        //		       적재량을 넘은 경우 -------------> 다리에 적재할 수 있을 때 까지 반복
        
        
        Queue<Integer> bridge = new LinkedList<Integer>();
        
        //길이만큼 0을 채움
        for(int i=0;i<bridge_length;i++) {
        	bridge.add(0);
        }
        
        int truck;
        while(true) {
        	b_weight -= bridge.poll(); // 현재 다리 가중치
        	truck = truck_weights[t_index];
        	
        	if(b_weight+truck <= weight) {
        		bridge.add(truck);
        		b_weight += truck;
        		
        		if(t_index == truck_weights.length-1) {
        			answer += bridge_length +1;
        			break;
        		}
        		t_index++;
        	}else{
        		bridge.add(0);
        	}
        	answer++; //시간 ++ 
        }
        return answer;
    }
}

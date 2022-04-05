import java.util.LinkedList;
import java.util.Queue;

public class TruckBridge {
	//�ٸ��� ������ Ʈ��
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int t_index = 0;
        int b_weight = 0;
        // �ٸ� ���̸�ŭ 1�ʿ� �ϳ��� �̵� 
        // queue ���̸� �ٸ� ���̸�ŭ ( 0���� ä�� )
        //while(){
        	// ���緮�� ���� ��� -> queue�� 0�� ����
        	// ���緮�� ���� ���� ��� -> Ʈ���� ���� ( t_index )
        	// b_weight�� ���� ���ϰ� �M
        //������ Ʈ���̸鼭, ���緮�� ���� ���� ��� ------> �ݺ����� �����Ű�� �ٸ� ���̸�ŭ �ð��� ����  
        //		       ���緮�� ���� ��� -------------> �ٸ��� ������ �� ���� �� ���� �ݺ�
        
        
        Queue<Integer> bridge = new LinkedList<Integer>();
        
        //���̸�ŭ 0�� ä��
        for(int i=0;i<bridge_length;i++) {
        	bridge.add(0);
        }
        
        int truck;
        while(true) {
        	b_weight -= bridge.poll(); // ���� �ٸ� ����ġ
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
        	answer++; //�ð� ++ 
        }
        return answer;
    }
}

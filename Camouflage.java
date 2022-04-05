import java.util.HashMap;
import java.util.Iterator;

public class Camouflage {
	//����
    public int solution(String[][] clothes) {
    	int answer = 1;
        //Map key -> ���� , value -> ����
        HashMap<String,Integer> cMap = new HashMap<String, Integer>();
        
        //�� ������ ���� count
        for(int i=0;i<clothes.length;i++) {
        	cMap.put(clothes[i][1], cMap.getOrDefault(clothes[i][1],0)+1);
        }
        
        Iterator<Integer> num = cMap.values().iterator(); 
        
        //����� �� ���
        while(num.hasNext()) {
        	answer = answer * (num.next().intValue()+1);
        }
        //�ƹ��͵� ���� ���� ��� ����
        answer -= 1;
        
        return answer;
    }
}

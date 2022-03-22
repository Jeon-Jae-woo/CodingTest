import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class ReportResult {
	
	//�Ű� ��� �ޱ�
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        /*  
         * reportProcess -> �Ű� ���� ��� - �Ű��� ��� ( key, value ) 
         * idMap -> �ش� ������ �Ű�� Ƚ���� k�� �̻��� ��쿡 �ش� ������ �Ű��� ������� count ���� ������Ų��
         * answer -> idMap�� i ��° �ִ� ���̵� ã�Ƽ� value�� answer�� �ִ´�
         */
        
        Map<String, Set<String>> reportProcess = new HashMap<String, Set<String>>();
        Map<String, Integer> idMap = new HashMap<String, Integer>();
        
        //�ʱ�ȭ
        for(String id : id_list) {
        	reportProcess.put(id, new HashSet<String>());
        	idMap.put(id, 0);
        }
        
        
        //�Ű� ����Ʈ
        String[] temp;
        for(int i=0;i<report.length;i++) {
        	temp = report[i].split(" ");
        	reportProcess.get(temp[1]).add(temp[0]);
        }
        
        
        //�Ű�� Ƚ���� k�� �̻��� ���... 
        for(String targets : reportProcess.keySet()) {
        	Set<String> target = reportProcess.get(targets);
        	if(target.size() >= k) {
        		//�ش� ������ �Ű��� ����� ã�� ����(count)�� ����
        		for(String reporter : target) {
        			idMap.put(reporter, idMap.getOrDefault(reporter, 0)+1);
        		}
        	}
        }
        
        //answer++
        for(int i=0;i<answer.length;i++) {
        	answer[i] = idMap.get(id_list[i]);
        }
        
        
        return answer;
    }
}

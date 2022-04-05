import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.Set;

public class ReportResult {
	
	//신고 결과 받기
    public int[] solution(String[] id_list, String[] report, int k) {
        int[] answer = new int[id_list.length];
        /*  
         * reportProcess -> 신고 당한 사람 - 신고한 사람 ( key, value ) 
         * idMap -> 해당 유저가 신고된 횟수가 k번 이상인 경우에 해당 유저를 신고한 사람들의 count 값을 증가시킨다
         * answer -> idMap의 i 번째 있는 아이디를 찾아서 value를 answer에 넣는다
         */
        
        Map<String, Set<String>> reportProcess = new HashMap<String, Set<String>>();
        Map<String, Integer> idMap = new HashMap<String, Integer>();
        
        //초기화
        for(String id : id_list) {
        	reportProcess.put(id, new HashSet<String>());
        	idMap.put(id, 0);
        }
        
        
        //신고 리스트
        String[] temp;
        for(int i=0;i<report.length;i++) {
        	temp = report[i].split(" ");
        	reportProcess.get(temp[1]).add(temp[0]);
        }
        
        
        //신고된 횟수가 k번 이상인 경우... 
        for(String targets : reportProcess.keySet()) {
        	Set<String> target = reportProcess.get(targets);
        	if(target.size() >= k) {
        		//해당 유저를 신고한 사람을 찾아 메일(count)를 증가
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

import java.util.HashMap;

public class FinishRace {

    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> hm = new HashMap<String, Integer>();
        
        for(String par : participant) {
        	hm.put(par, hm.getOrDefault(par,0)+1);
        }
        
        for(String com : completion) {
        	hm.put(com, hm.get(com).intValue()-1);
        }
        
        for(String h : hm.keySet()) {
        	if(hm.get(h) != 0) {
        		answer = h;
        	}
        }
        
        return answer;
        
    }
}

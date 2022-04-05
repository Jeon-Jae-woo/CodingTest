import java.util.HashMap;
import java.util.Iterator;

public class Camouflage {
	//위장
    public int solution(String[][] clothes) {
    	int answer = 1;
        //Map key -> 종류 , value -> 갯수
        HashMap<String,Integer> cMap = new HashMap<String, Integer>();
        
        //옷 종류와 갯수 count
        for(int i=0;i<clothes.length;i++) {
        	cMap.put(clothes[i][1], cMap.getOrDefault(clothes[i][1],0)+1);
        }
        
        Iterator<Integer> num = cMap.values().iterator(); 
        
        //경우의 수 계산
        while(num.hasNext()) {
        	answer = answer * (num.next().intValue()+1);
        }
        //아무것도 입지 않은 경우 제외
        answer -= 1;
        
        return answer;
    }
}

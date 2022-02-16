import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class FunctionDev {

    public int[] solution(int[] progresses, int[] speeds) {
        
        int day=0;
        Queue<Integer> qu = new LinkedList<Integer>();
        ArrayList<Integer> aList = new ArrayList<Integer>();
        
        for(int i=0;i<progresses.length;i++) {
        		day = (int)Math.ceil((double)(100-progresses[i])/speeds[i]);
        		if(day==0) {
        			qu.add(1);
        		}else {
        			qu.add(day);	
        		}
        		
        }
        
        int completeWork = 1;
        int prev = qu.poll();
        int current;
        while(!qu.isEmpty()) {
        	current = qu.poll();
        	if(prev >= current) {
        		completeWork++;
        	}else {
        		aList.add(completeWork);
        		completeWork = 1;
        		prev = current;
        	}
        }
        aList.add(completeWork);
        
        int[] answer = new int[aList.size()];
        for(int i=0;i<aList.size();i++) {
        	answer[i] = aList.get(i);
        }
        
        return answer;
    }

	
	//(100 - 작업진도)/speed = 일수 (나머지가 존재한다면 무조건 올림 )
	
		

}

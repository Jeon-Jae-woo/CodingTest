
public class MaxAndMin {
	
    public String solution(String s) {
        String[] strPar = s.split(" ");

        int max = Integer.parseInt(strPar[0]);
        int min = Integer.parseInt(strPar[0]);
        
        for(int i=1;i<strPar.length;i++) {
        	if(max < Integer.parseInt(strPar[i])) {
        		max = Integer.parseInt(strPar[i]);
        	}
        	if(min > Integer.parseInt(strPar[i])) {
        		min = Integer.parseInt(strPar[i]);
        	}
        	
        }
        return min + " " + max;
    }
    
}

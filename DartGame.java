public class DartGame {

    public int solution(String dartResult) {
        int answer = 0;
        
        //3��
        int[] score = new int[3];
        int scCount = -1;
        char[] strTemp = dartResult.toCharArray();
        //����|���ʽ�|�ɼ�
        
        for(int i=0;i<strTemp.length;i++) {
        	
        	if(strTemp[i] >= '0' && strTemp[i] <= '9') {
        		scCount++;
        		if(strTemp[i] == '1' && strTemp[i+1] == '0') {
        			score[scCount] = 10;
        			i++;
        		}else {
        			score[scCount] = Character.getNumericValue(strTemp[i]);
        		}
        	}
        	
        	if(strTemp[i] == 'D') {
        		score[scCount] *= score[scCount];
        		
        	}else if(strTemp[i] == 'T') {
        		score[scCount] *= score[scCount] * score[scCount];
        	}
        	
        	//�ɼ�
        	if(strTemp[i] == '*') {
        		if(scCount != 0) {
        			score[scCount] *=2;
        			score[scCount-1] *=2;
        		}else {
        			score[scCount] *=2;
        		}
        	}else if(strTemp[i] == '#') {
        		score[scCount] *=-1;
        	}
        }
        
        answer = score[0] + score[1] + score[2];
        return answer;
    }
}






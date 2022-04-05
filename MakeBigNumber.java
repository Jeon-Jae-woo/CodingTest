
public class MakeBigNumber {
    public String solution(String number, int k) {
        String answer = "";
        
        //index = 0
        //number의 길이 - k 만큼 반복 ( number - k 만큼의 길이를 확보 )
        	// index 부터 ~ k+i ? ? 
        
        //뒤에 k개의 수를 제거하고 남은 수 중에 큰 수를 찾음 -> 큰 수의 index를 기준으로 반복
        
        //4177252841 -> len 10 , for 6 -> 뒤에 5자리는 확보하고 앞에 자릿수 반복
        // i = 0 , k = 4 , j = 0,  < 4+0 -> 0 1 2 3 4
        // index - 큰 수 인덱스 다음을 기준으로 뒤에 자릿수를 찾아야 함
        StringBuffer sb = new StringBuffer();
        int index = 0;
        int max = 0;
        for(int i=0;i<number.length()-k;i++) {
        	max = 0;
        	for(int j=index;j<=k+i;j++) {
        		if(max < number.charAt(j)-'0') {
        			max = number.charAt(j)-'0';
        			index = j+1;
        		}
        	}
        	sb.append(max);
        }

        answer = sb.toString();

        return answer;
    }
}

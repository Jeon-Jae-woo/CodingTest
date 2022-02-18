
public class NumberEng {
    public int solution(String s) {
        String[] num = {"0","1","2","3","4","5","6","7","8","9"};
        String[] enNum = {"zero","one","two","three","four","five","six","seven","eight","nime"};
        
        for(int i=0;i<enNum.length;i++) {
        	s = s.replace(enNum[i], num[i]);
        }
        
        return Integer.parseInt(s);
    }
}


public class NEmoney {

    public long solution(int price, int money, int count) {
        
        //Ƚ�� �ݾ�
        long sumPrice = 0;
        for(int i=1;i<=count;i++) {
        	sumPrice += (price * i);
        }
        
        if(sumPrice <= money) {
        	return 0;
        }else {
        	return sumPrice - money;
        }
        
    }
}


public class MiniRectangle {
	
	//가로, 세로
	//비교 -> swap
	//최대값 , 최대값 찾기
	
    public int solution(int[][] sizes) {
        int max_width = 0;
        int max_heigth = 0;
        int temp;
        for(int i=0;i<sizes.length;i++) {
        	if(sizes[i][0] < sizes[i][1]) {
        		temp = sizes[i][0];
        		sizes[i][0] = sizes[i][1];
        		sizes[i][1] = temp;
        	}
        	
        	if(max_width < sizes[i][0]) {
        		max_width = sizes[i][0];
        	}
        	if(max_heigth < sizes[i][1]) {
        		max_heigth = sizes[i][1];
        	}
        	
        }
               
        return max_width * max_heigth;
    }
	
	
	
	
}

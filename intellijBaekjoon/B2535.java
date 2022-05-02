package intellijBaekjoon;

import java.util.*;

public class B2535 {

    //아시아 정보올림피아드
    public static void main(String[] args) {
        HashMap<Integer,Integer> country = new HashMap<Integer,Integer>();
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int[][] students = new int[n][3];
        for(int i=0;i<n;i++){
            students[i][0] = sc.nextInt();
            students[i][1] = sc.nextInt();
            students[i][2] = sc.nextInt();
        }

        Arrays.sort(students, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return o2[2] - o1[2];
            }
        });

        //3명만 넣으면 끝
        ArrayList<String> result = new ArrayList<>();
        for(int i=0;i<n;i++){
            if(result.size() == 3){
                break;
            }
            if(!country.containsKey(students[i][0])){
                result.add(students[i][0] + " " + students[i][1]);
            }else if(country.get(students[i][0]) < 2){
                result.add(students[i][0] + " " + students[i][1]);
            }
            country.put(students[i][0], country.getOrDefault(students[i][0], 0)+1);
        }

        for (String s : result){
            System.out.println(s);
        }

    }
}

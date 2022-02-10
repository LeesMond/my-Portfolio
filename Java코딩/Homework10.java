import java.util.HashMap;
import java.util.Iterator;
import java.util.Scanner;
import java.util.Set;

public class Homework10 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		Scanner v = new Scanner(System.in);
		Scanner r = new Scanner(System.in);
		
		HashMap<String, String> idx = new HashMap<String, String>();
		
		String n[];
		n = new String[5];
		String j[];
		j = new String[5];
		
		System.out.println("자바 점수관리 프로그램...");
		
		for(int i = 0; i<5; i++) {
			System.out.print(i+1 + "번째 학생이름을 입력하세요 : ");
			n[i] = s.nextLine();
			System.out.print(i+1 + "학생의 점수를 입력하세요 : ");
			j[i] = v.nextLine();
			idx.put(n[i], j[i]);
		}
		System.out.println(" ");
		System.out.println("-----학생목록-----");
		System.out.println(" ");
		
		Set<String> keys = idx.keySet();
		Iterator<String> it = keys.iterator();
		
		while(it.hasNext()) {
			String key = it.next();
			String value = idx.get(key);
			System.out.println("("+key+")");
		}
		while(true) {
			System.out.print("점수를 검색할 학생의 이름을 입력하세요 : ");
			String k =r.next();
			String g = idx.get(k);
			
			if(k.equals("끝"))
				break;
			if(g == null)System.out.println("없는 학생입니다");
			else System.out.println(g);
		}
		System.out.println("프로그램 종료...");
	}

}

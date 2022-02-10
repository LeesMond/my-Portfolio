import java.util.Scanner;

public class Homework1 {

	public static void main(String[] args) {
		String kor[] = {"학생", " 사랑", "자바", "행복한", "미래"};
		String eng[] = {"student", "love", "java", "happy", "future"};
		
		Scanner s = new Scanner(System.in);
		String w;
		
		while(true) {
			System.out.print("영어 단어를 입력하세요 : ");
			w = s.next();
			
			if(w.equals("exit")) {
				System.out.println("종료합니다...");
				break;
			}
			int i;
			for(i=0; i<eng.length; i++) {
				if(eng[i].equals(w)) {
					System.out.println(kor[i]);
					break;
				}
			}
			if(i == eng.length) {
				System.out.println("그런 영단어가 없습니다.");
			}
		}

	}

}

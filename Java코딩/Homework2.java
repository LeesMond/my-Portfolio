import java.util.Scanner;

public class Homework2 {

	public static void main(String[] args) {
		Scanner s = new Scanner(System.in);
		String str[] = {"가위", "바위", "보"};
		
		System.out.println("컴퓨터와 가위바위보 게임을 합니다");
		
		while(true) {
			System.out.println("가위 바위 보! >>");
			String what = s.next();
			
			int n = (int)(Math.random()*3);
			
			if(what.equals("그만"))
				break;
			
			if(str[n].equals("가위")) {
				if(what.equals("가위"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 가위 = 비겼습니다.");
				else if(what.equals("바위"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 가위 = 이겼습니다.");
				else if(what.equals("보"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 가위 = 졌습니다.");
			}
			if(str[n].equals("바위")) {
				if(what.equals("가위"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 바위 = 졌습니다.");
				else if(what.equals("바위"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 바위 = 비겼습니다.");
				else if(what.equals("보"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 바위 = 이겼습니다.");
			}
			if(str[n].equals("보")) {
				if(what.equals("가위"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 보 = 이겼습니다.");
				else if(what.equals("바위"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 보 = 졌습니다.");
				else if(what.equals("보"))
					System.out.println("사용자 : " + what + ", 컴퓨터 : 보 = 비겼습니다.");
			}
		}
		System.out.println("게임을 종료합니다...");
		s.close();
	}

}

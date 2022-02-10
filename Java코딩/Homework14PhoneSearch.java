import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Scanner;

public class Homework14PhoneSearch {
	private String fileName = "c:\\Temp\\phone.txt";
	private HashMap<String, String> phoneMap = new HashMap<String, String>();
	
	private void readPhoneFile() {
		File f = new File(fileName);
		try {
			Scanner sc = new Scanner(new FileReader(f));
			while(sc.hasNext()) {
				String name = sc.next();
				String tel = sc.next();
				phoneMap.put(name, tel);
			}
			
		}catch(IOException e) {
			e.printStackTrace();
		}
		int n = phoneMap.size();
		System.out.println("총 "+n+"개의 전화번호를 읽었습니다.");
	}
	
	private void processQuery() {
		Scanner sc = new Scanner(System.in);
		while(true) {
			System.out.print("이름 >> ");
			String name = sc.next();
			
			if(name.equals("그만")) {
				System.out.println("시스템을 종료합니다...");
				break;
			}
			String tel = phoneMap.get(name);
			if(tel == null)
				System.out.println(name+"이라는 사람은 등록되어 있지 않습니다...");
			else
				System.out.println(name + " 님의 전화번호는 " + tel + " 입니다.");
		}
		sc.close();
	}
	public void run() {
		readPhoneFile();
		processQuery();
	}
	public static void main(String[] args) {
	Homework14PhoneSearch ps = new Homework14PhoneSearch();
	ps.run();
	

	}

}

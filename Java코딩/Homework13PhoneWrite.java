import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class Homework13PhoneWrite {

	public static void main(String[] args) {
		FileWriter fw = null;
		File f = new File("c:\\Temp\\phone.txt");
		try {
			fw = new FileWriter(f);
			Scanner sc = new Scanner(System.in);
			System.out.println("전화번호 입력 프로그램입니다.");
			while(true) {
				System.out.print("이름 전화번호 입력 : ");
				String line = sc.nextLine();
				if(line.equals("그만"))
					break;
				fw.write(line+"\r\n");
			}
			System.out.println("\n"+f.getPath()+"에 저장하였습니다.");
			sc.close();
			fw.close();
		}catch(IOException e) {
			e.printStackTrace();
		}

	}

}

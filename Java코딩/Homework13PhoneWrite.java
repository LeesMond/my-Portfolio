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
			System.out.println("��ȭ��ȣ �Է� ���α׷��Դϴ�.");
			while(true) {
				System.out.print("�̸� ��ȭ��ȣ �Է� : ");
				String line = sc.nextLine();
				if(line.equals("�׸�"))
					break;
				fw.write(line+"\r\n");
			}
			System.out.println("\n"+f.getPath()+"�� �����Ͽ����ϴ�.");
			sc.close();
			fw.close();
		}catch(IOException e) {
			e.printStackTrace();
		}

	}

}

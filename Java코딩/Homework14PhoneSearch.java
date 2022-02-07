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
		System.out.println("�� "+n+"���� ��ȭ��ȣ�� �о����ϴ�.");
	}
	
	private void processQuery() {
		Scanner sc = new Scanner(System.in);
		while(true) {
			System.out.print("�̸� >> ");
			String name = sc.next();
			
			if(name.equals("�׸�")) {
				System.out.println("�ý����� �����մϴ�...");
				break;
			}
			String tel = phoneMap.get(name);
			if(tel == null)
				System.out.println(name+"�̶�� ����� ��ϵǾ� ���� �ʽ��ϴ�...");
			else
				System.out.println(name + " ���� ��ȭ��ȣ�� " + tel + " �Դϴ�.");
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

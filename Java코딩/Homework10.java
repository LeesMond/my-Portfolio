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
		
		System.out.println("�ڹ� �������� ���α׷�...");
		
		for(int i = 0; i<5; i++) {
			System.out.print(i+1 + "��° �л��̸��� �Է��ϼ��� : ");
			n[i] = s.nextLine();
			System.out.print(i+1 + "�л��� ������ �Է��ϼ��� : ");
			j[i] = v.nextLine();
			idx.put(n[i], j[i]);
		}
		System.out.println(" ");
		System.out.println("-----�л����-----");
		System.out.println(" ");
		
		Set<String> keys = idx.keySet();
		Iterator<String> it = keys.iterator();
		
		while(it.hasNext()) {
			String key = it.next();
			String value = idx.get(key);
			System.out.println("("+key+")");
		}
		while(true) {
			System.out.print("������ �˻��� �л��� �̸��� �Է��ϼ��� : ");
			String k =r.next();
			String g = idx.get(k);
			
			if(k.equals("��"))
				break;
			if(g == null)System.out.println("���� �л��Դϴ�");
			else System.out.println(g);
		}
		System.out.println("���α׷� ����...");
	}

}

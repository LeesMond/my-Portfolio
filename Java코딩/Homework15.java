import java.awt.*;
import java.awt.event.*;
import javax.swing.*;

public class Homework15 extends JFrame{
	private JLabel lbl = new JLabel("이종무");
	private JButton btn1;
	private JButton btn2;
	private JButton btn3;
	private JPanel p;

	public Homework15() {
		this.setTitle("마우스 어댑터 예제");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		
		c.addMouseListener(new MyMouseAdapter());
		
		lbl.setSize(50, 20);
		lbl.setLocation(50,50);
		c.add(lbl);
		p = new JPanel();
		
		btn1 = new JButton("노란색");
		p.add(btn1);
		btn2 = new JButton("핑크색");
		p.add(btn2);
		btn3 = new JButton("파란색");
		p.add(btn3);
		
		btn1.addActionListener(new Action1());
		btn2.addActionListener(new Action2());
		btn3.addActionListener(new Action3());
		
		this.add(p);
		this.setSize(500,400);
		this.setVisible(true);
	}
	
	class MyMouseAdapter extends MouseAdapter{
		public void mousePressd(MouseEvent e) {
			int x = e.getX();
			int y = e.getY();
			
			lbl.setLocation(x,y);
		}
	}
	class Action1 implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			if(e.getSource()==btn1) {
				p.setBackground(Color.yellow);
			}
		}	
	}
	class Action2 implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			if(e.getSource()==btn2) {
				p.setBackground(Color.pink);
			}
		}	
	}
	class Action3 implements ActionListener{
		@Override
		public void actionPerformed(ActionEvent e) {
			if(e.getSource()==btn3) {
				p.setBackground(Color.blue);
			}
		}	
	}
	public static void main(String[] args) {
		new Homework15();

	}

}

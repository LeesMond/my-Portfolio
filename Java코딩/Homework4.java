import java.awt.*;

import javax.swing.*;


public class Homework4 extends JFrame{
	public Homework4() {
		this.setTitle("Open Challenge 8");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		
		Container c = getContentPane();
		c.setLayout(new BorderLayout());
		c.add(new NorthPanel(), BorderLayout.NORTH);
		c.add(new CenterPanel(), BorderLayout.CENTER);
		
		setSize(300,200);
		setBackground(Color.LIGHT_GRAY);
		setVisible(true);
	}
	class NorthPanel extends JPanel{
		public NorthPanel() {
			add(new JButton("Open"));
			add(new JButton("Read"));
			add(new JButton("Close"));
			setBackground(Color.GRAY);
		}
	}
	class CenterPanel extends JPanel{
		public CenterPanel() {
			JLabel la = new JLabel("Hello Java!");
			add(la);
			la.setLayout(null);
			la.setSize(100,20);
			la.setLocation(100,50);
		}
	}

	public static void main(String[] args) {
		new Homework4();

	}

}

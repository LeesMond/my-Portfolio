import java.awt.*;

import javax.swing.*;

import java.awt.event.*;

public class Homework5 extends JFrame{
	private JButton [] btn = new JButton[16];
	private JTextField fTextfield = new JTextField(10);
	private JTextField sTextfield = new JTextField(10);
	private int [] changeOperand = new int[10];
	private int  firstOperand = 0;
	private int secondOperand = 0;
	private char operator;
	
	public Homework5() {
		this.setTitle("간단한 계산기");
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.setLocationRelativeTo(null);
		
		Container c = getContentPane();
		
		c.setLayout(new BorderLayout(3, 3));
		
		c.add(new FirstPanel(), BorderLayout.NORTH);
		c.add(new SecondPanel());
		
		this.setSize(400, 300);
		this.setVisible(true);
	}
	
	private class FirstPanel extends JPanel{
		public FirstPanel() {
			setBackground(Color.GRAY);
			setLayout(new FlowLayout());
			
			add(new JLabel("수식"));
			
			add(fTextfield);
			fTextfield.setEditable(false);		
			
			add(new JLabel("결과"));
			
			add(sTextfield);
			sTextfield.setEditable(false);		
		}
	}
	private class SecondPanel extends JPanel{
		public SecondPanel() {
			setLayout(new GridLayout(4, 4, 5, 5));
			
			for(int i = 0; i < 10; i++) {
				btn[i] = new JButton(Integer.toString(i));
				btn[i].addActionListener(new MyActionListener());
				add(btn[i]);
			}
			
			JButton btn_ce = new JButton("CE");
			JButton btn_calc = new JButton("계산");
			JButton btn_add = new JButton("+");
			JButton btn_sub = new JButton("-");
			JButton btn_mul = new JButton("x");
			JButton btn_div = new JButton("/");
			
			btn_ce.addActionListener(new MyActionListener());
			btn_calc.addActionListener(new MyActionListener());
			btn_add.addActionListener(new MyActionListener());
			btn_sub.addActionListener(new MyActionListener());
			btn_mul.addActionListener(new MyActionListener());
			btn_div.addActionListener(new MyActionListener());
			
			btn_add.setBackground(Color.CYAN);
			btn_sub.setBackground(Color.CYAN);
			btn_mul.setBackground(Color.CYAN);
			btn_div.setBackground(Color.CYAN);
			
			add(btn_ce);
			add(btn_calc);
			add(btn_add);
			add(btn_sub);
			add(btn_mul);
			add(btn_div);
		}
	}
	private class MyActionListener implements ActionListener {
		public void actionPerformed(ActionEvent e) {
			JButton btn = (JButton)e.getSource();
			
			int index = 0;
			
			if(btn.getText().equals("CE")) {		
				fTextfield.setText("");
				sTextfield.setText("");
				firstOperand = 0;
				secondOperand = 0;
			}
			else if(btn.getText().equals("계산")) {
				String str = fTextfield.getText();
				for(int i = fTextfield.getText().length()-1; i >= 0; i--) {
					char c = str.charAt(i);
					
					if(c == '+' | c == '-' | c == 'x' | c == '/') { 
						operator = c;
						break;
					}
					
					else {
						changeOperand[index] = Integer.parseInt(Character.toString(c));
						secondOperand += changeOperand[index]*(Math.pow(10, index));
						
						index++;
					}
				}
				
				switch(operator) {
				case '+':
					sTextfield.setText(Float.toString(firstOperand + secondOperand));
					break;
				case '-':
					sTextfield.setText(Float.toString(firstOperand - secondOperand));
					break;
				case 'x':
					sTextfield.setText(Float.toString(firstOperand * secondOperand));
					break;
				case '/':
					sTextfield.setText(Float.toString(firstOperand / secondOperand));
					break;
				}
			}
			
			else if(btn.getText().equals("+") | btn.getText().equals("-") | btn.getText().equals("x") | btn.getText().equals("/")) {
			
				firstOperand = Integer.parseInt(fTextfield.getText());
		
				switch(btn.getText()) {
				case "+":
					fTextfield.setText(fTextfield.getText() + "+");
					break;
				case "-":
					fTextfield.setText(fTextfield.getText() + "-");
					break;
				case "x":
					fTextfield.setText(fTextfield.getText() + "x");
					break;
				case "/":
					fTextfield.setText(fTextfield.getText() + "/");
					break;
				}
			}
			
			else {
				for(int i = 0; i < 10; i++) {
					if(btn.getText().equals(Integer.toString(i))) {
						fTextfield.setText(fTextfield.getText() + Integer.toString(i));
					}
				}
			}
		}
	}

	public static void main(String[] args) {
		new Homework5();

	}

}

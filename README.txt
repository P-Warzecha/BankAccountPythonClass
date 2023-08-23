This file was written to rehearse classes in Python. 

Thanks to the BankAccount class you can set up accounts with owners' names and their initial balance. After setting up an account you can deposit and withdraw money from it. If the amount you want to withdraw exceeds the amount on the account you get the refusal communicate.

Examples of uses:

	To set up an account:
		account1 = BankAccount('Peter',1000)
	
	To check whose account it is and what is the balance:
		print(account1)

	To check the owner:
		account1.owner

	To check the balance:
		account1.balanace

	To deposit an amount of money:
		account1.deposit(500)

	To withdraw an amount of money:
		account1.withdraw(750) 
	
	If you try to withdraw more money than there is on the account you get the refusal communicate:
		account1.withdraw(5000)

 


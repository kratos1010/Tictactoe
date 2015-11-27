from sys import stdout
def main():
	theBoard = [["0", "1", "2"],
				["3", "4", "5"],
				["6", "7", "8"]]



	for row in range(len(theBoard)):
		print("%s|%s|%s") %(theBoard[row][0], theBoard[row][1], theBoard[row][2])
		if row < len(theBoard) - 1:
			print "-" * 5
	
if __name__ == "__main__":
	main()

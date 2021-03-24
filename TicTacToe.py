class TicTacToe:
    def __init__(self):
        self.lst = [list("_" for i in range(3)) for j in range(3)]

    def output(self):
        print('---------')
        for i in range(3):
            print("| ", end="")
            for j in range(3):
                print(" " if self.lst[i][j] == '_' else self.lst[i][j], end=" ")
            print("|")
        print('---------')

    def checking(self):
        if all([self.lst[i] == ['X', 'X', 'X'] for i in range(3)]):
            return 'X'
        elif all([self.lst[i] == ['O', 'O', 'O'] for i in range(3)]):
            return 'O'
        if any([self.lst[0][i] == self.lst[1][i] == self.lst[2][i] == 'X' for i in range(3)]):
            return 'X'
        elif any([self.lst[0][i] == self.lst[1][i] == self.lst[2][i] == 'O' for i in range(3)]):
            return 'O'
        if self.lst[0][0] == self.lst[1][1] == self.lst[2][2] == 'X' or self.lst[0][2] == self.lst[1][1] == self.lst[2][
            0] == 'X':
            return 'X'
        elif self.lst[0][0] == self.lst[1][1] == self.lst[2][2] == 'O' or self.lst[0][2] == self.lst[1][1] == \
                self.lst[2][0] == 'O':
            return 'O'
        return 1

    def start(self):
        self.output()
        counter = 1
        while counter < 10:
            try:
                x, y = input("Enter the coordinates: ").split()
                x, y = int(x), int(y)
                if 0 < x < 4 and 0 < y < 4:
                    if self.lst[-y][x - 1] == 'X' or self.lst[-y][x - 1] == 'O':
                        print("This cell is occupied! Choose another one!")
                    else:
                        if counter % 2 == 1:
                            self.lst[-y][x - 1] = 'X'
                        else:
                            self.lst[-y][x - 1] = 'O'
                        self.output()
                        counter += 1
                else:
                    print("Coordinates should be from 1 to 3!")
            except ValueError or TypeError:
                print('You should enter numbers!')
            check = self.checking()
            if check == 'O':
                print("O wins")
                break
            elif check == 'X':
                print('X wins')
                break
        else:
            print('Draw')


game = TicTacToe().start()


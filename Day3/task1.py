class Number:
    def __init__(self, startX, endX, Y, value):
        self.startX = startX
        self.endX = endX
        self.Y = Y
        self.value = value

    def __repr__(self):
        return f"Number object {self.value} at [{self.startX}-{self.endX}, {self.Y}]"

class Symbol:
    def __init__(self, X, Y, value):
        self.X = X
        self.Y = Y
        self.value  = value

    def __repr__(self):
        return f"Symbol object {self.value} at [{self.X}, {self.Y}]"

class Parser:
    def __init__(self):
        self.numberList: list[Number] = []
        self.symbolList: list[Symbol] = []
        self.partNumberList: list[int] = []

    def parseLine(self, line, y_index):
        was_inside_number = False
        temp_number_value = ""
        x_start_index = 0
        for x_index, char in enumerate(line):
            # ignore dots
            if x_index+1 == len(line) and was_inside_number and char.isdigit(): # in case of last line, save the number
                temp_number_value += char
                self.numberList.append(Number(x_start_index, x_index-1,
                                               y_index, temp_number_value))
                break
            if char in "!&+=/#@*%€$":
                self.symbolList.append(Symbol(x_index, y_index, char))
            if was_inside_number and not char.isdigit(): # number ended
                was_inside_number = False
                self.numberList.append(Number(x_start_index, x_index-1,
                                               y_index, temp_number_value))
                # cleanup temp vars
                temp_number_value = ""
                x_start_index = 0    
            elif not was_inside_number and char.isdigit(): # number started
                was_inside_number = True
                temp_number_value += char
                x_start_index = x_index

            elif was_inside_number and char.isdigit(): # number continues
                temp_number_value += char

                    
    def checkNumberNeighbors(self):
        for number in self.numberList:
            for symbol in self.symbolList:
                if ((symbol.Y - 1 <= number.Y and number.Y <= symbol.Y + 1) and
                    ((symbol.X - 1 <= number.startX and number.startX <= symbol.X + 1) or
                    (symbol.X - 1 <= number.endX and number.endX <= symbol.X + 1))):
                        self.partNumberList.append(int(number.value))
                        break # dont continue with this number to avoid duplicate entries
                
# can be optimized by parsing only three lines at a time with
# one line lookbehind and one line lookahead

parser = Parser()
# look at three lines at a time
with open("input.txt", "r") as f:
    for index, line in enumerate(f.readlines()):
        parser.parseLine(line, index)
    parser.checkNumberNeighbors()
    print(sum(parser.partNumberList))
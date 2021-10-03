#Shadowfray
#Arithmetic formatter - freecodecamp.org

'''
This program takes two numbers, -9999 <= n <= 9999, and
adds or subtracts them in the following display:

ex: 303 + 27 =

  303
+  27
-----


if answers = True then it will also display the answer.
This code can take up to 5 problems at once. The questions
should be input as a list of strings with spaces between
the operator and the numers.

ex: ["303 + 27"] is a valid input
    ["5+3"] is NOT
'''

def arithmetic_arranger(problemList,answers=False):
    #takes a list of arithmetic questions inside a list
    #if answers = True then we also print the answers

    #stores the values for the final print out
    problemPieces = [ [], #the firt numbers(s) / row
                      [], #the second number(s) / row
                      [], #the symbol for addition / subtraction
                      []  #the answer(s)
                      ]

    if len(problemList) > 5:
        return 'Error: Too many problems.'

    #handles each of the problems given
    for prob in problemList:
        splitProb = prob.split()
        
        #ensures we only have numbers in the math
        try:
            num1 = int(splitProb[0])
            num2 = int(splitProb[2])
        except ValueError:
            return 'Error: Numbers must only contain digits.'
        
        #ensures our numers are 4 digits or less
        if num1 > 10000 or num2 > 10000 or num1 < 0 or num2 < 0:
            return "Error: Numbers cannot be more than four digits."
        
        #checks to see if the arithmetic is - or +, as well as what operation to do
        if splitProb[1] == '-':
            num2 = num2 * -1
            problemPieces[2].append('-')
        elif splitProb[1] == '+':
            problemPieces[2].append('+')
        else:
            return "Error: Operator must be '+' or '-'."

        #Adds values to output list now that we know we are error free
        problemPieces[0].append(num1)
        problemPieces[1].append(num2)

        #does the math
        answer = num1 + num2
        problemPieces[3].append(answer)        

    #the strings we will assemble to make our final output
    row1, row2, row3, row4 = '', '' , '', ''
    
    #the first row
    for j in problemPieces[0]:
        length = 5 - len(str(j))
        piece = (' '*length + str(j) + '    ')
        row1 += piece
    row1 += '\n'

    #the second row
    for k in range(len(problemPieces[1])):
        length = 4 - len(str(problemPieces[1][k]))
        piece = (problemPieces[2][k] + ' '*length + str(problemPieces[1][k]) + '    ')
        row2  += piece
    row2 += '\n'
        
    #the horizontal lines
    row3 = ('-----    ' * (len(problemList)-1))
    row3 += '-----'
    row3 += '\n'
    
    #prints answers potentially
    if answers == True:
        for i in problemPieces[3]:
            length = 5 - len(str(i))
            piece = (' '*length + str(i) + '    ')
            row4 += piece

    final_arranged = row1 + row2 + row3 + row4
    return final_arranged

x = arithmetic_arranger(['3801 - 2', '123 + 49'])
print(repr(x))


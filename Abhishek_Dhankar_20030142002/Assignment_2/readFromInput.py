
def readFile(fileName):
  with open(fileName, 'r') as inputFile:
    file_data = inputFile.read() #file_data is string object
    return file_data

def createMatrix(file_data):
  file_data = file_data+'\n' #adding new line character to mark end of matrix

  #initializing the matrix
  matrix = []

  number = ''

  #initialize row
  row = []

  try:
    if int(file_data) or int(file_data) == 0:
      row.append(int(file_data))
      matrix.append(row)
      return matrix

  except ValueError:
    for item in file_data:
      try:
        if item != ',' and item != '\n':
          number = number + item
        elif item == ',':
          row.append(int(number))
          number = ''
        elif item == '\n':
          if row == []:
            continue
          else:
            row.append(int(number))
            number = ''
            matrix.append(row)
            row = []
      except ValueError:
        return "Matrix in 'input.txt' is not in proper format. Please! check."     
    return(matrix)
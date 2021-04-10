def isIdentityMatrix(matrix): 
          
    flag = True;  
       
    #Calculating number of rows 
    rows = len(matrix);  

    #Calculating number of columns
    cols = len(matrix[0]);  
        
    #Checks elements of the matrix
    for i in range(0, rows):  
        for j in range(0, cols):
            #check if the diagonal elements are equal to 1  
            if(i == j and matrix[i][j] != 1):  
                flag = False;  
                break;  
            
            #check if elements other than diagonal elements are equal to 0       
            if(i != j and matrix[i][j] != 0):  
                flag = False;  
                break;  
    return flag
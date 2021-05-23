import numpy as np
from UnitTestCases import EigenValueCalc
from UnitTestCases import EigenVectorCalc
from UnitTestCases import EigenVectorCalc2
from UnitTestCases import ReadFile, CreateMatrix

Matrix = CreateMatrix(ReadFile("Input.txt"))
if not isinstance(Matrix, list):
	StringOutput = Matrix
	StringOutputLength = len(StringOutput)
	print("\n", "-"*StringOutputLength)
	print(f"{Matrix}")
	print("-"*StringOutputLength,"\n")
else:
	print(f"\nFactors are represented as: A = U.Sigma.V(T)\n")
	# U.Sigma.V(T)
	Matrix = np.array(Matrix)
	print(f"Our Matrix:\n{Matrix}\n")

#====================================== Calculate V ========================================
#==================================== Calculate A(T).A =====================================
	VMatrix = np.dot(Matrix.T, Matrix)
	VEigenValues = EigenValueCalc(VMatrix)
#================================ Calculate Eigen Vectors ==================================
	VEigenVectors = []
	try:
		for ll in VEigenValues:
			VEigenVectors.append(EigenVectorCalc(np.dot(Matrix.T, Matrix),ll).tolist())
	except:
		for l in VEigenValues:
			VEigenVectors.append(EigenVectorCalc2(np.dot(Matrix.T, Matrix),l).tolist())

#======================================= Calculate U ========================================
#===================================== Aalculate A.A(T) =====================================
	UMatrix = np.dot(Matrix,Matrix.T)
	UEigenValues = EigenValueCalc(UMatrix)


#================================== Calculate Eigen Vectors =================================
	UEigenVectors = []
	try:
		for ll in UEigenValues:
			UEigenVectors.append(EigenVectorCalc(np.dot(Matrix, Matrix.T),ll).tolist())
	except:
		for l in UEigenValues:
			UEigenVectors.append(EigenVectorCalc2(np.dot(Matrix, Matrix.T),l).tolist())


#================================= Calculating Sigma Matrix ==================================
	Sigma = np.diag(np.array(VEigenValues),k=0)
	Sigma = np.sqrt(Sigma)

	print(f"U Matrix is:\n{np.array(UEigenVectors).T}\n")
	print(f"Sigma Matrix is:\n{Sigma}\n")
	print(f"V Matrix is:\n{np.array(VEigenVectors).T}\n")
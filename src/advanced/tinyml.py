
## MicroPython implementation of Multi-layer Perceptron (MLP)
## Artificial Neural network-Fully connected Dense layer
## Trained hyperparameters are collected from tensorflow-keras
# and fed to our Neural network for testing and prediction
## Version:1.0.1
## Date 14/06/2022

def zeros1d(x):  # 1d zero matrix
    z = [0 for i in range(len(x))]
    return z


def add1d(x, y):
    if len(x) != len(y):
        print("Dimension mismatch")
        exit()
    else:
        z = [x[i] + y[i] for i in range(len(x))]
        return z


def relu(x):  # Relu activation function
    # print(x)
    y = []
    for i in range(len(x)):
        if x[i] >= 0:
            y.append(x[i])
        else:
            y.append(0)

    # print(y)
    return y


##Sigmoid function
def sigmoid(x):
    import math
    z = [1 / (1 + math.exp(-x[kk])) for kk in range(len(x))]
    return z


def dot(A, B):
    """
    Returns the product of the matrix A * B where A is m by n and B is n by 1 matrix
        :param A: The first matrix - ORDER MATTERS!
        :param B: The second matrix
        :return: The product of the two matrices
    """
    # Section 1: Ensure A & B dimensions are correct for multiplication
    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = 1
    if colsA != rowsB:
        raise ArithmeticError('Number of A columns must equal number of B rows.')

    # Section 2: Store matrix multiplication in a new matrix
    C = zeros(rowsA, colsB)
    for i in range(rowsA):
        total = 0
        for ii in range(colsA):
            total += A[i][ii] * B[ii]
            C[i] = total

    return C


def zeros(rows, cols):
    """
    Creates a matrix filled with zeros.
        :param rows: the number of rows the matrix should have
        :param cols: the number of columns the matrix should have
        :return: list of lists that form the matrix
    """
    M = []
    while len(M) < rows:
        M.append([])
        while len(M[-1]) < cols:
            M[-1].append(0.0)

    return M


def transpose(M):
    """
    Returns a transpose of a matrix.
        :param M: The matrix to be transposed
        :return: The transpose of the given matrix
    """
    # Section 1: if a 1D array, convert to a 2D array = matrix
    if not isinstance(M[0], list):
        M = [M]

    # Section 2: Get dimensions
    rows = len(M)
    cols = len(M[0])

    # Section 3: MT is zeros matrix with transposed dimensions
    MT = zeros(cols, rows)

    # Section 4: Copy values from M to it's transpose MT
    for i in range(rows):
        for j in range(cols):
            MT[j][i] = M[i][j]

    return MT


##Sigmoid function

def neuron(x, w, b, activation):  # perform operation on a single neuron and return a 1d array

    tmp = zeros1d(x[0])

    for i in range(len(x)):
        tmp = add1d(tmp, [(float(w[i]) * float(x[i][j])) for j in range(len(x[0]))])

    if activation == "sigmoid":
        yp = sigmoid([tmp[i] + b for i in range(len(tmp))])
    elif activation == "relu":
        yp = relu([tmp[i] + b for i in range(len(tmp))])
    else:
        print("Invalid activation function--->")

    return yp


def dense(nunit, x, w, b, activation):  # define a single dense layer followed by activation
    res = []
    for i in range(nunit):
        z = neuron(x, w[i], b[i], activation)
        # print(z)
        res.append(z)
    return res

def print_matrix(M, decimals=3):
    """
    Print a matrix one row at a time
        :param M: The matrix to be printed
    """
    for row in M:
        print([round(x, decimals) + 0 for x in row])

def classification_report(ytrue, ypred):  # print prediction results in terms of metrics and confusion matrix
    tmp = 0
    TP = 0
    TN = 0
    FP = 0
    FN = 0
    for i in range(len(ytrue)):
        if ytrue[i] == ypred[i]:  # For accuracy calculation
            tmp += 1
        ##True positive and negative count
        if ytrue[i] == 1 and ypred[i] == 1:  # find true positive
            TP += 1
        if ytrue[i] == 0 and ypred[i] == 0:  # find true negative
            TN += 1
        if ytrue[i] == 0 and ypred[i] == 1:  # find false positive
            FP += 1
        if ytrue[i] == 1 and ypred[i] == 0:  # find false negative
            FN += 1
    accuracy = tmp / len(ytrue)
    conf_matrix = [[TN, FP], [FN, TP]]
    #print(TP, FP, FN, TN)

    print("Accuracy: " + str(accuracy))
    print("Confusion Matrix:")
    print(print_matrix(conf_matrix))
## Test function

# Build a Dense layer
# Structure: Input layer 4 neuron with 8 feature, Relu activation
# 1st hidden layer: 2 neuron with 4 input each, Relu activation
# output layer: 1 neuron with 2 input, Sigmoid activation
w1 = [[-0.0921422 , -0.02542371,  0.30698848, -0.25456974],
       [-0.50550294, -1.0066229 ,  0.9122949 , -0.26058084],
       [ 0.51205075,  0.43376786, -0.07458406, -0.37492675],
       [-0.6911025 ,  0.6660218 , -0.0747927 , -0.18643615],
       [ 0.30719382,  0.519332  ,  0.52301043, -0.15813994],
       [-0.1978444 , -0.0485612 ,  0.60282296, -1.2380371 ],
       [-0.260084  , -0.00271817,  0.7422599 ,  0.00921784],
       [-1.2720652 , -0.08174618, -0.15088758,  0.68464226]]
b1 = [ 0.03986932,  0.7178214 ,  0.10937195, -0.07356258]
w2 = [[ 1.000371  ,  1.5499793 ],
       [-2.840075  ,  0.2513094 ],
       [ 0.07223273, -0.5448719 ],
       [ 0.25136417,  0.60296375]]
b2 = [0.4844855 , 0.61291546]
w3 = [[1.1305474],[-1.3455248]]
b3 = [0.91277504]
#Transpose all weight matrix
w1 = transpose(w1)
w2 = transpose(w2)
w3 = transpose(w3)
# Test data
Xtest = [[-8.44885053e-01, 2.44447821e+00, 3.56431752e-01,
          1.40909441e+00, -6.92890572e-01, 1.38436175e+00,
          2.78492300e+00, -9.56461683e-01],
         [-5.47918591e-01, -4.34859164e-01, 2.53036252e-01,
          5.93629620e-01, 1.75399020e-01, 2.04012771e-01,
          -2.04994488e-01, -8.71373930e-01],
         [4.60143347e-02, -1.40507067e+00, -3.67336746e-01,
          -1.28821221e+00, -6.92890572e-01, 2.54780469e-01,
          -2.44256030e-01, -7.01198424e-01],
         [3.42980797e-01, 1.41167241e+00, 1.49640753e-01,
          -9.63790522e-02, 8.26616214e-01, -7.85957342e-01,
          3.47687230e-01, 1.51108316e+00],
         [-1.14185152e+00, -3.09670582e-01, -2.12243497e-01,
          -1.28821221e+00, -6.92890572e-01, -9.38260437e-01,
          5.68155894e-01, -1.90671905e-01],
         [-8.44885053e-01, -1.24858494e+00, 1.49640753e-01,
          -1.59107113e-01, -3.45574735e-01, -6.84421946e-01,
          -5.70428848e-01, -7.86286177e-01],
         [1.53084665e+00, 9.73512376e-01, 4.59827252e-01,
          8.44541864e-01, 7.91884630e-01, 2.80164319e-01,
          1.27184355e+00, -2.04963989e-02],
         [-2.50952128e-01, 1.72464386e+00, 8.73409251e-01,
          4.05445437e-01, 6.61641192e-01, 1.65936998e-01,
          2.06009452e+00, 1.59617091e+00],
         [-5.47918591e-01, 1.91083743e-01, -5.74127746e-01,
          2.17261253e-01, 1.69490581e+00, -5.44810776e-01,
          3.40706745e+00, -7.01198424e-01],
         [6.39947260e-01, -5.60047745e-01, 1.49640753e-01,
          7.19085742e-01, 9.56859653e-01, 7.24381677e-01,
          -4.46603982e-01, 1.85143417e+00],
         [-2.50952128e-01, 1.16129525e+00, 3.56431752e-01,
          9.69997986e-01, 1.43441893e+00, -4.98257194e-02,
          1.14499856e+00, -4.45935165e-01],
         [3.42980797e-01, 2.06891246e+00, 3.56431752e-01,
          4.05445437e-01, 1.10446888e+00, 1.47320522e+00,
          1.69768028e+00, 1.68125866e+00],
         [3.42980797e-01, -2.15779146e-01, 2.53036252e-01,
          -1.28821221e+00, -6.92890572e-01, -9.00184663e-01,
          8.21845863e-01, 2.02160968e+00],
         [-5.47918591e-01, -1.21728780e+00, -8.84314245e-01,
          9.18051311e-02, 3.05642459e-01, -4.43275380e-01,
          3.70605920e+00, -7.01198424e-01],
         [1.23388019e+00, -1.74933927e+00, 1.49640753e-01,
          1.54533192e-01, -6.92890572e-01, 9.41978774e-04,
          3.86948773e-01, 7.45293379e-01],
         [-1.14185152e+00, -4.03562018e-01, -5.71502470e-02,
          -3.36509911e-02, -6.92890572e-01, -5.95578474e-01,
          9.51710966e-01, -1.05584152e-01],
         [1.23388019e+00, 1.81853530e+00, 1.49640753e-01,
          1.34636635e+00, 4.35885898e-01, 8.97854505e-02,
          7.46342896e-01, 2.34766861e-01],
         [-8.44885053e-01, -1.49896210e+00, -9.87709745e-01,
          -6.60931602e-01, -6.92890572e-01, -1.14133123e+00,
          -6.76133001e-01, -1.04154944e+00],
         [4.60143347e-02, 3.47569469e-01, 8.73409251e-01,
          6.56357681e-01, -6.92890572e-01, -5.06735003e-01,
          -1.59692708e-01, 2.53213620e+00],
         [3.42980797e-01, -6.85236326e-01, -7.80918745e-01,
          4.68173498e-01, 2.77897893e-02, 2.54780469e-01,
          8.19167867e-02, -2.75759658e-01],
         [4.60143347e-02, 7.23135213e-01, 6.66618252e-01,
          7.19085742e-01, -6.92890572e-01, 8.25917074e-01,
          2.48023314e-01, 3.19854614e-01],
         [-5.47918591e-01, -9.05905652e-02, 5.63222752e-01,
          -1.28821221e+00, -6.92890572e-01, 1.38436175e+00,
          6.67819810e-01, -1.04154944e+00],
         [-5.47918591e-01, -1.06080207e+00, -3.57259724e+00,
          1.54533192e-01, -6.92890572e-01, -3.92507682e-01,
          9.09429304e-01, -7.01198424e-01],
         [-2.50952128e-01, -1.87452785e+00, 6.66618252e-01,
          4.68173498e-01, -6.92890572e-01, 3.05548168e-01,
          -6.91233595e-01, 1.08564439e+00],
         [-8.44885053e-01, -7.47830617e-01, -1.60545747e-01,
          -3.47291297e-01, 5.22714857e-01, -1.11594738e+00,
          4.56753625e-02, -9.56461683e-01],
         [-8.44885053e-01, 9.71923068e-02, -4.70732246e-01,
          7.19085742e-01, -6.92890572e-01, 4.83235111e-01,
          1.27218567e-01, -1.04154944e+00],
         [-1.14185152e+00, -5.28750600e-01, 3.56431752e-01,
          -1.28821221e+00, -6.92890572e-01, -1.72515976e+00,
          3.32586637e-01, -5.31022918e-01],
         [2.71871250e+00, 1.00480952e+00, 9.76804751e-01,
          1.03272605e+00, 5.22714857e-01, 1.09244749e+00,
          2.12049689e+00, 4.90030120e-01],
         [-5.47918591e-01, -2.78373437e-01, -1.60545747e-01,
          9.18051311e-02, -6.92890572e-01, -8.87492739e-01,
          -4.97945999e-01, -7.86286177e-01],
         [3.42980797e-01, -3.40967728e-01, -5.71502470e-02,
          -1.28821221e+00, -6.92890572e-01, -7.60573493e-01,
          -5.43247780e-01, -2.75759658e-01],
         [9.36913723e-01, 4.72758051e-01, 2.53036252e-01,
          3.42717375e-01, 4.79300377e-01, -7.60573493e-01,
          5.28894351e-01, 1.51108316e+00],
         [-1.14185152e+00, -5.91344890e-01, -2.63941247e-01,
          1.59727860e+00, -1.56246903e-02, 1.09244749e+00,
          7.28564306e-02, -1.04154944e+00],
         [-1.14185152e+00, -5.91344890e-01, 8.73409251e-01,
          -2.21835174e-01, 2.18813500e-01, -3.41739984e-01,
          6.73860047e-01, -5.31022918e-01],
         [-5.47918591e-01, 3.45980161e-02, -8.84314245e-01,
          1.40909441e+00, 6.79006984e-01, 5.34002809e-01,
          1.03929441e+00, -4.45935165e-01],
         [-8.44885053e-01, -5.92934199e-02, -7.80918745e-01,
          -4.72747419e-01, -2.58745776e-01, -1.23017470e+00,
          -8.05998104e-01, -7.86286177e-01],
         [3.42980797e-01, 1.47426670e+00, -2.63941247e-01,
          -1.28821221e+00, -6.92890572e-01, 1.15169300e-01,
          -1.01740641e+00, 6.60205626e-01],
         [2.12477957e+00, 4.72758051e-01, 7.70013751e-01,
          9.07269925e-01, 4.35885898e-01, -4.68659229e-01,
          -6.39891577e-01, 7.45293379e-01],
         [-5.47918591e-01, -1.21887711e-01, 1.08020025e+00,
          -9.63790522e-02, -7.64049618e-02, -8.62108890e-01,
          -4.79825287e-01, -1.04154944e+00],
         [-8.44885053e-01, -5.92934199e-02, -1.29789624e+00,
          1.66000666e+00, -1.45868129e-01, 4.45159338e-01,
          -5.79489204e-01, -7.01198424e-01]]
ytrue = [1,0,0,1,0,0,1,1,0,0,1,1,0,0,0,0,1,0,0,0,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0,0]
print(len(ytrue))
#Transpose Xtest before feeding to NN
yout1 = dense(4, transpose(Xtest), w1, b1, 'relu') #input layer with 4 neuron
yout2 = dense(2, yout1, w2, b2, 'relu') #hidden layer with 2 neuron
ypred = dense(1, yout2, w3, b3,'sigmoid') #output layer
print(ypred)
ypred_class = [1 if i > 0.5 else 0 for i in ypred[0]]
print(ypred_class)
print(classification_report(ytrue,ypred_class))

# view rawann_micropython.py hosted with ❤ by GitHub
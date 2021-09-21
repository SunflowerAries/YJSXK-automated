def d(X, Q, B, E):
    H = len(X)
    I = ""
    U = None
    R = None
    O = None
    Y = None
    G = None
    J = None
    if (Q != None and Q != ""):
        U = r(Q)
        Y = len(U)

    if (B != None and B != ""):
        R = r(B)
        G = len(R)
    
    if (E != None and E != ""):
        O = r(E)
        J = len(O)
    
    if (H > 0):
        if (H < 4):
            V = a(X)
            F = None
            if (Q != None and Q != "" and B != None and B != "" and E != None and E != ""):
                T = V
                for M in range(Y):
                    T = e(T, U[M])
                
                for L in range(G):
                    T = e(T, R[L])
                
                for K in range(J):
                    T = e(T, O[K])
                
                F = T
            else:
                if (Q != None and Q != "" and B != None and B != ""):
                    T = V
                    for M in range(Y):
                        T = e(T, U[M])
                    
                    for L in range(G):
                        T = e(T, R[L])
                    
                    F = T
                else:
                    if (Q != None and Q != ""):
                        T = V
                        for M in range(Y):
                            T = e(T, U[M])
                        
                        F = T
            I = f(F)
        else:
            P = H // 4
            N = H % 4
            S = 0
            for S in range(P):
                D = X[S * 4 + 0: S * 4 + 4]
                W = a(D)
                if (Q != None and Q != "" and B != None and B != "" and E != None and E != ""):
                    T = W
                    for M in range(Y):
                        T = e(T, U[M])
                    
                    for L in range(G):
                        T = e(T, R[L])
                    
                    for K in range(J):
                        T = e(T, O[K])
                    
                    F = T
                else:
                    if (Q != None and Q != "" and B != None and B != ""):
                        T = W
                        for M in range(Y):
                            T = e(T, U[M])
                        
                        for L in range(G):
                            T = e(T, R[L])
                        
                        F = T
                    else:
                        if (Q != None and Q != ""):
                            T = W
                            for M in range(Y):
                                T = e(T, U[M])
                            
                            F = T
                I += f(F)
            
            if (N > 0):
                C = X[P * 4 + 0: H]
                W = a(C)
                if (Q != None and Q != "" and B != None and B != "" and E != None and E != ""):
                    T = W
                    for M in range(Y):
                        T = e(T, U[M])
                    
                    for L in range(G):
                        T = e(T, R[L])
                    
                    for K in range(J):
                        T = e(T, O[K])
                    
                    F = T
                else:
                    if (Q != None and Q != "" and B != None and B != ""):
                        T = W
                        for M in range(Y):
                            T = e(T, U[M])
                        
                        for L in range(G):
                            T = e(T, R[L])
                        
                        F = T
                    else:
                        if (Q != None and Q != ""):
                            T = W
                            for M in range(Y):
                                T = e(T, U[M])
                            
                            F = T
                I += f(F)
    return I

def r(E):
    B = []
    D = len(E)
    F = D // 4
    G = D % 4
    C = 0
    for C in range(F):
        B.append(a(E[C * 4 + 0: C * 4 + 4]))
    if (G > 0):
        if C == 0:
            B.append(a(E[C * 4 + 0: D]))
    
    return B

def o(B):
    return d(B, "1", "2", "3")

def a(J):
    B = len(J)
    K = [0] * 64
    if (B < 4):
        for H in range(B):
            F = ord(J[H])
            for G in range(16):
                I = 1
                for E in range(15, G, -1):
                    I *= 2
                
                K[16 * H + G] = (F // I) % 2
            
        
        for D in range(B, 4):
            F = 0
            for C in range(16):
                I = 1
                for E in range(15, C, -1):
                    I *= 2
                K[16 * D + C] = (F // I) % 2
            
        
    else:
        for H in range(4):
            F = ord(J[H])
            for G in range(16):
                I = 1
                for E in range(15, G, -1):
                    I *= 2
                
                K[16 * H + G] = (F // I) % 2
    return K

def b(C):
    if C == "0000":
        return "0"
    elif C == "0001":
        return "1"
    elif C == "0010":
        return "2"
    elif C == "0011":
        return "3"
    elif C == "0100":
        return "4"
    elif C == "0101":
        return "5"
    elif C == "0110":
        return "6"
    elif C == "0111":
        return "7"
    elif C == "1000":
        return "8"
    elif C == "1001":
        return "9"
    elif C == "1010":
        return "A"
    elif C == "1011":
        return "B"
    elif C == "1100":
        return "C"
    elif C == "1101":
        return "D"
    elif C == "1110":
        return "E"
    elif C == "1111":
        return "F"

def f(D):
    C = ""
    for i in range(16):
        B = ""
        for j in range(4):
            B += str(D[i * 4 + j])
        C += b(B)
    
    return C

def e(C, M):
    P = w(M)
    L = z(C)
    D = [0] * 32
    O = [0] * 32
    H = [0] * 32
    for I in range(32):
        D[I] = L[I]
        O[I] = L[32 + I]
    
    for K in range(16):
        for J in range(32):
            H[J] = D[J]
            D[J] = O[J]
        N = [0] * 48
        for G in range(48):
            N[G] = P[K][G]
        B = u(t(s(u(x(O), N))), H)
        for F in range(32):
            O[F] = B[F]
    E = [0] * 64
    for K in range(32):
        E[K] = O[K]
        E[32 + K] = D[K]
    
    return y(E)

def z(C):
    B = [0] * 64
    m = 1
    n = 0

    for i in range(4):
        k = 0
        for j in range(7, -1, -1):
            B[i * 8 + k] = C[j * 8 + m]
            B[i * 8 + k + 32] = C[j * 8 + n]
            k += 1
        m += 2
        n += 2
        
    return B

def x(B):
    C = [0] * 48
    for i in range(8):
        if (i == 0):
            C[i * 6 + 0] = B[31]
        else:
            C[i * 6 + 0] = B[i * 4 - 1]
        
        C[i * 6 + 1] = B[i * 4 + 0]
        C[i * 6 + 2] = B[i * 4 + 1]
        C[i * 6 + 3] = B[i * 4 + 2]
        C[i * 6 + 4] = B[i * 4 + 3]
        if (i == 7):
            C[i * 6 + 5] = B[0]
        else:
            C[i * 6 + 5] = B[i * 4 + 4]
        
    
    return C

def u(D, C):
    B = [0] * len(D)
    for i in range(len(D)):
        B[i] = D[i] ^ C[i]
    return B

def s(D):
    B = [0] * 32
    F = ""
    N = [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8], [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    M = [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5], [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]]
    L = [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1], [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]]
    K = [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9], [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]]
    J = [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6], [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]]
    I = [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8], [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]]
    H = [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6], [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2], [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]]
    G = [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2], [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
    for m in range(8):
        E = D[m * 6 + 0] * 2 + D[m * 6 + 5]
        C = D[m * 6 + 1] * 2 * 2 * 2 + D[m * 6 + 2] * 2 * 2 + D[m * 6 + 3] * 2 + D[m * 6 + 4]
        if m == 0:
            F = A(N[E][C])
        elif m == 1:
            F = A(M[E][C])
        elif m == 2:
            F = A(L[E][C])
        elif m == 3:
            F = A(K[E][C])
        elif m == 4:
            F = A(J[E][C])
        elif m == 5:
            F = A(I[E][C])
        elif m == 6:
            F = A(H[E][C])
        elif m == 7:
            F = A(G[E][C])
        
        
        B[m * 4 + 0] = int(F[0:1])
        B[m * 4 + 1] = int(F[1:2])
        B[m * 4 + 2] = int(F[2:3])
        B[m * 4 + 3] = int(F[3:4])
    
    return B

def t(C):
    B = [0] * 32
    B[0] = C[15]
    B[1] = C[6]
    B[2] = C[19]
    B[3] = C[20]
    B[4] = C[28]
    B[5] = C[11]
    B[6] = C[27]
    B[7] = C[16]
    B[8] = C[0]
    B[9] = C[14]
    B[10] = C[22]
    B[11] = C[25]
    B[12] = C[4]
    B[13] = C[17]
    B[14] = C[30]
    B[15] = C[9]
    B[16] = C[1]
    B[17] = C[7]
    B[18] = C[23]
    B[19] = C[13]
    B[20] = C[31]
    B[21] = C[26]
    B[22] = C[2]
    B[23] = C[8]
    B[24] = C[18]
    B[25] = C[12]
    B[26] = C[29]
    B[27] = C[5]
    B[28] = C[21]
    B[29] = C[10]
    B[30] = C[3]
    B[31] = C[24]
    return B

def y(B):
    C = [0] * 64
    C[0] = B[39]
    C[1] = B[7]
    C[2] = B[47]
    C[3] = B[15]
    C[4] = B[55]
    C[5] = B[23]
    C[6] = B[63]
    C[7] = B[31]
    C[8] = B[38]
    C[9] = B[6]
    C[10] = B[46]
    C[11] = B[14]
    C[12] = B[54]
    C[13] = B[22]
    C[14] = B[62]
    C[15] = B[30]
    C[16] = B[37]
    C[17] = B[5]
    C[18] = B[45]
    C[19] = B[13]
    C[20] = B[53]
    C[21] = B[21]
    C[22] = B[61]
    C[23] = B[29]
    C[24] = B[36]
    C[25] = B[4]
    C[26] = B[44]
    C[27] = B[12]
    C[28] = B[52]
    C[29] = B[20]
    C[30] = B[60]
    C[31] = B[28]
    C[32] = B[35]
    C[33] = B[3]
    C[34] = B[43]
    C[35] = B[11]
    C[36] = B[51]
    C[37] = B[19]
    C[38] = B[59]
    C[39] = B[27]
    C[40] = B[34]
    C[41] = B[2]
    C[42] = B[42]
    C[43] = B[10]
    C[44] = B[50]
    C[45] = B[18]
    C[46] = B[58]
    C[47] = B[26]
    C[48] = B[33]
    C[49] = B[1]
    C[50] = B[41]
    C[51] = B[9]
    C[52] = B[49]
    C[53] = B[17]
    C[54] = B[57]
    C[55] = B[25]
    C[56] = B[32]
    C[57] = B[0]
    C[58] = B[40]
    C[59] = B[8]
    C[60] = B[48]
    C[61] = B[16]
    C[62] = B[56]
    C[63] = B[24]
    return C

def A(B):
    if B == 0:
        return "0000"
    elif B == 1:
        return "0001"
    elif B == 2:
        return "0010"
    elif B == 3:
        return "0011"
    elif B == 4:
        return "0100"
    elif B == 5:
        return "0101"
    elif B == 6:
        return "0110"
    elif B == 7:
        return "0111"
    elif B == 8:
        return "1000"
    elif B == 9:
        return "1001"
    elif B == 10:
        return "1010"
    elif B == 11:
        return "1011"
    elif B == 12:
        return "1100"
    elif B == 13:
        return "1101"
    elif B == 14:
        return "1110"
    elif B == 15:
        return "1111"

def w(D):
    F = [0] * 56
    G = []
    for i in range(16):
        G.append([0] * 48)
    B = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for E in range(7):
        k = 7
        for j in range(8):
            F[E * 8 + j] = D[8 * k + E]
            k -= 1
    for E in range(16):
        for j in range(B[E]):
            I = F[0]
            C = F[28]
            for k in range(27):
                F[k] = F[k + 1]
                F[28 + k] = F[29 + k]
            
            F[27] = I
            F[55] = C
        
        H = [0] * 48
        H[0] = F[13]
        H[1] = F[16]
        H[2] = F[10]
        H[3] = F[23]
        H[4] = F[0]
        H[5] = F[4]
        H[6] = F[2]
        H[7] = F[27]
        H[8] = F[14]
        H[9] = F[5]
        H[10] = F[20]
        H[11] = F[9]
        H[12] = F[22]
        H[13] = F[18]
        H[14] = F[11]
        H[15] = F[3]
        H[16] = F[25]
        H[17] = F[7]
        H[18] = F[15]
        H[19] = F[6]
        H[20] = F[26]
        H[21] = F[19]
        H[22] = F[12]
        H[23] = F[1]
        H[24] = F[40]
        H[25] = F[51]
        H[26] = F[30]
        H[27] = F[36]
        H[28] = F[46]
        H[29] = F[54]
        H[30] = F[29]
        H[31] = F[39]
        H[32] = F[50]
        H[33] = F[44]
        H[34] = F[32]
        H[35] = F[47]
        H[36] = F[43]
        H[37] = F[48]
        H[38] = F[38]
        H[39] = F[55]
        H[40] = F[33]
        H[41] = F[52]
        H[42] = F[45]
        H[43] = F[41]
        H[44] = F[49]
        H[45] = F[35]
        H[46] = F[28]
        H[47] = F[31]
        if E == 0:
            for m in range(48):
                G[0][m] = H[m]
        elif E == 1:
            for m in range(48):
                G[1][m] = H[m]
        elif E == 2:
            for m in range(48):
                G[2][m] = H[m]
        elif E == 3:
            for m in range(48):
                G[3][m] = H[m]
        elif E == 4:
            for m in range(48):
                G[4][m] = H[m]
        elif E == 5:
            for m in range(48):
                G[5][m] = H[m]
        elif E == 6:
            for m in range(48):
                G[6][m] = H[m]
        elif E == 7:
            for m in range(48):
                G[7][m] = H[m]
        elif E == 8:
            for m in range(48):
                G[8][m] = H[m]
        elif E == 9:
            for m in range(48):
                G[9][m] = H[m]
        elif E == 10:
            for m in range(48):
                G[10][m] = H[m]
        elif E == 11:
            for m in range(48):
                G[11][m] = H[m]
        elif E == 12:
            for m in range(48):
                G[12][m] = H[m]
        elif E == 13:
            for m in range(48):
                G[13][m] = H[m]
        elif E == 14:
            for m in range(48):
                G[14][m] = H[m]
        elif E == 15:
            for m in range(48):
                G[15][m] = H[m]
        
    return G
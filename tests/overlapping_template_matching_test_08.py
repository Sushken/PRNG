import math
from tests import gamma_functions
# from scipy.special import gamma, gammainc, gammaincc


def lgamma(x):
    return math.log(gamma_functions.gamma(x))


def Pr(u, eta):
    if (u == 0):
        p = math.exp(-eta)
    else:
        sum = 0.0
        for l in range(1, u + 1):
            sum += math.exp(
                -eta - u * math.log(2) + l * math.log(eta) - lgamma(l + 1) + lgamma(u) - lgamma(l) - lgamma(u - l + 1))
        p = sum
    return p


def test(bits, n, blen=6):

    m = 10
    # Build the template B as a random list of bits
    B = [1 for x in range(m)]

    N = 968
    K = 5
    M = 1062
    if n < (M * N):
        print("Insufficient data. %d bit provided. 1,028,016 bits required" % n)
        return False, 0.0, None

    blocks = list()  # Split into N blocks of M bits
    for i in range(N):
        blocks.append(bits[i * M:(i + 1) * M])

    # Count the distribution of matches of the template across blocks: Vj
    v = [0 for x in range(K + 1)]
    for block in blocks:
        count = 0
        for position in range(M - m):
            if block[position:position + m] == B:
                count += 1

        if count >= (K):
            v[K] += 1
        else:
            v[count] += 1

    # lamd = float(M-m+1)/float(2**m) # Compute lambda and nu
    # nu = lamd/2.0

    chisq = 0.0  # Compute Chi-Square
    # pi = [0.324652,0.182617,0.142670,0.106645,0.077147,0.166269] # From spec
    pi = [0.364091, 0.185659, 0.139381, 0.100571, 0.0704323, 0.139865]  # From STS
    piqty = [int(x * N) for x in pi]

    lambd = (M - m + 1.0) / (2.0 ** m)
    eta = lambd / 2.0
    sum = 0.0
    for i in range(K):  # Compute Probabilities
        pi[i] = Pr(i, eta)
        sum += pi[i]

    pi[K] = 1 - sum

    # for block in blocks:
    #    count = 0
    #    for j in xrange(M-m+1):
    #        if B == block[j:j+m]:
    #            count += 1
    #    if ( count <= 4 ):
    #        v[count]+= 1
    #    else:
    #        v[K]+=1

    sum = 0
    chisq = 0.0
    for i in range(K + 1):
        chisq += ((v[i] - (N * pi[i])) ** 2) / (N * pi[i])
        sum += v[i]

    p = gamma_functions.gammaincc(5.0 / 2.0, chisq / 2.0)  # Compute P value

    print("  B = ", B)
    print("  m = ", m)
    print("  M = ", M)
    print("  N = ", N)
    print("  K = ", K)
    print("  model = ", piqty)
    print("  v[j] =  ", v)
    print("  chisq = ", chisq)

    success = (p >= 0.01)
    print("p = ", p)
    print("  success = ", success)






# import math
# import scipy.special as ss
# from random import randint
#
#
# def lgamma(x):
#     return math.log(ss.gamma(x))
#
#
# def Pr(u, eta):
#     if ( u == 0 ):
#         p = math.exp(-eta)
#     else:
#         sum = 0.0
#         for l in range(1,u+1):
#             sum += math.exp(-eta-u*math.log(2)+l*math.log(eta)-lgamma(l+1)+lgamma(u)-lgamma(l)-lgamma(u-l+1))
#         p = sum
#     return p
#
#
# def test(input, n, blen=6):
#
#     m = 10
#     # Build the template B as a random list of input
#     B = [1 for x in range(m)]
#
#     N = 968 # The number of blocks as specified in SP800-22rev1a
#     K = 5   # The number of degrees of freedom
#     M = 1062 # Length of each block as specified in SP800-22rev1a
#
#     if len(input) < (M*N):
#         # Too little data. Inputs of length at least M*N bits required (Recommended 1,028,016)
#         return [0]*12
#
#     blocks = list() # Split into N blocks of M input
#     for i in range(N):
#         block = [None]*M
#         for j in range(M):
#             block[j] = int(input[i*M+j],2)
#
#         blocks.append(block)
#
#     # Count the distribution of matches of the template across blocks: Vj
#     v=[0 for x in range(K+1)]
#     for block in blocks:
#         count = 0
#         for position in range(M-m):
#             if block[position:position+m] == B:
#                 count += 1
#
#         if count >= (K):
#             v[K] += 1
#         else:
#             v[count] += 1
#
#     chisq = 0.0  # Compute Chi-Square
#
#     pi = [0.364091, 0.185659, 0.139381, 0.100571, 0.0704323, 0.139865] # From STS
#     piqty = [int(x*N) for x in pi]
#
#     lambd = (M-m+1.0)/(2.0**m)
#     eta = lambd/2.0
#     sum = 0.0
#     for i in range(K): #  Compute Probabilities
#         pi[i] = Pr(i, eta)
#         sum += pi[i]
#
#     pi[K] = 1 - sum
#
#     sum = 0
#     chisq = 0.0
#     for i in range(K+1):
#         chisq += ((v[i] - (N*pi[i]))**2)/(N*pi[i])
#         sum += v[i]
#
#     p = ss.gammaincc(5.0/2.0, chisq/2.0) # Compute P value
#
#     if p >= 0.01:
#         return print("08 = ", True)
#     else:
#         return print("08 = ", False)

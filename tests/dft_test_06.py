import numpy
import math
import sys


def test(bits, n):
    # n = len(bits)
    if (n % 2) == 1:  # Make it an even number
        bits = bits[:-1]

    ts = list()  # Convert to +1,-1
    for bit in bits:
        ts.append((int(bit) * 2) - 1)

    ts_np = numpy.array(ts)
    fs = numpy.fft.fft(ts_np)  # Compute DFT

    if sys.version_info > (3, 0):
        mags = abs(fs)[:n // 2]  # Compute magnitudes of first half of sequence
    else:
        mags = abs(fs)[:n / 2]  # Compute magnitudes of first half of sequence

    T = math.sqrt(math.log(1.0 / 0.05) * n)  # Compute upper threshold
    N0 = 0.95 * n / 2.0
    print("  N0 = %f" % N0)

    N1 = 0.0  # Count the peaks above the upper theshold
    for mag in mags:
        if mag < T:
            N1 += 1.0
    print("  N1 = %f" % N1)
    d = (N1 - N0) / math.sqrt((n * 0.95 * 0.05) / 4)  # Compute the P value
    p = math.erfc(abs(d) / math.sqrt(2))
    print("p = ", p)

    success = (p >= 0.01)
    print("  success = ", success)





    # T = math.sqrt(math.log(1.0/0.05)*n) # Compute upper threshold
    #
    # N0 = 0.95*n/2.0
    #
    # write_array = [0.0,0.0,0.0,0.0]
    #
    # ts = list()             # Convert to +1,-1
    # for i in range(n):
    #     if input[i] == '1':
    #         ts.append(1)
    #     else:
    #         ts.append(-1)
    # ts_np = np.array(ts)
    #
    # fs = np.fft.fft(ts_np)  # Compute DFT
    #
    # mags = abs(fs)[:n/2]  #Compute magnitudes of first half of sequence
    #
    #
    # N1 = 0.0   # Count the peaks above the upper theshold
    #
    # for mag in mags:
    #     if mag < T:
    #         N1 += 1.0
    # d = (N1 - N0)/math.sqrt((n*0.95*0.05)/4)
    #
    # # Compute the P value
    # p = math.erfc(abs(d)/math.sqrt(2))
    #
    # if p >= 0.01:
    #     return True
    # else:
    #     return False
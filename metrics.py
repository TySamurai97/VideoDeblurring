import numpy as np
import math

def calculate_SNR(real_image, gen_image):
    arr = np.square( real_image - gen_image )
    dinom = []
    real_image = real_image*127.5 + 127.5
    gen_image = gen_image*127.5 + 127.5
    for i in range(real_image.shape[0]):
        l = []
        for j in range(real_image.shape[1]):
            l.append( arr[i][j][0] + arr[i][j][1] + arr[i][j][2])
        dinom.append(l)
    numer = []
    for i in range(real_image.shape[0]):
        l = []
        for j in range(real_image.shape[1]):
            l.append( real_image[i][j][0]**2 + real_image[i][j][1]**2 + real_image[i][j][2]**2 )
        numer.append(l)
    snr = 0
    for i in range(real_image.shape[0]):
        for j in range(real_image.shape[1]):
#             return dinom[i][j]
            if(not (numer[i][j] / dinom[i][j] == 0)):
                snr += 10 * math.log10( numer[i][j] / dinom[i][j] )
    return snr/(real_image.shape[0] * real_image.shape[1])


if __name__ == '__main__':
    print( calculate_SNR(np.array([[[0.11, 0.19, 0.21]]]), np.array([[[0.8, 0.23, 0.15]]])) )
import cv2
import subprocess
import numpy as np

class Exercise1:
    @staticmethod
    def RGB_to_YUV(R, G, B):
        Y = 0.299 * R + 0.587 * G + 0.114 * B
        U = -0.147 * R - 0.289 * G + 0.436 * B
        V = 0.615 * R - 0.515 * G - 0.100 * B
        return Y, U, V

    @staticmethod
    def YUV_to_RGB(Y, U, V):
        R = Y + 1.13983 * V
        G = Y - 0.39465 * U - 0.58060 * V
        B = Y + 2.03211 * U
        return R, G, B

class Exercise2:
    @staticmethod
    def resize(input_file, scale, outputfile):
        try:
            size = ['ffmpeg', '-i', input_file, '-vf', scale, outputfile]
            subprocess.run(size, check=True)
        except Exception as e:
            print("Los valores no son correctos")

class Exercise3:
    @staticmethod
    def serpentina(input_file):
        img = cv2.imread(input_file)

        # Convert the image to grayscale
        gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        height, width = gray_image.shape

        zigzag_order = np.array([
            [0, 1, 5, 6, 14, 15, 27, 28],
            [2, 4, 7, 13, 16, 26, 29, 42],
            [3, 8, 12, 17, 25, 30, 41, 43],
            [9, 11, 18, 24, 31, 40, 44, 53],
            [10, 19, 23, 32, 39, 45, 52, 54],
            [20, 22, 33, 38, 46, 51, 55, 60],
            [21, 34, 37, 47, 50, 56, 59, 61],
            [35, 36, 48, 49, 57, 58, 62, 63]
        ])
        blocks = []

        for i in range(0, height, 8):
            for j in range(0, width, 8):
                block = gray_image[i:i+8, j:j+8]
                blocks.append(block)

        for block in blocks:
            flattened_block = block.flatten()[zigzag_order]
            print(flattened_block)

class Exercise4:
    @staticmethod
    def RGB_to_BW(input_file):
        try:
            BW = ['ffmpeg', '-i', input_file, '-vf', 'format=gray', '-q:v', '0.001', 'output_BW.jpg']
            subprocess.run(BW, check=True)
        except Exception as e:
            print("Los valores no son correctos")

class Exercise5:
    @staticmethod
    def run_length_encode(data):
        encoded_data = []
        i = 0
        n = len(data)

        while i < n:
            count = 1
            while i < n - 1 and data[i] == data[i + 1]:
                count += 1
                i += 1
            encoded_data.extend([count, data[i]])
            i += 1

        return bytes(encoded_data)

class Exercise6:
    def __init__(self):
        pass

    def encode(self, input_data):
        # Apply DCT encoding to input data
        encoded_data = cv2.dct(np.float32(input_data))
        return encoded_data

    def decode(self, encoded_data):
        # Apply inverse DCT to encoded data to retrieve the original data
        decoded_data = cv2.idct(np.float32(encoded_data))
        return decoded_data

if __name__ == '__main__':
    # Ejemplo de uso de las clases y métodos
    y, u, v = Exercise1.RGB_to_YUV(255, 128, 128)
    print("YUV:", y, u, v)
    R, G, B = Exercise1.YUV_to_RGB(y, u, v)
    print("RGB:", R, G, B)
    ''' Podemos llamar a cualquiera de estos dos funciones, y podemos ver como pasa de un modo a otro.'''
    # Ejercicio 2
    Exercise2.resize('image1.jpg', 'scale=320:200', 'outputfile.jpg')

    ''' Aquí he utilizado el ffmpeg, con el suborosses y tiene como input la imagen que tenemos, las scala que queremos hacer resize, y el nombre del archivo del output. 
    Si alguuno de estos valores no esta bien definido como deberia estar, hace un break y no calcula el outputfile. Si todo funciona bien, podemos ver como la imagen que queda, 
    tiene menor calidad.'''
    # Ejercicio 3
    Exercise3.serpentina('image1.jpg')

    '''El print de esa ejercicio son los balores de cada byte de la imagen, pero dividida en bloques de 8x8, para ello dividivos la imagen
     en esos bloques, y luego hacemos un zigzag pattern para leer cada uno de lo bloques en diagonal.'''

    # Ejercicio 4
    Exercise4.RGB_to_BW('image1.jpg')
    '''Aqui, he utilizado la funcion de subproccess con ffmpeg para pasarlo a blanco y negro y hacerle una compresión maxima, para la pasar a blanco y negro
     he hecho format = gray que automaticamente lo pasa al blanco y negro. En cuanto a la compressión, he visto que se hacia la maxima compresión, es decir que ocupe muy poco, 
     pero que la calidad se pueda perder con -q:v 0, pero nose porque, al cambiar este valor al máximo o minimo el output no cambia.'''
    # Ejercicio 5
    input_bytes = b'\x01\x01\x01\x01\x01\x02\x02\x03\x04\x04\x04'
    encoded_bytes = Exercise5.run_length_encode(input_bytes)
    print(encoded_bytes)
    '''En este ejercicio en run_length_encode nos devuelve el primero el numero de repeticiones de un mismo pixel, 
    y luego el pixel que se repite, ten en cuenta que los inputs bytes tienes que estar escritos de forma correcta.'''
    # Ejercicio 6
    input_data = np.array([[255, 128, 128, 128, 128, 128, 128, 128],
                           [128, 128, 128, 128, 128, 128, 128, 128],
                           [128, 128, 128, 128, 128, 128, 128, 128],
                           [128, 128, 128, 128, 128, 128, 128, 128],
                           [128, 128, 128, 128, 128, 128, 128, 128],
                           [128, 128, 128, 128, 128, 128, 128, 128],
                           [128, 128, 128, 128, 128, 128, 128, 128],
                           [128, 128, 128, 128, 128, 128, 128, 128]], dtype=np.uint8)

    dct_encoder_decoder = Exercise6()

    # Encode the data using DCT
    encoded_data = dct_encoder_decoder.encode(input_data)
    print("Encoded Data:")
    print(encoded_data)

    # Decode the encoded data to retrieve the original data
    decoded_data = dct_encoder_decoder.decode(encoded_data)
    print("\nDecoded Data:")
    print(decoded_data)

    '''Como podemos observar en el encoder, aunque sean mismos numeros no devuelve el mismo resultado,
    ya que no solo depende del numero sino tambien de la posición de las frecuencias en la imagen y como
    se distribuyen en los componentes del DCT
    Al hacer decoder, los resultados son los mismos que los del input, pero con un error muy pequeño'''
import subprocess
import re
import os
import subprocess
from moviepy.editor import VideoFileClip
import RGB_YUV
import json

def convert_to_mp2(input_file, output_file):
    # Convert MP4 to MP2 using ffmpeg
    subprocess.run(["ffmpeg", "-i", input_file, "-c:a", "mp2", output_file])

def get_video_info(input_file):
    # Get video information using moviepy

    cmd= ["ffmpeg", "-i", input_file]
    try:
        subprocess.run(cmd, check=True)
        print(f"Chroma subsampling changed and video saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")



def change_resolution(input_file, output_file,width,height):

    cmd = ["ffmpeg","-i", input_file,"-vf", f"scale={width}:{height}",output_file]

    try:
        subprocess.run(cmd, check=True)
        print(f"Video resolution modified and saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
def change_chroma_subsampling(input_file, output_file, subsampling):

    cmd = ["ffmpeg","-i", input_file, "-vf", f"format=yuv420p", "-c:v", "libx264", "-pix_fmt", subsampling, output_file]

    try:
        subprocess.run(cmd, check=True)
        print(f"Chroma subsampling changed and video saved to {output_file}")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


if __name__ == "__main__":

    input_file = "Big_Buck_Bunny.mp4"

    # Obtener información del video
    # Exercise 5
    get_video_info(input_file)
    ''' con este función sabemos que el video tiene el chroma_subsampling de yuv420p es decir 4:2:0, y la resolución del video es de 1280x720. 
    Si leemos todos los datos que hay podemos saber mas sobre el video tambien.'''
    #Exercise 1

    output_file = 'Big_Buck_Bunny_mp2.mp4'
    # Convertir MP4 a MP2
    convert_to_mp2(input_file, output_file)

    #Exercise 2
    output_file = "new_resolution.mp4"
    width = 320
    height = 240
    change_resolution(input_file, output_file, width,height)


    #Exercise 3
    output_file = "new_subsampling.mp4"
    subsampling = "yuv444p"  # Set your desired subsampling format
    change_chroma_subsampling(input_file, output_file, subsampling)
    '''En el primer apartado hemos visto que el chroma_subsampling es de 4:2:0 y para que la diferencia de color 
    sea notable, en esta lo he pasado a 4:4:4. La principal diferencia entre estos dos es que el primero tiene menos precision en color
    que el 4:4:4.'''



    #Exercise 6
    RGB_YUV.Exercise1.RGB_to_YUV(255, 128, 128)
    '''Aqui he utilizado el primer ejercicio del lab uno.'''
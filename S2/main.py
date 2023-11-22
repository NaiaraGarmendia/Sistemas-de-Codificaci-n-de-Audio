
import subprocess
import re

def cut_vide(input_file,start_time, duration):
    try:
        cut = ['ffmpeg', '-i',input_file, '-ss', start_time, '-t',duration ,'-c:v','copy' ,'-c:a','copy','cut_BBB.mp4']
        subprocess.run(cut, check=True)
        motion= ['ffmpeg', '-flags2', '+export_mvs' ,'-i', 'cut_BBB.mp4', '-vf', 'codecview=mv=pf+bf+bb' ,'motion.mp4']
        subprocess.run(motion, check=True)
    except Exception as e:
        print("Los valores no son correctos")

def create_container(input_file, output_file):
    try:
        # cortar video
        cut_command = ['ffmpeg', '-i', input_file, '-t', '50', '-c:v', 'copy', '-c:a', 'copy',
                       'cut_50s_BBB.mp4']
        subprocess.run(cut_command, check=True)

        #mono mp3
        mp3_mono_command = ['ffmpeg', '-i', 'cut_50s_BBB.mp4', '-q:a', '0', '-map', 'a', 'audio_mono.mp3']
        subprocess.run(mp3_mono_command, check=True)

        #stereo mp3
        mp3_stereo_command = ['ffmpeg', '-i', 'cut_50s_BBB.mp4', '-q:a', '2', '-map', 'a', 'audio_stereo.mp3']
        subprocess.run(mp3_stereo_command, check=True)

        #audio aac
        aac_command = ['ffmpeg', '-i', 'cut_50s_BBB.mp4', '-strict', '-2', '-c:a', 'aac', 'audio.aac']
        subprocess.run(aac_command, check=True)

        #crear un container con todo lo anterior
        mp4_command = ['ffmpeg', '-i', 'cut_50s_BBB.mp4', '-i', 'audio_mono.mp3', '-i', 'audio_stereo.mp3', '-i',
                       'audio.aac', '-map', '0', '-map', '1', '-map', '2', '-map', '3', '-c:v', 'copy', '-c:a',
                       'copy', output_file]
        subprocess.run(mp4_command, check=True)
    except Exception as e:
        print("An error occurred:", str(e))


def see_tracks(container):
    #con esto podemos ver lo que sale, y puedes mirar los stream#
    tracks = ['ffmpeg','-i',container]

    subprocess.run(tracks)




def add_subtitles(input_file,subtitles,output_video):
    try:
        subtitiles = ['ffmpeg', '-i', input_file, '-vf',f'subtitles={subtitles}',output_video]
        subprocess.run(subtitiles, check=True)
    except Exception as e:
        print("An error ocurred:",str(e))







#######################################################################3
input_file = 'Big_Buck_Bunny.mp4'

## Exercise 1
start_time = '00:46'
duration = '9'
cut_vide(input_file, start_time, duration)

'''First we cut the video with a ffmpeg, and then add another ffmpeg to add all the motions '''
## Exercise 2
output_file = 'container.mp4'
create_container(input_file, output_file) ## MIRA SI EL CONTAINER ESTA BIEN

'''He utilizado diferentes funciones de ffmpeg para procesar el archivo al archivo que se nos pedia en el examen, y luego meter todos en un container
con otra funcion del ffmpeg.'''

## Exercise 3
container = 'container.mp4'
see_tracks(container)
'''En este ejercicio podemos ver como aparecen todos los #stream que le hemos añadido al video en el ejercicio anterior, no he consiguido
que me printe exactamente un print diciendo que hay exactamente tantos tracks, pero en al procesar el subprocess.run, dentro de todos los datos
que aparecen, podemos ver claramente los Stream #'''

## Exercise 4 funciona bien
subtitles = 'subtitles.srt'
output_video = 'video_subtitles.mp4'
add_subtitles(input_file , subtitles , output_video)


## Exercise 5
from Ex5 import split_video

split_video('cut_50s_BBB.mp4','first.mp4','second.mp4')

'''En el script de Ex5.py, he creado usando ffmpeg, una funcion para que parte de la mitad un video. 
luego con el import lo he llamado ha este script y utilizado esa función para el video de 50s de BBB'''

## Exercise 6
from Ex6 import create_video_with_histogram

create_video_with_histogram('cut_50s_BBB.mp4','cut_BBB_histogrma.mp4')
'''Para esta tambien he creado un script y usando ffmpeg, con la funcion para que aparezcan los histrograms YUV
en el video, lo he llamado desde aqui.'''
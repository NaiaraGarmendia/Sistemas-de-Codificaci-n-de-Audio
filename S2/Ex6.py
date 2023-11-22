import subprocess

def create_video_with_histogram(input_video,output_video):
    # Utilizar ffmpeg para generar histogramas en el video
    command = ['ffmpeg', '-i', input_video,'-vf', "split=2[a][b],[b]histogram,format=yuva444p[hh],[a][hh]overlay",
               '-c:v', 'libx264' ,'-preset','ultrafast' ,'-c:a', 'copy' , output_video]

    subprocess.run(command)
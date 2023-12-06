import os
import subprocess

def compare_videos(video1, video2, comparision):
    command_compare = [
        'ffmpeg',
        '-i', video1,
        '-i', video2,
        '-filter_complex', f'[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]',
        '-map', '[vid]',
        '-c:a', 'copy',
        comparision
    ]
    subprocess.run(command_compare)

def scale_video(input_video, resolution, output_path):
        command = [
            'ffmpeg',
            '-i', input_video,
            '-vf', f'scale={resolution}',
            '-c:a', 'aac',
            '-c:v', 'libx264',  # Cambia aquí el códec según tus necesidades
            output_path
        ]
        subprocess.run(command)

def codec_vp8(input_file):
    command = [ 'ffmpeg', '-i',input_file,
    '-c:v','libvpx',
    '-b:v','1M',
    '-c:a','libvorbis',
    'outputVP8.webm']

    subprocess.run(command)
def codec_vp9(input_file):
    command = ['ffmpeg', '-i', input_file,
               '-c:v', 'libvpx-vp9',
               '-b:v', '2M', 'outputVP9.webm']

    subprocess.run(command)

def codec_h265(input_file):
    command = ['ffmpeg', '-i', input_file,
               '-c:v', 'libx265',
               '-crf', '26', '-preset', 'fast',
               '-c:a', 'aac' ,'-b:a','128k',
                'outputH265.mp4']

    subprocess.run(command)

def codec_AV1(input_file):
    command = ['ffmpeg', '-i', input_file,
               '-c:v', 'libaom-av1', 'crf', '30'
               '-b:v', '2000k', 'outputAV1.mkv']

    subprocess.run(command)

def cut_video(input_video,end_time,start_time,output_path):
    command = [
            'ffmpeg',
            '-i', input_video,
            '-ss', str(start_time),
            '-to', str(end_time),
            '-c:v', 'copy',
            '-c:a', 'copy',
            output_path
        ]
    subprocess.run(command)


def main():
    ## El recorte del video BBB
    input_video = 'Big_Buck_Bunny.mp4'
    end_time = 50
    start_time = 20
    output_path = 'BBB_cut.mp4'
    #cut_video(input_video, end_time, start_time,output_path)

    ## cambiar de escala el video, cambiando el ouput_file y el resolution, puedes crear el video que quieras
    output = 'BBB_360x240.mp4'
    resolution = '360:240'
    #scale_video('BBB_cut.mp4',resolution,output)

    ## hay una funcion para cada codec, y lo unico que necesitas como input es el video con la resolucion que quierew

    #codec_vp8('BBB_360x240.mp4')
    #codec_vp9('BBB_360x240.mp4')
    #codec_h265('BBB_360x240.mp4')
    #codec_AV1('BBB_360x240.mp4')


    ##Comparar los dos video que queremos, poniendo como input los outputs de los codec.
    video1 = 'outputVP8.webm'
    video2 = 'outputVP9.webm'
    comparision = 'comparando.mp4'
    compare_videos(video1,video2,comparision)


if __name__ == "__main__":
    main()


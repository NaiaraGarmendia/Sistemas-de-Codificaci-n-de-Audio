import subprocess
def split_video(input_file, output_file1, output_file2):

    cmd = ['ffprobe', '-i', input_file, '-show_entries', 'format=duration', '-v', 'quiet', '-of', 'csv=p=0']
    duration = float(subprocess.check_output(cmd).decode('utf-8').strip())

    # Calcular el punto medio
    midpoint = duration / 2

    # Repartilo en dos partes
    cmd1 = ['ffmpeg', '-i', input_file, '-t', str(midpoint), '-c', 'copy', output_file1]
    subprocess.run(cmd1)

    cmd2 = ['ffmpeg', '-i', input_file, '-ss', str(midpoint), '-c', 'copy', output_file2]
    subprocess.run(cmd2)


import tkinter as tk
from tkinter import filedialog
import subprocess

def cut_video(input_video, end_time, start_time, output_path):
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

def scale_video(input_video, resolution, output_path):
    command = [
        'ffmpeg',
        '-i', input_video,
        '-vf', f'scale={resolution}',
        '-c:a', 'aac',
        '-c:v', 'libx264',
        output_path
    ]
    subprocess.run(command)

def codec_vp8(input_file):
    command = ['ffmpeg', '-i', input_file,
               '-c:v', 'libvpx',
               '-b:v', '1M',
               '-c:a', 'libvorbis',
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
               '-c:a', 'aac', '-b:a', '128k',
               'outputH265.mp4']
    subprocess.run(command)

def codec_AV1(input_file):
    command = ['ffmpeg', '-i', input_file,
               '-c:v', 'libaom-av1', 'crf', '30',
               '-b:v', '2000k', 'outputAV1.mkv']
    subprocess.run(command)

def compare_videos(video1, video2, comparison):
    command_compare = [
        'ffmpeg',
        '-i', video1,
        '-i', video2,
        '-filter_complex', f'[0:v]pad=iw*2:ih[int];[int][1:v]overlay=W/2:0[vid]',
        '-map', '[vid]',
        '-c:a', 'copy',
        comparison
    ]
    subprocess.run(command_compare)

class VideoToolGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Tool GUI")

        # Botones para realizar acciones
        self.cut_button = tk.Button(root, text="Recortar Video", command=self.cut_video)
        self.cut_button.pack(pady=10)

        self.scale_button = tk.Button(root, text="Cambiar Escala", command=self.scale_video)
        self.scale_button.pack(pady=10)

        self.codec_buttons = tk.Frame(root)
        self.codec_buttons.pack(pady=10)
        tk.Button(self.codec_buttons, text="Codec VP8", command=self.codec_vp8).pack(side=tk.LEFT, padx=5)
        tk.Button(self.codec_buttons, text="Codec VP9", command=self.codec_vp9).pack(side=tk.LEFT, padx=5)
        tk.Button(self.codec_buttons, text="Codec H.265", command=self.codec_h265).pack(side=tk.LEFT, padx=5)
        tk.Button(self.codec_buttons, text="Codec AV1", command=self.codec_av1).pack(side=tk.LEFT, padx=5)

        self.compare_button = tk.Button(root, text="Comparar Videos", command=self.compare_videos)
        self.compare_button.pack(pady=10)

    def open_file_dialog(self):
        return filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo", filetypes=[("Archivos de video", "*.mp4;*.webm")])

    def cut_video(self):
        input_video = self.open_file_dialog()
        end_time = 50
        start_time = 20
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Archivos de video", "*.mp4")])
        if input_video and output_path:
            cut_video(input_video, end_time, start_time, output_path)

    def scale_video(self):
        input_video = self.open_file_dialog()
        resolution = "360:240"
        output_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Archivos de video", "*.mp4")])
        if input_video and output_path:
            scale_video(input_video, resolution, output_path)

    def codec_vp8(self):
        input_file = self.open_file_dialog()
        if input_file:
            codec_vp8(input_file)

    def codec_vp9(self):
        input_file = self.open_file_dialog()
        if input_file:
            codec_vp9(input_file)

    def codec_h265(self):
        input_file = self.open_file_dialog()
        if input_file:
            codec_h265(input_file)

    def codec_av1(self):
        input_file = self.open_file_dialog()
        if input_file:
            codec_AV1(input_file)

    def compare_videos(self):
        video1 = self.open_file_dialog()
        video2 = self.open_file_dialog()
        comparison = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("Archivos de video", "*.mp4")])
        if video1 and video2 and comparison:
            compare_videos(video1, video2, comparison)

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoToolGUI(root)
    root.mainloop()

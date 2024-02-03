import cv2
from moviepy.editor import *


# Fungsi untuk membuat video dari teks dengan avatar
def create_video_with_avatar(text, avatar_path, output_path):
    # Inisialisasi komposisi video dengan latar belakang putih
    video = ColorClip((640, 480), color=(255, 255, 255)).set_duration(5)

    # Load avatar
    avatar = cv2.imread(avatar_path)

    # Menambahkan teks ke dalam avatar (contoh sederhana)
    cv2.putText(avatar, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0), 2)

    # Konversi gambar ke format yang kompatibel dengan MoviePy
    avatar = cv2.cvtColor(avatar, cv2.COLOR_BGR2RGB)

    # Menyimpan avatar sebagai video menggunakan MoviePy
    avatar_clip = ImageClip(avatar).set_duration(5)

    # Menambahkan avatar ke dalam video
    video = CompositeVideoClip([video.set_pos(('center', 'center')), avatar_clip.set_pos(('center', 'center'))])

    # Menyimpan video ke output_path
    video.write_videofile(output_path, fps=24)


# Teks yang ingin diubah menjadi video
text_to_convert = "Ini adalah contoh teks yang akan diubah menjadi video."

# Path untuk avatar
avatar_path = "avatar.png"

# Path untuk menyimpan video hasil
output_video_path = "output_video_with_avatar.mp4"

# Membuat video dari teks dengan avatar
create_video_with_avatar(text_to_convert, avatar_path, output_video_path)
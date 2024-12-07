# import yt_dlp
# import sys
#
# def descargar(link):
#     print("Descargando...")
#     ydl_opts = {
#         # Seleccionar la mejor calidad de video y audio
#         "format": "bestvideo+bestaudio/best",
#         "merge_output_format": "mp4",  # Formato de salida
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         ydl.download([link])
#     print("Descargado!!!")
#
# def descargar2(link):
#     # YouTube(link).streams.first().download()
#     yt = YouTube(link)
#     print("descargando -> " + yt.title)
#     yt.streams.filter(progressive=True, file_extension="mp4").order_by(
#         "resolution"
#     ).desc().first().download()

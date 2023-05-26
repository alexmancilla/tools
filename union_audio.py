from pydub import AudioSegment

def unir_audios(audio_files, output_file):
    """
    Une múltiples archivos de audio en un solo archivo.

    Args:
        audio_files (list): Lista de archivos de audio a unir.
        output_file (str): Nombre del archivo de salida.
    """
    combined_audio = None

    for file in audio_files:
        audio = AudioSegment.from_file(file)

        if combined_audio is None:
            combined_audio = audio
        else:
            combined_audio += audio

    # Exportar el archivo de audio combinado
    combined_audio.export(output_file, format="mp3")

if __name__ == "__main__":
    # Lista de archivos de audio a unir
    audio_files = ["1.mp3", "2.mp3", "3.mp3", "4.mp3", "5.mp3", "6.mp3", "7.mp3", "8.mp3", "9.mp3", "10.mp3"]

    # Nombre del archivo de salida
    output_file = "audio_combinado_1_9.mp3"

    unir_audios(audio_files, output_file)

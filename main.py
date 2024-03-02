import os
import random
import logging

logging.basicConfig(level=logging.INFO)


def shuffle_and_rename(path: str, ext: str = '.mp3'):
    try:
        songs = os.listdir(path)

    except FileNotFoundError:
        logging.error(f"Diretório não encontrado: {path}")
        return []

    songs = [song for song in songs if song.lower().endswith(ext)]

    random.shuffle(songs)

    if not songs:
        logging.warning("Nenhuma música encontrada no diretório.")
        return []

    # Desfazer renomeações anteriores
    for song in songs:
        current_name = song.split(".")[-1]
        old_name = f'{songs.index(song) + 1}.{current_name}'
        old_path = os.path.join(path, old_name)
        new_path = os.path.join(path, song)

        # Verificar se o arquivo novo já existe e, se sim, gerar um novo nome
        i = 1
        while os.path.exists(new_path):
            i += 1
            new_path = os.path.join(path, f'{i}.{current_name}')

        os.rename(old_path, new_path)

    return songs


def main():
    songs_paths = ['E:/SERTANEJO']

    if not songs_paths:
        logging.error("Nenhum diretório de músicas foi especificado.")
        return

    for song_path in songs_paths:
        if not os.path.exists(song_path):
            logging.error(f"Diretório {song_path} não encontrado. Verifique o caminho especificado.")
            continue

        renamed_songs = shuffle_and_rename(song_path)
        logging.info(f"Músicas embaralhadas e renomeadas em {song_path}.")

    input("Pressione qualquer tecla para sair.")


if __name__ == "__main__":
    main()

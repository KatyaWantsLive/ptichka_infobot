import os

def get_jpg_paths(directory):
    photo_paths = []
    for file in os.listdir(directory):
        photo_paths.append(f'D:/test/ptichka_infobot/src/Правиласдачи/{file}')

    return photo_paths
directory = 'D:/test/ptichka_infobot/src/Правиласдачи'

jpg_paths = get_jpg_paths(directory)

def get_jpg_paths1(directory1):
    photo_paths = []
    for file in os.listdir(directory1):
        photo_paths.append(f'D:/test/ptichka_infobot/src/Птичкапринимает/{file}')

    return photo_paths
directory1 = 'D:/test/ptichka_infobot/src/Птичкапринимает'

jpg_paths1 = get_jpg_paths1(directory1)



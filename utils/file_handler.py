# utils/file_handler.py
# 画像ファイルの処理やキャプション保存を管理します

import os

# サポートされる画像拡張子
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

def is_supported_image(file_name):
    """サポートされる拡張子の画像かどうかを判定"""
    return any(file_name.lower().endswith(ext) for ext in SUPPORTED_EXTENSIONS)

def get_image_files(folder_path):
    """フォルダ内のすべての画像ファイルを取得"""
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if is_supported_image(file):
                image_files.append(os.path.join(root, file))
    return image_files

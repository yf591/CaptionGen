# app/gui.py
# GUIアプリケーションのロジック

import os
from tkinter import Tk, filedialog, messagebox
from utils.file_handler import get_image_files
from utils.caption_generator import CaptionGenerator

def select_folder():
    """フォルダを選択し、画像を取得する"""
    folder_path = filedialog.askdirectory()
    if folder_path:
        print(f"Selected folder: {folder_path}")
        image_files = get_image_files(folder_path)
        if not image_files:
            print("No supported image files found in the selected folder.")
            messagebox.showinfo("情報", "選択したフォルダには画像ファイルがありません。")
            return None, []
        return folder_path, image_files
    else:
        print("No folder selected.")
        return None, []

def generate_captions():
    """キャプション生成処理"""
    root = Tk()
    root.withdraw()  # メインウィンドウを隠す
    folder_path, image_files = select_folder()
    if not folder_path or not image_files:
        print("No images found or folder selection cancelled.")
        return

    generator = CaptionGenerator()
    print(f"Processing {len(image_files)} image(s)...")

    for image_file in image_files:
        print(f"Processing image: {image_file}")
        try:
            caption = generator.generate_caption(image_file)
            print(f"Generated caption: {caption}")

            # キャプションを保存
            save_path = f"data/captions/{os.path.basename(image_file)}.txt"
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(caption)
            print(f"Caption saved to: {save_path}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    print("Caption generation completed.")



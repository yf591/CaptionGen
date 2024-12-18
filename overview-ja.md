# CaptionGen 詳細説明

## キャプション生成の仕組み

CaptionGenは、`Salesforce/blip-image-captioning-base`という事前学習済みの画像キャプション生成モデルを使用しています。このモデルは、BLIP (Bootstrapping Language-Image Pre-training) と呼ばれるアーキテクチャに基づいており、大量の画像とテキストのペアデータから学習されています。


### BLIPモデル

BLIPモデルは、以下の特徴を持っています。

- **マルチモーダルな理解**: 画像とテキストの両方の情報を組み合わせて処理することができます。
- **転移学習**: 大規模なデータセットで事前学習されているため、少ないデータでもファインチューニングすることで高い精度を実現できます。
- **多様なタスクへの応用**: 画像キャプション生成だけでなく、画像検索や視覚質問応答など、様々なタスクに応用できます。


### キャプション生成プロセス

1. **画像の前処理**: 入力画像は、モデルが処理できる形式に変換されます（例：リサイズ、正規化）。
2. **特徴抽出**: モデルは、画像から特徴量を抽出します。
3. **キャプション生成**: 抽出された特徴量に基づいて、モデルはキャプションを生成します。
4. **後処理**: 生成されたキャプションは、読みやすくするために整形される場合があります。


## コードの詳細

### `utils/caption_generator.py`

このモジュールは、キャプション生成のコアロジックを担当します。`CaptionGenerator`クラスは、モデルの読み込みとキャプション生成メソッドを提供します。

```python
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class CaptionGenerator:
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)

    def generate_caption(self, image_path):
        """指定された画像にキャプションを生成"""
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        caption = self.processor.decode(outputs[0], skip_special_tokens=True)
        return caption
```


### `utils/file_handler.py`

このモジュールは、画像ファイルの読み込みとキャプションの保存を担当します。

```python
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
```


### `app/gui.py`

このモジュールは、ユーザーインターフェースを提供します。`tkinter`ライブラリを使用して、フォルダ選択とキャプション生成の開始をユーザーに促します。

```python
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
```


## カスタマイズ

- **モデルの変更**: `caption_generator.py`の`model_name`を変更することで、異なる事前学習済みモデルを使用することができます。
- **サポートする画像形式の追加**: `file_handler.py`の`SUPPORTED_EXTENSIONS`に拡張子を追加することで、サポートする画像形式を増やすことができます。


## 謝辞

このアプリケーションは、Hugging Faceの`transformers`ライブラリとSalesforceの`blip-image-captioning-base`モデルを使用しています。これらの素晴らしいリソースの作成者に感謝します。

## How Caption Generation Works

CaptionGen uses a pre-trained image captioning model called `Salesforce/blip-image-captioning-base`. This model is based on the BLIP (Bootstrapping Language-Image Pre-training) architecture and has been trained on a large dataset of image-text pairs.


### BLIP Model

The BLIP model has the following features:

- **Multimodal Understanding**: It can process both image and text information together.
- **Transfer Learning**: Since it is pre-trained on a large dataset, it can achieve high accuracy with fine-tuning on a smaller dataset.
- **Applicability to Various Tasks**: In addition to image captioning, it can be applied to various tasks such as image search and visual question answering.

### Caption Generation Process

1. **Image Preprocessing**: The input image is converted into a format that the model can process (e.g., resizing, normalization).
2. **Feature Extraction**: The model extracts features from the image.
3. **Caption Generation**: Based on the extracted features, the model generates a caption.
4. **Post-processing**: The generated caption may be formatted for better readability.


## Code Details

### `utils/caption_generator.py`

This module handles the core logic of caption generation. The `CaptionGenerator` class provides methods for loading the model and generating captions.

```python
from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

class CaptionGenerator:
    def __init__(self, model_name="Salesforce/blip-image-captioning-base"):
        self.processor = BlipProcessor.from_pretrained(model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(model_name)

    def generate_caption(self, image_path):
        """Generates a caption for the given image."""
        image = Image.open(image_path).convert("RGB")
        inputs = self.processor(images=image, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        caption = self.processor.decode(outputs[0], skip_special_tokens=True)
        return caption
```


### `utils/file_handler.py`

This module handles the loading of image files and saving of captions.

```python
import os

# Supported image extensions
SUPPORTED_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.bmp', '.gif']

def is_supported_image(file_name):
    """Checks if the image has a supported extension."""
    return any(file_name.lower().endswith(ext) for ext in SUPPORTED_EXTENSIONS)

def get_image_files(folder_path):
    """Gets all image files in the folder."""
    image_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if is_supported_image(file):
                image_files.append(os.path.join(root, file))
    return image_files
```


### `app/gui.py`

This module provides the user interface. It uses the `tkinter` library to prompt the user for folder selection and caption generation initiation.

```python
import os
from tkinter import Tk, filedialog, messagebox
from utils.file_handler import get_image_files
from utils.caption_generator import CaptionGenerator

def select_folder():
    """Selects a folder and retrieves images."""
    folder_path = filedialog.askdirectory()
    if folder_path:
        print(f"Selected folder: {folder_path}")
        image_files = get_image_files(folder_path)
        if not image_files:
            print("No supported image files found in the selected folder.")
            messagebox.showinfo("Information", "No image files found in the selected folder.")
            return None, []
        return folder_path, image_files
    else:
        print("No folder selected.")
        return None, []

def generate_captions():
    """Caption generation process."""
    root = Tk()
    root.withdraw()  # Hide the main window
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

            # Save the caption
            save_path = f"data/captions/{os.path.basename(image_file)}.txt"
            with open(save_path, "w", encoding="utf-8") as f:
                f.write(caption)
            print(f"Caption saved to: {save_path}")
        except Exception as e:
            print(f"Error processing {image_file}: {e}")

    print("Caption generation completed.")
```


## Customization

- **Changing the Model**: You can use a different pre-trained model by changing the `model_name` in `caption_generator.py`.
- **Adding Supported Image Formats**: You can increase the supported image formats by adding extensions to `SUPPORTED_EXTENSIONS` in `file_handler.py`.


## Acknowledgements

This application uses the `transformers` library from Hugging Face and the `blip-image-captioning-base` model from Salesforce. We thank the creators of these wonderful resources.
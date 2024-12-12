# utils/caption_generator.py
# キャプション生成のロジックを定義

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



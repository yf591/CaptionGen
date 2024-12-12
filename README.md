# CaptionGen: Automatic Image Captioning App

## Overview
CaptionGen is a lightweight application that generates captions for images in a selected folder. Leveraging a pre-trained Hugging Face model, this app provides a simple GUI to process image data and save captions as text files.


## Features
- Automatically scans and processes images from a folder.
- Generates captions using the `Salesforce/blip-image-captioning-base` model.
- Saves each caption as a `.txt` file in a dedicated folder.


## How It Works
1. **Image Detection**: The app scans the selected folder for supported image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`).
2. **Caption Generation**: Each image is processed using a Hugging Face pre-trained model, and a natural-language description is generated.
3. **Saving Results**: Captions are saved as text files under the `captions/` folder.


## File Structure
```
CaptionGen/
├── README.md               # Overview and usage in English
├── overview.md             # Detailed explanation of the application's behavior in English
├── requirements.txt        # Required Python packages
├── main.py                 # Main script to launch the app
├── utils/
│   ├── __init__.py         # Package initialization file
│   ├── caption_generator.py # Caption generation logic
│   ├── file_handler.py     # File handling logic
├── data/
│   ├── images/             # Folder for input images
│   └── captions/           # Folder for generated captions
└── app/
    ├── __init__.py         # Package initialization file
    └── gui.py              # GUI application
```


## Installation and Usage
### Requirements
- Python 3.9 or above
- GPU recommended but not mandatory

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yf591/CaptionGen.git
   cd CaptionGen
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app:
   ```bash
   python main.py
   ```
   A folder selection dialog will appear. Select the folder where your images are stored. The captions will be generated (this may take time depending on the number of images).
   *Note: For approximately 20 images, it may take around 3-5 minutes to generate captions after selecting the folder.*


## Disclaimer
The developer is not responsible for any damages, losses, or disadvantages arising from the use of this application. Use at your own risk. This application is provided "as is" without any warranty of any kind.


## License
This application uses the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0) for included libraries. Ensure you adhere to the model's specific license terms.


## Developer
yf591
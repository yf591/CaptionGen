# CaptionGen: Automated Image Captioning Application


## Overview
CaptionGen is a lightweight application that automatically generates captions for images within a selected folder.

It utilizes pre-trained models from Hugging Face and processes image data through a simple GUI, saving the captions as text files.


## Features
- Automatically scans and processes images within a folder.
- Generates captions using the `Salesforce/blip-image-captioning-base` model.
- Saves each caption in a `.txt` file format in a dedicated folder.


## How It Works
1. **Image Detection**: Scans the selected folder for supported image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`).
2. **Caption Generation**: Analyzes each image using a pre-trained model from Hugging Face and generates natural language descriptions.
3. **Result Storage**: Saves each caption as a text file in the `captions/` folder.


## File Structure
```
CaptionGen/
├── README-en.md            # English overview and usage instructions
├── overview-en.md          # Detailed English description
├── README-ja.md            # Japanese overview and usage instructions
├── overview-ja.md          # Detailed Japanese description
├── requirements.txt        # Required Python packages
├── main.py                 # Application startup script
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

### Prerequisites
- Python 3.9 or higher
- GPU recommended (but not required)


### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yf591/CaptionGen.git
   cd CaptionGen
   ```

2. Install the required libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

4. When the GUI appears, click the "Select Folder" button and choose the folder (**not zipped**) containing the images for which you want to generate captions.
   *Note: Depending on the number of images, it may take some time.

5. The application will generate captions for each image in the selected folder and save them as text files in the `data/captions/` directory.
   *Note: For about 20 images, it takes approximately 3-5 minutes for caption generation to start after selecting a folder.


## Detailed Description

A more detailed description of the application can be found in `overview-en.md`.


## Disclaimer

The developer is not responsible for any damages, losses, or disadvantages arising from the use of this application. Please use it at your own risk. This application is provided as is, without any warranty.


## License

This application is built under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0). Please comply with the specific license terms of the models used.


## Developer

yf591
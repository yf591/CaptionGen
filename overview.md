# Overview.md

### System and Behavior Overview
This application automatically generates captions (descriptions) for the images within a specified folder and saves the results as text files. Below is an overview of the application's overall structure and behavior flow.

#### 1. **Main Features of the Application**
- The user selects an image folder via the GUI.
- The application detects images within the selected folder.
- Captions are generated for each image, saved in the `captions/` folder.
- Generated captions are stored in text files, one for each image.

#### 2. **Caption Generation Process**
1. **Obtaining Images from the Selected Folder**
   - Supported image formats (`.jpg`, `.jpeg`, `.png`, `.bmp`, `.gif`) are detected.
2. **Caption Generation**
   - The pre-trained model provided by Hugging Face (`Salesforce/blip-image-captioning-base`) is used.
   - The model analyzes the images and generates captions in natural language.
3. **Saving the Results**
   - The caption for each image is saved as a text file in the `captions/` folder.

#### 3. **Overall Structure**
The application is modular, consisting of the following files, each with specific responsibilities:

- **`main.py`**
  - The entry point of the application, responsible for launching the GUI.
  
- **`utils/file_handler.py`**
  - Provides functionality to fetch image files within a folder.
  
- **`utils/caption_generator.py`**
  - Wraps the Hugging Face caption generation model, providing the caption generation functionality.

- **`app/gui.py`**
  - Handles the construction of the GUI interface and event handling.

- **`data/`**
  - Folder for managing input images and output captions.

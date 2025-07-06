# Image to 3D Mesh Converter

This project provides a web-based application that converts the dark areas of an uploaded image into a 3D mesh and provides the output as both OBJ and FBX files.

## Prerequisites

- Python 3.7+
- Blender (must be installed and accessible via the command line)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/tatsuya1970/image-to-3d-converter.git
    cd image-to-3d-converter
    ```

2.  **Install Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure the Blender Path:**
    Open the `main.py` file and update the `BLENDER_EXECUTABLE` variable to the absolute path of your Blender executable. For example:

    - **Windows:** `BLENDER_EXECUTABLE = "C:\Program Files\Blender Foundation\Blender 4.1\blender.exe"`
    - **macOS:** `BLENDER_EXECUTABLE = "/Applications/Blender.app/Contents/MacOS/Blender"`
    - **Linux:** `BLENDER_EXECUTABLE = "/usr/bin/blender"`

## How to Run

1.  **Start the web server:**
    ```bash
    python main.py
    ```

2.  **Open the application:**
    Open your web browser and navigate to `http://localhost:8000`.

3.  **Upload an image:**
    - Click the "Choose File" button and select an image file.
    - Click "Submit".
    - The application will process the image, which may take a few moments.

4.  **Download the results:**
    Once processing is complete, download links for the generated `.obj` and `.fbx` files will appear.


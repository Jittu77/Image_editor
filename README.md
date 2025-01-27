# Image Processing and Conversion Application

## Overview
This is a Flask-based web application that provides various image processing and conversion functionalities. Users can upload an image and perform operations like resizing, cropping, rotating, applying effects, adjusting brightness/contrast, and converting images to different formats (PDF, DOCX, PNG, etc.).

---

## Features

1. **Upload and Process Images:**
   - Supported formats: `.webp`, `.png`, `.jpg`, `.jpeg`, `.gif`.

2. **Image Processing Operations:**
   - Grayscale Conversion.
   - Rotation (by degree).
   - Cropping (by specifying coordinates).
   - Resizing.
   - Blurring.
   - Adjusting Brightness.
   - Adjusting Contrast.

3. **Special Effects:**
   - Alchemy.
   - Mercury.
   - Wacko.
   - Unstable.
   - Ore.
   - Contour.
   - Snicko.

4. **Image Format Conversion:**
   - Convert to PDF.
   - Convert to DOCX (with image included).
   - Convert to PNG, JPEG, JPG.

5. **View History:**
   - A page to view processed images stored in the `static` folder.

6. **About Page:**
   - Provides details about the application and its usage.

---

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Create the following directories if they don't exist:
   - `uploads/`: For storing uploaded files.
   - `static/`: For storing processed images.

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the app in your browser at:
   ```
   http://127.0.0.1:5000/
   ```

---

## Folder Structure
```
|-- app.py                  # Main application script
|-- templates/              # HTML templates
|   |-- index.html          # Home page
|   |-- img-pdf-doc.html    # Conversion page
|   |-- effects.html        # Effects page
|   |-- background.html     # Background change page
|   |-- history.html        # History page
|   |-- about.html          # About page
|-- static/                 # Folder for storing processed images
|-- uploads/                # Folder for storing uploaded images
|-- requirements.txt        # Python dependencies
```

---

## Usage Instructions

1. **Upload an Image:**
   - Navigate to the homepage (`/`).
   - Upload your image using the file input.

2. **Apply Effects:**
   - Go to the **Effects** page (`/effects`).
   - Choose an effect from the dropdown and submit.

3. **Convert Image Format:**
   - Go to the **Convert** page (`/convert`).
   - Select the desired format and submit.

4. **View Processed Images:**
   - Visit the **History** page (`/history`) to view all processed images.

5. **About the App:**
   - Visit the **About** page (`/about`) for more details.

---

## Configuration

- **Upload Folder:** Modify `UPLOAD_FOLDER` in `app.py` to change the directory where uploaded files are stored.
- **Allowed File Extensions:** Add or remove formats in the `ALLOWED_EXTENSIONS` set.

---

## Notes

- Make sure to have OpenCV (`cv2`) and other required libraries installed before running the application.
- Images processed are stored in the `static/` directory.
- Avoid uploading very large files to prevent server slowdowns.

---

## Dependencies

- Flask
- OpenCV (`cv2`)
- NumPy
- python-docx
- img2pdf
- Werkzeug

---

## Authors
Jitendra Kumar - Backend Developer.
Pankaj Rishi - FrontEnd Developer.

## License

This project is licensed under the MIT License.

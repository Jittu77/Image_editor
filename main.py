from flask import Flask, request, render_template, flash, send_file, send_from_directory
from werkzeug.utils import secure_filename
import os
import cv2  # opencv python library
import numpy as np


# upload file settings
UPLOAD_FOLDER = "uploads"
ALLOWED_EXTENSIONS = {"webp", "png", "jpg", "jpeg", "gif"}

# base dir
basedir = os.path.abspath(os.path.dirname(__file__))

# init flask app
app = Flask(__name__)
app.secret_key = "super secret key"

# apps upload folder
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


# limiting allowed files
def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


# processing image
def processImage(filename, operation):
    
    
    img = cv2.imread(f"{basedir}/uploads/{filename}")
    # print(filename, operation)
    if operation=="uploadImage":
        return filename
    # convert to grayscale
    elif operation=="cgray":
        print(filename, operation)
        print("done 1")
        name = filename
        imgProcessed = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        print("done2")
        newFile = f"{basedir}/static/{filename}"
        print("donr3")
        cv2.imwrite(newFile, imgProcessed)
        print("done4")
        return name

    # convert to png, jpeg, jpg file
    
    elif operation in ["cpng", "cjpeg", "cjpg"]:
        name = f"{filename.split('.')[0]}.{operation[1:]}"
        newFile = f"{basedir}/static/{filename.split('.')[0]}.{operation[1:]}"
        cv2.imwrite(newFile, img)
        return name

    # rotate an image
    
    elif operation == 'degree':
        name = filename
        angle = float(request.form.get('degree'))
        height, width = img.shape[:2]
        rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)

        # Apply the rotation to the image
        rotated_image = cv2.warpAffine(img, rotation_matrix, (width, height))
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile, rotated_image)
        return name
    # crop an image
    
    elif operation == 'cutting_edge_values':
        name = filename
        x1 = int(request.form.get('x1'))
        x2 = int(request.form.get('x2'))
        y1 = int(request.form.get('y1'))
        y2 = int(request.form.get('y2'))
        height, width = img.shape[:2]
        # checking the possibilty to crop
        crop_possible = True
        if not 0 <= x1 < width:
            crop_possible = False
        if not 0 < x2 <= width:
            crop_possible = False
        if not 0 <= y1 < height:
            crop_possible = False
        if not 0 < y2 <= height:
            crop_possible = False
        if not x1 < x2:
            crop_possible = False
        if not y1 < y2:
            crop_possible = False
        if crop_possible:
            print(filename, operation)
            
            imgProcessed = img[y1:y2, x1:x2]  # OpenCV slicing: [y1:y2, x1:x2]
            
            newFile = f"{basedir}/static/{filename}"
            
            cv2.imwrite(newFile, imgProcessed)
            print(filename, operation)
            return name
            
    # resize the crop
    elif operation == 'resize':
        new_height=int(request.form.get('newWidth'))
        new_width=int(request.form.get('newWidth'))
        new_points = (new_height, new_width)
        newFile = f"{basedir}/static/{filename}"
        resized_img = cv2.resize(img, new_points, interpolation= cv2.INTER_LINEAR)
        cv2.imwrite(newFile, resized_img)

        return filename
        
    # blur an  image
    elif operation == 'blur':
        kernal=int(request.form.get('blurValue'))
        blurred_image = cv2.blur(img, (kernal, kernal))
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile, blurred_image)
        return filename
        
    # manage brightness
    elif operation=="brightness":
        value=int(request.form.get('brightness'))
        zero=np.zeros(img.shape,img.dtype)
        bright_img = cv2.addWeighted(img,1,zero,0,value)
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,bright_img)
        return filename
        
    # manage contrast
    elif operation=="contrast":
        value=float(request.form.get('contrast'))
        zero=np.zeros(img.shape,img.dtype)
        con = cv2.addWeighted(img,value,zero,0,0)
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,con)
        return filename
    
    elif operation=="alchemy":
        rgb=cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        alchemy=cv2.fastNlMeansDenoisingColored(rgb,None,20,10,7,21)
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,alchemy)
        return filename
        
    # applying mercury effect
    elif operation=="mercury":
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        clahe = cv2.createCLAHE() 
        clahe_img = clahe.apply(gray)
        mercury =cv2.fastNlMeansDenoising(clahe_img,None,40,7,21)
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,mercury)
        return filename
        
    # applying wacko effect
    elif operation=="wacko":
        hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        _,s,v=cv2.split(hsv)
        wacko= cv2.merge([s,v,v])        
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,wacko)
        return filename

    # applying unstable effect
    elif operation=="unstable":
        kernel=np.array([[0.272, 0.534, 0.131],[0.349, 0.686, 0.168],[0.393, 0.769, 0.189]])
        unstable=cv2.filter2D(img, -1, kernel)       
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,unstable)
        return filename

    # applying ore effect
    elif operation=="ore":
        kernel=np.array([[0,-1,-1],[1,0,-1],[1,1,0]])
        ore=cv2.filter2D(img, -1, kernel)      
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,ore)
        return filename

    # applying contour effect
    elif operation=="contour":    
        denoised_color=cv2.fastNlMeansDenoisingColored(img, None, 10, 10, 7, 21)
        gray=cv2.cvtColor(denoised_color,cv2.COLOR_BGR2GRAY)
        adap=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,1)
        contours,hierarchy=cv2.findContours(adap,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        contour=denoised_color.copy()
        color=(255,255,255)
        for c in contours:
            cv2.drawContours(contour,[c],-1,color,1)                
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,contour)
        return filename

    # applying snicko effect
    elif operation=="snicko":
        clone=img.copy()
        denoised=cv2.fastNlMeansDenoisingColored(clone, None, 5, 5, 7, 21)
        snicko=cv2.Canny(denoised,100,200)      
        newFile = f"{basedir}/static/{filename}"
        cv2.imwrite(newFile,snicko)
        return filename
    
   
    
    


# # first web page
@app.route("/")
def index():
    return render_template("index.html")

# effects web page
@app.route("/effects")
def effects():
    return render_template("effects.html")

# changing the effect of an image
@app.route("/effect", methods=["GET", "POST"])
def effect():
    global processedImg
    # operation = request.form.get("operation")
    

    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file Submission")
            return render_template("index.html")
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return render_template("index.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir, app.config["UPLOAD_FOLDER"], filename))
            # Image processing
            if request.form.get("operation")=="uploadImage":
                abc=7
            else:
                abc=None
            if request.form['submit'] == "type_change":
                
                processedImg = processImage(filename, request.form.get("operation"))
                return render_template("effects.html", image_name=processedImg, abc=abc)

# visit out latest work page (portfolio place)
@app.route("/history")      
def history():
    # Get list of image filenames from the static folder
    image_files = os.listdir('static')
    
    # Filter out non-image files
    image_files = [filename for filename in image_files if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

    # Calculate the number of rows needed for the table
    num_rows = (len(image_files) + 2) // 3
    
    return render_template('history.html', image_files=image_files, num_rows=num_rows)

# render to about section page
@app.route("/about")
def about():
    return render_template('about.html')

processedImg=""
# image editing
# edit main section for edit page
@app.route("/edit", methods=["GET", "POST"])
def edit():
    global processedImg
    # operation = request.form.get("operation")
    

    if request.method == "POST":
        # check if the post request has the file part
        if "file" not in request.files:
            flash("No file Submission")
            return render_template("index.html")
        file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == "":
            flash("No selected file")
            return render_template("index.html")
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(basedir, app.config["UPLOAD_FOLDER"], filename))
            # Image processing
            if request.form.get("operation")=="uploadImage":
                abc=7
            else:
                abc=None
            if request.form['submit'] == "type_change":
                
                processedImg = processImage(filename, request.form.get("operation"))
                return render_template("index.html", image_name=processedImg, abc=abc)


    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)



import os
from flask import Flask, request  
from werkzeug.utils import secure_filename

### Unrelated to the exercise -- Starts here -- Please ignore
app = Flask(__name__)
@app.route("/")
def source():
    TaxPayer('foo', 'bar').get_tax_form_attachment(request.args["input"])
    TaxPayer('foo', 'bar').get_prof_picture(request.args["input"])
### Unrelated to the exercise -- Ends here -- Please ignore

# Function to validate Path of file and perform checks
def validatePath(path, base_dir=os.path.dirname(os.path.abspath(__file__))):
    fileName = secure_filename(path)
    validatedPath = os.path.normpath(os.path.join(base_dir, fileName))

    return validatedPath;

# Function To check is file exist
def IsFileExist(fileName):
    return os.path.isfile(fileName);

class TaxPayer:
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.prof_picture = None
        self.tax_form_attachment = None

    # returns the path of an optional profile picture that users can set        
    def get_prof_picture(self, path=None):
        # setting a profile picture is optional
        if not path:
            pass
        
        # defends against path traversal attacks
        if path.startswith('/') or path.startswith('..'):
            return None
        
        # builds path
        prof_picture_path = validatePath(path)
    
        # opening if file exists
        if IsFileExist(prof_picture_path):
                with open(prof_picture_path, 'rb') as pic:
                    return pic.read()
                
        return prof_picture_path

    # returns the path of an attached tax form that every user should submit
    def get_tax_form_attachment(self, path=None):
        tax_data = None
        
        if not path:
            raise Exception("Error: Tax form is required for all users")
       
        # validate the input path
        text_data_path = validatePath(path)
        
        # opening if file exists
        if IsFileExist(text_data_path):
            with open(text_data_path, 'rb') as form:
                tax_data = bytearray(form.read())

        # assume that taxa data is returned on screen after this
        return path
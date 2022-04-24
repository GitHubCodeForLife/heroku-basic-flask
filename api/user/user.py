from flask import Blueprint, request
import os

from werkzeug.utils import secure_filename

from helper.FileHelper import FileHelper
fileHelper = FileHelper()

user_blueprint = Blueprint('user_blueprint', __name__)


@user_blueprint.route('/', methods=['GET'])
def index():
    s = os.getenv("SECRET_KEY")
    print("secret key: ", s)
    return 'user'


@user_blueprint.route('/upload', methods=['POST'])
def upload():
    UPLOAD_FOLDER = './static/uploads/'
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(UPLOAD_FOLDER + filename)
    # url = "/dvfmeif0y/raw/upload/v1650710696/porju0dwrnwyktsialt1.csv"
    # public_id = "cekk3dylhk7cywmolybr.csv"
    result = fileHelper.upload_file(UPLOAD_FOLDER+filename)
    # result = fileHelper.update_file_upload(
    #     UPLOAD_FOLDER+filename, public_id)
    return result


@user_blueprint.route('/upload', methods=['GET'])
def get_upload():
    # return form upload
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@user_blueprint.route('/update_upload', methods=['GET'])
def get_upload_update():
    # return form upload
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''


@user_blueprint.route('/update_upload', methods=['POST'])
def update_upl():
    UPLOAD_FOLDER = './static/uploads/'
    file = request.files['file']
    filename = secure_filename(file.filename)
    file.save(UPLOAD_FOLDER + filename)
    public_id = "cezgdvfxkgntutfkhgmz.csv"
    result = fileHelper.update_file_upload(
        UPLOAD_FOLDER+filename, public_id)
    return result

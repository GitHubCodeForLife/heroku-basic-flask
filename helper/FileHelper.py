# from dotenv import load_dotenv
import imp
import cloudinary
import cloudinary.uploader
import cloudinary.api
import requests
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env')


class FileHelper:
    def __init__(self):
        self.cloudinary = cloudinary.config(
            cloud_name="dvfmeif0y",
            api_key="662568823432849",
            api_secret="bNKY_tPvbMlGYOzF2grPXD9t3SA",
            secure=True
        )
        print("cloudinary config: ", os.getenv("cloud_name"))

    def upload_image(self, file_path):

        resource_type = "image"
        return cloudinary.uploader.upload(file_path, resource_type=resource_type)

    def upload_file(self, file_path):

        resource_type = "raw"
        return cloudinary.uploader.upload(file_path, resource_type=resource_type)

    def downloadFileFromURL(self, url):
        print("current os path: ", url)
        file_name = url.split("/")[-1]
        file_path = "./static/download/" + file_name
        r = requests.get(url, allow_redirects=True)
        open(file_path, 'wb').write(r.content)
        return file_path

    def downloadFileFromCloudinary(self, public_id):
        file_path = "./static/download/" + public_id
        cloudinary.uploader.download(public_id, file_path)
        return file_path

    def update_file_upload(self, file_path, public_id):
        # update file in cloudinary storage
        resource_type = "raw"
        return cloudinary.uploader.upload(file_path, public_id=public_id, resource_type=resource_type)

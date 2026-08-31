from google.colab import files


def upload_pdf():
    uploaded = files.upload()
    return uploaded

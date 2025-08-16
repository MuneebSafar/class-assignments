import os  
import shutil

directory = "/Users/User/Desktop"
font_extensions = [".ttf", ".otf", ".woff", ".woff2", ".eot"]
document_extensions = [".pdf", ".docx", ".xlsx", ".pptx"]
other_extensions = [".zip", ".rar", ".7z", ".tar", ".gz"]
image_extensions = [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg"]
video_extensions = [".mp4", ".avi", ".mov", ".mkv", ".wmv", ".flv"]

for file in os.listdir(directory):
    name, ext = os.path.splitext(file)

    # 1: Only for videos
    if ext in video_extensions:
        video_repo = f"{directory}/video"
        if not os.path.exists(video_repo):
            os.makedirs(video_repo)
        if not os.path.exists(f"{video_repo}/{file}"):
            shutil.move(f"{directory}/{file}", video_repo)

    # 2:Only for Images
    if ext in image_extensions:
        image_repo = f"{directory}/image"
        if not os.path.exists(image_repo):
            os.makedirs(image_repo)
        if not os.path.exists(f"{image_repo}/{file}"):
            shutil.move(f"{directory}/{file}", image_repo)

    # 3 : Only for fonts.
    if ext in font_extensions:
        font_repo = f"{directory}/Fonts"
        if not os.path.exists(font_repo):
            os.makedirs(font_repo)
        if not os.path.exists(f"{font_repo}/{file}"):
            shutil.move(f"{directory}/{file}", font_repo)

    # 4: Only for Documents.
    if ext in document_extensions:
        documents_repo = f"{directory}/Documents"
        if not os.path.exists(documents_repo):
            os.makedirs(documents_repo)
        if not os.path.exists(f"{documents_repo}/{file}"):
            shutil.move(f"{directory}/{file}", documents_repo)

    # 5: For other type of Files
    if ext in other_extensions:
        other_repo = f"{directory}/other"
        if not os.path.exists(other_repo):
            os.makedirs(other_repo)
        if not os.path.exists(f"{other_repo}/{file}"):
            shutil.move(f"{directory}/{file}", other_repo)
"""Create home blueprint  and all the views in it here.
"""

from flask import Blueprint, render_template, request, jsonify
from models import UtilImage, ModelImage

main = Blueprint('main', __name__,
                 url_prefix='/main',
                 template_folder='templates',
                 static_folder='static')


@main.route('/obtencionimagenes')
def home():
    # https://dribbble.com/tags/image_upload
    # https://dribbble.com/shots/15832392-File-Upload-DailyUI-031
    return render_template('main/upload_images.html')


@main.route('/links')
def links():
    # https://dribbble.com/tags/image_upload
    # https://dribbble.com/shots/15832392-File-Upload-DailyUI-031
    return render_template('main/links.html')


@main.route('/convertir_images_excel', methods=['POST'])
def convertir_images_excel():
    try:
        json_images = request.json
        list_images = ModelImage().get_images(json_images)

    except Exception as e:
        print(f'error: {e}')
    return jsonify({'message': 'Success'})

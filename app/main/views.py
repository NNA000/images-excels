"""Create home blueprint  and all the views in it here.
"""

from flask import Blueprint, render_template, request, jsonify
from .models import UtilImage, ModelImage, ResponseMethod

main = Blueprint('main', __name__,
                 url_prefix='/main',
                 template_folder='templates',
                 static_folder='static')


@main.route('/obtencionimagenes')
def home():
    return render_template('main/upload_images.html')


@main.route('/links')
def links():
    return render_template('main/links.html')


@main.route('/convert_image_excel', methods=['POST'])
def convert_image_excel():
    try:
        json_images = request.json
        list_images = ModelImage().get_images(json_images)
        lista_data = ModelImage().get_data_images(list_images)
        # Save in xlsx in multiple sheets by name
        response: ResponseMethod = ModelImage().save_dfs_csv(lista_data)
        return response.get_json_response(), 200
    except Exception as e:
        print(f'error: {e}')
        return jsonify({'message': 'Error'}), 500

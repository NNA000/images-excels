"""Create home blueprint  and all the views in it here.
"""

from flask import Blueprint, render_template

main = Blueprint('main', __name__,
                 url_prefix='/main',
                 template_folder='templates',
                 static_folder='static')


@main.route('/obtencionimagenes')
def home():
    # https://dribbble.com/tags/image_upload
    # https://dribbble.com/shots/15832392-File-Upload-DailyUI-031
    return render_template('main/upload_images.html')

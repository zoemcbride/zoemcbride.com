from flask_frozen import Freezer
from my_flask_app.app import app

freezer = Freezer(app)

# Set the output directory to '/docs'
# freezer.register_generator(..., output_dir='/docs')

if __name__ == '__main__':
    freezer.freeze()
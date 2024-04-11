from flask import Flask, request, render_template, send_file
from PIL import Image
from rembg import remove

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/remove_background', methods=['POST'])
def remove_background():
    # Get the uploaded image file
    image = request.files['image']

    # Save the image to a temporary file
    input_path = 'temp_image.jpg'
    image.save(input_path)

    # Perform background removal
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_path = 'temp_output.png'
    output_image.save(output_path)

    # Provide the result message to the HTML template
    message = 'Background removed successfully'

    # Return the result message and the processed image to the user
    return render_template('index.html', message=message, output_path=output_path)

@app.route('/download_processed', methods=['GET'])
def download_processed():
    # Define the path to the processed image
    processed_image_path = 'temp_output.png'

    # Download the processed image
    return send_file(processed_image_path, as_attachment=True)

if __name__ == '__main__':
    app.run()

# from rembg import remove
# from PIL import Image
# input_path = "lambo.jpg"
# output_path = "lambo_removed.png"
# input = Image.open(input_path)
# output = remove(input)
# output.save(output_path)
# # print(output)


from rembg import remove
from PIL import Image

def remove_background(input_path, output_path):
    input_image = Image.open(input_path)
    output_image = remove(input_image)
    output_image.save(output_path)

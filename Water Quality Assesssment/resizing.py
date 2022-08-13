import os
from PIL import Image

def resize_image(input_dir, infile, output_dir='resized', size=(512,512)):
    outfile = os.path.splitext(infile)[0] + '_resized'
    extension = os.path.splitext(infile)[1]

    try:
        img = Image.open(input_dir + '/' + infile)
        img = img.resize((size[0], size[1]), Image.LANCZOS)

        new_file = output_dir + '/' + outfile + extension
        img.save(new_file)
    except IOError:
        print('unable to resize image {}'.format(infile))

if __name__ == '__main__':
    output_dir = 'real_resized'
    dir = os.getcwd()
    input_dir = 'real'
    full_input_dir = dir + '/' +input_dir

    if not os.path.exists(os.path.join(dir,output_dir)):
        os.mkdir(output_dir)

    try:
        for file in os.listdir(full_input_dir):
            resize_image(input_dir, file, output_dir)
    except OSError:
        print('file not fount')

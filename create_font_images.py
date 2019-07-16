import os
from tqdm import tqdm

from PIL import Image, ImageDraw, ImageFont
from IPython.display import Image as ImageDisplay
from pathlib import Path
import glob

# Set up the letters being snapshotted

alphabet_uppercase = ['A','B','C','D','E','F','G','H','I','J',
                      'K','L','M','N','O','P','Q','R','S','T',
                      'U','V','W','X','Y','Z']

# Backbone of the image generation

# selected_font_family(string)
# postfix(string)
def loop_through_alphabet(font_file_path, family_name, font_file, postfix):
    target_letters = alphabet_uppercase
    for letter in target_letters:
        # W, H = (1280, 720) # image size
        W, H = (1600, 2000) # image size
        txt = letter # text to render
        background = (255,255,255) # white
        fontsize = 800
        font = ImageFont.truetype(font_file_path, fontsize)

        image = Image.new('RGBA', (W, H), background)
        draw = ImageDraw.Draw(image)

        # w, h = draw.textsize(txt) # not that accurate in getting font size
        w, h = font.getsize(txt)

        draw.text(((W-w)/2,(H-h)/2), txt, fill='black', font=font)
        # draw.text((10, 0), txt, (0,0,0), font=font)
        # img_resized = image.resize((188,45), Image.ANTIALIAS)

        save_location = os.getcwd() + '/images/' + letter + '/'

        if not os.path.exists(save_location):
            os.makedirs(save_location)
        
        # img_resized.save(save_location + '/sample.jpg')
        file_name = '/' + family_name + '-' + font_file + '-' +'-letter-' + letter + '-' + postfix + '.png'
        final_path = save_location + file_name
        if not os.path.exists(final_path):
            image.save(final_path)

def prepare_font_files_from_google_fonts():
    font_families = []
    for filepath in glob.glob('fonts/ofl/**/*.ttf'):
        folder_name = filepath.split('fonts/ofl/')
        family = folder_name[1].split('/')[0]
        font_file = folder_name[1].split('/')[1].split('.ttf')[0]
        font_item = { 'family': family, 'font_file': font_file}
        font_families.append(font_item)
    return font_families

font_families = prepare_font_files_from_google_fonts()

for font_obj in tqdm(font_families):
    family_name = font_obj['family']
    font_file = font_obj['font_file']
    font_family_path = 'fonts/ofl/' + family_name + '/' + font_file + '.ttf'
    try:
        loop_through_alphabet(font_family_path, family_name, font_file, 'uc')
    except Exception:
        pass

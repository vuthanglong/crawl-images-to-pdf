import argparse
from PIL import Image
from tqdm import tqdm
from pathlib import Path
from config import cfg

def convert_images_folder_to_pdf(output,end_idx,start_idx=1,imgs_dir='imgs',output_dir='pdf',ext='.jpg'):
  print(f'Start converting images from {imgs_dir}')
  img_list = []

  for i in tqdm(range(start_idx, end_idx + 1)):
    with Image.open(f'./{imgs_dir}/{i}{ext}') as image:
      img_list.append(image.convert('RGB'))
      
  Path(f'./{output_dir}').mkdir(parents=True, exist_ok=True)
  
  if not img_list:
    print(r"No image was found from image directory.")
  else:
    img_list[0].save(f'./{output_dir}/{output}', save_all=True, append_images=img_list[1:])
    print(f'Converting to PDF completed. Output at: /{output_dir}/{output}')

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--cfg_file', default='config.yml', help='Config file for converting ( must be in "./config" directory )')
  opt = parser.parse_args()
  cfg.merge_from_file(f'./config/{opt.cfg_file}')
  cfg.freeze()
  convert_images_folder_to_pdf(cfg.OUTPUT, cfg.END_INDEX, cfg.START_INDEX, cfg.IMG_DIR, cfg.OUTPUT_DIR, cfg.IMG_EXTENSTION)

if __name__ == '__main__':
  main()
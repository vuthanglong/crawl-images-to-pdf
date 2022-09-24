import argparse
from config import cfg
from crawl_imgs import crawl_imgs
from convert_to_pdf import convert_images_folder_to_pdf

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--cfg_file', default='config.yml', help='Config file for images crawling ( must be in "./config" directory )')
  opt = parser.parse_args()
  cfg.merge_from_file(f'./config/{opt.cfg_file}')
  cfg.freeze()
  
  crawl_imgs(cfg.URL_PREFIX, cfg.IMG_EXTENSTION, cfg.FILL_TO, cfg.START_INDEX, cfg.END_INDEX, cfg.IMG_DIR)
  convert_images_folder_to_pdf(cfg.OUTPUT, cfg.END_INDEX, cfg.START_INDEX, cfg.IMG_DIR, cfg.OUTPUT_DIR, cfg.IMG_EXTENSTION)

if __name__ == '__main__':
  main()
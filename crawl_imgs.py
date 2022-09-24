import argparse
import requests
from tqdm import tqdm
from pathlib import Path
from config import cfg

def get_pic_url(prefix, index, extentsion, fill_to):
  return f'{prefix}{str(index).zfill(fill_to)}{extentsion}'

def crawl_imgs(prefix, extentsion, fill_to, start_idx, end_idx, imgs_dir):
  print(f'Downloading images from: {prefix}')

  with tqdm(range(start_idx, end_idx + 1)) as t:
    for i in t:
      pic_url = get_pic_url(prefix, i, extentsion, fill_to)
      t.set_description(f'{pic_url.replace(prefix,"")}')
      
      Path(f'./{imgs_dir}').mkdir(parents=True, exist_ok=True)
      with open(f'{imgs_dir}/{i}{extentsion}', 'wb') as handle:
        response = requests.get(pic_url, stream=True)

        if not response.ok:
            print(response)

        for block in response.iter_content(1024):
            if not block:
                break

            handle.write(block)
  print(f'Download completed. Images are located at: /{imgs_dir}')

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--cfg_file', default='config.yml', help='Config file for images crawling ( must be in "./config" directory )')
  opt = parser.parse_args()
  cfg.merge_from_file(f'./config/{opt.cfg_file}')
  cfg.freeze()
  crawl_imgs(cfg.URL_PREFIX, cfg.IMG_EXTENSTION, cfg.FILL_TO, cfg.START_INDEX, cfg.END_INDEX, cfg.IMG_DIR)

if __name__ == '__main__':
  main()
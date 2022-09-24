# Crawl Images To PDF
This script is for crawling multiple images on the internet and converting them into a single PDF file.

## Requirements
- Python3, pip

## Usage
### 1. Install dependencies
- (**Recommended**) Create a virtual environment & activate :
```
python3 -m venv venv
source venv/bin/activate
```
- Install dependencies with `pip` :
```
pip install -r requirements.txt
```
### 2. Config
Edit `config.yml` in `/config` directory to suit your needs. Things you should change are:
* **URL_PREFIX**: string URL of the website contains images you want to crawl. (everything except the images' name)
* **FILL_TO**: number indicates how images' names are constructed. 
  (for example: **FILL_TO**: 5 will convert index '1' -> '00001'. This is how the script is currently working. You can change how the script constructs the path to the images by modifying the `get_pic_url()` function in `crawl_imgs.py`)
* **IMG_EXTENSTION**: default is '.jpg'.
* **START_INDEX**: number indicates where to start iterating images' names. The default is 1.
* **END_INDEX**: total number of images you want to crawl.

* **IMG_DIR**: name of the directory to store your crawled images.

* **OUTPUT**: name of the final pdf.
* **OUTPUT_DIR**: name of the directory to store your final pdf.

### 3. Run the script
```
python3 run_crawl_and_convert.py
```
- You can create another `.yml` file in `/config` directory and pass it to the script by using the `--cfg_file` flag :
```
python3 run_crawl_and_convert.py --cfg_file=[your-file-name].yml
```
> Both `crawl_imgs.py` and `convert_to_pdf.py` can be run separately. `run_crawl_and_convert.py` simply calls both of them.

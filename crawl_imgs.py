import requests

def get_pic_url(i):
  return 'http://thuvien.hmu.edu.vn/pages/cms/TempDir/books/4393e103-0ffa-4a0d-8670-1726750491f0/2021/12/30/202112301044-fe7bdee8-958b-4d11-a623-faa5ecfd2392/FullPreview/000%s.jpg' % i

for i in range(1,353):
  pic_url = get_pic_url(str(i).zfill(3))
  print('downloading: %s' % pic_url)
  with open('imgs'+'/%s.jpg' % (i), 'wb') as handle:
    response = requests.get(pic_url, stream=True)

    if not response.ok:
        print(response)

    for block in response.iter_content(1024):
        if not block:
            break

        handle.write(block)
import requests #pip install requests

url = 'http://.../resoluteqa/upload_mstest/#' #replace ... and #
files = {'xmlfile': open('file.xml','rb')}

r = requests.post(url, files=files)

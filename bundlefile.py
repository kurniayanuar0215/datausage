import os
import zipfile
from datetime import datetime, timedelta

date_1 = datetime.today() - timedelta(days=7)
date_2 = datetime.today() - timedelta(days=1)
day1 = date_1.strftime("%Y-%m-%d")
day2 = date_2.strftime("%Y-%m-%d")

fantasy_zip = zipfile.ZipFile('F:\\KY\\data_usage\\archive\\DU_'+day1+'_'+day2+'.zip', 'w')

for folder, subfolders, files in os.walk('F:\\KY\\data_usage\\download'):

    for file in files:
        if file.endswith('.csv'):
            fantasy_zip.write(os.path.join(folder, file), os.path.relpath(os.path.join(folder,file), 'F:\\KY\\data_usage\\download'), compress_type = zipfile.ZIP_DEFLATED)

fantasy_zip.close()

dir = 'F:/KY/data_usage/download'
for f in os.listdir(dir):
    os.remove(os.path.join(dir, f))

os.environ["https_proxy"] = "https://10.59.66.1:8080"
os.system("telegram-send --file F:/KY/data_usage/archive/DU_"+day1+"_"+day2+".zip")


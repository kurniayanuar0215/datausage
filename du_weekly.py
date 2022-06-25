import mysql.connector
import pandas as pd
import os
from datetime import datetime, timedelta

date_1 = datetime.today() - timedelta(days=7)
date_2 = datetime.today() - timedelta(days=1)
day1 = date_1.strftime("%Y-%m-%d")
day2 = date_2.strftime("%Y-%m-%d")

# DB CONFIG
conn = mysql.connector.connect(
    host="10.47.150.144",
    user="rto_jkt",
    password="Rt0_J4k4Rt4@ts3L",
    database="capmon"
)

query = '''SELECT `SiteID`, `Tipe`, `tanggal`, MAX(`RxMax`), MAX(`RxAvg`)
FROM `capmon`.`sum_traffic_hourly`
WHERE tanggal BETWEEN "'''+day1+'''" AND "'''+day2+'''" AND LEFT(siteid,3) IN (
'BDG','BDK','BDS','CMI','COD',
'BDB','IND','SUB','CRB','CMS',
'KNG','MJL','CJR','CRJ','SMD',
'BJR','TSK','GRT','PAN','BDX') AND tipe IN ('S1','IUB','ABIS')
GROUP BY `SiteID`, `Tipe`, `tanggal`;'''

name_file = 'DU_WEEKLY_'+day1+'-'+day2+'.csv'
df = pd.read_sql(query, conn)

df.to_csv(
    '''F:/KY/data_usage/download/'''+name_file, index=False)

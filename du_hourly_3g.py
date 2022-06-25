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

query = '''SELECT a.`SiteID`, a.`Tipe`, a.`tanggal`, LEFT(a.`jam`,5) jam, YEAR(a.tanggal) YEAR, WEEK(a.tanggal,4) WEEK, DAY(a.tanggal) DAY,
b.`kabupaten`, b.`kecamatan`, CONCAT(b.`kabupaten`,'-',b.`kecamatan`) kabkec, b.`branch`, b.`cluster`, b.`rtp`,
a.`RxMax`, a.`RxAvg`
FROM `capmon`.`sum_traffic_hourly` a
LEFT JOIN `test`.`dapot_sitename` b
ON a.`SiteID` = b.`site_id`
WHERE a.tanggal BETWEEN "'''+day1+'''" AND "'''+day2+'''" AND a.tipe IN ('iub') AND b.`region` = 'JABAR'
GROUP BY `SiteID`, `Tipe`, `tanggal`, `jam`;'''

name_file = 'DU_HOURLY_3G_'+day1+'-'+day2+'.csv'
df = pd.read_sql(query, conn)

df.to_csv(
    '''F:/KY/data_usage/download/'''+name_file, index=False)

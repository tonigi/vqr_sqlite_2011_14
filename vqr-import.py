import sqlite3
import xlrd
import glob
import os.path
import re

indir="/home/toni/work/anvur/ALLGEVS/xls"

conn = sqlite3.connect('vqr.db')

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS soglie')
c.execute('''CREATE TABLE soglie (GEV text, VENDOR text, CATEGORY text, YEAR text, METRIC_NAME text, TYPE text,
                                  JOURNAL text, CODE text, METRIC real, THRA text, THRB text,
                                  THRC text, THRD text, THRE text, IRh TEXT, IRl TEXT ) ''' )

xlslist=glob.glob(indir+'/*.xls')

for x in xlslist:
    fn=os.path.basename(x)
    fn,ext=os.path.splitext(fn)

    fn=re.sub(r"scopus-[0-9][0-9][0-9][0-9]-(.+?)-",'scopus-\\1-',fn)

    try:
        gev,vendor,category,year,metric_name,type=fn.split('-')
    except:
        print("ERROR: file name %s does not parse" % fn)
        continue

    wb=xlrd.open_workbook(x)
    ws=wb.sheet_by_index(0)

    for i in range(1,ws.nrows):
        row=ws.row_values(i)
        if len(row) != 10:
            print("ERROR: file %s has %d columns, not the expected 10" % (x,len(row)))
            break

        rowl = [ gev,vendor,category,year,metric_name,type ] + row
        c.executemany( '''INSERT INTO soglie values (?, ?, ?, ?, ?, ?,
                                                     ?, ?, ?, ?, ?,
                                                     ?, ?, ?, ?, ?) ''', [rowl] )

conn.commit()
conn.close()


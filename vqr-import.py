import sqlite3
import xlrd
import glob
import os.path

indir="/home/toni/work/anvur/ALLGEVS/xls_r"

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

    gev,vendor,category,year,metric_name,type=fn.split('-')

    wb=xlrd.open_workbook(x)
    ws=wb.sheet_by_index(0)
    rows=ws.get_rows()
    next(rows)

    for row in rows:
        rowl = [ gev,vendor,category,year,metric_name,type ] + row
        c.executemany( '''INSERT INTO soglie values (?, ?, ?, ?, ?, ?,
                                                     ?, ?, ?, ?, ?,
                                                     ?, ?, ?, ?, ?) ''', [rowl] )

conn.commit()
conn.close()


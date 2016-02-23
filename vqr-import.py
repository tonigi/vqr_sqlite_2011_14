import sqlite3
import xlrd
import glob
import os.path
import re
import sys

# Note: try on a subset before
indir="../ALLGEVS/xls"
outdb='vqr.sqlite3'

conn = sqlite3.connect(outdb)

c = conn.cursor()

c.execute('DROP TABLE IF EXISTS thresholds')
c.execute('''CREATE TABLE thresholds (GEV text, VENDOR text, CATEGORY text, YEAR text, METRIC_NAME text, TYPE text,
                                  JOURNAL text, CODE text, METRIC real, THRA text, THRB text,
                                  THRC text, THRD text, THRE text, IRh TEXT, IRl TEXT ) ''' )

xlslist=glob.glob(indir+'/*.xls')
errfile=open("errors.log", "w")
done=0

for x in xlslist:
    fn=os.path.basename(x)
    fn,ext=os.path.splitext(fn)

    # Remove a variety of variations
    fn=re.sub(r"- Copia",'',fn)
    fn=re.sub(r"- Copia",'',fn)  # Repetita juvant
    fn=re.sub(r"Copia di ",'',fn) 
    fn=re.sub(r"scopus-[0-9][0-9][0-9][0-9]-(.+?)-",'scopus-\\1-',fn)
    fn=str.strip(fn)

    spl=re.search(r"^(.+?)-(.+?)-(.+)-(anno.+?)-(.+?)-(.+?)$",fn)
    if spl:
        gev,vendor,category,year,metric_name,type=spl.groups()
    else:
        errfile.write("ERROR: file name %s does not parse\n" % fn)
        continue

    wb=xlrd.open_workbook(x)
    ws=wb.sheet_by_index(0)

    for i in range(1,ws.nrows):
        row=ws.row_values(i)
        rowl = [ gev,vendor,category,year,metric_name,type ] + row
        if len(row) == 5:
            c.executemany( '''INSERT INTO thresholds values (?, ?, ?, ?, ?, ?,
                                                     ?, ?, ?, ?, NULL,
                                                     NULL, NULL, NULL, ?, NULL) ''', [rowl] )
        elif len(row) == 10:
            c.executemany( '''INSERT INTO thresholds values (?, ?, ?, ?, ?, ?,
                                                         ?, ?, ?, ?, ?,
                                                         ?, ?, ?, ?, ?) ''', [rowl] )
        else:
            errfile.write("ERROR: file %s has %d columns, not the expected 5 or 10" % (x,len(row)))

    done=done+1
    print( "Done %d/%d files \r" % (done,len(xlslist)), end="", flush=True)
    sys.stdout.flush()

conn.commit()
conn.close()

print("\nDone, see database "+outdb)

errfile.close()

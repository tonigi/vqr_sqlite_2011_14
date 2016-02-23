import MySQLdb as mdb
import sqlite3
import xlrd
import glob
import os.path
import re
import sys

# Note: try on a subset before
indir="../ALLGEVS/xls"

if len(sys.argv)>1:
    mode=sys.argv[1]
else:
    mode="sqlite3"

    
sql_ins11 = '''INSERT INTO thresholds (gev, vendor, category, year, metric_name, type,
                                       journal, code, metric, thra, IRl) VALUES
                                      (?, ?, ?, ?, ?, ?,
                                       ?, ?, ?, ?, ? ) '''
sql_ins16 = '''INSERT INTO thresholds (gev, vendor, category, year, metric_name, type,
                                       journal, code, metric, thra, thrb,
                                       thrc, thrd, thre, IRh, IRl) VALUES
                                      (?, ?, ?, ?, ?, ?,
                                                         ?, ?, ?, ?, ?,
                                                         ?, ?, ?, ?, ?) '''

if mode == "sqlite3":
    outdb='vqr.sqlite3'
    conn = sqlite3.connect(outdb)
    sql_auto_increment = ""
elif mode == "mysql":
    sql_ins11 = str.replace(sql_ins11,'?','%s')
    sql_ins16 = str.replace(sql_ins16,'?','%s')
    sql_auto_increment = "AUTO_INCREMENT"
    conn=mdb.connect('localhost','root','','vqr')
    conn.autocommit(True)
else:
    raise Error("Wrong mode")

    
c = conn.cursor()
c.execute('DROP TABLE IF EXISTS thresholds')
c.execute('''CREATE TABLE thresholds (gev TEXT, vendor TEXT, category TEXT, year INTEGER, metric_name TEXT, type TEXT,
                                  journal TEXT, code TEXT, metric REAL, thra TEXT, thrb TEXT,
                                  thrc TEXT, thrd TEXT, thre TEXT, irh TEXT, irl TEXT,
                                  id INTEGER NOT NULL PRIMARY KEY %s ) ''' % sql_auto_increment )

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
        year=re.sub(r"anno","",year)
    else:
        errfile.write("ERROR: file name %s does not parse\n" % fn)
        continue

    wb=xlrd.open_workbook(x)
    ws=wb.sheet_by_index(0)

    for i in range(1,ws.nrows):
        row=ws.row_values(i)
        rowl = [ gev,vendor,category,year,metric_name,type ] + row
        if len(rowl) == 11:
            c.executemany( sql_ins11, [rowl] )
        elif len(rowl) == 16:
            c.executemany( sql_ins16, [rowl] )
        else:
            errfile.write("ERROR: file %s has %d columns, not the expected 5 or 10" % (x,len(row)))

    done=done+1
    print( "Done %d/%d files \r" % (done,len(xlslist)), end="", flush=True)
    sys.stdout.flush()

conn.commit()
conn.close()

print("\nDone.")

errfile.close()

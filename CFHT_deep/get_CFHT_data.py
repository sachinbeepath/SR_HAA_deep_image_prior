from cadcdata import CadcDataClient
from cadcutils import net

fname = "cadcUrlList.txt"

with open(fname) as f:
    txt = f.readlines()

txt = [x.strip() for x in txt] 

print(len(txt))

txt = list(map(lambda x : x[73:81],txt))

for pid in txt:
    if "." in pid:
        pid = pid[:-1]
    else:
        pid = pid
    try:
        client = CadcDataClient(net.Subject())
        client.get_file('CFHT', pid + '.fits.fz')
        print(pid)
    except Exception as e: 
        print(e)
        continue


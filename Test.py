import requests
import sys
import json

def conectar(ldata,dst,ptype,src,seq,datalen,SNR,RSSI,bw,cr,sf,tdata,gwid):
        URL = 'http://192.168.1.110/tesis-backend/public/'


        sens = ldata.split("/")
        data = {'nombre':'default_name','lat':0,'long':0,'dst':dst,'ptype':ptype,'src':src,'seq':seq,'len':datalen,'snr':SNR,'rssi':RSSI,'bw':bw,'cr':cr,'sf':sf,'freq':'433.3','gw_id':gwid,'tdata':tdata,'tc':sens[1],'pa':sens[9],'co':se$
        resp = requests.post(URL + 'nodo', data)

        #resp = requests.get(URL + '/{}/'.format(pdata) )

        print(resp.request.body)
        if resp.status_code == 200:
                print ('resp.content')
        elif resp.status_code == 422:
                print('error de validacion', resp.content)
        elif resp.status_code == 201:
                print('datos recibidos por la API', resp.content)
        else:
                print('error de conexion', resp.content)

def main(ldata, pdata, rdata, tdata, gwid):
        arr = map(int,pdata.split(','))
        dst=arr[0]
        ptype=arr[1]
        src=arr[2]
        seq=arr[3]
        datalen=arr[4]
        SNR=arr[5]
        RSSI=arr[6]

        arr = map(int,rdata.split(','))
        bw=arr[0]
        cr=arr[1]
        sf=arr[2]

        #DO-WHATEVER-YOU-NEED-TO-DO-FOR-DATA-UPLOADING

        conectar(ldata,dst,ptype,src,seq,datalen,SNR,RSSI,bw,cr,sf,tdata,gwid)

        #USE-PARAMETERS-AS-YOU-NEED

if __name__ == "__main__":
        main(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

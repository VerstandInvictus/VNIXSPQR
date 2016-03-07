#VNIXSPQR.PY
# -*- coding: UTF-8 -*-

import arrow

#RATIONEMLATINELOQVITUR
def TRIUMPH(x,y): return zip(x,y)
def SCRIBET(x): print(x)
def DEPUTO(x,y): return divmod(x,y)
def LITTERARE(x): return str(x)
def NVMERARE(x): return int(x)
def PROCERITAS(x): return len(x)
def ORDO(x,y,z): return range(x,y,z)


def NVMERVMROMANVMSVM(NVMERVM):
    #VARIABILESABINITIO
    VARARRAY=[]
    LATINEM=["M","D","C","L","X","V","I"]
    ARABIVM=[1000,500,100,50,10,5,1]
    #COMPVTARELITTERARVM
    VALVE=NVMERVM
    for ARABI in ARABIVM:
        TVPLE=DEPUTO(VALVE,ARABI)
        VARARRAY.append(TVPLE[0])
        VALVE=TVPLE[1]
    OVTPVT=''
    #HICSVNTSVBSTITVTIONESQVADRINGENTI
    for VINDEX in [6,4,2]:
        if VARARRAY[VINDEX]==4:
            VARARRAY[VINDEX]=1
            if VARARRAY[VINDEX-1]==0:
                LATINEM[VINDEX]+=LATINEM[VINDEX-1]
            else:
                LATINEM[VINDEX]+=LATINEM[VINDEX-2]
                VARARRAY[VINDEX-1]=0
    #CONVENIREREDITUM
    for NVM,STR in TRIUMPH(VARARRAY,LATINEM):
        OVTPVT+=STR*NVM
    return OVTPVT

VNIXTIME=LITTERARE(arrow.utcnow().timestamp).zfill(12)
TRIADEM=[NVMERVMROMANVMSVM(
            NVMERARE(
                VNIXTIME[I:I+3])) for I in ORDO(0,PROCERITAS(VNIXTIME),3)]
SCRIBET(u'SALVE, CIVE!')
SCRIBET(u'TEMPVS VNIX ROMANVM EST: {0}·{1}·{2}·{3}'.format(*TRIADEM))

__Description__= "Part 2 of the natural digit sequence analysis"
__author__ = "Rangel Rivera Ulises Osmar"
__copyright__ = ""
__credits__ = ["Rangel Ulises"]
__license__ = ""
__version__ = "1.0"
__maintainer__ = "Rangel Rivera Ulises Osmar"
__email__ = "uo.rangelrivera@ugto.mx"
__status__ = "Complete"

# We import some stuff

import mpmath as m
import math
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

# We make the neccesary functions

# To get our digit list

def l_digs(prc=9,cte='pi'):
    params = ['pi','nn','phi','e','r2']

    try:
        if prc < 9:
            raise Exception('not enough digits')
    except Exception as inst_1:
        print('Error: {} please use an input larger than 9 next time!'.format(inst_1))
    else:
        try:
            if type(cte) != str:
                raise Exception('invalid type')
        except Exception as inst_2:
            print('Error: {} please use string type!'.format(inst_2))
        else:
            try:
                if cte not in params:
                    raise Exception('invalid input')
            except Exception as inst_3:
                print('Error: {} please use one of the following: pi, nn, phi, e, r2 !'.format(inst_3))

            else:
                
                if cte == 'nn':

                    cn = [str(v_2+1) for v_2 in range(prc)]
                    v_3 = '0'
                    for i in cn:
                        d_v = v_3 + i 
                        v_3 = d_v
                        
                    v_4,*v_5 = v_3
                    v_5.insert(0,v_4)

                    l_m = list(map(int,v_5))
                    l_m = np.array(l_m)
                    l_m = list(l_m[0:prc].flatten())

                else:

                    m.mp.dps=prc

                    if cte == 'pi':
                        c_n = m.atan(1)*4 
                    elif cte == 'phi':
                        c_n = m.phi*1
                    elif cte == 'r2':
                        c_n = m.sqrt(2)
                    elif cte == 'e':
                        c_n = m.e * 1 
                    
                    d_1, *r_d = str(c_n).split('.')
                    c_1, *u_r_d = r_d[0]
                    u_r_d.insert(0, c_1)
                    l_m = list(map(int, u_r_d))
                    l_m.insert(0, int(d_1))

            return l_m

# To get the digits frequency

def d_count(dl):
    try:
        if type(dl) != list:
            raise Exception('not a list')
    except Exception as inst_1:
        print('Error: input type is {}, please select a list as input next time!'.format(inst_1))
    else:
        r = []
        for i in range(10):
            if i in dl:
                oc = dl.count(i)
                l_p = [i,oc]
                r.append(l_p)
            else:
                pass
        return r

# To get the percentage of every digit in a list

def porc(l,aes=True):

    try:
        if type(l) != list:
            raise Exception('not a list')
    except Exception as inst_1:
        print('Error! the input is {}, please use the correct data type'.format(inst_1)) 
    
    else:
        if aes:
            m = max(l)
        else:
            m = sum(l)
        nl = []

        for i in l:
            p = round(i/m, 4)
            nl.append(p)

        return nl

# To get colors from a colomap with a list

def mp_clr(l, c=0.75, m='viridis'):

    cmap = matplotlib.cm.get_cmap(m)

    vs = porc(l)

    l_1 = list(map(cmap, vs))
    l_2 = np.array(l_1)
    l_2[:, 0:3] *= c

    return l_2

# Arithmetic mean
def m_ar(l):
    s = sum(l)
    d = len(l)
    av = s/d
    r = round(av,4)
    return r

# To get the standard deviation from a population

def s_dv(m_a,l_v):
    sqs = []
    for i in l_v:
        sq = round((m_a - i)**2, 4)
        sqs.append(sq)
    s_sq = sum(sqs)
    Nu = len(sqs)

    return round(math.sqrt(s_sq/Nu),4)

# We declare some varibles for our loop

s_f = 30
e_f = 1200
st= 5

# Now some lists for our graphs

av_gs_l = []
de_gs_l = []
gsm_l = []
pr_g_l = []
pr_ng_l = []
count_l = [i for i in range(s_f,e_f+1,st)]


# Constants we'll look into and a something extra (natural number sequence) for comparison

ncdg_l = ['pi','e','phi','r2','nn']

# Loop to animate stuff

for ds_1 in ncdg_l:
    print(ds_1)
    av_dl = []
    de_dl = []
    gs_dl = []
    g_dl = []
    ng_dl = []

    for vals in range(s_f,e_f+1,st):
        l_m = l_digs(prc=vals,cte=ds_1)

        # Algorith to get the gaps between XYX patterns

        g_sl = []
        s_v = 1
        g_c = 0
        l_r = len(l_m)
        ct = 0

        while l_r != 0:

            fp = ct+1+s_v
            if fp >= len(l_m):
                break

            if l_m[ct] == l_m[fp]:

                g_sl.append(g_c)
                g_c = 0
                nv = 3
               
                ct = ct + nv
                l_r = l_r - nv
            
            else:
                g_c += 1
                ct += 1
                l_r = l_r - 1 

        # Relevant values

        n_ga = len(g_sl)
        v_rem = n_ga*3
        v_rs = len(l_m)-v_rem

        gs_dl.append(n_ga)

        pr_c = round(v_rem/len(l_m) * 100, 3)
        pr_r = round(v_rs/len(l_m) * 100, 3)
        g_dl.append(pr_c)
        ng_dl.append(pr_r)


        ma_gs = m_ar(g_sl)
        sd_gs = s_dv(ma_gs,g_sl)
        
        av_dl.append(ma_gs)
        de_dl.append(sd_gs)

        # Grafica de interes
        # plt.rc('font', size=15)
        # plt.rc('axes', titlesize=20)
        # figs,ax = plt.subplots(figsize=(8,7), facecolor='aliceblue')
        # ax.set_facecolor('white')
        # ax.set_ylabel('Patternless positions')
        # ax.set_xlabel('XYX pattern index')
        # ax.set_title('XYX patterns in the sequence with {} digits'.format(vals), pad=20)
        # ax.set_ylim(0,60)
        # ax.set_xlim(0,110)
        # i_s = np.linspace(1,len(g_sl),num=len(g_sl))
        # plt.plot(i_s,g_sl,color='mediumseagreen',linestyle='solid')
        # name = ds_1 +'/' + ds_1 +'_'+ str(vals) + '.jpg'
        # plt.savefig(directory + name)
        # plt.close()

        

    av_gs_l.append(av_dl)
    de_gs_l.append(de_dl)
    gsm_l.append(gs_dl)
    pr_g_l.append(g_dl)
    pr_ng_l.append(ng_dl)

av_gs_l = np.array(av_gs_l)
count_l = np.array(count_l)
de_gs_l = np.array(de_gs_l)
gsm_l = np.array(gsm_l)
pr_g_l = np.array(pr_g_l)
pr_ng_l = np.array(pr_ng_l)

print(av_gs_l[0,0:5])

c_1 = 0
for cts in ncdg_l:
    print(cts)
    for k in range(int(((e_f - s_f)/st)) + 1):

        plt.rc('font', size=15)
        plt.rc('axes', titlesize=20)
        figs,ax = plt.subplots(figsize=(8,7), facecolor='lavender')
        ax.set_facecolor('aliceblue')
        ax.set_ylabel('Variable value')
        ax.set_xlabel('Sequence with {} digits'.format(5+k*5))
        ax.set_title('Gap behaviour between XYX patterns', pad=20)
        ax.set_xlim(0,1200)
        ax.set_ylim(0,16)
        i_s = np.linspace(1,len(g_sl),num=len(g_sl))
        plt.plot(count_l[0:k],av_gs_l[c_1,0:k],color='cornflowerblue',linestyle='solid')
        plt.plot(count_l[0:k], de_gs_l[c_1,0:k], color='cornflowerblue',linestyle='--')
        v_1 = 'Arithmetic Mean'
        v_2 = 'Standard Deviation'
        plt.legend([v_1,v_2],loc='lower right')
        name = cts +'/' + cts + '_gsavg'+'_'+ str(k) + '.jpg'
        plt.savefig("directory"+ name)
        plt.close()

        plt.rc('font', size=15)
        plt.rc('axes', titlesize=20)
        figs,ax = plt.subplots(figsize=(8,7), facecolor='whitesmoke')
        ax.set_facecolor('ghostwhite')
        ax.set_ylabel('Digit percentage')
        ax.set_xlabel('Sequence with {} digits'.format(5+k*5))
        ax.set_title('Evolution of percentages in the sequence', pad=20)
        ax.set_xlim(0,1200)
        ax.set_ylim(0,100)
        i_s = np.linspace(1,len(g_sl),num=len(g_sl))
        plt.plot(count_l[0:k],pr_g_l[c_1,0:k],color='seagreen',linestyle='solid')
        plt.plot(count_l[0:k], pr_ng_l[c_1,0:k], color='indianred',linestyle='solid')
        v_1 = 'In the pattern'
        v_2 = 'Out of the pattern'
        plt.legend([v_1,v_2],loc='center right')
        name = cts +'/' + cts + '_prc'+'_'+ str(k) + '.jpg'
        plt.savefig("directory"+ name)
        plt.close()

        plt.rc('font', size=15)
        plt.rc('axes', titlesize=20)
        figs,ax = plt.subplots(figsize=(8,7), facecolor='white')
        ax.set_facecolor('ghostwhite')
        ax.set_ylabel('Digit amount')
        ax.set_xlabel('Sequence with {} digits'.format(5+k*5))
        ax.set_title('Digit in XYX pattern evolution', pad=20)
        ax.set_xlim(0,1200)
        ax.set_ylim(0,140)
        plt.grid()
        i_s = np.linspace(1,len(g_sl),num=len(g_sl))
        plt.plot(count_l[0:k],gsm_l[c_1,0:k],color='dodgerblue',linestyle='solid')
        name = cts +'/' + cts + '_mag'+'_'+ str(k) + '.jpg'
        plt.savefig("directory"+ name)
        plt.close()


    c_1 += 1


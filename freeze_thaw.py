#!/usr/bin/env python3
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#import data
raw = pd.read_excel('./PCPG_all_compositions_freeze_thaw_cicles.ods', header = 2, usecols = 'B:H')

#rolling average of z average and PdI
temp= raw.iloc[:,-2:].rolling(3).mean()

#pegar a média de cada trinca, pulando dois valores Nan
selected = temp.iloc[2::3]


#rearranjar pra que os diferentes cada composição fiquem juntos 
Zave = (selected.iloc[:,0].to_numpy().reshape((-1,4)))

Pdi  = (selected.iloc[:,1].to_numpy().reshape((-1,4)))

#pegar um nome  pra cada composição
temp = raw.iloc[0::12,2]

#pegar só a composição do nome
compositions = temp.str.slice(start=0, stop=9).to_numpy()

ciclos = np.arange(5,25,5)

#plotting
fig, (ax1,ax2) = plt.subplots(1,2)
for quartet in range(0, len(Zave)):
    ax1.plot(ciclos, Zave[quartet])
    ax1.scatter(ciclos, Zave[quartet], label = compositions[quartet])
    ax2.plot(ciclos, Pdi[quartet])
    ax2.scatter(ciclos, Pdi[quartet], label = compositions[quartet])

#set subplot titles
ax1.set_title('Z Average')
ax2.set_title('PdI')
#set title
fig.suptitle('DLS mesurments of Freeze Thawn vesicles.\n10 mM NaCl 7.4 pH 10 mM Tris HCl buffer, 30 °C')

#setting axes labels
ax1.set_xlabel('Number of cycles')
ax1.set_ylabel('Diameter (nm)')
ax1.set_xticks(ciclos)

ax2.set_xlabel('Number of cycles')
ax2.set_ylabel('PdI')
ax2.set_xticks(ciclos)

#set legend
ax1.legend()
ax2.legend()
fig.tight_layout()
plt.savefig('size_PCPG.png', dpi = 200, bbox_inches='tight')
plt.show()

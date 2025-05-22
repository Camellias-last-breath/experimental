#!/usr/bin/env python3
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

#import data
raw = pd.read_excel('./PCPG_e_PEPG.ods', usecols = 'A:G', nrows = 72)
temp= raw.iloc[:,-2:].rolling(3).mean()


#pegar a média de cada trinca, pulando dois valores Nan
selected = temp.iloc[2::3]
print(selected)

#rearranjar pra que os diferentes cada composição fiquem juntos 
Zave = (selected.iloc[:,0].to_numpy().reshape((-1,4)))

Pdi  = (selected.iloc[:,1].to_numpy().reshape((-1,4)))

#pegar um nome  pra cada composição
temp = raw.iloc[0::12,2]

#pegar só a composição do nome
compositions = temp.str.slice(start=0, stop=9).to_numpy()
print(compositions)
ciclos = np.arange(5,25,5)

#plotting
colour= ['#000000', '#E69F00','#56B4E9', '#000000', '#E69F00','#56B4E9'] #okabe ito yellow 'F0E442'
fig, (ax1,ax2) = plt.subplots(1,2)
fig.set_figwidth(8)
percent = 25
for quartet in range(0, len(Zave)):
    if quartet == 0:
        ax1.scatter(ciclos, Zave[quartet], label = "POPC", color = colour[quartet])

    if quartet == 3:
        ax1.scatter(ciclos, Zave[quartet], label = "POPE", marker='v', color = colour[quartet])
        
    if quartet <= 2:
        ax1.plot(ciclos, Zave[quartet], color = colour[quartet])
        ax1.scatter(ciclos, Zave[quartet], color = colour[quartet])
        ax2.plot(ciclos, Pdi[quartet], label = percent, color = colour[quartet])
        ax2.scatter(ciclos, Pdi[quartet], color = colour[quartet])
    else: 
        ax1.plot(ciclos, Zave[quartet], color = colour[quartet])
        ax2.plot(ciclos, Pdi[quartet], color = colour[quartet])
        ax1.scatter(ciclos, Zave[quartet], marker = "v", color = colour[quartet])
        ax2.scatter(ciclos, Pdi[quartet], marker = "v", color = colour[quartet])
    percent += 25
   # if quartet == 2:
    #    percent = 25
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
ax1.legend( title = 'Neutral Lipid', bbox_to_anchor = [1, -0.2])
ax2.legend(title = 'Percentage of POPG', bbox_to_anchor = [1,-0.2])
fig.tight_layout()
plt.savefig('size_all.png', dpi = 400, bbox_inches='tight')
#plt.show()

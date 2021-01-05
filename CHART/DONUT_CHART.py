import matplotlib.pyplot as plt
from matplotlib import animation
from matplotlib.animation import FuncAnimation, PillowWriter  
import numpy as np
from datetime import datetime
import dateutil.parser as parser
from collections import Counter
import pandas as pd
from pandas.plotting import table
import matplotlib as mpl 
import calendar

# mpl.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg\bin'
plt.rcParams['animation.ffmpeg_path'] = r'C:\ffmpeg\bin\ffmpeg'

IDNCoronaData = [ ['IDN','Asia','Indonesia','02/03/2020',2.0     ],
['IDN','Asia','Indonesia','03/03/2020',2.0     ],
['IDN','Asia','Indonesia','04/03/2020',2.0     ],
['IDN','Asia','Indonesia','05/03/2020',2.0     ],
['IDN','Asia','Indonesia','06/03/2020',4.0     ],
['IDN','Asia','Indonesia','07/03/2020',4.0     ],
['IDN','Asia','Indonesia','08/03/2020',6.0     ],
['IDN','Asia','Indonesia','09/03/2020',19.0    ],
['IDN','Asia','Indonesia','10/03/2020',27.0    ],
['IDN','Asia','Indonesia','11/03/2020',34.0    ],
['IDN','Asia','Indonesia','12/03/2020',34.0    ],
['IDN','Asia','Indonesia','13/03/2020',69.0    ],
['IDN','Asia','Indonesia','14/03/2020',96.0    ],
['IDN','Asia','Indonesia','15/03/2020',117.0   ],
['IDN','Asia','Indonesia','16/03/2020',134.0   ],
['IDN','Asia','Indonesia','17/03/2020',172.0   ],
['IDN','Asia','Indonesia','18/03/2020',227.0   ],
['IDN','Asia','Indonesia','19/03/2020',311.0   ],
['IDN','Asia','Indonesia','20/03/2020',369.0   ],
['IDN','Asia','Indonesia','21/03/2020',450.0   ],
['IDN','Asia','Indonesia','22/03/2020',514.0   ],
['IDN','Asia','Indonesia','23/03/2020',579.0   ],
['IDN','Asia','Indonesia','24/03/2020',686.0   ],
['IDN','Asia','Indonesia','25/03/2020',790.0   ],
['IDN','Asia','Indonesia','26/03/2020',893.0   ],
['IDN','Asia','Indonesia','27/03/2020',1046.0  ],
['IDN','Asia','Indonesia','28/03/2020',1155.0  ],
['IDN','Asia','Indonesia','29/03/2020',1285.0  ],
['IDN','Asia','Indonesia','30/03/2020',1414.0  ],
['IDN','Asia','Indonesia','31/03/2020',1528.0  ],
['IDN','Asia','Indonesia','01/04/2020',1677.0  ],
['IDN','Asia','Indonesia','02/04/2020',1790.0  ],
['IDN','Asia','Indonesia','03/04/2020',1986.0  ],
['IDN','Asia','Indonesia','04/04/2020',2092.0  ],
['IDN','Asia','Indonesia','05/04/2020',2273.0  ],
['IDN','Asia','Indonesia','06/04/2020',2491.0  ],
['IDN','Asia','Indonesia','07/04/2020',2738.0  ],
['IDN','Asia','Indonesia','08/04/2020',2956.0  ],
['IDN','Asia','Indonesia','09/04/2020',3293.0  ],
['IDN','Asia','Indonesia','10/04/2020',3512.0  ],
['IDN','Asia','Indonesia','11/04/2020',3842.0  ],
['IDN','Asia','Indonesia','12/04/2020',4241.0  ],
['IDN','Asia','Indonesia','13/04/2020',4557.0  ],
['IDN','Asia','Indonesia','14/04/2020',4839.0  ],
['IDN','Asia','Indonesia','15/04/2020',5136.0  ],
['IDN','Asia','Indonesia','16/04/2020',5516.0  ],
['IDN','Asia','Indonesia','17/04/2020',5923.0  ],
['IDN','Asia','Indonesia','18/04/2020',6248.0  ],
['IDN','Asia','Indonesia','19/04/2020',6575.0  ],
['IDN','Asia','Indonesia','20/04/2020',6760.0  ],
['IDN','Asia','Indonesia','21/04/2020',7135.0  ],
['IDN','Asia','Indonesia','22/04/2020',7418.0  ],
['IDN','Asia','Indonesia','23/04/2020',7775.0  ],
['IDN','Asia','Indonesia','24/04/2020',8211.0  ],
['IDN','Asia','Indonesia','25/04/2020',8607.0  ],
['IDN','Asia','Indonesia','26/04/2020',8882.0  ],
['IDN','Asia','Indonesia','27/04/2020',9096.0  ],
['IDN','Asia','Indonesia','28/04/2020',9511.0  ],
['IDN','Asia','Indonesia','29/04/2020',9771.0  ],
['IDN','Asia','Indonesia','30/04/2020',10118.0 ],
['IDN','Asia','Indonesia','01/05/2020',10551.0 ],
['IDN','Asia','Indonesia','02/05/2020',10843.0 ],
['IDN','Asia','Indonesia','03/05/2020',11192.0 ],
['IDN','Asia','Indonesia','04/05/2020',11587.0 ],
['IDN','Asia','Indonesia','05/05/2020',12071.0 ],
['IDN','Asia','Indonesia','06/05/2020',12438.0 ],
['IDN','Asia','Indonesia','07/05/2020',12776.0 ],
['IDN','Asia','Indonesia','08/05/2020',13112.0 ],
['IDN','Asia','Indonesia','09/05/2020',13645.0 ],
['IDN','Asia','Indonesia','10/05/2020',14032.0 ],
['IDN','Asia','Indonesia','11/05/2020',14265.0 ],
['IDN','Asia','Indonesia','12/05/2020',14749.0 ],
['IDN','Asia','Indonesia','13/05/2020',15438.0 ],
['IDN','Asia','Indonesia','14/05/2020',16006.0 ],
['IDN','Asia','Indonesia','15/05/2020',16496.0 ],
['IDN','Asia','Indonesia','16/05/2020',17025.0 ],
['IDN','Asia','Indonesia','17/05/2020',17514.0 ],
['IDN','Asia','Indonesia','18/05/2020',18010.0 ],
['IDN','Asia','Indonesia','19/05/2020',18496.0 ],
['IDN','Asia','Indonesia','20/05/2020',19189.0 ],
['IDN','Asia','Indonesia','21/05/2020',20162.0 ],
['IDN','Asia','Indonesia','22/05/2020',20796.0 ],
['IDN','Asia','Indonesia','23/05/2020',21745.0 ],
['IDN','Asia','Indonesia','24/05/2020',22271.0 ],
['IDN','Asia','Indonesia','25/05/2020',22750.0 ],
['IDN','Asia','Indonesia','26/05/2020',23165.0 ],
['IDN','Asia','Indonesia','27/05/2020',23851.0 ],
['IDN','Asia','Indonesia','28/05/2020',24538.0 ],
['IDN','Asia','Indonesia','29/05/2020',25216.0 ],
['IDN','Asia','Indonesia','30/05/2020',25773.0 ],
['IDN','Asia','Indonesia','31/05/2020',26473.0 ],
['IDN','Asia','Indonesia','01/06/2020',26940.0 ],
['IDN','Asia','Indonesia','02/06/2020',27549.0 ],
['IDN','Asia','Indonesia','03/06/2020',28233.0 ],
['IDN','Asia','Indonesia','04/06/2020',28818.0 ],
['IDN','Asia','Indonesia','05/06/2020',29521.0 ],
['IDN','Asia','Indonesia','06/06/2020',30514.0 ],
['IDN','Asia','Indonesia','07/06/2020',31186.0 ],
['IDN','Asia','Indonesia','08/06/2020',32033.0 ],
['IDN','Asia','Indonesia','09/06/2020',33076.0 ],
['IDN','Asia','Indonesia','10/06/2020',34316.0 ],
['IDN','Asia','Indonesia','11/06/2020',35295.0 ],
['IDN','Asia','Indonesia','12/06/2020',36406.0 ],
['IDN','Asia','Indonesia','13/06/2020',37420.0 ],
['IDN','Asia','Indonesia','14/06/2020',38277.0 ],
['IDN','Asia','Indonesia','15/06/2020',39294.0 ],
['IDN','Asia','Indonesia','16/06/2020',40400.0 ],
['IDN','Asia','Indonesia','17/06/2020',41431.0 ],
['IDN','Asia','Indonesia','18/06/2020',42762.0 ],
['IDN','Asia','Indonesia','19/06/2020',43803.0 ],
['IDN','Asia','Indonesia','20/06/2020',45029.0 ],
['IDN','Asia','Indonesia','21/06/2020',45891.0 ],
['IDN','Asia','Indonesia','22/06/2020',46845.0 ],
['IDN','Asia','Indonesia','23/06/2020',47896.0 ],
['IDN','Asia','Indonesia','24/06/2020',49009.0 ],
['IDN','Asia','Indonesia','25/06/2020',50187.0 ],
['IDN','Asia','Indonesia','26/06/2020',51427.0 ],
['IDN','Asia','Indonesia','27/06/2020',52812.0 ],
['IDN','Asia','Indonesia','28/06/2020',54010.0 ],
['IDN','Asia','Indonesia','29/06/2020',55092.0 ],
['IDN','Asia','Indonesia','30/06/2020',56385.0 ],
['IDN','Asia','Indonesia','01/07/2020',57770.0 ],
['IDN','Asia','Indonesia','02/07/2020',59394.0 ],
['IDN','Asia','Indonesia','03/07/2020',60695.0 ],
['IDN','Asia','Indonesia','04/07/2020',62142.0 ],
['IDN','Asia','Indonesia','05/07/2020',63749.0 ],
['IDN','Asia','Indonesia','06/07/2020',64958.0 ],
['IDN','Asia','Indonesia','07/07/2020',66226.0 ],
['IDN','Asia','Indonesia','08/07/2020',68079.0 ],
['IDN','Asia','Indonesia','09/07/2020',70736.0 ],
['IDN','Asia','Indonesia','10/07/2020',72347.0 ],
['IDN','Asia','Indonesia','11/07/2020',74018.0 ],
['IDN','Asia','Indonesia','12/07/2020',75699.0 ],
['IDN','Asia','Indonesia','13/07/2020',76981.0 ],
['IDN','Asia','Indonesia','14/07/2020',78572.0 ],
['IDN','Asia','Indonesia','15/07/2020',80094.0 ],
['IDN','Asia','Indonesia','16/07/2020',81668.0 ],
['IDN','Asia','Indonesia','17/07/2020',83130.0 ],
['IDN','Asia','Indonesia','18/07/2020',84882.0 ],
['IDN','Asia','Indonesia','19/07/2020',86521.0 ],
['IDN','Asia','Indonesia','20/07/2020',88214.0 ],
['IDN','Asia','Indonesia','21/07/2020',89869.0 ],
['IDN','Asia','Indonesia','22/07/2020',91751.0 ],
['IDN','Asia','Indonesia','23/07/2020',93657.0 ],
['IDN','Asia','Indonesia','24/07/2020',95418.0 ],
['IDN','Asia','Indonesia','25/07/2020',97286.0 ],
['IDN','Asia','Indonesia','26/07/2020',98778.0 ],
['IDN','Asia','Indonesia','27/07/2020',100303.0],
['IDN','Asia','Indonesia','28/07/2020',102051.0],
['IDN','Asia','Indonesia','29/07/2020',104432.0],
['IDN','Asia','Indonesia','30/07/2020',106336.0],
['IDN','Asia','Indonesia','31/07/2020',108376.0],
['IDN','Asia','Indonesia','01/08/2020',109936.0],
['IDN','Asia','Indonesia','02/08/2020',111455.0],
['IDN','Asia','Indonesia','03/08/2020',113134.0],
['IDN','Asia','Indonesia','04/08/2020',115056.0],
['IDN','Asia','Indonesia','05/08/2020',116871.0],
['IDN','Asia','Indonesia','06/08/2020',118753.0],
['IDN','Asia','Indonesia','07/08/2020',121226.0],
['IDN','Asia','Indonesia','08/08/2020',123503.0],
['IDN','Asia','Indonesia','09/08/2020',125396.0],
['IDN','Asia','Indonesia','10/08/2020',127083.0],
['IDN','Asia','Indonesia','11/08/2020',128776.0],
['IDN','Asia','Indonesia','12/08/2020',130718.0],
['IDN','Asia','Indonesia','13/08/2020',132816.0],
['IDN','Asia','Indonesia','14/08/2020',135123.0],
['IDN','Asia','Indonesia','15/08/2020',137468.0],
['IDN','Asia','Indonesia','16/08/2020',139549.0],
['IDN','Asia','Indonesia','17/08/2020',141370.0],
['IDN','Asia','Indonesia','18/08/2020',143043.0],
['IDN','Asia','Indonesia','19/08/2020',144945.0],
['IDN','Asia','Indonesia','20/08/2020',147211.0],
['IDN','Asia','Indonesia','21/08/2020',149408.0],
['IDN','Asia','Indonesia','22/08/2020',151498.0],
['IDN','Asia','Indonesia','23/08/2020',153535.0],
['IDN','Asia','Indonesia','24/08/2020',155412.0],
['IDN','Asia','Indonesia','25/08/2020',157859.0],
['IDN','Asia','Indonesia','26/08/2020',160165.0],
['IDN','Asia','Indonesia','27/08/2020',162884.0],
['IDN','Asia','Indonesia','28/08/2020',165887.0],
['IDN','Asia','Indonesia','29/08/2020',169195.0],
['IDN','Asia','Indonesia','30/08/2020',172053.0],
['IDN','Asia','Indonesia','31/08/2020',174796.0],
['IDN','Asia','Indonesia','01/09/2020',177571.0],
['IDN','Asia','Indonesia','02/09/2020',180646.0],
['IDN','Asia','Indonesia','03/09/2020',184268.0],
['IDN','Asia','Indonesia','04/09/2020',187537.0],
['IDN','Asia','Indonesia','05/09/2020',190665.0],
['IDN','Asia','Indonesia','06/09/2020',194109.0],
['IDN','Asia','Indonesia','07/09/2020',196989.0],
['IDN','Asia','Indonesia','08/09/2020',200035.0],
['IDN','Asia','Indonesia','09/09/2020',203342.0],
['IDN','Asia','Indonesia','10/09/2020',207203.0],
['IDN','Asia','Indonesia','11/09/2020',210940.0],
['IDN','Asia','Indonesia','12/09/2020',214746.0],
['IDN','Asia','Indonesia','13/09/2020',218382.0],
['IDN','Asia','Indonesia','14/09/2020',221523.0],
['IDN','Asia','Indonesia','15/09/2020',225030.0],
['IDN','Asia','Indonesia','16/09/2020',228993.0],
['IDN','Asia','Indonesia','17/09/2020',232628.0],
['IDN','Asia','Indonesia','18/09/2020',236519.0],
['IDN','Asia','Indonesia','19/09/2020',240687.0],
['IDN','Asia','Indonesia','20/09/2020',244676.0],
['IDN','Asia','Indonesia','21/09/2020',248852.0],
['IDN','Asia','Indonesia','22/09/2020',252923.0],
['IDN','Asia','Indonesia','23/09/2020',257388.0],
['IDN','Asia','Indonesia','24/09/2020',262022.0],
['IDN','Asia','Indonesia','25/09/2020',266845.0],
['IDN','Asia','Indonesia','26/09/2020',271339.0],
['IDN','Asia','Indonesia','27/09/2020',275213.0],
['IDN','Asia','Indonesia','28/09/2020',278722.0],
['IDN','Asia','Indonesia','29/09/2020',282724.0],
['IDN','Asia','Indonesia','30/09/2020',287008.0],
['IDN','Asia','Indonesia','01/10/2020',291182.0],
['IDN','Asia','Indonesia','02/10/2020',295499.0],
['IDN','Asia','Indonesia','03/10/2020',299506.0],
['IDN','Asia','Indonesia','04/10/2020',303498.0],
['IDN','Asia','Indonesia','05/10/2020',307120.0],
['IDN','Asia','Indonesia','06/10/2020',311176.0],
['IDN','Asia','Indonesia','07/10/2020',315714.0],
['IDN','Asia','Indonesia','08/10/2020',320564.0],
['IDN','Asia','Indonesia','09/10/2020',324658.0],
['IDN','Asia','Indonesia','10/10/2020',328952.0],
['IDN','Asia','Indonesia','11/10/2020',333449.0],
['IDN','Asia','Indonesia','12/10/2020',336716.0],
['IDN','Asia','Indonesia','13/10/2020',340622.0],
['IDN','Asia','Indonesia','14/10/2020',344749.0],
['IDN','Asia','Indonesia','15/10/2020',349160.0],
['IDN','Asia','Indonesia','16/10/2020',353461.0],
['IDN','Asia','Indonesia','17/10/2020',357762.0],
['IDN','Asia','Indonesia','18/10/2020',361867.0],
['IDN','Asia','Indonesia','19/10/2020',365240.0],
['IDN','Asia','Indonesia','20/10/2020',368842.0],
['IDN','Asia','Indonesia','21/10/2020',373109.0],
['IDN','Asia','Indonesia','22/10/2020',377541.0],
['IDN','Asia','Indonesia','23/10/2020',381910.0],
['IDN','Asia','Indonesia','24/10/2020',385980.0],
['IDN','Asia','Indonesia','25/10/2020',389712.0],
['IDN','Asia','Indonesia','26/10/2020',392934.0],
['IDN','Asia','Indonesia','27/10/2020',396454.0],
['IDN','Asia','Indonesia','28/10/2020',400483.0],
['IDN','Asia','Indonesia','29/10/2020',404048.0],
['IDN','Asia','Indonesia','30/10/2020',406945.0],
['IDN','Asia','Indonesia','31/10/2020',410088.0],
['IDN','Asia','Indonesia','01/11/2020',412784.0],
['IDN','Asia','Indonesia','02/11/2020',415402.0],
['IDN','Asia','Indonesia','03/11/2020',418375.0],
['IDN','Asia','Indonesia','04/11/2020',421731.0],
['IDN','Asia','Indonesia','05/11/2020',425796.0],
['IDN','Asia','Indonesia','06/11/2020',429574.0],
['IDN','Asia','Indonesia','07/11/2020',433836.0],
['IDN','Asia','Indonesia','08/11/2020',437716.0],
['IDN','Asia','Indonesia','09/11/2020',440569.0],
['IDN','Asia','Indonesia','10/11/2020',444348.0],
['IDN','Asia','Indonesia','11/11/2020',448118.0],
['IDN','Asia','Indonesia','12/11/2020',452291.0],
['IDN','Asia','Indonesia','13/11/2020',457735.0],
['IDN','Asia','Indonesia','14/11/2020',463007.0],
['IDN','Asia','Indonesia','15/11/2020',467113.0],
['IDN','Asia','Indonesia','16/11/2020',470648.0],
['IDN','Asia','Indonesia','17/11/2020',474455.0],
['IDN','Asia','Indonesia','18/11/2020',478720.0],
['IDN','Asia','Indonesia','19/11/2020',483518.0],
['IDN','Asia','Indonesia','20/11/2020',488310.0],
['IDN','Asia','Indonesia','21/11/2020',493308.0],
['IDN','Asia','Indonesia','22/11/2020',497668.0],
['IDN','Asia','Indonesia','23/11/2020',502110.0],
['IDN','Asia','Indonesia','24/11/2020',506302.0],
['IDN','Asia','Indonesia','25/11/2020',511836.0],
['IDN','Asia','Indonesia','26/11/2020',516753.0],
['IDN','Asia','Indonesia','27/11/2020',522581.0],
['IDN','Asia','Indonesia','28/11/2020',527999.0],
['IDN','Asia','Indonesia','29/11/2020',534266.0],
['IDN','Asia','Indonesia','30/11/2020',538883.0],
['IDN','Asia','Indonesia','01/12/2020',543975.0],
['IDN','Asia','Indonesia','02/12/2020',549508.0],
['IDN','Asia','Indonesia','03/12/2020',557877.0],
['IDN','Asia','Indonesia','04/12/2020',563680.0],
['IDN','Asia','Indonesia','05/12/2020',569707.0],
['IDN','Asia','Indonesia','06/12/2020',575796.0],
['IDN','Asia','Indonesia','07/12/2020',581550.0],
['IDN','Asia','Indonesia','08/12/2020',586842.0],
['IDN','Asia','Indonesia','09/12/2020',592900.0],
['IDN','Asia','Indonesia','10/12/2020',598933.0],
['IDN','Asia','Indonesia','11/12/2020',605243.0],
['IDN','Asia','Indonesia','12/12/2020',611631.0],
['IDN','Asia','Indonesia','13/12/2020',617820.0],
['IDN','Asia','Indonesia','14/12/2020',623309.0],
['IDN','Asia','Indonesia','15/12/2020',629429.0],
['IDN','Asia','Indonesia','16/12/2020',636154.0],
['IDN','Asia','Indonesia','17/12/2020',643508.0],
['IDN','Asia','Indonesia','18/12/2020',650197.0],
['IDN','Asia','Indonesia','19/12/2020',657948.0],
['IDN','Asia','Indonesia','20/12/2020',664930.0],
['IDN','Asia','Indonesia','21/12/2020',671778.0],
['IDN','Asia','Indonesia','22/12/2020',678125.0],
['IDN','Asia','Indonesia','23/12/2020',685639.0],
['IDN','Asia','Indonesia','24/12/2020',692838.0],
['IDN','Asia','Indonesia','25/12/2020',700097.0],
['IDN','Asia','Indonesia','26/12/2020',706837.0],
['IDN','Asia','Indonesia','27/12/2020',713365.0],
['IDN','Asia','Indonesia','28/12/2020',719219.0],
['IDN','Asia','Indonesia','29/12/2020',727122.0],
['IDN','Asia','Indonesia','30/12/2020',735124.0],
]

name = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'limegreen', 
          'red', 'navy', 'blue', 'magenta', 'crimson', 'yellow', 'forestgreen', 'orange']
values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
explode = (0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01)

fig, ax = plt.subplots()

#Calculate Percentage
def my_autopct(pct):
    # return ('%0.f%%' % pct) if pct > 20 else ''
    return ''

#Check Value For Display Labels
def my_level_list(data):
    list = []
    for i in range(len(data)):
        if (data[i]*100/np.sum(data)) > 0 : #2%
            list.append(name[i])
        else:
            list.append('')
    return list

#CalculateAllMonth
def calculateAllMonth(mDataAllMonth):
    returnVal = 0
    for i in mDataAllMonth:
        returnVal += i
    return returnVal

#FillListValuePerMonth
def calculateTotalPerMonth(mIndex):
    mMonth = datetime.strptime(IDNCoronaData[mIndex][3], '%d/%m/%Y').month
    mYear = datetime.strptime(IDNCoronaData[mIndex][3], '%d/%m/%Y').year
    
    #FillNewValue
    if(mMonth > 3):
        mLastDayPreviousMonth = calendar.monthrange(mYear,(mMonth-1))[1]

        #GetValueLastMonth
        strDate = ""
        mPreviosData = []

        if(mMonth-1) < 10:    
            strDate = str(mLastDayPreviousMonth)+"/"+"0"+str((mMonth-1))+ "/" +str(mYear)
        else:
            strDate = str(mLastDayPreviousMonth)+"/"+str((mMonth-1))+ "/" +str(mYear)
        for i in IDNCoronaData:
            if strDate in i:
                mPreviosData = i
        values[(mMonth-1)] = IDNCoronaData[mIndex][4] - mPreviosData[4]
    else:
        values[(mMonth-1)] = IDNCoronaData[mIndex][4]

def fixOverLappingText(text):
    # if undetected overlaps reduce sigFigures to 1
    sigFigures = 2
    positions = [(round(item.get_position()[1],sigFigures), item) for item in text]

    overLapping = Counter((item[0] for item in positions))
    overLapping = [key for key, value in overLapping.items() if value >= 2]

    for key in overLapping:
        textObjects = [text for position, text in positions if position == key]

        if textObjects:
            # If bigger font size scale will need increasing
            scale = 0.08

            spacings = np.linspace(0,scale*len(textObjects),len(textObjects))

            for shift, textObject in zip(spacings,textObjects):
                textObject.set_y(key + shift)
    

def updateChart(num):
    calculateTotalPerMonth(num)
    mTotal = IDNCoronaData[num][4]
    ax.clear()
    text = ax.pie(values, labels=my_level_list(values), autopct=my_autopct, colors = colors, 
    shadow=True, startangle=90, pctdistance=0.9, explode =explode)

    fixOverLappingText(text[1])
    ax.axis('equal')
    circle = plt.Circle((0,0),0.7,fc='white') #draw circle for look like donut chart>>> 
    donut = plt.gcf()
    donut.gca().add_artist(circle)
    label = plt.annotate('Total ='+str(int(mTotal)), xy=(0,0), fontsize=20, ha="center") #give label on the center circle

    val = []
    for i in values:
        val.append(str(int(i)))
    # plt.title("Corona Cases In Indonesia 2020")
    plt.legend(text[0], val, loc="best", bbox_to_anchor = (1,1))

    plt.tight_layout()
    plt.pause(0.3)

raw_data = {'officer_name': ['Jason', 'Molly', 'Tina', 'Jake', 'Amy'],
        'jan_arrests': [4, 24, 31, 2, 3],
        'feb_arrests': [25, 94, 57, 62, 70],
        'march_arrests': [5, 43, 23, 23, 51]}
df = pd.DataFrame(raw_data, columns = ['officer_name', 'jan_arrests', 'feb_arrests', 'march_arrests'])
df['total_arrests'] = df['jan_arrests'] + df['feb_arrests'] + df['march_arrests']

# plot table
# ax2 = plt.subplot(122)
# plt.axis('off')
# ax2.plot(1,1)
# tbl = table(ax2, df, loc='center')
# tbl.auto_set_font_size(False)
# tbl.set_fontsize(14)
    
#updateChart
ani = FuncAnimation(fig, updateChart,frames=range(len(IDNCoronaData)), interval=50, repeat=False) #Run Animation
# ani.save('C:/Users/GALUH/Desktop/anima.gif', writer='imagemagick', fps=30)
# f = r"C:/Users/GALUH/Desktop/anima.mp4" 
# writervideo = animation.FFMpegWriter(fps=60) 
# ani.save(f, writer=writervideo)

FFwriter = animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
ani.save('C:/Users/GALUH/Desktop/anima.mp4', writer = FFwriter)


# FFwriter=animation.FFMpegWriter(fps=30, extra_args=['-vcodec', 'libx264'])
# anim.save(r'I:\Understanding_objective functions\test\basic_animation.mp4', writer=FFwriter)

# ani.save('2osc.mp4', writer="ffmpeg")
# plt.show()

#usr/bin/env python3
# Nawaraj Paudel
################################################################################
########### Final Project:- Nb3Sn Electromagnetic Characterization #############
################################################################################

#"""This module provides a tool for parsing, plotting and analysing VSM data"""

################################################################################
#################********* IMPORT REQUIRED MODULES *********####################
################################################################################
import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import math
import webbrowser
################################################################################
#***************** GET REQUIRED INPUTS FROM USERS *****************************#
################################################################################
fileName = sys.argv[1]
HT = sys.argv[2]
################################################################################
#                  ***plotrcParam Customization***                             #
################################################################################
plt.rcParams.update({
        'font.size'           : 10.0      ,        #print(plt.style.available)
        'xtick.top'           : False    ,
        'xtick.major.size'    : 4        ,
        'xtick.major.width'   : 1     ,
        'xtick.labelsize'     : 10.0      ,
        'xtick.direction'     : 'out'      ,
        'xtick.minor.visible' : True      ,
        'ytick.major.size'    : 4        ,
        'ytick.major.width'   : 1     ,
        'ytick.labelsize'     : 10.0      ,
        'ytick.direction'     : 'out'      ,
        'ytick.minor.visible' : True      ,
        'xtick.major.pad'     : 2        ,
        'xtick.minor.pad'     : 2        ,
        'ytick.major.pad'     : 2        ,
        'ytick.minor.pad'     : 2        ,
        'savefig.dpi'         : 600      ,
        'axes.linewidth'      : 1     ,
        'text.usetex'         : False,
        'axes.titlesize': 14  ,
        'axes.labelsize': 20  ,
        'lines.linewidth': 3   ,
        'lines.markersize': 10   ,
        'xtick.labelsize': 14  ,
        'ytick.labelsize': 14,
        'legend.frameon': True,
         'legend.labelspacing'  : 0.5 ,
        'figure.titleweight' : 'bold',
        'image.aspect' : 'equal'})

################################################################################
def main():
################################################################################
    df, sampleLength, T = readFile(fileName)
    Hall,H,Fp,Km,dm,m,Hnorm,Fpnorm,Fpmax,Hmax,df = dataManipulate (df,sampleLength)
    pltFpvsH(Fp,H,Hmax,Fpmax,T,HT)
    pltMvsH(m,Hall,T,HT)
    pltDMvsH(dm,Hall,T,HT)
    pltKmvsH(H,Km,T,HT)
    pltFpnormvsHnorm(Hnorm,Fpnorm,T,HT)
    manipulated_df(df)
    print("Done! Please check your html output file.")
    print("*************************************************")
            
##############################################################################
#           *** define the functions called above ***                          #
##############################################################################
#******************************************************************************#
def readFile(fileName):
#******************************************************************************#
    sampleLength = 0.0
    tempMeasured = 0.0
    DataFrame = pd.DataFrame()
    while not (os.path.isfile(fileName)):
        fileName = input("Please enter the correct name of your file: ")

    with open(fileName,'r+') as df:
        print("File found! Please wait.......!\n")
        print("*************************************************")
        lines = df.readlines()[0:12]
        if lines[2][0:4] == "File":
            sampleLength = float(lines[2][20:24])
            print("The length of the sample is {:.2f} mm.".format(sampleLength))
            print("*************************************************")
        if lines[10][33:37] == "Temp":
            tempMeasured = round(float(lines[11][35:41]))
    if tempMeasured == 4.0:
               tempMeasured += 0.2
    print("Your input file is measured at temperature {} K. ".format(tempMeasured))

    DataFrame = pd.read_csv (fileName, sep ='\t', skiprows=11,
    usecols = [i for i in range (0,6,1)], names = ["Time", "Field",
    "Moment", "Temerature", "dMoment", "Kramer"])
    #df_cols = ["Time","Field","Moment","Temperature","dMoment","Kramer"]
    #df.columns = df_cols
    #df = df.iloc [:, 0:6] # essentially all data
    #pd.set_option("display.max_columns",100)  #.max_rows
    return DataFrame, sampleLength, tempMeasured  # return to main function & stored in df
#*******************************************************************************#
def dataManipulate (df, sampleLength):
#*******************************************************************************#
    dm = df.iloc [ : , 4 ]
    m = df.iloc [ :, df.columns.get_loc ("Moment") ]
    Hall = df.iloc [:, 1]   # all values of Field
    H = (df ["Field"])[ 401:3160 ]  # this is a series
    #print(H.head())
    df.insert(6,"Jc",df.dMoment/sampleLength)
    df.insert(7,"Fp",df.Jc*df.Field)
    df.insert(8,"Km",((df[df.Jc>0]["Jc"])**0.5)*(df[df.Field>0]["Field"]**0.25))
    Fpall = df.Fp
    Fp = df.Fp [401:3160]
    Fpmaxindex = Fp.idxmax()
    Fpmax = Fp [Fpmaxindex]
    Hmax = H [Fpmaxindex]
    df.insert (9, "Hnorm", (Hall/Hmax))
    #print(Fpmax)
    df.insert(10, "Fpnorm", Fpall/Fpmax)
    #print(df.Fpnorm.idxmax())
    print("For this temp,(Hmax,Fpmax) are ({0:.2f},{1:.2f})".format(Hmax,Fpmax))
    #df=df[(df.Field>0)& (df.Jc>0)]
    #df.insert(8,"Km",((df.Jc)**0.5)*(df.Field**0.25))
    #Fp = (df ["Fp"]) [ 401:3160 ]
    #print(Fp.head())
    Km = df.iloc [ 401:3160, 8]
    #select particular values
    #print(x1.size)
    #print(x1.index)
    #print(df.head())
    #gives the idx of Fpmax
    Hnorm = df ["Hnorm"] [401:3160] # its 0 is 401 of df["Hnorm"]
    Fpnorm = df ["Fpnorm"] [401:3160]
    return Hall, H, Fp, Km, dm, m,Hnorm, Fpnorm, Fpmax, Hmax,df

#******************************************************************************#
def pltFpvsH(Fp,H,Hmax,Fpmax,inputTemp,HT): 
#******************************************************************************#

    plt.figure(figsize=(7,7))  # 7 cm * 7 cm 
    plt.plot(H,Fp, c = 'r', linewidth = 2.5, linestyle ='-', alpha = 0.5 )
    plt.plot(Hmax,Fpmax,"*b", )
    #plt.text ((Hmax-1.0),(Fpmax-0.17), s = 'Hmax ~ {0:.2f}T'.format(Hmax),
    #c = 'm', fontsize = 18)
    plt.xlabel (" \N{GREEK SMALL LETTER MU}\N{SUBSCRIPT ZERO}H(T) ")
    plt.ylabel (" Fp (a. u.) ")
    plt.xlim ([0.,14.])
    #plt.gca().set_xlim(left = 0)  # gca()--get current axis method
    plt.gca().set_ylim(bottom=0)
    #plt.grid (True)
    plt.title ("{0:.1f}K_m vs H @".format(inputTemp) +  HT)
    #plt.text(11.8,2.1, s = "@ T = 4.2 K ", fontsize = 12,
        #bbox = dict (boxstyle='round', facecolor = 'None',
        #alpha = 0.5, edgecolor = 'r'))
    plt.savefig ("{0:.1f}K_FpvsH.png".format(inputTemp))
    plt.show()

#******************************************************************************#
def pltMvsH (m,Hall,inputTemp,HT):
#******************************************************************************#
    
    plt.figure(figsize=(7,7))   
    plt.plot(Hall,m, c = 'r', linewidth = 2.5, linestyle ='-', alpha = 0.5)
    plt.xlabel (" \N{GREEK SMALL LETTER MU}\N{SUBSCRIPT ZERO}H(T) ")
    plt.ylabel (" Moment (emu) ")
    x_lim_right = int (Hall.max())
    plt.xlim ([0.,x_lim_right])
    plt.gca().set_ylim(bottom=0)
    plt.title ("{0:.1f}K_m vs H @".format(inputTemp) +  HT) 
    plt.savefig ("{0:.1f}K_mvsH.png".format(inputTemp))
    plt.show()

#******************************************************************************#
def pltDMvsH (dm, Hall,inputTemp,HT):
#******************************************************************************#
    
    plt.figure(figsize=(7,7))   
    plt.plot(Hall,dm, c = 'r', linewidth = 2.5, linestyle ='-', alpha = 0.5)
    plt.xlabel ("\N{GREEK SMALL LETTER MU}\N{SUBSCRIPT ZERO}H(T)")
    plt.ylabel (" \u0394m (emu) ")
    x_lim_right = math.ceil (Hall.max())
    plt.xlim ([0.,x_lim_right])
    plt.gca().set_ylim(bottom=0)
    plt.title ("{0:.1f}K_\u0394m vs H @".format(inputTemp) +  HT) 
    plt.savefig ("{0:.1f}K_dmvsH.png".format(inputTemp))
    plt.show()

#******************************************************************************#
def pltKmvsH (H, Km, inputTemp,HT):
#******************************************************************************#

    plt.figure(figsize=(7,7))   
    plt.plot(H,Km, c = 'r', linewidth = 2.5, linestyle ='-', alpha = 0.5)
    plt.xlabel ("\N{GREEK SMALL LETTER MU}\N{SUBSCRIPT ZERO}H(T)")
    plt.ylabel (" Km (a.u.) ")
    x_lim_right = math.ceil (H.max())
    plt.xlim ([0.,x_lim_right])
    plt.gca().set_ylim(bottom=0)
    plt.title ("{0:.1f}K_Km vs H @".format(inputTemp) +  HT) 
    plt.savefig ("{0:.1f}K_KmvsH.png".format(inputTemp))
    plt.show()
#******************************************************************************#
def pltFpnormvsHnorm (Hnorm,Fpnorm,inputTemp,HT):
#******************************************************************************#

    plt.figure(figsize=(7,7))   
    plt.plot(Hnorm,Fpnorm, c = 'r', linewidth = 2.5, linestyle ='-', alpha = 0.5)
    plt.xlabel (" H/Hmax ")
    plt.ylabel (" Fp/Fpmax ")
    x_lim_right = math.ceil (Hnorm.max())
    plt.xlim ([0.,x_lim_right])
    plt.gca().set_ylim(bottom=0)
    plt.title ("{0:.1f}K_Fpnorm vs Hnorm @".format(inputTemp) + HT) 
    plt.savefig ("{0:.1f}K_HnormvsFpnorm.png".format(inputTemp))
    plt.show()
#******************************************************************************#   
def manipulated_df(df):
    return df.to_csv("out.csv",sep="\t")
#******************************************************************************#
html_str = """<!DOCTYPE html>
<html lang="en">
	<head>
		<meta charset="utf-8">
		<link rel="stylesheet" type="text/css" href="css/stylesheet2.css">
		<title>EM characterization of Nb<sub>3</sub>Sn Superconductor</title>
	</head>
	<body>
		<h1 style="color:blue;">Electromagnetic Characterization of A15 Nb<sub>3</sub>Sn and Data Analysis with Python</h1>
		<div class="intro">
			<p>Nb<sub>3</sub>Sn is a superconduting material when cooled below 18 K. Small samples of length around 5 mm
			and diameter around 1 mm are measured in quantum Vibrating Sample Magnetometer (VSM). The measurement
			scheme is shown below:<br>
			<img src ="measurement.png" height = 800 width = 800></img>
<br>
For more reading <a href="https://fs.magnet.fsu.edu/~lee/superconductor-history_files/Centennial_Supplemental/
11_3_Tachikawa+Lee-History_of_Nb3Sn_and_Related_A15_Wires.pdf" target="_blank">click here.</a>
</div>
<hr>
<div>
<p> <ol>
    <li>VSM data are stored in .txt, .xlsx, .csv form and they contain all sample information along with columns that we don’t need for our data analysis.</li>
    <li> We parse the data using python pandas library: it reads all files format and gives us a dataFrame.</li>
    <li> The temperature at which sample was measured and length of sample are extracted from sample description text itself instead of asking user input.</li>
    <li> We need to manipulate the data as for some columns, we will plot only the positive values and it contains both positive, negative values</li>
    <li> Need to construct new data columns from the columns we measured: Critical current density (J<sub>c</sub>), Pinning force (F<sub>p</sub>),Kramer value
    (K<sub>m</sub>), Normalized Pinning Force (F<sub>p</sub>) etc.</li>
    <br>
Our program will perform the following:<ul>
        <li> Calculate Critical Current Density</li>
        <li> Calculate magnitude of Pinning force and which field corresponds to that value (H<sub>max</sub>)</li>
        <li> Calculate Irreversibility Field from Kramer Extrapolation </li>
        <li> Plot diffference in magnetization for up and down sweeping field to see if any noises </li>
        <li> It gives a ready to export manipulated DataFrame so other users can analyze in different softwares</li></ul>
<br>
Summary:
    <ol>
    <li>User inputs for filename:.\\vsmanalysis.py 4.2K_Nb4Ta.txt ( just provide the data file name) </li>
    <li> It will display the peak value along with four graphs as shown below</li>
    </ol></p>
<hr>
<p>
<h3 style="color:blue;">What python packages do I use for this analysis?</h3>
<ul>
<li>NumPy</li>
<li>Pandas</li>
<li>Matplotlib.pyplot</li>
<li>Math</li><ul></p>
<hr>
<p>
<h3 style="color:red;"> The pinning force peaks at 4.21 T and its pinning strength ( height) is 0.09 which is pretty weak compared
to our best sample which has pinning strength more than 5.5.</h3>
<img src ="4.2K_FpvsH.png" height = 800 width = 800></img>
<hr>
<h3 style="color:red;"> The Kramer trend is a straight line beyond 5 T and hence Kramer extrapolation can be used to calculate H<sub>irr</sub>.</h3>
<img src ="4.2K_KmvsH.png" height = 800 width = 800></img>
<hr>
<h3 style="color:red;"> The small humps near zero field shows there is flux jump at low temerature.</h3>
<img src ="4.2K_mvsH.png" height = 800 width = 800></img>
<hr>
<h3 style="color:red;"> The normalized pinning force shows its contribution is mainly from GB pinning.</h3>
<img src ="4.2K_HnormvsFpnorm.png" height = 800 width = 800></img>
<h3 style="color:red;"> The hysteresis curve below shows there is no noise or the noise cancels out.</h3>
<img src ="4.2K_mvsH.png" height = 800 width = 800></img>
<hr>
<h3 style="color:red;">Click in the link below to download the manipulated csv file.</h3>
<a href="out.csv" target="_blank"> Download. </a>
</div>
</body>
</html>
"""


# Write HTML String to file.html
with open("file.html", "w") as f:
    f.write(html_str)
webbrowser.open_new_tab("file.html")

################################################################################
main ()                # call main function
################################################################################


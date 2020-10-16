#!/usr/bin/env python3
################################################################################
###################****Project -01 || Date:10/15/2020****#######################
#####***** Name: Nawaraj Paudel  *****##########################################
####****** Course Name : BCH5884,Programming for Chemist and BioChemist*****####
################################################################################
""" Write the script described below and turn in the code on Canvas as well as
your GitHub repository. The assignment extends work you've already done on reading
in and writing out a pdb, but I want you to pay extra attention to getting the
output in the proper format for this assignment. In other words, the columns need
to line up properly.

Copy the file 2FA9noend.pdb from my GitHub repository to your project directory.

Write a program that will do the following:

1) Read in the pdb file

2) Make a list of lists where each item in the outer list represents the information 
about a single atom.i.e. your list would look something like this:

l=[[‘ATOM’, 1, ‘N’, …],

[‘ATOM’, 2, ‘CA’, …],

[‘ATOM’, 3, ‘C’, …]]

3) Center the pdb based on the user’s choice of geometric center or the center of mass,
and output the c entered pdb file. The center of mass is given by: ∑miri/∑mi 
where m specifies the mass of a given atom and r is the coordinates for a given atom. 
Try to figure out how to determine the geometric center on your own. Note, the summation 
sign is essentially an instruction to do a loop in programming. In other words, you
will loop over the list of atoms that you create when you read the program in.

This program will require everything you’ve learned so far including reading a file,
parsing a string, and loops. Please be sure to comment your work.

4) You should use formatted strings to write the new pdb file in the proper format.
The PDB format document uploaded to canvas will help you determine the proper pdb
format. (Hint: In my PDB output program, I have a write statement that starts like
this outfile.write("%-6s%5d %-4s ...)"""

##################################################################################
######################### **** IMPORT REQUIRED MODULES ****#######################
##################################################################################
from datetime import datetime
import os
import sys
##################################################################################
###################### user guide to how to use this program? ####################
##################################################################################
print("********************************************************************************************************************")
print("This system takes up to five additional command line arguments if you choose 'G'.")
print("The first argument is default project01_10_15_2020.py and additional five")
print("are pdb Path,'G' and x,y,z coordinates for your own geometry. If you choose 'M',")
print("pdb path and then this argument 'M' is enough. For ex: python project01_10_15_2020.py 2FA9noend.pdb g 1.0 2.0 3.0 or")
print("project01_10_15_2020.py 2FA9noend.pdb m")
print("*********************************************************************************************************************")
#Go to the folder where your .py and pdb files are and run: python project01_10_15_2020.py
#/home/newkin9088/Desktop/2FA9noend.pdb m
##########################################################################################################
#pdbPath, usrChoice, x_geom, y_geom, z_geom = sys.argv[1], sys.argv[2],sys.argv[3],sys.argv[4], sys.argv[5]
#pdbName = os.getcwd() +"/Desktop/2FA9noend.pdb"
#usrChoice, x_geom, y_geom, z_geom  = sys.argv[1],sys.argv[2],float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])
if len(sys.argv) == 3 and (sys.argv[2].lower() == 'm'):
	pdbPath = sys.argv[1]
	if os.path.exists(pdbPath):
		print("File Found. Please wait for output file! This output file is for you .")
	else:
		print("File not found. Please make sure you enter the absolute path for .pdb file: ex. /home/../filefolder/file.pdb")
		print("*************************************************************************************************************")
		sys.exit()

elif len(sys.argv) == 6 and (sys.argv[2].lower() == 'g'):
	pdbPath, x_geom, y_geom, z_geom  = sys.argv[1],float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])
	if os.path.exists(pdbPath):
		print("File Found. Please wait for output file!")
	else:
		print("File not found. Please make sure you enter the absolute path for .pdb file: ex. /home/file/folder/file.pdb")
		print("*************************************************************************************************************")
		sys.exit()
else:
	print("**************************************************************************************************************")
	print("Usage:", "you entered", len(sys.argv), "arguments which is not 3 if you chose 'm' or not 6 if you chose 'g'.")
	print("Please read carefully how to use this program at the top right below your execution line.")
	print("***************************************************************************************************************")
	print("             Date of program execution: {}".format(datetime.now()))
	print("***************************************************************************************************************")
	sys.exit()
#if sys.argv[2].lower() == "g":
	#pdbPath, x_geom, y_geom, z_geom  = sys.argv[1],float(sys.argv[3]),float(sys.argv[4]),float(sys.argv[5])

#else:
	#pdbPath = sys.argv[1]

##########################################################################################################
########################Open and close file with open method#####################
#################################################################################      
with open(pdbPath,"r") as f:
    atomInfo = [line.strip("\n").split() for line in f.readlines()]
lengthOfList = len(atomInfo)

################################################################
#########Find what elements are in the pdb file#################
################################################################
#elements = []
#for eachElementList in atomInfo:
    #if eachElementList[11].strip() not in elements:
        #elements.append(eachElementList[11])
#################################################################
################## create a list containing mass ################
#################################################################
massOfElement = []
for eachElementList in atomInfo:
    if eachElementList[11] == "N":
        massOfElement.append(14.01)
    elif eachElementList[11] == "C":
        massOfElement.append(12.01)
    elif eachElementList[11] == "O":
        massOfElement.append(16.0)
    elif eachElementList[11] == "S":
        massOfElement.append(32.07)
#####################################################################
# Set up x,y,z coordinates and mass of atom list to calculate r_cmx,
# r_cmy, r_cmz where r =(r_cmx,r_cmy,r_cmz) are x , y and z coordina-
# tes of center of mass of our pdf file
# Our new list called xyzm, coordinates and mass will contain first
# element as x-coordinate, second element as y-coordinate, third
# element as z-coordinate and fourth elemet as mass in each sublist
#####################################################################
xyzm = [[float(atomInfo[i][6]),float(atomInfo[i][7]),
         float(atomInfo[i][6]),float(massOfElement[i])]
        for i in range (lengthOfList)]
######################################################################
### Find center of mass coordinate  using the formula given above ####
######################################################################
sum_mi = sum(massOfElement)
r_cmx, r_cmy, r_cmz = [sum([xyzm[i][0]*xyzm[i][3] for i in range(lengthOfList)])/sum_mi,
                       sum([xyzm[i][1]*xyzm[i][3] for i in range(lengthOfList)])/sum_mi,
                       sum([xyzm[i][2]*xyzm[i][3] for i in range(lengthOfList)])/sum_mi]
#r = [r_cmx, r_cmy, r_cmz]
#######################################################################
# Ask for user input how they want to center the pdb.
# They can either choose their own arbitrary geometric
# coordinate as center of mass, "G", or center of mass
# calculated form the pdb file, "M"
########################################################################
if (sys.argv[1]).lower() == 'g':
    x_t,y_t,z_t = [[xyzm[i][0]-x_geom for i in range(lengthOfList)],
                   [xyzm[i][1]-y_geom for i in range(lengthOfList)],
                   [xyzm[i][0]-z_geom for i in range(lengthOfList)]]
    
else:
    x_t,y_t,z_t = [[xyzm[i][0]-r_cmx for i in range(lengthOfList)],
                   [xyzm[i][1]-r_cmx for i in range(lengthOfList)],
                   [xyzm[i][0]-r_cmx for i in range(lengthOfList)]]
#########################################################################
#########  **** writing out the file **** ###############################
#########################################################################
with open("2FA9noend_cm.out","w") as f:
    for i in range(lengthOfList):
        f.write("{:6s}{:>5s}{:>5s} {:3s} {:1s}{:>4s}    {:>8.3f}{:>8.3f}{:>8.3f}{:>6s} {:6s}{:>11s}\n"
.format(atomInfo[i][0],atomInfo[i][1],atomInfo[i][2],atomInfo[i][3],atomInfo[i][4],atomInfo[i][5],
        x_t[i],y_t[i],z_t[i],atomInfo[i][9],atomInfo[i][10],atomInfo[i][11]))
##########################################################################
print("Please check if your file 2FA9noend_cm.out is well formatted. \
Job Done! {}".format(datetime.now()))
print("*********************************************************************************************************")

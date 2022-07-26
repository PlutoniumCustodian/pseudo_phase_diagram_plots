# -*- coding: utf-8 -*-
"""
Created on Mon Jul 25 09:50:09 2022

@author: Titus
"""

import os
import pandas as pd
import numpy as np
import matplotlib as plt
import ternary


print("Version", ternary.__version__)
#%% Prep some data
pc_mineral = pd.read_csv('input/Weight_percent_oxides_in_PC.csv')

# Normalize data
pc_mineral['total']=pc_mineral.iloc[:,1:5].sum(axis = 1)
pc_mineral['Mg_nor'] = pc_mineral['MgO'] /pc_mineral['total'] * 100
pc_mineral['Al_nor'] = pc_mineral['Al2O3'] /pc_mineral['total'] * 100
pc_mineral['Si_nor'] = pc_mineral['SiO2'] /pc_mineral['total'] * 100
pc_mineral['P_nor'] = pc_mineral['P2O5'] /pc_mineral['total'] * 100


#%% plot setup Mg Al ternary

# Make images higher resolution and set default size
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (4, 4)

## Boundary and Gridlines
scale = 100
figure, tax = ternary.figure(scale=scale)
#plt.rcParams['text.usetex'] = True
# Draw Boundary and Gridlines
tax.boundary(linewidth=1.5)
# tax.gridlines(color="black", multiple=6)
tax.gridlines(color="blue", multiple=10, linewidth=0.5)

# Set Axis labels and Title
fontsize = 12
offset = 0.18
#tax.set_title("Various Lines\n", fontsize=fontsize)
# tax.right_corner_label("$SiO_2 + P_2O_5$", fontsize=fontsize, offset= -0.1) # bottom right and is "x" value SiO_2 + P_3O_5
# tax.top_corner_label("MgO", fontsize=fontsize) # top and is "y" value
# tax.left_corner_label("$Al_2O_3$", fontsize=fontsize, offset= -0.1) #bottom left and is "z" value
tax.left_axis_label("$Al_2O_3$ (wt. %)", fontsize=fontsize, offset=offset)
tax.right_axis_label("MgO (wt. %)", fontsize=fontsize, offset=offset)
tax.bottom_axis_label("$SiO_2 + P_2O_5$ (wt. %)", fontsize=fontsize, offset=offset)

df = pd.DataFrame({'P_Si' : (pc_mineral['Si_nor'] + pc_mineral['P_nor'])}) #seting X value
df['Mg_nor'] = pc_mineral['Mg_nor'] # seting "Y" value
df['Al_nor'] = pc_mineral['Al_nor'] # seting "Z" value
df_Al_Mg = df.iloc[[0,1,2,5,6],:]
df_Si_P = df.iloc[[3,4,7,8],:]
points_in = df_Al_Mg.values.tolist()
points_out = df_Si_P.values.tolist()
tax.scatter(points_in, marker='o', color='green')
tax.scatter(points_out, marker='o', color='blue')
# tax.legend()

# Set ticks
tax.ticks(axis='lbr', linewidth=1, multiple=10, offset=0.03)

# Background color
tax.set_background_color(color="white", alpha=0.7) # the detault, essentially

# Remove default Matplotlib Axes
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')
svg_name_path = 'output/Mg_Al_ternary.svg'
#Uncoment to save
# tax.savefig(svg_name_path, transparent=False, bbox_inches="tight")
# ternary.plt.show()

#%% plot setup P and Si ternary

# Make images higher resolution and set default size
plt.rcParams['figure.dpi'] = 300
plt.rcParams['figure.figsize'] = (4, 4)

## Boundary and Gridlines
scale = 100
figure, tax = ternary.figure(scale=scale)
#plt.rcParams['text.usetex'] = True
# Draw Boundary and Gridlines
tax.boundary(linewidth=1.5)
# tax.gridlines(color="black", multiple=6)
tax.gridlines(color="blue", multiple=10, linewidth=0.5)

# Set Axis labels and Title
fontsize = 12
offset = 0.18
#tax.set_title("Various Lines\n", fontsize=fontsize)
# tax.right_corner_label("$MgO + SiO_2$", fontsize=fontsize, offset= -0.1) # bottom right and is "x" value
# tax.top_corner_label("$SiO_2$", fontsize=fontsize) # top and is "y" value
# tax.left_corner_label("$P_2O_5$", fontsize=fontsize, offset= -0.1) #bottom left and is "z" value
tax.left_axis_label("$P_2O_5$ (wt. %)", fontsize=fontsize, offset=offset)
tax.right_axis_label("$SiO_2$ (wt. %)", fontsize=fontsize, offset=offset)
tax.bottom_axis_label("$MgO + SiO_2$ (wt. %)", fontsize=fontsize, offset=offset)

df = pd.DataFrame({'Mg_Al' : (pc_mineral['Mg_nor'] + pc_mineral['Al_nor'])}) #seting X value
df['Si_nor'] = pc_mineral['Si_nor'] # seting "Y" value
df['P_nor'] = pc_mineral['P_nor'] # seting "Z" value
df_Al_Mg = df.iloc[[1,2,5,6],:]
df_Si_P = df.iloc[[0,3,4,7,8],:]
points_in = df_Al_Mg.values.tolist()
points_out = df_Si_P.values.tolist()
tax.scatter(points_in, marker='o', color='green')
tax.scatter(points_out, marker='o', color='blue')
# tax.legend()

# Set ticks
tax.ticks(axis='lbr', linewidth=1, multiple=10, offset=0.03)

# Background color
tax.set_background_color(color="white", alpha=0.7) # the detault, essentially

# Remove default Matplotlib Axes
tax.clear_matplotlib_ticks()
tax.get_axes().axis('off')
svg_name_path = 'output/P_Si_ternary.svg'
#Uncoment to save
# tax.savefig(svg_name_path, transparent=False, bbox_inches="tight")
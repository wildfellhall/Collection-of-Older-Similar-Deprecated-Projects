# A short project that I wrote as a kid (around 10 years old?) . Throughout the years, I've pulled this out as a quick party trick to entertain younger kids during coding classes/camps. 
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
import random
html_colors = [
    "AliceBlue", "AntiqueWhite", "Aqua", "Aquamarine", "Azure", "Beige", "Bisque",
    "Black", "BlanchedAlmond", "Blue", "BlueViolet", "Brown", "BurlyWood", "CadetBlue",
    "Chartreuse", "Chocolate", "Coral", "CornflowerBlue", "Cornsilk", "Crimson",
    "Cyan", "DarkBlue", "DarkCyan", "DarkGoldenrod", "DarkGray", "DarkGreen",
    "DarkKhaki", "DarkMagenta", "DarkOliveGreen", "DarkOrange", "DarkOrchid",
    "DarkRed", "DarkSalmon", "DarkSeaGreen", "DarkSlateBlue", "DarkSlateGray",
    "DarkTurquoise", "DarkViolet", "DeepPink", "DeepSkyBlue", "DimGray", "DodgerBlue",
    "FireBrick", "FloralWhite", "ForestGreen", "Fuchsia", "Gainsboro", "GhostWhite",
    "Gold", "Goldenrod", "Gray", "Green", "GreenYellow", "Honeydew", "HotPink",
    "IndianRed", "Indigo", "Ivory", "Khaki", "Lavender", "LavenderBlush", "LawnGreen",
    "LemonChiffon", "LightBlue", "LightCoral", "LightCyan", "LightGoldenrodYellow",
    "LightGray", "LightGreen", "LightPink", "LightSalmon", "LightSeaGreen",
    "LightSkyBlue", "LightSlateGray", "LightSteelBlue", "LightYellow", "Lime",
    "LimeGreen", "Linen", "Magenta", "Maroon", "MediumAquamarine", "MediumBlue",
    "MediumOrchid", "MediumPurple", "MediumSeaGreen", "MediumSlateBlue",
    "MediumSpringGreen", "MediumTurquoise", "MediumVioletRed", "MidnightBlue",
    "MintCream", "MistyRose", "Moccasin", "NavajoWhite", "Navy", "OldLace", "Olive",
    "OliveDrab", "Orange", "OrangeRed", "Orchid", "PaleGoldenrod", "PaleGreen",
    "PaleTurquoise", "PaleVioletRed", "PapayaWhip", "PeachPuff", "Peru", "Pink",
    "Plum", "PowderBlue", "Purple", "Red", "RosyBrown", "RoyalBlue", "SaddleBrown",
    "Salmon", "SandyBrown", "SeaGreen", "SeaShell", "Sienna", "Silver", "SkyBlue",
    "SlateBlue", "SlateGray", "Snow", "SpringGreen", "SteelBlue", "Tan", "Teal",
    "Thistle", "Tomato", "Turquoise", "Violet", "Wheat", "White", "WhiteSmoke",
    "Yellow", "YellowGreen"
]
log = []
print("Welcome to Ripoff Microsoft Paint")
print("You will get 3 paint blob groups to make the best piece of art. ")
print("If you're struggling to make a decision, type the number 911 to get a random ")
times = 0
while times < 3:
  paint_dobs = int(input("How many blobs of paint would you like to make? "))
  if paint_dobs == 911:
    paint_dobs = random.randint(1,100)
  X,y = make_blobs(centers = paint_dobs,n_samples = 200,cluster_std = 0.2)
  color = input("What color would you like the blob group to be? ")
  if color == "911":
    color = random.choice(html_colors)
  size = int(input("How big would you like the blobs to be? For best results, choose a number between 50 and 500. "))
  if size == 911:
    size = random.randint(50,500)
  superline = int(input("Please choose a very large number for the size of your drips on the canvas. (Cannot exceed 500) "))
  if superline == 911:
    superline = random.randint(1,500)
  plt.scatter(X[:,0],X[:,1],color = color,s = size, linewidth = superline)
  log.append(color)
  times+=1
print("Here are the colors you used:",log)

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import *
import pdb

print("""
MatPlotLib Advanced Tutorial
----------------------------
This is a tutorial covering the features and usage of the matplotlib package
in more detail. In truth, no single tutorial can cover all the features that
exist in the matplotlib package since it is extremely expansive. This tutorial
will cover as much material as possible to let you know of the features that
are available to you when plotting data. 

Some Notes:
1) A few parts of this program uses pdb to pause the program and allow the
   user to try making things for themselves. Use c to continue with the
   program.

2) This program uses plt for the reference name of pyplot. All pyplot methods
   should be preceded with the qualifier plt such as plt.show().

3) For the best results, run this program with ipython. Regular python may
   dislike plotting during program execution.
""")

pause = input("Press [Enter] to continue...")
print('\n'*100)

print("""
###
## pyplot
###

Within the matplotlib package, the main module you want to be using is the
pyplot module. It is generally imported as

import matplotlib.pyplot as plt

The pyplot module has many useful functions that can be called and used and
we will go over them one by one. For reference, some useful methods are shown
below.

>>> plt.close()              # Closes the current figure. Optional arguments
                               include passing in a figure, figure number,
                               or the string 'all' which closes all figures.
>>> plt.draw()               # Forces the figure to be redrawn. Useful if it
                               was been updated after it was last shown or
                               drawn.
>>> plt.gca()                # Returns the currently active axes object
>>> plt.gcf()                # Returns the currently active figure object
>>> plt.show()               # Shows the latest figure. By default, matplotlib
                               pauses and waits for the window to be closed
                               before continuing. This feature can be turned
                               off with the keyword block = False.
>>> plt.savefig('title.png') # Saves the figure to a file. The file type is
                               automatically determined by the extension.
                               Supported formats include png, pdf, ps, eps,
                               and svg. This has the keywords dpi which
                               specifies the resolution of the output and
                               bbox_inches which, when set to 'tight' reduces
                               any extra white space in the saved file.
>>> plt.subplots_adjust()    # Allows for adjusting parameters of the layout
                               such as the horizontal space (hspace) or width
                               space (wspace) between plots, as well as the
                               left, right, top, and bottom padding.
""")

pause = input("Press [Enter] to continue...")
print('\n'*100)

print("""
###
## Components of a Plot
###

At it's core, matplotlib is nothing more than a graphics package. Every
component of a plot is just a particular "Artist", all drawn on top of
each other to make a nice looking plot.

The beauty of pyplot is the degree of customization that you can have. 
You have control over every individual component of this plot and you can
change each of them individually. To do this properly, we will focus on
using the object oriented feature of matplotlib.

Before we talk about how to work with all these features, we need to know
what they are. A window should have just popped up that you can examine.
This window shows all the various components of a figure and the names that
pyplot uses for them. This figure contains the following components

-> Figure    The main part of the plot which everything is shown on. This
             encompasses the entire area of the window, excluding the toolbar.
-> Axes      A single plot, added to the figure. This can have many sets of
             data added to it along with other components such as legends.
             Axes can even sit on top of other axes, but importantly, they
             are still a component of figure, not the axes they may sit inside
             of.
-> Axis      Note the difference here! This is an axIs not an axEs. This
             component is a single axis on the axes and defines how the data
             is plotted. An axes, by default has two axises, the x and y
             (unless you're plotting in 3D in which case it has a z). You can
             add more axises though. Each axis has various components such as
             the spine, tick labels, major ticks, and minor ticks.
-> Spine     Each axis has various components. One of them is the spine. This
             is the actual black line at the border of the plots that the
             tick marks are drawn on. Each default axis has 2 spines. For the
             x axis, it has the top and bottom spine and likewise the y axis
             has the right and left.
-> Legend    Each axes can have a legend added to it. The legend can have lines
             on it, one for each curve labeled.
""")

x = np.arange(0,4*np.pi+np.pi/8,np.pi/8)
y1 = np.sin(x)
y2 = np.cos(x)

fig, (ax1, ax2) = plt.subplots(2, figsize = (10,7))
fig.canvas.set_window_title('Pyplot Figure Components')

plt.subplots_adjust(hspace = 0.4)
plt.suptitle('Figure title', fontsize = 20)

#Create subplot 1
ax1.plot(x, y1, '-dr', label = '$sin(x)$')
ax1.plot(x, np.array([0]*len(x)), '--k')
ax1.set_xlim([0,4*np.pi])
ax1.set_title('Axes 1 Title')
ax1.set_xlabel('Axes 1 x-axis label')
ax1.set_ylabel('Axes 1 y-axis label')
ax1.legend(loc = 'best')

#Create subplot 2
ax2.plot(x, y2, ':og', label = '$cos(x)$')
ax2.plot(x, np.array([0]*len(x)), '-k')
ax2.set_xlim([0,4*np.pi])
ax2.set_title('Axes 2 Title')
ax2.set_xlabel('Axes 2 x-axis label')
ax2.set_ylabel('Axes 2 y-axis label')
ax2.legend(loc = 'best')

#Add artists
ax = fig.add_axes([0,0,1,1])
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)
ax.set_zorder(0)
ax.set_axis_bgcolor((0, 0, 0, 0))

ax.add_patch(Rectangle((0.01,0.01),0.98,0.98, fill = False, lw = 2, ec = 'b', transform=ax.transAxes))
ax.annotate('Figure', (0.02,0.02), textcoords = 'axes fraction',
            fontsize = 20, color = 'b', transform=ax.transAxes)

ax.add_patch(Rectangle((0.04,0.5),0.9,0.44, fill = False, lw = 2, ec = 'g', transform=ax.transAxes))
ax.annotate('Axes', (0.05,0.52), textcoords = 'axes fraction',
            fontsize = 20, color = 'g', transform=ax.transAxes)

ax.add_patch(Rectangle((0.11,0.08),0.03,0.38, fill = False, lw = 2, ec = 'r', transform=ax.transAxes))
ax.annotate('Axis', (0.045,0.4), textcoords = 'axes fraction',
            fontsize = 20, color = 'r', transform=ax.transAxes)

ax.add_patch(Rectangle((0.11,0.08),0.8,0.04, fill = False, lw = 2, ec = 'r', transform=ax.transAxes))
ax.annotate('Axis', (0.85,0.04), textcoords = 'axes fraction',
            fontsize = 20, color = 'r')

ax.annotate('Spine', (0.8,0.43), xytext = (0.8,0.35), xycoords = 'axes fraction',
            color = (1,0.5,0), fontsize = 20, 
            textcoords = 'axes fraction', horizontalalignment='left',
            arrowprops=dict(arrowstyle = '-|>', fc=(1,0.5,0)))

ax.annotate('', (0.9,0.32), xytext = (0.84,0.34), xycoords = 'axes fraction',
            arrowprops=dict(arrowstyle = '-|>', fc=(1,0.5,0)))

plt.show(block = False)
plt.pause(0.01)

pause = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Objects in matplotlib
###

The above mentioned components of a figure (along with a few others) are
all representable as objects. These objects are stored in a variable which
maintains the state of that object and also has functions the object can
call to change its state. Let's look at how we can use these objects to
create a new figure.
""")

pause = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Creating a New Figure
###

There multiple ways to create a new figure. Probably the simplest is

>>> fig = figure(1, figsize = (5,5), tight_layout = True)

The 1 in this case is an ID for the figure (much like the logical unit
number in IDL). The keywords figsize and tight_layout are optional. The
former sets the physical size of the figure and the second tells the layout
manager to make the plots as close as possible. The state of the figure is
stored in the fig variable which knows entirely about this new figure.
Calling this figure method tells matplotlib that any subsequent plotting
commands should apply to this figure. We can switch to plotting on a new
figure by calling the figure command for another figure (or even switch
back to an old figure). Another method for creating figures is the following

>>> fig = plt.subplots()

This method is much more powerful, but these features will be discussed in
the next section. For reference here are a set of methods and their
functionality that the figure object can call

>>> fig.add_subplot(111)   # Adds a subplot at the specified position
>>> fig.clear()            # Clears the figure's axes
>>> fig.suptitle('Title')  # Adds a title to the figure

Many of the methods listed above as pyplot methods, such as subplots_adjust or
draw, can be applied to a specific figure as well.
""")

pause = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Creating a New Axes
###

Once you have a figure, it's time to add some Axeses to it. As mentioned
before, matplotlib supports using objects. If you've properly created your
figure, it will have been stored into an object. You can now call the method
add_subplot.

>>> ax = fig.add_subplot(1,1,1)

The order of these parameters is add_subplot(rows, columns, plotNo), where
plotNo is the number of the plot, starting at 1 in the upper left and counting
left to right then top to bottom. If all values are less than 10, an equivalent
procedure is to do

>>> ax = fig.add_subplot(111)

Note how this function has created and returned an axes object which we have
stored into the variable ax. There is another method which creates the figure
an axes at the same time

>>> fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, figsize = (8,8))

The figure is stored into the first variable and the axes are stored into
the second variable with is a tuple of axes.

You can also call the plt.subplot() which acts like add_subplot() but adds
an axes to the currently active figure (determined by the last one referenced).

For more control over your axes positioning, you can specify the exact position
and extent of an axes with the subplot2grid function.

>>> ax = plt.subplot2grid((2,3),(1,0), colspan = 2, rowspan = 1)

This tells figure that there will be a grid of 2 x 3 plots (2 rows, 3 cols) and
this creates a new plot at the position (1,0) (second row, first column) with a
column span of 2 and a row span of 1. If you really want to specify the exact
location, try the add_axes method.

>>> ax = fig.add_axes([0.5, 0.5, 0.3, 0.3])

This tells the figure to put the lower left corner of the axes at the position
(0.5, 0.5) (as fractions of the figure size) and have it span a width and height
of (0.3, 0.3). This is useful to putting plots inside plots. Try this out for
yourself!
""")

pdb.set_trace()
print('\n'*100)

print("""
###
## Plotting to Axes
###

There are many types of plots that can be put on an axes. Below are some simple
examples.

>>> ax.plot()     # Simple scatter/line plot
>>> ax.bar()      # Vertical bar plot
>>> ax.barh()     # Horizonatal bar plot
>>> ax.boxplot()  # Box and wisker plot
>>> ax.contour()  # Contour plot of lines
>>> ax.contourf() # Filled contour plot
>>> ax.errorbar() # Scatter/line plot with errorbars
>>> ax.fill()     # Scatter/line plot which is filled below the curve
>>> ax.hist()     # A histogram of the input data
>>> ax.loglog()   # Scatter/line plot that is logarithmic on both axes
>>> ax.pie()      # Pie chart
>>> ax.polar()    # Polar plot
>>> ax.quiver()   # 2D field of arrows
>>> ax.semilogx() # Scatter/line plot with logarithmic x and linear y.
>>> ax.semilogy() # Equivalent to semilogx, but now y is logarithmic
>>> ax.steamplot()# A streamline of a vector flow
>>> ax.step()     # A step plot

Feel free to try out some of these. You may have to look up the proper
procedures online.
""")

pdb.set_trace()
print('\n'*100)

print("""
###
## Axes Methods
###

Aside from the many plots, there are many useful methods to adjust the
properties of of the axes

>>> ax.add_patch()     # Adds a 'patch' which is an artist like arrows or circles
>>> ax.annotate()      # Adds a string with an arrow to the axes
>>> ax.axhspan()       # Adds a horizontal bar across the plot
>>> ax.axvspan()       # Adds a vertical bar across the plot
>>> ax.arrow()         # Adds an arrow
>>> ax.cla()           # Clears the axes
>>> ax.colorbar()      # Colorbar added to the plot
>>> ax.grid()          # Turns on grid lines, keywords include which (major or
                         minor) and axis (both, x, or y).
>>> ax.legend()        # Legend added to the plot
>>> ax.minorticks_on() # Turns on minor tick marks
>>> ax.set_cmap()      # Sets the color map of the axes
>>> ax.set_title()     # Sets the title of the axes
>>> ax.set_xlabel()    # Sets the x label of the axes
>>> ax.set_xlim()      # Sets the x limits of the axes
>>> ax.set_xscale()    # Sets the scale, either linear, log, or symlog
>>> ax.set_xticklabels()#A list of strings to use for the tick labels
>>> ax.set_xticks()    # Set's values of tick marks with list
## The above x axis specific functions have analagous y axis functions
>>> ax.text()          # Adds a string to the axes
>>> ax.tick_params()   # Changes tick and tick label appearances

Try playing with these various features after creating a figure and axes.
""")

pdb.set_trace()
print('\n'*100)

print("""
###
## Axis and Spines
###

Just as you can work with the specific axes on a figure, you can also work with
specific axis and spines on your axes. These can be extracted and stored in
their own variables, but it is generally easier to refer to them as the
components of the axes object. They are accessed in the following way.

>>> ax.xaxis
>>> ax.yaxis
>>> ax.spine['top']    # Spine is a dict with components, 'top', 'bottom',
                         'left', and 'right'.

These components of the axes have the following useful methods.

>>> ax.xaxis.set_major_formatter()# Set's how the tick marks are formatted
>>> ax.xaxis.set_major_locator()  # Sets location of tick marks (see locators)
## The above major methods have analagous minor methods
>>> ax.xaxis.set_ticklabels()     # Set to empty list to turn off labels
>>> ax.xaxis.set_ticks_position() # Change tick position to only 'top', 'left, etc.
## The above xaxis methods have analagous yaxis methods
>>> ax.spines['top'].set_color()  # Sets the color of the spine
>>> ax.spines['top'].set_position()# Changes position of the spine
>>> ax.spines['top'].set_visible()# Turns off the spine
## The above spine methods have analagous methods for 'bottom', 'left', and
   'right'

Feel free to play with these properties as well.
""")

pdb.set_trace()
print('\n'*100)

print("""
###
## Higher Degrees of Customization
###

We could choose to go even further down the ladder than axis and spines. It is
possible to get the tickmark objects from an axis (via get_major_ticks()) and
change properties on a tickmark by tickmark basis. However, it is no longer
instructive to continue showing methods and ways of doing this as it can always
be looked up. For extreme control over every component of plotting, it is sometimes
useful to use the rcParams variable. This should be imported as

from matplotlib import rcParams

You can then refer to any component of the figure by referencing the dict's
keyword, and setting the value. Common examples include

>>> rcParams['lines.linewidth'] = 2   # Sets linewidths to be 2 by default
>>> rcParams['lines.color'] = 'r'     # Sets line colors to be red by default

There are hundreds of parameters that can be set, all of which can be seen by
going here http://matplotlib.org/users/customizing.html.
""")

pause = input('Press [Enter] to continue...')
print('\n'*100)

print("""
###
## Animations
###

This will only introduce the idea of animations. To actually produce saved
animations in the form of mp4 or some similar format requires installing third
party programs such as ffmpeg. However, matplotlib comes with an animation
package imported as matplotlib.animation. It has tools to allow you to
continually update a plot such that it is animated. There are abilities to
save the animation as well. Below is the code for a very simple animation plot.

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.set_xlim([0,2*np.pi])

x = np.arange(0, 2*np.pi, 0.01)   # x-array
line, = ax.plot(x, np.sin(x))     # The comma after line makes it a tuple

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

#blit=True means only redraw the components which have updated. This is
#faster than redrawing everything.
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              interval=25, blit=True)
plt.show()
""")

fig, ax = plt.subplots()
ax.set_xlim([0,2*np.pi])

x = np.arange(0, 2*np.pi, 0.01)   # x-array
line, = ax.plot(x, np.sin(x))     # The comma after line makes it a tuple

#Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

def animate(i):
    line.set_ydata(np.sin(x+i/10.0))  # update the data
    return line,

#blit=True means only redraw the components which have updated. This is
#faster than redrawing everything.
ani = animation.FuncAnimation(fig, animate, init_func=init,
                              interval=25, blit=True)
plt.show(block = False)

print('Done...')

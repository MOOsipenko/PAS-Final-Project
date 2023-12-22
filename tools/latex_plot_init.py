from matplotlib.pyplot import rc
import matplotlib

rc('text', usetex=True)
#rc('text.latex', unicode=True)
#rc('text.latex', preamble="\\usepackage{amsfonts}")
rc('font', family='times')
fontsize=18
matplotlib.rcParams.update({'axes.labelsize' : fontsize, \
                            'font.size' : fontsize, \
                            'legend.fontsize': fontsize, \
                            'xtick.labelsize' : fontsize, \
                            'ytick.labelsize' : fontsize})
rc('figure', figsize=(16, 8)) 
plt = matplotlib.pyplot
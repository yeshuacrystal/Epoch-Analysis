import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import glob
import statsmodels.api as sm
from sklearn.utils import shuffle
from calendar import isleap

import nolds


# matplotlib inline
# config InlineBackend.figure_format = 'svg' # 'svg', 'retina'
plt.style.use('seaborn-white')

xx = pd.read_excel(r'C:\Users\DELL\Documents\Research\Conferences\Ilorin conference\FIGgeosub\ExtSYMM.xlsx')

x=np.array(xx['SMH'])
x = x.reshape((3,4320)) # now we reshape it: here each row is an epoch
epoch_average = x.mean(axis=1)

# Plot figure to show results
show_figure = True
if show_figure:
    fig, axs = plt.subplots(nrows=3, ncols=1, figsize=(12,15), sharey='row')
    for i, (ax, x_epoch) in enumerate(zip(axs.flatten(), x)):
        plt.sca(ax)
        plt.plot(np.arange(x.shape[1]), x_epoch, 'k-', label='epoch-{}'.format(i))
        plt.axhline(epoch_average[i], label='epoch-average', color='red', alpha=0.8, lw=2.0, ls='--')
        plt.legend()
        plt.title('Epoch-{} Average: {:.3f}'.format(str(i).zfill(2), epoch_average[i]))

    plt.tight_layout()
    plt.show()
    fig.savefig('output.png', dpi=300)   
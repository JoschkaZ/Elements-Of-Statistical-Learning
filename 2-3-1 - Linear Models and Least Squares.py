# %%
import utils
reload(utils)
from utils import *
from importlib import reload


df = get_data1()

df.head()



#%%

ax = df[df['y']==0].plot.scatter(x='x1', y='x2', color='blue', label='G1');
df[df['y']==1].plot.scatter(x='x1', y='x2', color='orange', label='G2', ax=ax);

plt.show()

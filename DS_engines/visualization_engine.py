# Data Analysis
import pandas as pd
import numpy as np

# Data Visualization
import matplotlib.pyplot as plt
import seaborn as sns

from DS_engines.analysis_engine import AnalysisPrototype

"""!VISUALIZATION PROTOTYPE!"""

class VisualizationPrototype(object):
    def __init__(self, path):
        self.path = path
        self.dataset = None
        self.analysis_engine = None
        self.encoders = None

    def read(self):
        self.dataset = pd.read_csv(self.path)

    def load_analysis_engine(self, columns_to_drop):
        self.analysis_engine = AnalysisPrototype(self.path)
        self.analysis_engine.read()
        self.analysis_engine.create_vis_dataset(columns_to_drop)
        self.dataset = self.analysis_engine.vis_dataset
        
    def peak(self, rows=10):
        return self.dataset.head(rows)
    def summary(self):
        return self.dataset.describe()


    def create_normal_distribution_graph(self, colormap, column, distribution_size, sample_size):
      cm = plt.cm.get_cmap(colormap)
      distribution = self.analysis_engine.create_sample_distribution(column, distribution_size, sample_size)

      # # Plot histogram
      fig, ax = plt.subplots()
      n, bins, patches = ax.hist(distribution, 20, density=1)
      bin_centers = 0.5 * (bins[:-1] + bins[1:])

      # Set the ticks to be at the edges of the bins.
      ax.set_xticks(bins)

      # scale values to interval [0,1]
      col = bin_centers - min(bin_centers)
      col /= max(col)

      for c, p in zip(col, patches):
          plt.setp(p, 'facecolor', cm(c))

      for count, x in zip(n, bin_centers):
          # Label the percentages
          percent = '%0.0f%%' % (100 * float(count) / n.sum())
          ax.annotate(percent, xy=(x, 0), xycoords=('data', 'axes fraction'),
              xytext=(0, -32), textcoords='offset points', va='top', ha='center')

      plt.xlabel(column)
      plt.ylabel('Values')
      plt.title(f'Normal Distribution of {column}')
      fig = plt.gcf()
      fig.set_size_inches(18.5, 10.5)
      plt.show()

    def value_count_bar(self, column, increments, title):
      # get data dictionary using analysis engine's method
      print(self.dataset[column])
      data = self.analysis_engine.break_up_by_value_count(column, increments)
      print(data)

      i = 0
      # iterate over each increment and create bar plots for each
      for i in range(len(data)):
        x = data[i].keys() # column data
        y = data[i].values() # value counts

        # create bar plot
        plt.bar(x, y, color = 'c')
        # set title to reflect increments
        if i == 0:
          plt.title(f'{title} (Under {increments[i]} Value Counts)')
        elif i == len(data):
          plt.title(f'{title} (Over {increments[i]} Value Counts)')
        else:
          plt.title(f'{title} (Between {increments[i-1]+1} and {increments[i]} Value Counts)')
        # set x and y axis labels
        plt.xlabel(column)
        plt.ylabel('Value Counts')

        plt.show()

    def data_incremented_scatter(self, column, increments, title):
      data = self.analysis_engine.break_up_by_data_size(column, increments)
      i = 0
      for i in range(len(data)):
        x = data[i].keys()
        y = data[i].values()

        plt.scatter(x, y)
        plt.ylabel('Value Counts')
        plt.xlabel(column)
        if i == 0:
          plt.title(f'{title} ({column} Under {increments[i]})')
        elif i == len(data):
          plt.title(f'{title} ({column} Over {increments[i]})')
        else:
          plt.title(f'{title} ({column} Between {increments[i-1]+1} and {increments[i]})')
        plt.show()
        print(f'Average value count: {(np.array(list(data[i].values()))).mean()}')
        print(f'Average data point: {(np.array(list(data[i].keys()))).mean()}')


    def Q1(self, dataset, x_arg, y_arg, title, toggle_quantities=False, stacked=False, save=False):
        """ Custom function to visualize answers for Q1 of the OITA project. """
        # Instantiate grid spaces across bar chart for both title and plot
        if stacked is True:
            figure = plt.figure(figsize=(12, 12))
            grids = figure.add_gridspec(2, 1)
            grids.update(wspace=0.3, hspace=0.15)
            ax0 = figure.add_subplot(grids[0, 0])
            ax1 = figure.add_subplot(grids[1, 0])
        else:
            figure = plt.figure(figsize=(18, 7))
            grids = figure.add_gridspec(1, 2)
            grids.update(wspace=0.3, hspace=0.15)
            ax0 = figure.add_subplot(grids[0, 0])
            ax1 = figure.add_subplot(grids[0, 1])
        
        # Create and set title grid
        TITLE_AX0 = title
        
        ax0.text(0.5, 0.5,
                TITLE_AX0,
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=28,
                fontweight="bold",
                fontfamily="serif",
                color="#000000")
        
        # Remove chart labels outline from title grid
        ax0.set_xticklabels([]); ax0.set_yticklabels([])
        ax0.tick_params(left=False, bottom=False)
        
        # Set bar chart in second grid space and remove spine
        ax_states = ax1
        barp = sns.barplot(x=x_arg,
                          y=y_arg,
                          data=dataset,
                          ax=ax_states,
                          palette="crest")
        sns.despine()
        
        # Obtain and set quantitative values on top of bars
        if toggle_quantities is True:
          for patch in barp.patches:
              barp.annotate(format(patch.get_height(), ".2f"), (patch.get_x() + patch.get_width() / 2.,
                                                              patch.get_height()), ha="center", va="center", 
                            xytext=(0, 10), textcoords="offset points")
        
        # Remove grid spinal outline from title grid
        for orientation in ["top", "left", "bottom", "right"]:
            ax0.spines[orientation].set_visible(False)

        # Save file
        if save is True:
            SAVEPATH = f"Q1_Visualization{title}.png"
            plt.savefig(SAVEPATH, facecolor="white")
        
        # Render visualization
        plt.show()
        return
    
    
    def Q2(self, dataset, x_arg, y_arg, title, stacked=False, save=False):
        """ Plotting method to obtain visual answer to Inquiry #2. """
        """ Custom function to visualize answers for Q2 of the OITA project. """
        # Instantiate grid spaces across scatter plot for both title and plot
        if stacked is True:
            figure = plt.figure(figsize=(12, 12))
            grids = figure.add_gridspec(2, 1)
            grids.update(wspace=0.3, hspace=0.15)
            ax0 = figure.add_subplot(grids[0, 0])
            ax1 = figure.add_subplot(grids[1, 0])
        else:
            figure = plt.figure(figsize=(18, 7))
            grids = figure.add_gridspec(1, 2)
            grids.update(wspace=0.3, hspace=0.15)
            ax0 = figure.add_subplot(grids[0, 0])
            ax1 = figure.add_subplot(grids[0, 1])
        
        # Create and set title grid
        TITLE_AX0 = title
        ax0.text(0.5, 0.5,
                TITLE_AX0,
                horizontalalignment="center",
                verticalalignment="center",
                fontsize=28,
                fontweight="bold",
                fontfamily="serif",
                color="#000000")
        
        # Remove chart labels outline from title grid
        ax0.set_xticklabels([]); ax0.set_yticklabels([])
        ax0.tick_params(left=False, bottom=False)
        
        # Set bar chart in second grid space and remove spine
        ax_scattered = ax1
        scap = sns.scatterplot(x=x_arg, y=y_arg, data=dataset, ax=ax_scattered, hue="state", alpha=0.5, palette="dark")
        scap.legend(loc="center left", bbox_to_anchor=(1.25, 0.5), ncol=1)
        sns.despine()
        
        # Remove grid spinal outline from title grid
        ax0.spines["top"].set_visible(False)
        ax0.spines["left"].set_visible(False)
        ax0.spines["bottom"].set_visible(False)
        ax0.spines["right"].set_visible(False)

        # Save file
        if save is True:
            SAVEPATH = f"Q2_Visualization_{title}.png"
            plt.savefig(SAVEPATH, facecolor="white")

        # Render visualization
        plt.show()
        return
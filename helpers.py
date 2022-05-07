import seaborn as sns
import matplotlib.pyplot as plt

# HELPER FUNCTION 1
#   set null values to -0.00001
#   highlights negative numbers (useful if imputing null values as negative nums)
def impute_null_as_neg(dataframe):
    dataframe.fillna(-0.00001, inplace=True)
    return dataframe

def highlight_neg_num(cell):
    if type(cell) != str and cell < 0 :
        return 'background: #fa8072; color:black'
    else:
        # do i need a background color here or will it just not do anything?
        return

# HELPER FUNCTION 2
    # create a stylized dataframe viewer
def create_stylized_df(dataframe, num_rows, background_color, text_color='black', border_color='white', highlight_null=False, highlight_neg=False):
    VIEWING_PROPERTIES = {
        "background-color": background_color,
        "color": text_color,
        "border-color": border_color
    }

    stylized_dataframe = dataframe.head(num_rows).style.set_properties(**VIEWING_PROPERTIES)

    if highlight_null==True:
        stylized_dataframe = stylized_dataframe.highlight_null(null_color="red")
    if highlight_neg==True:
        stylized_dataframe = stylized_dataframe.applymap(highlight_neg_num)
    return stylized_dataframe
        

# HELPER FUNCTION 3
    # save a visualization as an image
    # takes in parameters:
    #   filename (the name of the img file to be saved)
    #   visualization plot (a matplotlib.pyplot)
def save_visualization_as_img(filename, visualization_plt):
    SAVEPATH = filename
    visualization_plt.savefig(SAVEPATH, facecolor="white")


# HELPER FUNCTION 4
def create_sub_dataset(dataframe, new_df_name, col_list):
    new_df_name = dataframe[col_list]
    new_df_name = new_df_name.reset_index()
    return new_df_name

# HELPER FUNCTION 5
def get_basic_stats(dataset):
    # Initialize plotting boundaries for larger matrixes
    plt.figure(figsize=(24, 18))

    # Generate quantitative heatmap to visualize correlations across data
    sns.heatmap(dataset.corr(),
                annot=True,
                cmap=sns.diverging_palette(20, 220, n=200),
                square=True)

    # Set title for correlation matrix
    plt.title("Correlation Matrix")

    dataset.describe()
    dataset.cov()
    dataset.corr()


# HELPER FUNCTION 6



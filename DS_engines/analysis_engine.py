# Data Analysis
import pandas as pd
import numpy as np

# Data Processing
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder


"""!DATA ANALYSIS PROTOTYPE!"""
class AnalysisPrototype(object):
    def __init__(self, path):
        self.path = path
        self.dataset = None
        self.vis_dataset = None
        self.encoders = None
        self.reference_dict = None
    def read(self):
        self.dataset = pd.read_csv(self.path)
        assert type(self.dataset) == pd.core.frame.DataFrame
    def peak(self, rows=10):
        return self.dataset.head(rows)
    def summary(self):
        return self.dataset.describe()


#———————————————————————FOR NULL ANALYSIS AND SUMMARIZATION———————————————————————————#

    def null_summary(self, three_columns):
      print('NUMBER OF NULL VALUES FOR EACH COLUMN')
      print(self.dataset.isna().sum())
      print('—————————————————————————————————————————————————————————————————')
      print('INFO FOR EACH ROW WITH NULL VALUES')
      for column in self.dataset.columns:
        for index, row in self.dataset.iterrows():
          if np.isnan(row[column]) == True:
            for column in self.dataset.columns:
              print(row[column])
      print('—————————————————————————————————————————————————————————————————')
      print('ROWS WITH NULL VALUES OF GIVEN COLUMNS')
      for index, row in self.dataset.iterrows():
        if np.isnan(row[three_columns[0]]) == True and np.isnan(row[three_columns[1]]) == True and np.isnan(row[three_columns[2]]) == True:
          print(row)
          print('—————————————')


    def null_analysis_column(self, column, column_filter=None):
      is_NaN = self.dataset.isnull()
      row_has_NaN = is_NaN.any(axis=1)
      rows_with_NaN = self.dataset[row_has_NaN]
      # check if it is string or int and perform operations accordingly
      if self.dataset[column].dtype == 'int64' or self.dataset[column].dtype == 'float64':
        if column_filter == None:
          print(f"the most commonly occuring {column} with null values is: {rows_with_NaN[column].mode()}")
          print(f"the average {column} with null values is {rows_with_NaN[column].mean()}")
        else:
          ARG_FILTERED = self.dataset[column] == column_filter
          dataset_filtered = self.dataset[ARG_FILTERED]
          print(f'For the column {column} filtered by the match {column_filter}, there were {len(dataset_filtered.index)} recorded meteorites')
          is_NaN_filtered = dataset_filtered.isnull()
          row_has_NaN_filtered = is_NaN_filtered.any(axis=1)
          rows_with_NaN_filtered = dataset_filtered[row_has_NaN_filtered]
          print(f'Of those {len(dataset_filtered.index)} recorded data points, {len(rows_with_NaN_filtered.index)} have null values')
      else:
        if column_filter == None:
          print(f"the most commonly occuring {column} with null values is: {rows_with_NaN[column].mode()}")
        else:
          ARG_FILTERED = self.dataset[column] == column_filter
          dataset_filtered = self.dataset[ARG_FILTERED]
          print(f'For the column {column} filtered by the match {column_filter}, there were {len(dataset_filtered.index)} recorded meteorites')
          is_NaN_filtered = dataset_filtered.isnull()
          row_has_NaN_filtered = is_NaN_filtered.any(axis=1)
          rows_with_NaN_filtered = dataset_filtered[row_has_NaN_filtered]
          print(f'Of those {len(dataset_filtered.index)} recorded data points, {len(rows_with_NaN_filtered.index)} have null values')
    
    '''——————REMOVING NULL DATA——————'''
    def remove_null_data(self, columns):
      try:
        self.dataset = self.dataset.dropna(subset=columns)
      except:
        KeyError('columns not found or already dropped')
      for column in self.dataset:
        for data in column:
          # for each data point assert it is not a nan value
          assert data != np.nan
      return self.dataset.info()



#——————————————CREATING DICTIONARY TO USE FOR ANALYSIS AND VISUALIZATION——————————#

    ## custom feature for encoding features without int or float values
    def encode_categorical_feature(self, dataset, feature, encoding="label"):
      # Instantiate encoder architecture
      if encoding == "label":
        self.encoder = LabelEncoder()
      # Transform dataset feature using labeling schema (performs in-place)
      dataset[feature] = self.encoder.fit_transform(dataset[feature])
      # Get fitted encoder (just in case)
      return self.encoder


    ## creating a copy of the dataset that will be enumerated and have certain values removed
    def create_vis_dataset(self, columns_to_drop):
      self.vis_dataset = self.dataset.copy()
      features_to_enumerate = []
      try:
        self.vis_dataset.drop(columns=columns_to_drop, inplace=True)
      except:
        KeyError("agjsadh")
      for column in self.vis_dataset:
        if self.vis_dataset[column].dtype == 'object':
          features_to_enumerate.append(column)
      # Impute non int/float values to number values
      imputer = SimpleImputer(strategy="most_frequent")
      self.vis_dataset.iloc[:, :] = imputer.fit_transform(self.vis_dataset)
      self.encoders = dict.fromkeys(features_to_enumerate)
      for key in self.encoders.keys():
        self.encoders[key] = self.encode_categorical_feature(dataset=self.vis_dataset,
                                                             feature=key,
                                                             encoding="label")
        
      assert type(self.test_obj.vis_dataset) == pd.core.frame.DataFrame
      for column in self.vis_dataset.columns:
        assert column not in columns_to_drop
        # assert there are only int and float values in the dataset
        for data in self.vis_dataset[column]:
          assert type(data) == int or type(data) == float
      return self.vis_dataset


    ## custom function to create dictionary
    def operate_data_dictionary(self, features, descriptors, method="set", refpath=None):
      """ Operational function to work in creating or getting data dictionary. """
      if method == "set":
        # Produce dictionary-wrapped key-value associations of feature summaries
        data_dictionary = dict(zip(features, descriptors))
        # Convert data dictionary to cleaner reference table
        reference = pd.DataFrame(data_dictionary, index=[0])
        # Save reference table for future access
        if refpath is not None and type(refpath) == str:
          reference.to_csv(refpath, index=False)
      if method == "get":
        # Get reference table from saved data dictionary
        if refpath is not None and type(refpath) == str:
          return pd.read_csv(refpath)
        else:
          raise TypeError("Saved file for data dictionary not found.")


    ## creating dictionary and reference file
    def create_data_dictionary(self, descriptors):
      FEATURES = self.vis_dataset.columns.tolist()
      DESCRIPTORS = descriptors
      REFPATH = 'data_reference.csv'
      self.operate_data_dictionary(features=FEATURES,
                                   descriptors=DESCRIPTORS,
                                   method="set",
                                   refpath=REFPATH)
      # Get data dictionary as reference table
      reference = self.operate_data_dictionary(features=FEATURES,
                                          descriptors=DESCRIPTORS,
                                          method="get",
                                          refpath=REFPATH)
      self.reference_dict = reference
      assert len(self.vis_dataset.columns) == len(self.reference_dict.columns)
      return reference.T


#———————————————————————————ANALYSIS METHODS——————————————————————————————————#

    ## Get the top n values for a feature a print accordingly
    def get_top_values(self, column, number_of_values):
      length = len(self.vis_dataset[column].unique())
      top_values = self.vis_dataset[column].value_counts().head(number_of_values)
      top_values_dict = dict(top_values)
      print(f"Out of {length} unique values for {column}, the {number_of_values} most commonly occuring values are :")
      for key in top_values_dict.keys():
        if column in self.encoders.keys():
          print(f"{column} of {self.encoders[column].inverse_transform([key])} with {top_values_dict[key]} recorded data points.")
        else:
          print(f"{column} of {key} with {top_values_dict[key]} recorded data points.")
      return


    ## Get the average value for a feature and print accordingly
    def get_average_value(self, column):
      avg_num = round(self.vis_dataset[column].mean())
      if column in self.encoders.keys():
        avg_feature = self.encoders[column].inverse_transform([avg_num])
      else:
        return print(f"The average value for {column} is {avg_num}")
      return print(f"The average value for {column} is {avg_feature}.")


    # Get an n number of samples of a feature and take the mean
    def get_sample(self, column, sample_size):
      samples = []
      for count in range(0, sample_size):
        index = np.random.randint(len(self.vis_dataset) - 1)
        samples.append(self.vis_dataset[column].values[index])
      samples_array = np.array(samples)
      return samples_array.mean()


    # Create a distribution of n samples
    def create_sample_distribution(self, column, distribution_size, sample_size):
      distribution = []
      for count in range(0, distribution_size):
        distribution.append(self.get_sample(column, sample_size))
      distribution_array = np.array(distribution)
      return distribution_array


    def break_up_by_value_count(self, column, increment_points):
      # create dictionary with data of column as keys and value counts of each unique data point as values
      column_vis = self.dataset[column].value_counts()
      column_data_dict = dict(column_vis)
      # print(column_data_dict)

      vis_dicts = [] 
      x = 0
      # iterate through each given increment
      for x in range(len(increment_points)):
        num = increment_points[x]
        vis_dict_num = {}
        # iterate through each key value pair in dictionary and add to the new dictionary if data is within increment range
        for i in column_data_dict:
          # ?maybe change to... if value in range(last increment, current increment)?
          if x==0 and column_data_dict[i] >= 0 and column_data_dict[i] <= increment_points[x]:
            vis_dict_num[i] = column_data_dict[i]
          elif column_data_dict[i] > increment_points[x-1] and column_data_dict[i] <= increment_points[x]:
            vis_dict_num[i] = column_data_dict[i]
          elif x == len(increment_points) - 1 and column_data_dict[i] > increment_points[x]:
            vis_dict_num[i] = column_data_dict[i]
        # append the new dict created above to the list of dictionaries
        vis_dicts.append(vis_dict_num)
      # return list of new dictionaries that contain data within range of each increment
      return vis_dicts


    def break_up_by_data_size(self, column, increment_points):
      i = 0
      dicts = []
      # iterate through each increment point
      for i in range(len(increment_points)):
        if i == 0:
          # if its the first point, find values between 0 and increment
          ARG_1 = self.dataset[column] >= 0
          ARG_2 = self.dataset[column] <= increment_points[i]
          value_counts = self.dataset[ARG_1 & ARG_2][column].value_counts()
          print(f'Number of data points with {column} between 0 and {increment_points[i]}: {len(self.dataset[ARG_1 & ARG_2])}')
        elif i == len(increment_points) - 1:
          # if its the last point, find values over increment
          ARG_1 = self.dataset[column] > increment_points[i]
          value_counts = self.dataset[ARG_1][column].value_counts()
          print(f'Number of data points with {column} over {increment_points[i]}: {len(self.dataset[ARG_1])}')
        else:
          # else find values between last increment point and this current one
          ARG_1 = self.dataset[column] > increment_points[i-1]
          ARG_2 = self.dataset[column] <= increment_points[i]
          value_counts = self.dataset[ARG_1 & ARG_2][column].value_counts()
          print(f'Number of data points with {column} between {increment_points[i-1]} and {increment_points[i]}: {len(self.dataset[ARG_1 & ARG_2])}')
        # create a dictionary with data as keys and value counts as values, append to dictionary list
        new_dict = dict(value_counts)
        dicts.append(new_dict)

      return dicts
        

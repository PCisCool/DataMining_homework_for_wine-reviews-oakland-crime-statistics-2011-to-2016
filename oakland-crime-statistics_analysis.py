import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

data2011 = pd.read_csv("./data/Oakland-Crime-Statistics-2011-to-2016/records-for-2011.csv",encoding="utf-8")
data2012 = pd.read_csv("./data/Oakland-Crime-Statistics-2011-to-2016/records-for-2012.csv",encoding="utf-8")
data2013 = pd.read_csv("./data/Oakland-Crime-Statistics-2011-to-2016/records-for-2013.csv",encoding="utf-8")
data2014 = pd.read_csv("./data/Oakland-Crime-Statistics-2011-to-2016/records-for-2014.csv",encoding="utf-8")
data2015 = pd.read_csv("./data/Oakland-Crime-Statistics-2011-to-2016/records-for-2015.csv",encoding="utf-8")
data2016 = pd.read_csv("./data/Oakland-Crime-Statistics-2011-to-2016/records-for-2016.csv",encoding="utf-8")
"""
print("2011数据集有以下属性",data2011.columns)
print("2012数据集有以下属性",data2012.columns)
print("2013数据集有以下属性",data2013.columns)
print("2014数据集有以下属性",data2014.columns)
print("2015数据集有以下属性",data2015.columns)
print("2016数据集有以下属性",data2016.columns)
"""

data2011_temp = data2011[[ 'Area Id', 'Priority', 'Incident Type Id', 'Event Number']]
data2012_temp = data2012[[ 'Area Id', 'Priority', 'Incident Type Id', 'Event Number']]
data2013_temp = data2013[[ 'Area Id', 'Priority', 'Incident Type Id', 'Event Number']]
data2014_temp = data2014[[ 'Area Id', 'Priority', 'Incident Type Id', 'Event Number']]
data2015_temp = data2015[[ 'Area Id', 'Priority', 'Incident Type Id', 'Event Number']]
data2016_temp = data2016[[ 'Area Id', 'Priority', 'Incident Type Id', 'Event Number']]

data_all = pd.concat( [data2011_temp, data2012_temp, data2013_temp, data2014_temp, data2015_temp, data2016_temp], axis=0)

print(data_all.info())

data_all_Area_Id = data_all['Area Id']
data_all_Priority = data_all['Priority']
data_all_Incident_Type_Id = data_all['Incident Type Id']

"""
#data_all_Area_Id
data_all_Area_Id.value_counts().head(10).plot.bar()
plt.title('data_all_Area_Id')
plt.show()
"""
"""
#data_all_Priority
data_all_Priority.value_counts().head(10).plot.bar()
plt.title('data_all_Priority')
plt.show()
"""
"""
#data_all_Incident_Type_Id
data_all_Incident_Type_Id.value_counts().head(10).plot.bar()
plt.title('data_all_Incident_Type_Id')
plt.show()
"""

"""
#将缺失部分剔除

data_all_Area_Id = data_all['Area Id'].dropna(how='any')
data_all_Priority = data_all['Priority'].dropna(how='any')
data_all_Incident_Type_Id = data_all['Incident Type Id'].dropna(how='any')

"""
"""
#data_all_Area_Id
data_all_Area_Id.value_counts().head(10).plot.bar()
plt.title('data_all_Area_Id')
plt.show()
"""
"""
#data_all_Priority
data_all_Priority.value_counts().head(10).plot.bar()
plt.title('data_all_Priority')
plt.show()
"""
"""
#data_all_Incident_Type_Id
data_all_Incident_Type_Id.value_counts().head(10).plot.bar()
plt.title('data_all_Incident_Type_Id')
plt.show()
"""
"""
#使用众数填补
data_all_Area_Id[data_all_Area_Id.isnull()] = data_all_Area_Id.dropna().mode().values
data_all_Priority[data_all_Priority.isnull()] = data_all_Priority.dropna().mode().values
data_all_Incident_Type_Id[data_all_Incident_Type_Id.isnull()] = data_all_Incident_Type_Id.dropna().mode().values
"""

"""
#data_all_Area_Id
data_all_Area_Id.value_counts().head(10).plot.bar()
plt.title('data_all_Area_Id')
plt.show()
"""
"""
#data_all_Priority
data_all_Priority.value_counts().head(10).plot.bar()
plt.title('data_all_Priority')
plt.show()
"""
"""
#data_all_Incident_Type_Id
data_all_Incident_Type_Id.value_counts().head(10).plot.bar()
plt.title('data_all_Incident_Type_Id')
plt.show()
"""

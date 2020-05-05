import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from diff_plt import diff_hist

import warnings
warnings.filterwarnings("ignore")

wine_reviews = pd.read_csv("./data/wine-reviews/winemag-data-130k-v2.csv", index_col=0)
print(wine_reviews.columns)

#print(wine_reviews_price.isnull())
#print(wine_reviews.info())

wine_reviews_country = wine_reviews['country']
wine_reviews_designation = wine_reviews['designation']
wine_reviews_points = wine_reviews['points']
wine_reviews_price = wine_reviews['price']
wine_reviews_province = wine_reviews['province']
wine_reviews_region_1 = wine_reviews['region_1']
wine_reviews_region_2 = wine_reviews['region_2']
wine_reviews_variety = wine_reviews['variety']
wine_reviews_winery = wine_reviews['winery']
wine_reviews_taster_name = wine_reviews['taster_name']












"""
print(wine_reviews_points.describe())            #求points五数概括
points_missing_value = wine_reviews_points.shape[0] - wine_reviews_points.count()
print("points缺失值个数为：", points_missing_value)


#画points盒图
wine_reviews_points.plot.box(title="wine_reviews_points")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画points直方图
plt.hist(wine_reviews_points,bins = 20, facecolor='green', alpha=0.75)
plt.title('wine_reviews_points')
plt.show()
"""

"""
print(wine_reviews_price.describe())            #求price五数概括
price_missing_value = wine_reviews_price.shape[0] - wine_reviews_price.count()
print("price缺失值个数为：", price_missing_value)


#画price盒图
wine_reviews_price.plot.box(title="wine_reviews_price")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
plt.hist(wine_reviews_price,bins = 100, facecolor='green', alpha=0.75)
plt.title('wine_reviews_price')
plt.show()
"""
"""
#画country直方图
wine_reviews_country.value_counts().head(10).plot.bar()
plt.title('wine_reviews_country')
plt.show()
"""
"""
#画wine_reviews_designation直方图
wine_reviews_designation.value_counts().head(10).plot.bar()
plt.title('wine_reviews_designation')
plt.show()
"""
"""
#画province直方图
wine_reviews_province.value_counts().head(10).plot.bar()
plt.title('wine_reviews_province')
plt.show()
""""""
#画region_1直方图
wine_reviews_region_1.value_counts().head(10).plot.bar()
plt.title('wine_reviews_region_1')
plt.show()
""""""
#画region_2直方图
wine_reviews_region_2.value_counts().head(10).plot.bar()
plt.title('wine_reviews_region_2')
plt.show()
"""
"""
#画taster_name直方图
wine_reviews_taster_name.value_counts().head(10).plot.bar()
plt.title('wine_reviews_taster_name')
plt.show()
"""
"""
#画variety直方图
wine_reviews_variety.value_counts().head(10).plot.bar()
plt.title('wine_reviews_variety')
plt.show()
"""
"""
#画winery直方图
wine_reviews_winery.value_counts().head(10).plot.bar()
plt.title('wine_reviews_winery')
plt.show()
"""



"""

#将缺失部分剔除


wine_reviews_country2 = wine_reviews_country.dropna(how='any')
wine_reviews_designation2 = wine_reviews_designation.dropna(how='any')
wine_reviews_points2 = wine_reviews_points.dropna(how='any')
wine_reviews_price2 = wine_reviews_price.dropna(how='any')
wine_reviews_province2 = wine_reviews_province.dropna(how='any')
wine_reviews_region_12 = wine_reviews_region_1.dropna(how='any')
wine_reviews_region_22 = wine_reviews_region_2.dropna(how='any')
wine_reviews_variety2 = wine_reviews_variety.dropna(how='any')
wine_reviews_winery2 = wine_reviews_winery.dropna(how='any')


"""

"""
print(wine_reviews_price2.describe())            #求price2五数概括
price_missing_value2 = wine_reviews_price2.shape[0] - wine_reviews_price2.count()
print("price缺失值为：", price_missing_value2)

#画price盒图
wine_reviews_price2.plot.box(title="wine_reviews_price2")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
diff_hist(wine_reviews_price, wine_reviews_price2)
"""

"""
#画country直方图
diff_hist(wine_reviews_country, wine_reviews_country2)
"""
"""
#画wine_reviews_designation直方图
diff_hist(wine_reviews_designation, wine_reviews_designation2)
"""

"""
#画province直方图
diff_hist(wine_reviews_province, wine_reviews_province2)
"""

"""
#画region_1直方图

diff_hist(wine_reviews_region_1, wine_reviews_region_12)

""""""
#画region_2直方图
diff_hist(wine_reviews_region_2, wine_reviews_region_22)

"""





"""


#使用众数填补
wine_reviews.country[wine_reviews.country.isnull()] = wine_reviews.country.dropna().mode().values
wine_reviews.designation[wine_reviews.designation.isnull()] = wine_reviews.designation.dropna().mode().values
wine_reviews.points[wine_reviews.points.isnull()] = wine_reviews.points.dropna().mode().values
wine_reviews.price[wine_reviews.price.isnull()] = wine_reviews.price.dropna().mode().values
wine_reviews.province[wine_reviews.province.isnull()] = wine_reviews.province.dropna().mode().values
wine_reviews.region_1[wine_reviews.region_1.isnull()] = wine_reviews.region_1.dropna().mode().values
wine_reviews.region_2[wine_reviews.region_2.isnull()] = wine_reviews.region_2.dropna().mode().values
wine_reviews.variety[wine_reviews.variety.isnull()] = wine_reviews.variety.dropna().mode().values
wine_reviews.winery[wine_reviews.winery.isnull()] = wine_reviews.winery.dropna().mode().values




wine_reviews_country = wine_reviews['country']
wine_reviews_designation = wine_reviews['designation']
wine_reviews_points = wine_reviews['points']
wine_reviews_price = wine_reviews['price']
wine_reviews_province = wine_reviews['province']
wine_reviews_region_1 = wine_reviews['region_1']
wine_reviews_region_2 = wine_reviews['region_2']
wine_reviews_variety = wine_reviews['variety']
wine_reviews_winery = wine_reviews['winery']

"""
"""

print(wine_reviews_price.describe())            #求price2五数概括
price_missing_value = wine_reviews_price.shape[0] - wine_reviews_price.count()
print("price缺失值为：", price_missing_value)

#画price盒图
wine_reviews_price.plot.box(title="wine_reviews_price2")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
wine_reviews_price.value_counts().head(10).plot.bar()
plt.title('wine_reviews_price')
plt.show()
"""
"""
#画country直方图
wine_reviews_country.value_counts().head(10).plot.bar()
plt.title('wine_reviews_country')
plt.show()
"""
"""
#画wine_reviews_designation直方图
wine_reviews_designation.value_counts().head(10).plot.bar()
plt.title('wine_reviews_designation')
plt.show()
"""
"""
#画province直方图
wine_reviews_province.value_counts().head(10).plot.bar()
plt.title('wine_reviews_province')
plt.show()
""""""
#画region_1直方图
wine_reviews_region_1.value_counts().head(10).plot.bar()
plt.title('wine_reviews_region_1')
plt.show()
""""""
#画region_2直方图
wine_reviews_region_2.value_counts().head(10).plot.bar()
plt.title('wine_reviews_region_2')
plt.show()
"""
"""
#相关性
from sklearn.impute import SimpleImputer

df_relation = wine_reviews[['price']]
Simpleimp = SimpleImputer(missing_values=np.nan, strategy='mean')
Simpleimp.fit(df_relation)
df_relation = Simpleimp.transform(df_relation)
wine_reviews_price = pd.DataFrame(df_relation, columns = ['price'])

print(wine_reviews_price.describe())            #求price2五数概括
price_missing_value = wine_reviews_price.shape[0] - wine_reviews_price.count()
print("price缺失值为：", price_missing_value)

#画price盒图
wine_reviews_price.plot.box(title="wine_reviews_price2")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
plt.hist(wine_reviews_price,bins = 100, facecolor='green', alpha=0.75)
plt.title('wine_reviews_price')
plt.show()
"""
"""
#相似性
new_wine_reviews = wine_reviews.dropna(subset=['price'])
x = new_wine_reviews['points']
y = new_wine_reviews['price']

from sklearn.linear_model import LinearRegression
from sklearn.svm import SVC

X = np.array(x).reshape(-1, 1)
model = LinearRegression()
model.fit(X, y)

new_wine_reviews = wine_reviews.copy()
for index, row in new_wine_reviews[wine_reviews['price'].isna()].iterrows():
    new_wine_reviews['price'][index] = model.predict(np.array(row['points']).reshape(-1, 1))

print(new_wine_reviews.info())
wine_reviews_price = new_wine_reviews['price']
print(wine_reviews_price.describe())            #求price2五数概括
price_missing_value = wine_reviews_price.shape[0] - wine_reviews_price.count()
print("price缺失值为：", price_missing_value)

#画price盒图
wine_reviews_price.plot.box(title="wine_reviews_price2")
plt.grid(linestyle="--", alpha=0.3)
plt.show()

#画price直方图
plt.hist(wine_reviews_price,bins = 100, facecolor='green', alpha=0.75)
plt.title('wine_reviews_price')
plt.show()

"""

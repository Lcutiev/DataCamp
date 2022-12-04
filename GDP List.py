'''Mô tả

Bộ dữ liệu GDP list chứa dữ liệu dự báo về GDP của một số quốc gia, các thông tin được thống kê bao gồm:

    Country: Tên quốc gia
    Continent: Tên châu lục
    GDP (millions of US$): GDP tính theo đơn vị triệu USD

Hãy đưa bộ dữ liệu vào phân tích và giải đáp các thắc mắc sau:

    Bộ dữ liệu chứa bao nhiêu dòng, bao nhiêu cột
    Thang đo tương ứng của các thuộc tính được lưu trữ
    GDP của các quốc gia có đồng đều không
    Mỗi châu lục có bao nhiêu quốc gia nằm trong bảng dữ liệu
    Tổng GPD của các châu lục
    Top 10 quốc gia có GDP cao nhất

'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reading the CSV file
gdp = pd.read_csv('GDPlist.csv', encoding='ISO-8859-1')

# Displaying the DataFrame
gdp.head()

gdp.info()

'''Nhận xét:

 Bộ dữ liệu chứa 125 dòng, 3 cột

Nhận diện thang đo cho từng biến quan sát

    Country, Continent: có kiểu object –> norminal attribute
    GDP (millions of US$): là dữ liệu dạng số nguyên (int64)
'''
   


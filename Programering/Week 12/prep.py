import numpy as np
# sales_2022 = np.array([3000, 0, 4000, 2000, 5000])
# # sales_2023 = np.array([3200, 1400, 4200, 1200, 4400])

# # good_sale = sales_2022 >2001
# # print(good_sale)


# print(np.array([3000, 0, 4000, 2000, 5000.4]).dtype)

# val=np.ones(4)
# print(val)

# a=np.array([10,20])
# b=np.array(2*a)
# print(b)
# c=np.array([0,1])
# print(a-c)

# year=np.array([[1,2,3,4],[5,6,7,8],[9,1,11,12]])
# print(year.shape)


# a_list = [1, 1.2, True]
# a_array = np.array(a_list)
# print(a_array)

# array0 = np.array([4.87, 3.25, 6.15, 0.0])
# array1 = array0.astype(int)
# array2 = array0.astype(bool)

# print(array0, array0.dtype)
# print(array1, array1.dtype)
# print(array2, array2.dtype)


a =[0, 15, 20, 25, 20]
a_array = np.array(a)

b_list = [1, 2, 3, 4, 5]
b_array = np.array(b_list)

c_list = a_array**a_array.size
c_array = a_array + b_array


print(c_array)
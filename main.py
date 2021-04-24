import numpy as np

def calculate(alist):
    if len(alist) != 9 : raise ValueError('List must contain nine numbers.')
    #Dividing the 3x3 matrix into 3 Lists!
    List1 = list()
    List2 = list()
    List3 = list()
    count = 0
    for ele in alist:
        ele = int(ele)
        count = count +1
        if count < 4 :
            List1.append(ele)
        if count < 7 and count >= 4 :
            List2.append(ele)
        if count > 6 :
            List3.append(ele)
    matrix = np.array([List1,List2,List3],dtype='int8')
    
    # Finding the mean!
    axis1_mean = np.mean(matrix, axis=0)
    axis1_mean = axis1_mean.tolist()
    axis2_mean = np.mean(matrix, axis=1)
    axis2_mean = axis2_mean.tolist()
    flattened_mean = np.mean(matrix)
    Mean_list = [axis1_mean,axis2_mean,flattened_mean]
    
    #Finding the variance
    axis1_variance = np.var(matrix, axis=0)
    axis1_variance = axis1_variance.tolist()
    axis2_variance = np.var(matrix, axis=1)
    axis2_variance = axis2_variance.tolist()
    flattened_variance = np.var(matrix)
    flattened_variance = flattened_variance.tolist()
    Variance_list = [axis1_variance,axis2_variance,flattened_variance]
    
    #Finding the standard deviation
    axis1_std = np.std(matrix, axis=0)
    axis1_std = axis1_std.tolist()
    axis2_std = np.std(matrix, axis=1)
    axis2_std = axis2_std.tolist()
    flattened_std = np.std(matrix)
    flattened_std = flattened_std.tolist()
    std_list = [axis1_std,axis2_std,flattened_std]
    
    #Finding the max & min
    axis1_max = np.max(matrix, axis=0)
    axis1_max = axis1_max.tolist()
    axis1_min = np.min(matrix,axis=0)
    axis1_min = axis1_min.tolist()
    axis2_max = np.max(matrix, axis=1)
    axis2_max = axis2_max.tolist()
    axis2_min =np.min(matrix,axis=1)
    axis2_min = axis2_min.tolist()
    flattened_max = np.max(matrix)
    flattened_max = flattened_max.tolist()
    flattened_min = np.min(matrix)
    flattened_min = flattened_min.tolist()
    max_list = [axis1_max,axis2_max,flattened_max]
    min_list = [axis1_min,axis2_min,flattened_min]
    
    #Finding the sum
    axis1_sum = np.sum(matrix, axis=0)
    axis1_sum = axis1_sum.tolist()
    axis2_sum = np.sum(matrix, axis=1)
    axis2_sum = axis2_sum.tolist()
    flattened_sum = np.sum(matrix)
    flattened_sum = flattened_sum.tolist()
    sum_list = [axis1_sum,axis2_sum,flattened_sum]
    
    # Dictionary according to the Readme doc in fcc!
    calculations = {'mean': Mean_list, 'variance': Variance_list,
    'standard deviation': std_list, 'max': max_list,
    'min': min_list, 'sum': sum_list }
            

    return calculations
    
    
numbers = input('Input 9 digits with spaces : ')
alist = numbers.split()
print(calculate(alist))

def arrayOfProducts(array):
    Products = []
    i=0
    while i<len(array):
        product = 1
        for j in range(1,len(array)):
            product = array[j]*product
        Products.append(product)
        array.append(array[0])
        array.pop(0)
        i+=1
    return Products

arrayOfProducts([5,1,4,2])
a=int(input('enter the purchased amount'))
if a>1000:
    print('the discount offered will be 10%')
    d1=0.1*a
    print('the reduction in price is ',d1)
    p1=a-d1
    print('the discounted price will be',p1)
elif a>2000:
    print('the discount offered will be 20%')
    d2=0.2*a
    print('the reduction in price is ',d2)
    p2=a-d2
    print('the discounted price will be',p2)
elif a>3000:
    print('the discount offered will be 30%')
    d3=0.3*a
    print('the reduction in price is ',d3)
    p3=a-d3
    print('the discounted price will be',p3)
elif a>5000:
    print('the discount offered will be 40%')
    d4=0.4*a
    print('the reduction in price is ',d4)
    p4=a-d4
    print('the discounted price will be',p4)
else:
    print('not eligible for discount')
output----
enter the purchased amount1500
the discount offered will be 10%
the reduction in price is  150.0
the discounted price will be 1350.0

    
 





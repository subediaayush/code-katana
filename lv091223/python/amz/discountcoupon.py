def findValidDiscountCoupons(discounts):

    def findValidCoupons(coupons):
        for coupon in coupons:
            while (len(coupon) > 0):
                if len(coupon) % 2 == 1:
                    return False
                elif (coupon[0] == coupon[-1]):
                    return findValidCoupons([coupon[1:-1]])
                else:
                    if len(coupon) == 2: 
                        return False
                    return findValidCoupons([coupon[0: len(coupon) // 2], coupon[len(coupon) // 2: -1]])
        return True

    output = []
    for coupon in discounts:
        if findValidCoupons([coupon]):
            output.append(1)
        else:
            output.append(0)
    
    return output


print(findValidDiscountCoupons(['abba', 'abca']))
print(findValidDiscountCoupons(['daabbd', 'abc']))
print(findValidDiscountCoupons(['daabbda', 'daabbd']))
print(findValidDiscountCoupons(['acac']))
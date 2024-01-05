def formatter (interest):
    reslst = [((str(round(interest)))[::-1])[i]+"," if i % 2 != 0 and i != 1 else ((str(round(interest)))[::-1])[i] for i in range(len(str(round(interest))))]
    # for i in range((len(str(round(interest))))):
    #     if i%2!=0 and i!=1:
    #         reslst.append(',')
    #     reslst.append(((str(round(interest)))[::-1])[i])
    if '.' in str(interest):
        result = ''.join(reversed(reslst)) + str(round(interest,2))[-3:]
    else:
        result = ''.join(reversed(reslst))
    return result

def simple_interest(principal, term, rate):
    
    return formatter(principal+principal*rate*term)


def compound_interest(principal, term, rate):
    # A = P * (1 + r/1)^(1t)
    interest = principal * (1 + rate)**(term)
    return formatter(interest)

result = compound_interest(123456, 23, 0.08)
#print(formatter(35034.666666))

def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True):
    total_value = principal
    for i in range(term):
        if end_of_period:
            total_value = (total_value + payment) * (1 + rate)
        else:
            total_value = total_value * (1 + rate) + payment

    return formatter(total_value)

def savings_calculator(present_value, future_value, term, rate, end_of_period=True):...

def files_innerjoin(filename1, filename2, **kwargs):...

def files_leftouterjoin(filename1, filename2, **kwargs):...

def files_rightouterjoin(filename1, filename2, **kwargs):...

def list_to_dict(data: list):
    #n = [{"name": "a", "age": 21}, {"name": "b", "age": 43}]
    #   op:{"name": ["a", "b"], "age": [21,43]}
    dicn = {}
    for i in data:
        for j in i:
            if j not in dicn:
                dicn[j] = []
            dicn[j].append(i[j])
    return dicn

def dict_to_list(data: dict):
    n = {"name": ["a", "b"], "age": [21,43]}
 # [{"name": "a", "age": 21}, {"name": "b", "age": 43}]
    
    for i,j in n.items():
        print(i,j)
        
        for k in j:
            print (i,k)



#print(simple_interest(123456, 23, 0.08))
dict_to_list({})
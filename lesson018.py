def formatter(interest):
    """formats the numbers and adds commas and rounds to 2 decimal places"""
    reslst = [
        ((str(round(interest)))[::-1])[i] + ","
        if i % 2 != 0 and i != 1
        else ((str(round(interest)))[::-1])[i]
        for i in range(len(str(round(interest))))
    ]
    # for i in range((len(str(round(interest))))):
    #     if i%2!=0 and i!=1:
    #         reslst.append(',')
    #     reslst.append(((str(round(interest)))[::-1])[i])
    if "." in str(interest):
        result = "".join(reversed(reslst)) + str(round(interest, 2))[-3:]
    else:
        result = "".join(reversed(reslst))
    return result


def simple_interest(principal, term, rate):
    """Returns the total value of the principal"""
    return formatter(principal + principal * rate * term)


def compound_interest(principal, term, rate):
    """returns the total value of the principal"""
    # A = P * (1 + r/1)^(1t)
    interest = principal * (1 + rate) ** (term)
    return formatter(interest)
result = compound_interest(123456, 23, 0.08)
# print(formatter(35034.666666))


def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True):
    """returns the total value of the principal"""
    amount = principal
    for i in range(term):
        if end_of_period:
            amount = (amount + payment) * (1 + rate)
        else:
            amount = amount * (1 + rate) + payment

    return formatter(amount)


def savings_calculator(present_value, future_value, term, rate, end_of_period=True):
    """Returns EMI"""
    if not end_of_period:
        rate = rate / (1 + rate)
    amount = future_value - ((1 + rate) ** term) * present_value
    return amount / ((1 + rate) ** term - 1)


def files_innerjoin(filename1, filename2, **kwargs):
    """performs inner join on two csv files"""
    with open(filename1, "r") as file1:
        header1 = file1.readline().strip().split(",")
        data1 = [line.strip().split(",") for line in file1]

    with open(filename2, "r") as file2:
        header2 = file2.readline().strip().split(",")
        data2 = [line.strip().split(",") for line in file2]

    index1 = [header1.index(*i) for i in kwargs.values()]
    index2 = [header2.index(*i) for i in kwargs.values()]

    result = [i + j for i in data1 for j in data2 if i[index1[0]] == j[index2[0]]]

    with open("results.csv", "w") as result_file:
        result_file.write(",".join(header1 + header2) + "\n")
        for row in result:
            result_file.write(",".join(row) + "\n")


def files_leftouterjoin(filename1, filename2, **kwargs):
    ...


def files_rightouterjoin(filename1, filename2, **kwargs):
    ...


def list_to_dict(data: list):
    """Convert a list of dicts to a dict of lists"""
    dicn = {}
    for i in data:
        for j in i:
            if j not in dicn:
                dicn[j] = []
            dicn[j].append(i[j])
    return dicn


def dict_to_list(data: dict):
    """Convert a dict of lists to a list of dicts"""
    lst = []
    for k in range(len(list(data.values())[0])):
        lst.append({i: j[k] for i, j in data.items()})
    return lst


#files_innerjoin("file1.csv", "file2.csv", key=["employee_id"])

# print(savings_calculator(0, 1e8, 35, 0.10))
# print(dict_to_list({"name": ["a", "b"], "age": [21,43]}))

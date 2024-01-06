"""lessson 018"""
import csv
from itertools import zip_longest


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


def compound_interest_with_payments(principal, payment, term, rate, end_of_period=True):
    """returns the total value of the principal"""
    amount = principal
    for _ in range(term):
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
    """inner joins two files"""
    with open(filename1, "r", encoding="utf-8") as file1:
        data1 = [i[0].split(",") for i in list(csv.reader(file1, delimiter=" "))]

    with open(filename2, "r", encoding="utf-8") as file2:
        data2 = [i[0].split(",") for i in list(csv.reader(file2, delimiter=" "))]

    index1 = [data1[0].index(*i) for i in kwargs.values()]
    index2 = [data2[0].index(*i) for i in kwargs.values()]

    lst = []
    for i, j in zip(data1, data2):
        flag = [i[k] == j[l] for k, l in zip(index1, index2)]
        if all(flag):
            lst.append(i + j)

    with open("results.csv", "w", encoding="utf-8") as result_file:
        for row in lst:
            result_file.write(",".join(row) + "\n")


def files_leftouterjoin(filename1, filename2, **kwargs):
    """left joins two files"""
    with open(filename1, "r", encoding="utf-8") as file1:
        data1 = [i[0].split(",") for i in list(csv.reader(file1, delimiter=" "))]

    with open(filename2, "r", encoding="utf-8") as file2:
        data2 = [i[0].split(",") for i in list(csv.reader(file2, delimiter=" "))]

    index1 = [data1[0].index(*i) for i in kwargs.values()]
    index2 = [data2[0].index(*i) for i in kwargs.values()]

    lst = []
    for i, j in zip(data1, data2):
        for k, l in zip(index1, index2):
            if not i or not j or i[k] != j[l]:
                lst.append(i + ["NaN" for i in range(len(data2[0]))])
            else:
                lst.append(i + j)

    with open("results.csv", "w", encoding="utf-8") as result_file:
        for i in lst:
            result_file.write(",".join(i) + "\n")


def files_rightouterjoin(filename1, filename2, **kwargs):
    """right joins two files"""
    with open(filename1, "r", encoding="utf-8") as file1:
        data1 = [i[0].split(",") for i in list(csv.reader(file1, delimiter=" "))]

    with open(filename2, "r", encoding="utf-8") as file2:
        data2 = [i[0].split(",") for i in list(csv.reader(file2, delimiter=" "))]

    index1 = [data1[0].index(*i) for i in kwargs.values()]
    index2 = [data2[0].index(*i) for i in kwargs.values()]

    lst = []
    for i, j in zip_longest(data1, data2):
        for k, l in zip(index1, index2):
            if not i or not j or i[k] != j[l]:
                lst.append(j + ["NaN" for i in range(len(data1[0]))])
            else:
                lst.append(j + i)
    with open("results.csv", "w", encoding="utf-8") as result_file:
        for i in lst:
            result_file.write(",".join(i) + "\n")


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


def split_file(filename, split_cols: list):
    """splits a file into multiple files according to the columns"""
    with open(filename, "r", encoding="utf-8") as file1:
        reader1 = csv.reader(file1, delimiter=" ", quotechar="|")
        tmp = list(reader1)
        data = [i[0].split(",") for i in tmp]
        header = [data[0]]

    indices = [data[0].index(i) for i in split_cols]
    dicn = {}
    for i in data[1:]:
        key = tuple(i[col] for col in indices)
        if key not in dicn:
            dicn[key] = []
        dicn[key].append(i)

    for i,j in dicn.items():
        ofname = "_".join(i) + ".csv"
        with open(ofname, "w", newline="", encoding="utf-8") as output:
            writer = csv.writer(output)
            writer.writerows(header)
            writer.writerows(j)

def circle_array(n, m):
    count_lst = []
    s = []
    lst = "1"
    i = 1
    while True:
        i += 1
        lst += str(i)
        if len(lst) % m == 0:
            count_lst.append(lst)
            lst = str(i)
        if i == n:
            i = 0
        if len(count_lst) >= 2 and count_lst[0][0] == count_lst[-1][-1]:
            break
    for i in count_lst:
        s.append(i[0])
    return s


lst = circle_array(int(input("Введите n: ")), int(input("Введите m: ")))
st = ""
for i in lst:
    st = st + i

print(st)

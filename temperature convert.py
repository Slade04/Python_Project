import sys
temp_str=input('input temperature with its unit:    ')
if temp_str[-1]=="c" or temp_str[-1]=="C":
    F=1.8*(eval(temp_str[0:-1]))+32
    print("As in Fahrenheit,it\'s {:.2f}F".format(F))
elif temp_str[-1] in ["f","F"]:
    C=(eval(temp_str[0:-1])-32)/1.8
    print("As in Celsius,it\'s {:.2f}C".format(C))
else:
    print("invalid input data")

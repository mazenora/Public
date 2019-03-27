stm = "Python Programming"

try:
    print(stm.index("Java"))
except ValueError:
    print("Cannot find the substring")
finally:
    # Always executed even if there is no Exception
    print("Finally Block Here")

print(stm.upper())

while True:
    try:
        first_num = int(input("Enter First value: "))
        second_num = int(input("Enter First value: "))
        res = first_num / second_num
        print("result=", res)
        # break
    # except ValueError:
    #   print("Enter an Integer value please")
    except (ZeroDivisionError, ValueError) as obj:
        print("Not allowed to Dived on Zero")
        print(obj)
    except Exception as ex:
        # for any exception
        print(ex)
    else:
        break

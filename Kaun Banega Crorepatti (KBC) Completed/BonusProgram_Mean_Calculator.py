def mean():
    type = input("Enter the type of Mean calculation to Perform:\nArithmetic Mean\nHarmonic Mean\n\n").lower()
    if "a m" in type:
        method = input("Enter Mean method:\nUngrouped\nGrouped\n\n").lower()
        if "u g" in method:
            n = int(input("Enter total count of Data: "))
            v1 = 1
            temp = [input("Enter data:\n")]

            try:
                while(v1<=n):
                    v1 = v1 + 1
                    data = []
                    data = data.append(temp)
                    print(data)

            except:
                print("Invalid input!\a")

    elif "harmonic mean" in type:
        method = input("Enter Mean method:\nUngrouped\nGrouped\n\n").lower()

    else:
        print(f"The entered value \'{type}\' is unexpected.")


if __name__ == '__main__':
    mean()
def commission(option):
    if option == "COMMISSION":
        line = "-"
        sPersonname = str(input("Enter your name:\t"))
        sEmployeestatus = input("Please enter your employee from the following options:\n 1 = Fulltime, 2 = Part time\t")
        dSalesamount = input("Please enter the sales amount for this period:\t")
        dCommissionF = float(dSalesamount) * 0.04
        dCommissionP = float(dSalesamount) * 0.02
        print(line * 45)
        if float(sEmployeestatus) == 1 and float(dSalesamount) > 3000:
            print(
                sPersonname + " has earned a commission amount of a fulltime employee, the commission\n amount is $%.2f" % dCommissionF + " also " + sPersonname + " has exceeded the sales quota for the period")
        elif float(sEmployeestatus) == 1 and float(dSalesamount) < 3000:
            print(
                sPersonname + " has earned a commission amount of a fulltime employee, the commission\n amount is $%.2f" % dCommissionF + " also " + sPersonname + " has not reached their sales quota for the period")
        if float(dSalesamount) >= 1200 and float(sEmployeestatus) == 2:
            print(
                sPersonname + " has earned a commission amount of a part time employee, the commission\n amount is $%.2f" % dCommissionP + " also " + sPersonname + " has exceeded the sales quota for the period")
        elif float(sEmployeestatus) == 2 and float(dSalesamount) < 3000:
            print(
                sPersonname + " has earned a commission amount of a part time  employee, the commission\n amount is $%.2f" % dCommissionP + " also " + sPersonname + " has not reached their sales quota for the period")
        print(line * 45)

def grosspay(option):
    line = "-"
    if option == "GROSSPAY":
        sEmployeename = input("Enter the employees name:\t")
        sGender = input("Enter your gender, F or M:\t")
        dHoursworked = float(input("Enter hours worked for the week:\t"))
        dPayrate = float(input("Enter your payrate per hour:\t"))
        dGross = dHoursworked * dPayrate
        dOvertimepayrate = 1.5 * dPayrate
        if dHoursworked <= 40:
            print("The gross pay for " + sEmployeename + " is: $%.2f" % dGross)
        else:
            iOTHours = dHoursworked - int(40)
            dOvertimepay = iOTHours * dOvertimepayrate
            dGross2 = dHoursworked - iOTHours
            dGross3 = dGross2 * dPayrate
            dGross4 = dOvertimepay + dGross3
            print(line * 45)
            print("The gross pay for " + sEmployeename + " is: $%.2f" % dGross4)
        if (sGender == "F"):
            print(sEmployeename + " is a female employee that worked " + str(dHoursworked) + " hours this week")
        else:
         print(sEmployeename + " is a male employee that worked " + str(dHoursworked) + " hours this week")
         print(line * 45)

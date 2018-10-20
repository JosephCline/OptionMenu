import grosspay
import omcalc
import convert
import rpsls
import commission
import Grade
line = "-"
print(line * 45)
print("Option Menu")
print(line * 45)
option = input("Grosspay:\n" "Calculator:\n" "Convert:\n" "RPSLS:\n" "Commission\n" "Grade:\n" "Enter option here:\t").upper()
print(line * 45)
omcalc.calculator(option)
grosspay.grosspay(option)
convert.convert(option)
rpsls.rpsls(option)
commission.commission(option)
Grade.Grade(option)

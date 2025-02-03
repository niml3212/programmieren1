
def match_number(number):

    match number:
        case _ if number < 2.0:
            print("Detected only by seismographes")
        case _ if  2.0 <= number < 4.0:
            print("Rarely felt, but recorded")
        case _ if 4.0 <= number < 5.0:
            print("Felt by people, minor damage")
        case _ if  5.0 <= number < 6.0:
            print("Can cause damage populated areas")
        case _ if  6.0 <= number < 7.0:
            print("Serious damage in arease up to 100 miles")
        case _ if  7.0 <= number < 8.0:
            print("Sever damage over large arease")
        case _ if  number <= 8.0:
            print("Massive Destruction")

number = int(input("Bitte die stärke eingeben: "))
match_number(number)

try:
    fobj = open("employees1111.txt","r")
    for line in fobj:
        line = line.strip()
        print(line)
    fobj.close()
except Exception as e: # default exception
    print(e)

###########################################

try:
    fobj = open("employees.txt","r")
    for line in fobj:
        line = line.strip()
        print(line)
    fobj.close()
    output = "helo" +  "python"
except FileNotFoundError as err:
    print(err)
except TypeError as err:
    print(err)
except ValueError as err:
    print(err)
except (KeyError,IndexError) as err:
    print(err)
except Exception as err:
    print(err)
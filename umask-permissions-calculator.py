# This code calculates umask-, directory- and filepermissions for
# a given number.
# 10/24/2024
# by Niels Evers

# Until the next paragraph: Function for duplication and conversion
# of the (in this case) integer values (numerical octal) to
# string values (alphabetical)
def f_perm_alp():
    for digit in range(3):
        if perm_oct[digit] == 0:
            perm_alp.append("---")
        elif perm_oct[digit] == 1:
            perm_alp.append("--x")
        elif perm_oct[digit] == 2:
            perm_alp.append("-w-")
        elif perm_oct[digit] == 3:
            perm_alp.append("-wx")
        elif perm_oct[digit] == 4:
            perm_alp.append("r--")
        elif perm_oct[digit] == 5:
            perm_alp.append("r-x")
        elif perm_oct[digit] == 6:
            perm_alp.append("rw-")
        else:
            perm_alp.append("rwx")

# Until the next paragraph: Definition of the umask
umask = int(input("Please insert a valid umask (0-777): "))

# Until the next paragraph: Checking the umask
if umask < 0 or umask > 777:
    print("Invalid umask. Please enter a valid umask between 0 and 777.")

# Until the end: The Main program
else:

    # Until the next paragraph: Conversion and ouput of the umask
    perm_oct = [int(numeric) for numeric in str(umask).zfill(3)]
    perm_alp = []
    f_perm_alp()
    print("\nUM: ", f"{str(umask).zfill(3)} (numeric) ", *perm_alp, f" (alph.)", sep='')

    # Until the next paragraph: Calculation of the directory-permissions
    fulldp = 777
    umaskdp = int(fulldp - umask)

    # Until the next paragraph: Conversion and output of the
    # directory permissions
    perm_oct = [int(numeric) for numeric in str(umaskdp).zfill(3)]
    perm_alp = []
    f_perm_alp()
    print("DP: ",*perm_oct, f" (numeric) ", *perm_alp, f" (alph.)", sep='')

    # Until the next paragraph: Calculation, conversion and output of
    # the file permissions
    perm_oct = [int(numeric) for numeric in str(umaskdp).zfill(3)]
    perm_alp = []
    for i in range(3):
        if perm_oct[i] % 2 == 1:
            perm_oct[i] -= 1
    f_perm_alp()
    print("FP: ",*perm_oct, f" (numeric) ", *perm_alp, f" (alph.)", sep='')
    print(f"\nUM = umask, DP = Directory Permissions, FP = File Permissions")
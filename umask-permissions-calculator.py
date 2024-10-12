# This code calculates umask-, directory- and filepermissions for
# a given number.
# 10/24/2024
# by Niels Evers

# UNTIL THE NEXT PARAGRAPH: FUNCTION FOR DUPLICATION AND
# CONVERSION OF THE (IN THIS CASE) INTEGER VALUES (NUMERICAL OCTAL)
# TO STRING VALUES (ALPHABETICAL)
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

# UNTIL THE NEXT PARAGRAPH: DEFINITION OF THE UMASK
umask = int(input("Please insert a valid umask (0-777): "))

# UNTIL THE NEXT PARAGRAPH: CHECKING THE UMASK
# Check the entered values
if umask < 0 or umask > 777:
    # Show an error-message
    print("Invalid umask. Please enter a valid umask between 0 and 777.")

# UNTIL THE END: THE MAIN PROGRAM
else:

    # UNTIL THE NEXT PARAGRAPH: CONVERSION AND OUTPUT OF THE UMASK
    # Insert the values in a list as a string
    perm_oct = [int(numeric) for numeric in str(umask).zfill(3)]
    # Define another list
    perm_alp = []
    # Use the f_perm_alp-function to duplicate the integer-values and
    # convert them to string-values
    f_perm_alp()
    # Output the integer-values, the string-values and
    # hide the visible list-characteristics
    print("\nUM: ", f"{str(umask).zfill(3)} (numeric) ", *perm_alp, f" (alph.)", sep='')

    # UNTIL THE NEXT PARAGRAPH: CALCULATION OF THE DIRECTORY-PERMISSIONS
    fulldp = 777
    umaskdp = int(fulldp - umask)

    # UNTIL THE NEXT PARAGRAPH: CONVERSION AND
    # OUTPUT OF THE DIRECTORY PERMISSIONS
    # Insert the values in a list as a string
    perm_oct = [int(numeric) for numeric in str(umaskdp).zfill(3)]
    # Define another list
    perm_alp = []
    # Use the f_perm_alp-function to duplicate the integer-values and
    # convert them to string-values
    f_perm_alp()
    # Output the integer-values, the string-values and
    # hide the visible list-characteristics
    print("DP: ",*perm_oct, f" (numeric) ", *perm_alp, f" (alph.)", sep='')

    # UNTIL THE NEXT PARAGRAPH: CALCULATION, CONVERSION AND
    # OUTPUT OF THE FILE PERMISSIONS
    # Insert the values in a list as a string
    perm_oct = [int(numeric) for numeric in str(umaskdp).zfill(3)]
    # Define another list
    perm_alp = []
    # Use Mr. A. Ehlen's function
    for i in range(3):
        if perm_oct[i] % 2 == 1:
            perm_oct[i] -= 1
    # Use the f_perm_alp-function to duplicate the integer-values and
    # convert them to string-values
    f_perm_alp()
    # Output the integer-values, the string-values and
    # hide the visible list-characteristics
    print("FP: ",*perm_oct, f" (numeric) ", *perm_alp, f" (alph.)", sep='')
    # Output the list of abbreviations
    print(f"\nUM = umask, DP = Directory Permissions, FP = File Permissions")
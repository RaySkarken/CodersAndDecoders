def float_bin(number, places=3):
    if isinstance(number, int):
        return f"{number}." + "0"*places

    whole, dec = str(number).split(".")
    whole = int(whole)
    dec = float("0." + dec)
    res = bin(whole).lstrip("0b") + "."

    # Iterate the number of times, we want
    # the number of decimal places to be
    for x in range(places):
        # Multiply the decimal value by 2
        # and separate the whole number part
        # and decimal part
        whole, dec = str(dec * 2).split(".")

        dec = float("0." + dec)

        # Keep adding the integer parts
        # receive to the result variable
        res += whole

    return res

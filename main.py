from coders import BWT_MTF, ShannonCoder

def shannon_procedure():
    alpha = ["a", "b", "s", "d", "e"]
    probs = [0.2, 0.1, 0.3, 0.2, 0.2]

    s_coder = ShannonCoder(alpha, probs)

    msg = "based"
    print("Shannon Algorithm")
    print("Example:")
    print(f"\tAlphabet: {alpha}\n\tProbabilities: {probs}\n\tMessage: {msg}\n")
    enc = s_coder.encode(msg)
    print(f"\t{msg} -> {enc}")

    dec = s_coder.decode(enc)
    print(f"\t{enc} -> {dec}")

    print("\t" + "-"*116)

    for c, code in s_coder.alpha_to_code.items():
        print(f"\t{c} -- {code}")

    print("-"*120)
    print("Enter alphabet without any separators:")
    alpha = list(input())
    assert len(set(alpha)) == len(alpha), "Alphabet should not contain duplicates"

    print("Enter probabilities separated with spaces:")
    probs = list(map(lambda x: float(x.replace(",", ".")), input().split(" ")))
    assert len(alpha) == len(probs), "There are different amount of elements in alphabet and probabilities list. It caused Error!"
    assert 0 < sum(probs) <= 1, "Sum of probabilities must be positive number less than one!"

    s_coder = ShannonCoder(alpha, probs)

    msg = input("Enter your message: ")
    enc = s_coder.encode(msg)
    print(f"{msg} -> {enc}")

    dec = s_coder.decode(enc)
    print(f"{enc} -> {dec}")

    print("-"*120)

    for c, code in s_coder.alpha_to_code.items():
        print(f"\"{c}\" -- {code}")
    print("\n"+"#"*120+"\n")

def bwt_procedure():
    print("Burrows-Wheeler transform + move to front")
    print("Example:")
    bwt = BWT_MTF("based")
    enc, row = bwt.encode("based")
    print(f"\tbased -> {enc} | index - {row}")

    dec = bwt.decode(enc)
    print(f"\t{enc} | index - {row} -> {dec}")

    print("\t" + "-"*116)

    print("Input the alphabet:")
    alpha = input()
    bwt = BWT_MTF(alpha)
    enc = list(map(int, input("Input encoded message (separate indexes with space): ").split()))
    row = int(input("Input the index that were gotten in Burrows-Wheeler transformation: "))
    dec = bwt.decode(enc, row)
    print(f"\n{enc} | index - {row} -> {dec}")
    enc, row = bwt.encode(dec)
    print(f"{dec} -> {enc} | index - {row}")
    print("\n"+"#"*120+"\n")


if __name__ == '__main__':
    cmd = None
    while cmd != "3":
        cmd = input("Select an option\n1. Shannon encoder.\n2. Burrows-Wheeler transformation + Move to front decoder.\n3. Exit\n(your input): ")
        if cmd == "1":
            try:
                shannon_procedure()
            except Exception as e:
                print(e)
                print()
        elif cmd == "2":
            try:
                bwt_procedure()
            except Exception as e:
                print(e)
                print()
        elif cmd != "3":
            print("You've selected wrong option! Please try again.\n")


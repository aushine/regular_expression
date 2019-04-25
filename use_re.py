import re


def main():
    list1 = ["age", "_age", "1age", "age1", "a_age", "age_1", "age!", "a#123"]
    for each in list1:
        ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$", each)
        if ret:
            print(f"{each}:符合规范")
        else:
            print(f"{each}不符合规范")

if __name__ == "__main__":
    main()
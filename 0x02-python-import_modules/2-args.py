#!/usr/bin/python3
#!/usr/bin/python3
def Print_Argv(list = []):
        if len(list) == 0:
                print("0 arguments.")
        elif len(list) == 1:
                print(f"{len(list)} argument:")
                print(f"1: {list[0]:s}")
        else:
                print(f"{len(list)} arguments:")
                for i in range(len(list)):
                        print(f"{i + 1}: {list[i]}")
                 
if __name__ == "__main__":
    import sys
    Print_Argv(sys.argv)
    
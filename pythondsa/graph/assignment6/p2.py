data = {} 
while True: 
    print("\n1.Insert 2.Search 3.Update 4.Delete 5.Display 6.Exit") 
    try:
        ch = int(input("Choice: "))
    except ValueError:
        print("Invalid choice")
        continue
    if ch == 1: 
        k = input("Key: "); v = input("Value: ") 
        data[k] = v; print("Inserted") 
    elif ch == 2: 
        k = input("Key: "); print(data.get(k, "Key not found")) 
    elif ch == 3: 
        k = input("Key: ") 
        if k in data: 
            data[k] = input("New value: "); print("Updated") 
        else: print("Key not found") 
    elif ch == 4: 
        k = input("Key: ") 
        if k in data: del data[k]; print("Deleted") 
        else: print("Key not found") 
    elif ch == 5: print(data) 
    elif ch == 6: break 
    else: print("Invalid choice")
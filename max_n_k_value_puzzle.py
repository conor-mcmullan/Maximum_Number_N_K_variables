



def max_number_possible(n, k):
    #print(n)
    #print(k)

    invalid_inputs = False
    
    if k>30:
        invalid_inputs = True
        print("Error: K range is [0..30]")

    if n<100 or n >999:
        invalid_inputs = True
        print("Error: N range is [100..999]")

    # invalid out of range accepted
    if invalid_inputs:
        print("Invalid Parameters Rule Broken")
        return n

    else:
        hundreds, tens, units = tuple(int(c) for c in str(n))
        #print(f"Hundreds:\t{hundreds}")
        #print(f"Tens:\t\t{tens}")
        #print(f"Units:\t\t{units}")

        # make a copy to update the values
        max_hundreds, max_tens, max_units = hundreds, tens, units

        # Hundreds
        max_h = 9 - hundreds
        #max_hundreds += max_h
        if k > max_h:
            k -= max_h
        else:
            max_h = k  
            k = 0
        max_hundreds += max_h
        #print(f"Max Hundreds Value:\t{max_hundreds}")

        # Balance
        #print(f"Remainig Balance:\t{k}")

        # Tens
        max_t = 9 - tens
        if k > max_t:
            k -= max_t
        else:
            max_t = k
            k = 0 
        max_tens += max_t       
        #print(f"Max Tens Value:\t{max_tens}")

        # Balance
        #print(f"Remainig Balance:\t{k}")

        # Tens
        max_u = 9 - units
        if k > max_u:
            k -= max_u
        else:
            max_u = k
            k = 0      
        max_units += max_u
        #print(f"Max Units Value:\t{max_units}")

        max_number = int(f"{max_hundreds}{max_tens}{max_units}")
        print(f"MAX:\t{max_number}")


        return max_number



if __name__ == "__main__":

    test_n = 512
    test_k = 10 
    max_number = max_number_possible(test_n, test_k)
    print("\n")

    test_n = 191
    test_k = 4
    max_number = max_number_possible(test_n, test_k)
    print("\n")

    test_n = 285
    test_k = 20
    max_number = max_number_possible(test_n, test_k)
    print("\n")

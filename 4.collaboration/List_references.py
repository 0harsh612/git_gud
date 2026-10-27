def update_guest_list():
    original_guests = ["Aarav", "Aarya", "jaanya", "Onkar", "pranit"]
    
    # HINT: In Python, using '=' with lists doesn't make a new copy. 
    # Both variables now point to the EXACT SAME list in memory. 
    # How can you create a true, independent copy of the original list?
    updated_guests = original_guests
    
    # We only want to add advait to the updated list
    updated_guests.append("advait")
    
    print(f"Original list : {original_guests}")
    print(f"Updated list : {updated_guests}")

update_guest_list()
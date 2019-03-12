text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc accumsan sem ut ligula scelerisque sollicitudin. Ut at sagittis augue. Praesent quis rhoncus justo. Aliquam erat volutpat. Donec sit amet suscipit metus, non lobortis massa. Vestibulum augue ex, dapibus ac suscipit vel, volutpat eget massa. Donec nec velit non ligula efficitur luctus."
counter = 65
num = len(text)
counter_2 = 97
for i in range(26):
    lower = text.count(chr(counter_2))
    upper = text.count(chr(counter))
    print(chr(counter), ":", lower + upper)
    counter += 1
    counter_2 += 1
    

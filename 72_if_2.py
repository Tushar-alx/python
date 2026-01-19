# write a program to find out whether given shape is square or portrait or landscape using user given length and width 

length = int(input("Enter length"))
width = int(input("Enter width"))

#square length and width same 
if length==width: 
    print("given shape is square")

#portrait length is greater than width
if length>width:
    print("given shape is portrait")

#landscape width is greater than length
if length<width:
    print("given shape is landscape")

 
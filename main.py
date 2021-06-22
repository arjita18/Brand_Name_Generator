print("Welcome to the Brand Name Generator!")
city = input("What is the name of the city you grew up in? ")
country = input("What is the name of your country? ")
brandName = city[:2] + country[-2:]
print("Your brand name is: " + brandName.title())

people = {"name" : "anubhav", "gender" : "male", "age" : "20", "adress" : "green valley chhattishgarh india", "phone" : "6267833958"}

user = input("type the information you want to know: ").lower()
info = people.get(user,"that info is not available")
print(info)
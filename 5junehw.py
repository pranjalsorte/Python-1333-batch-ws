movies_db={}
caste1=["Ranveer Singh","Akshay Khanna","Sara Arjun"]
caste2=["Amir Khan","Sharman Joshi","R.Madhavan"]
caste3=["Ritesh Deshmukh","Genelia Deshmukh","Abhishek Bachchan"]
caste4=["Farhan Akhtar","Sonam Kappor","Prakash Raj"]
caste5=["Vicy Kaushal","Yami Gautam"]
movies_db["Dhurandhar"]=caste1
movies_db["3 Idiots"]=caste2
movies_db["Raja Shivaji"]=caste3
movies_db["Bhag Milka Bhag"]=caste4
movies_db["Uri"]=caste5
freq={}
for cast in movies_db.values():
    for actors in cast:
        if actors in freq:
            freq[actors] += 1
        else:
            freq[actors] = 1
print(freq)
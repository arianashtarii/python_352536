#for test #practicing
import pickle

# تمرین نوشتن در فایل
data = ["apple", "banana", "computer"]
file = open("test.pkl", "wb")  # wb = write binary
pickle.dump(data, file)
file.close()
print("Data saved!")

# تمرین خواندن از فایل
file = open("test.pkl", "rb")  # rb = read binary
loaded_data = pickle.load(file)
file.close()
print("Loaded data:", loaded_data)
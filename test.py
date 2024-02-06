import pickle

model = pickle.load(open('model.pkl', 'rb'))
vector = pickle.load(open('vectorizer.pkl', 'rb'))


message = input("Enter your message: ")

processed_msg = vector.transform([message])

prediction = model.predict(processed_msg)

if prediction == 1:
    print("Spam Email")
else:
    print("Not Spam Email" )
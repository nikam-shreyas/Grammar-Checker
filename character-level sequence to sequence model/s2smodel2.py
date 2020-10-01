from keras.models import load_model

model = load_model('s2s.h5')
model.predict('s')
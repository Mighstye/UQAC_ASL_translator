from tensorflow import keras


def main():
    model = keras.models.load_model('models/py/model.h5', compile=False)
    print("Model has been loaded !")

    model.compile()
    print(model.inputs[0].dtype)


if __name__ == "__main__":
    main()

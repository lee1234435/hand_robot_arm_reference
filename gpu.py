
import tensorflow as tf

gpus = tf.config.list_physical_devices('GPU')

if gpus:
    print("GPU를 사용하고 있습니다.")
    for gpu in gpus:
        print(gpu)
else:
    print("GPU를 사용하지 않고 있습니다.")




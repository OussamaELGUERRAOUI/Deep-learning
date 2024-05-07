from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential, Model
from tensorflow.keras.layers import Dense, Conv2D, Flatten, MaxPooling2D, GlobalAveragePooling2D
from tensorflow.keras import optimizers

# Création du modèle simple
def create_model_simple(image_size = 64, num_classes=6):
    
    model = Sequential()
    
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(image_size, image_size, 3)))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Conv2D(64, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Conv2D(96, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Conv2D(128, (3, 3), activation='relu'))
    model.add(MaxPooling2D((2, 2)))
    
    model.add(Flatten())

    model.add(Dense(512, activation='relu')) 
    model.add(Dense(num_classes, activation="softmax"))  # 6 classes d'émotions différentes
    
    return model
    

# Création du modèle VGG16
def create_model_vgg16(image_size = 64, num_classes=6):
    
    # Charger le modèle VGG16 pré-entraîné avec les poids du jeu de données ImageNet
    base_model = VGG16(weights='imagenet', include_top=False, input_shape=(image_size, image_size, 3)) 

    model = Sequential()
    
    # Ajouter le modèle VGG16
    model.add(Dense(256, activation='relu', input_dim=2*2*512))
    model.add(Dense(num_classes, activation="softmax"))  # 6 classes d'émotions différentes
    
    model.compile(optimizer=optimizers.Adam(learning_rate=3e-4), loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    
    return model

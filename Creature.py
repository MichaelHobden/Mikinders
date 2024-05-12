import tensorflow as tf
import numpy as np


class Creature:
    def __init__(self, input_size=6, output_size=3, position_x=3, position_y=3, direction=1):
        self.input_size = input_size
        self.output_size = output_size
        self.position_x = position_x
        self.position_y = position_y
        self.direction = direction
        self.model = self.create_model()
        self.training_buffer = []

    def create_model(self):
        model = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation='relu',
                                  input_shape=(self.input_size,)),
            tf.keras.layers.Dense(32, activation='relu'),
            tf.keras.layers.Dense(self.output_size, activation='softmax')
        ])
        model.compile(optimizer='adam', loss='categorical_crossentropy')
        return model

    def get_action(self, visual_data):
        input_data = self.process_input(visual_data)
        input_data = np.expand_dims(
            input_data, axis=0)  # Add a batch dimension
        predictions = self.model.predict(input_data)
        action = np.argmax(predictions)
        return action

    def process_input(self, visual_data):
        input_data = np.array(visual_data).flatten()
        input_data = input_data / np.max(input_data)
        return input_data

    def train(self):
        if len(self.training_buffer) > 0:
            states, actions = zip(*self.training_buffer)
            X_train = np.array(states)
            y_train = np.array(actions)
            print(X_train.shape)
            self.model.fit(X_train, y_train, epochs=1, verbose=0)
            self.training_buffer = []  # Clear the training buffer after training

    def add_to_training_buffer(self, state, action):
        self.training_buffer.append((state, action))

    def get_positional_data(self):
        return self.position_x, self.position_y, self.direction

    def set_direction(self, direction):
        self.direction = direction

    def set_position_x(self, position_x):
        self.position_x = position_x

    def set_position_y(self, position_y):
        self.position_y = position_y

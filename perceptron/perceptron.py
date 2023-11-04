import numpy as np

CANVAS_WIDTH = 28
CANVAS_HEIGHT = 28

def sigmoid(x):
    return 1/(1 + np.exp(-x))

class PerceptronNetwork:
    def __init__(self):
        # inputs
        self.w0 = np.zeros(CANVAS_WIDTH * CANVAS_HEIGHT)
    
        # hidden layers
        self.w1 = np.random.rand(CANVAS_WIDTH * CANVAS_HEIGHT * 2)
        self.w2 = np.random.rand(CANVAS_WIDTH * CANVAS_HEIGHT * 2)
        self.w3 = np.random.rand(CANVAS_WIDTH * CANVAS_HEIGHT)

        # output layer
        self.w4 = np.zeros(10)

def load_dataset(path):
    dataset = []
    with open(path, "r") as f:
        data = f.readlines()
        for i in range(1, len(data)):
            cells = data[i].rstrip().split(",")
            dataset.append({
                "value" : cells[0],
                "canvas": np.array(cells[1:])
            })
    return dataset

def train():
    print("loading dataset...")
    dataset = load_dataset("mnist_train.csv")
    print("dataset loaded.")




if __name__ == "__main__":
    train()

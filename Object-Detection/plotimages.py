import matplotlib.pyplot as plt


class plotimages:
    def __init__(self, num_rows, num_cols):
        self.fig = plt.figure(figsize=(20, 10))
        self.rows = num_rows
        self.cols = num_cols
        self.current_cell = 0


def display_img(self, img, title, cmap=None):
    self.current_cell += 1
    ax = self.fig.add_subplot(self.rows, self.cols, self.current_cell)
    ax.imshow(img, cmap)
    ax.set_title(title)

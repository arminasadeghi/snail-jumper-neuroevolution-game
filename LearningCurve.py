import csv
import matplotlib.pyplot as plt

# def plot():
file = open("result_file.csv", "r")
reader = csv.reader(file)
res = []
for row in reader:
     res.append(row)
file.close()
x_coords = []
y_coords_max = []
y_coords_avg = []
y_coords_min = []
for i in range(0, len(res)):
    x_coords.append(i + 1)
    print(int(res[i][0]))
    y_coords_max.append(int(res[i][0]))
    y_coords_avg.append(float(res[i][1]))
    y_coords_min.append(int(res[i][2]))

    plt.plot(x_coords, y_coords_min, label='min')
    plt.plot(x_coords, y_coords_max, label='max')
    plt.plot(x_coords, y_coords_avg, label='avg')

    plt.xlim(xmin=0, xmax=10)
        # plt.ylim(ymin=-1, ymax=10)

        # plt.yticks([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [0, 30, 60, 90, 120, 150, 180, 210, 240, 270])

    plt.legend()
    plt.grid(True)

    plt.show()

# if __name__ == '__main__':
#     plot()


import numpy as np
import sys
import csv
import os
import matplotlib.pyplot as plt
from matplotlib.widgets import CheckButtons


def click_comp(label):
    i = labels.index(label)
    comp[i].set_visible(not comp[i].get_visible())
    plt.draw()


def click_comp_log(label):
    i = labels.index(label)
    comp_log[i].set_visible(not comp_log[i].get_visible())
    plt.draw()


def click_time(label):
    i = labels.index(label)
    time[i].set_visible(not time[i].get_visible())
    plt.draw()


def create_plots(file_name):
    global labels, comp, comp_log, time
    rows = []
    with open(file_name, newline='') as f:
        lines = csv.reader(f)
        for line in lines:
            rows += [list(map(float, line))]

    data = np.transpose(np.array(rows))
    n = np.unique(data[0])
    k = np.unique(data[1])

    labels = ''
    for v in k:
        labels += 'k = ' + str(int(v)) + ','
    labels = tuple(labels.split(",")[:-1])

    series = np.ones((3, n.size, k.size)) * np.nan
    for i in range(3):
        for j in range(n.size):
            d = data[i + 2][j * k.size: (j + 1) * k.size]
            series[i][j][:d.size] = d
    series = series.transpose(0, 2, 1)

    fig_comp, ax_comp = plt.subplots()
    comp = [ax_comp.plot(n, series[0][j], lw=2)[0] for j in range(k.size)]
    plt.subplots_adjust(left=0.2)
    plt.title('Comparisons vs. N')
    rax_comp = plt.axes(
        [0.01, 0.5 - 0.02 * len(labels), 0.1, 0.04 * len(labels)])
    check_comp = CheckButtons(rax_comp, labels, tuple([True] * len(labels)))
    check_comp.on_clicked(click_comp)
    comp_colors = [c.get_color() for c in comp]
    [l.set_color(comp_colors[i]) for i, l in enumerate(check_comp.labels)]
    [r.set_facecolor(comp_colors[i])
     for i, r in enumerate(check_comp.rectangles)]

    fig_comp_log, ax_comp_log = plt.subplots()
    comp_log = [ax_comp_log.plot(n, series[1][j], lw=2)[0]
                for j in range(k.size)]
    plt.subplots_adjust(left=0.2)
    plt.title('Comparisons/(N*lnN) vs. N')
    rax_comp_log = plt.axes(
        [0.01, 0.5 - 0.02 * len(labels), 0.1, 0.04 * len(labels)])
    check_comp_log = CheckButtons(
        rax_comp_log, labels, tuple([True] * len(labels)))
    check_comp_log.on_clicked(click_comp_log)
    comp_log_colors = [c.get_color() for c in comp_log]
    [l.set_color(comp_log_colors[i])
     for i, l in enumerate(check_comp_log.labels)]
    [r.set_facecolor(comp_log_colors[i])
     for i, r in enumerate(check_comp_log.rectangles)]

    fig_time, ax_time = plt.subplots()
    time = [ax_time.plot(n, series[2][j], lw=2)[0] for j in range(k.size)]
    plt.subplots_adjust(left=0.2)
    plt.title('Time(s) vs. N')
    rax_time = plt.axes(
        [0.01, 0.5 - 0.02 * len(labels), 0.1, 0.04 * len(labels)])
    check_time = CheckButtons(rax_time, labels, tuple([True] * len(labels)))
    check_time.on_clicked(click_time)
    time_colors = [t.get_color() for t in time]
    [l.set_color(time_colors[i]) for i, l in enumerate(check_time.labels)]
    [r.set_facecolor(time_colors[i])
     for i, r in enumerate(check_time.rectangles)]

    plt.show()


def main():
    path = os.path.dirname(os.path.realpath(__file__))
    try:
        file_name = sys.argv[1]
    except IndexError:
        file_name = path + '/qsort_out_default.csv'
    create_plots(file_name)


if __name__ == '__main__':
    main()

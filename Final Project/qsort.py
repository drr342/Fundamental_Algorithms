import numpy as np
import sys
import os
import math
import threading
from time import monotonic
from time import sleep
import qsort_plot


prompt = ("\nThe program will execute Quicksort {} times.\n"
          "Output will be saved to 'qsort_out.csv' and plotted after program completion.\n"
          "To terminate the program before completion, press 'CTRL + C' followed by Enter:\n"
          "after the Quicksort in progress is completed the program will terminate and partial results will be saved and plotted.\n")

progress = "Running Quicksort {} of {} (n = {}, k = {}, f = {})      "

output_file = os.path.dirname(os.path.realpath(__file__)) + "/qsort_out.csv"


def partition_median(l, left, right, pi):
    global comp
    p = l[pi]
    si = left
    for i in range(left, right - 1):
        comp += 1
        if (l[i] < p):
            temp = l[si]
            l[si] = l[i]
            l[i] = temp
            si += 1
    temp = l[si]
    l[si] = l[right - 1]
    l[right - 1] = temp
    return si


def find_median(l, left, right, k):
    if (left == right - 1):
        return l[:left], l[left], l[left + 1:]
    pi = partition_median(l, left, right, right - 1)
    if (k == pi):
        return l[:k], l[k], l[k + 1:]
    elif (k < pi):
        return find_median(l, left, pi, k)
    else:
        return find_median(l, pi + 1, right, k)


def partition(a, p, r, dp=0, dr=0):
    global b, comp
    left = p + dp
    right = r - 1 - dr
    x = a[r - 1]
    for j in range(p + dp, r - 1 - dr):
        comp += 1
        if (a[j] < x):
            b[left] = a[j]
            left += 1
        else:
            b[right] = a[j]
            right -= 1
    b[left] = x
    a[p:r] = np.concatenate(
        [a[p:p + dp], b[p + dp:r - dr], a[r - dr - 1:r - 1]])
    return left


def qsort(a, p, r, k=1):
    if (k != 1 and k <= r - p):
        c = a[r - k:r]
        pm, x, rm = find_median(c, 0, k, (k - 1) // 2)
        a[p:r] = np.concatenate([pm, a[p:r - k], rm, [x]])
        q = partition(a, p, r, pm.size, rm.size)
        qsort(a, p, q, k)
        qsort(a, q + 1, r, k)
    elif (1 < r - p):
        q = partition(a, p, r)
        qsort(a, p, q)
        qsort(a, q + 1, r)


def quicksort_k(a, k=1):
    qsort(a, 0, a.size, k)


def sort_thread():
    global b, comp
    try:
        maxn = int(sys.argv[1])
    except IndexError:
        maxn = 11
    except:
        print("WARNING:", sys.argv[1], "is not a valid input, using default value = 11")
        maxn = 11
    try:
        maxk = int(sys.argv[2])
    except IndexError:
        maxk = 6
    except:
        print("WARNING:", sys.argv[2], "is not a valid input, using default value = 6")
        maxk = 6
    try:
        folds = int(sys.argv[3])
    except IndexError:
        folds = 10
    except:
        print("WARNING:", sys.argv[3], "is not a valid input, using default value = 10")
        folds = 10

    ns = [100 * 2 ** i for i in range(maxn)]
    ks = [2 * i + 1 for i in range(maxk)]
    print(prompt.format(maxn * maxk * folds))
    with open(output_file, "w") as f:
        f.write("")
    for n in range(maxn):
        for k in range(maxk):
            comp = 0
            t = 0
            for i in range(folds):
                if threading.currentThread().stop:
                    return
                print(progress.format(n * maxk * folds + k * folds + i + 1,
                                      maxn * maxk * folds, ns[n], ks[k], i + 1), end="\r")
                a = np.arange(ns[n])
                np.random.shuffle(a)
                b = np.zeros(a.size, dtype=np.int32)
                start = monotonic()
                quicksort_k(a, ks[k])
                end = monotonic()
                t += (end - start)
            with open(output_file, "a") as f:
                f.write("{},{},{},{},{}\n".format(ns[n], ks[k], comp / 10,
                                                  comp / (10 * ns[n] * math.log(ns[n])), t / 10))


def main():
    t1 = threading.Thread(name='sort_thread', target=sort_thread)
    t1.start()
    t1.stop = False
    while (t1.is_alive()):
        try:
            for i in range(5):
                sleep(1)
        except KeyboardInterrupt:
            print("\nCTRL + C received. Waiting for Quicksort to finish...")
            t1.stop = True
            t1.join()
            break
    print("\nGenerating plots...")
    qsort_plot.create_plots(output_file)


if __name__ == "__main__":
    main()

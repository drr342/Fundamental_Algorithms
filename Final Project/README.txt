Fundamental Algorithms - Spring 2018
Daniel Rivera Ruiz - drr342@nyu.edu

QUICKSORT PROJECT

Files included:
  1. qsort.py - Quicksort implementation in python 3.
  2. qsort_plot.py - Subroutine to plot the results from "qsort.py"
  3. qsort_out_default.csv - Example of the output generated by "qsort.py"
  4. Figure_1.pdf - Example of the output generated by "qsort_plot.py" (C vs. N)
  5. Figure_2.pdf - Example of the output generated by "qsort_plot.py" (C/(N*lnN) vs. N)
  6. Figure_3.pdf - Example of the output generated by "qsort_plot.py" (t vs. N)

Dependencies:
  1. Python 3.3 or higher
  2. numpy
  3. matplotlib

How to run "qsort.py":
  1. Run $ python qsort.py n k f
  2. If the arguments n, k, f are not passed or non-valid values are passed,
    the default values will be considered (n = 11, k = 6, f = 10).
  3. n = number of arrays to be sorted. The arrays will have size 100 * 2 ^ i,
    with 0 <= i <= n - 1, and the elements in each array will be 0, 1, ..., n - 1.
  4. k = number of Quicksort variants to consider. Each variant will be of the form
    Quicksort-(2 * i + 1), with 0 <= i <= k - 1, and the variant of the algorithm
    as specified in the project description.
  5. f = number of folds. Each array will be shuffled and sorted f times, with the results
    for the comparisons and execution time calculated as the average over all repetitions.
  6. Under this conditions, each run of the program will sort (n * k * f) different arrays.
  7. The program will output the overall progress of the execution to stdout.
  8. If the program is taking to long to terminate, abort the execution by pressing "CTRL + C".
  9. After the program terminates (either by itself or by user intervention) the results
    will be available in the output file "qsort_out.csv".
  10. Finally, "qsort_plot.py" will be called to output a graphical visualization of the results.

How to run "qsort_plot.py":
  1. Run $ python qsort_plot.py path_to_file
  2. If the argument path_to_file is not passed, the default value will be considered
    ("qsort_out_default.csv")
  3. path_to_file must be the absolute path to an output file previously generated by "qsort.py",
    otherwise the execution of "qsort_plot.py" will not be successful.
  4. The program will generate three figures:
    Figure 1: Number of comparisons (as specified in project definition) C vs. size of array N.
    Figure 2: C/(N*lnN) vs. N.
    Figure 3: Execution time of the Quicksort routine (in seconds) vs. N.
    Each figure will consist of k series of data, one for each value of k. The visualization of each
    series can be activated/deactivated by checking/unchecking the buttons to the left of the series name.
  5. Use the controls available to manipulate (resize, zoom, etc.) and/or save the figures.
  6. To terminate the program, close all the figures.

Format of the "qsort_out.csv" file:
  Column 1 - Size of the array (N).
  Column 2 - Value of k (used for the variant of Quicksort).
  Column 3 - Average number of comparisons over all folds (C).
  Column 4 - Average value of C/(N*lnN) over all folds.
  Column 5 - Average execution time (of the Quicksort routine) over all folds (t).

Important remarks for "qsort_out_default.csv" and the example figures:
  1. The default output file was generated with parameters n = 15, k = 20, f = 10. The execution with this
    parameters took a long time but provided valuable information for arrays of size over 1M.
  2. For easier readability, the PDF figures show only the series for k = {1, 3, 5, 7, 9, 11}. To visualize
    other series or interact with the figures it is necessary to re-generate them using "qsort_plot.py".
  3. Looking at Figure 1, we confirm that Quicksort-1 (regular Quicksort) is taking more comparisons
    than any other variant of the algorithm for large values of N.
  4. Looking at Figure 2, we notice that even though regular Quicksort is taking more comparisons,
    it is still growing linearly with respect to C/(N*lnN). Regular Quicksort presents a constant factor
    of about 1.8, while for other variants of the algorithm this value varies between 1.5 and 1.7.
  5. Looking at Figure 3, we notice that even though regular Quicksort is taking more comparisons,
    it does not take more "real" time than other variants of the algorithm. In fact, Quicksort-3 has
    the worst time performance for large N. This can be explained by the fact that the other variants of
    Quicksort might be taking less comparisons, but they are also executing additional instructions that
    regular Quicksort is not. Because of this trade-off the performance of all the variants is very similar
    time-wise.

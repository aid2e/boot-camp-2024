# Introduction to Optimization Theory

Optimization is a mathematical discipline that focuses on finding the most efficient solution to a problem, given a set of constraints and objectives. It involves the selection of the best element from some set of available alternatives. In the context of mathematics and computer science, optimization can help in finding the minimum or maximum of a function within a given domain.

In optimization theory, we can formulate the problem using mathematical equations. Let's consider a generic optimization problem with the following components:

1. Design Variables: These are the variables that we can manipulate or control in order to find the optimal solution. They represent the decision variables in the problem. We typically denote them as x = (x1, x2, ..., xn).

2. Objectives: The objectives define what we want to optimize or maximize/minimize. They represent the quantities that we aim to improve or minimize. We can have single or multiple objectives, depending on the problem. We typically denote the objective function as f(x).

3. Constraints: Constraints are the conditions or limitations that must be satisfied in order to find a feasible solution. They represent the restrictions on the design variables. Constraints can be equality constraints (e.g., x1 + x2 = 10) or inequality constraints (e.g., x1 >= 0, x2 <= 5). We typically denote the constraints as g(x) <= 0 or h(x) = 0.

With these components, we can formulate an optimization problem as follows:

```{math}
:label: fig-optim_deg

\text{Minimize/Maximize: } f(x) \\
\text{Subject to: } g(x) \leq 0 \\
h(x) = 0 \\
lb \leq x \leq ub \\
```



Here, lb and ub represent the lower and upper bounds on the design variables, respectively.

By solving this optimization problem, we aim to find the values of the design variables (x) that minimize or maximize the objective function (f(x)), while satisfying the constraints (g(x) <= 0 and h(x) = 0).

Optimization theory provides various algorithms and techniques to solve these optimization problems and find the optimal solution. These techniques include linear programming, nonlinear programming, integer programming, and many more.

```{tableofcontents}
```
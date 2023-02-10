# codeforces_user_total_difficulty
This plots users vs their score(weighted sum of difficulties of solves problems) and solved problems 
## requrements
* `python3`
* and run `pip install -r requirements.txt`
## Run
`python main.py`
## checking latex
$$b \cdot x_1 + (a \bmod b) \cdot y_1 = g$$
## Implementation

```{.cpp file=extended_gcd}
int gcd(int a, int b, int& x, int& y) {
    if (b == 0) {
        x = 1;
        y = 0;
        return a;
    }
    int x1, y1;
    int d = gcd(b, a % b, x1, y1);
    x = y1;
    y = x1 - y1 * (a / b);
    return d;
}
```

The recursive function above returns the GCD and the values of coefficients to `x` and `y` (which are passed by reference to the function).

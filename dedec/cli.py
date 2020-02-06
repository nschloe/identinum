import argparse

import sympy
from mpmath import mp

from .main import findpoly, identify


def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Convert decimal to (approximate) rational number."
    )
    parser.add_argument("decimal", type=str, help="input decimal number")
    parser.add_argument(
        "--tolerance",
        "-t",
        type=float,
        help="absolute tolerance (default: precision of the given decimal)",
    )

    args = parser.parse_args(argv)

    if args.tolerance is None:
        num_digits = len(args.decimal.rsplit(".", 1)[-1])
        args.tolerance = 10 ** (-num_digits)

    # def _granularity(x, max_digits=100):
    #     '''Computes the "granularity" of a floating point number, i.e.,
    #     1.0e-3 for 3.141.
    #     '''
    #     for k in range(max_digits):
    #         if abs(x - int(x)) < 1.0e-15 * x:
    #             break
    #         x *= 10
    #     return 10**(-k)

    x = float(args.decimal)
    sols = identify(x, abs_tol=args.tolerance)
    if sols:
        errors = [sympy.N(float(args.decimal) - sol) for sol in sols]
        # order = [
        #     i[0]
        #     for i in sorted(
        #         enumerate([abs(diff) for diff in diffs]), key=lambda x: x[1]
        #     )
        # ]
        # for k in order:
        #     print("{}   {}".format(sols[k], diffs[k]))
        for sol, error in zip(sols, errors):
            print(f"{sol}   {error}")

    poly_sol = findpoly(x, tol=args.tolerance * 10)
    if poly_sol is not None:
        mp.dps = 20
        residual = mp.polyval(poly_sol, x)
        n = len(poly_sol)
        print()
        print(
            f"{residual} = "
            + " + ".join(
                ["{}*x^{}".format(a, n - k - 1) for k, a in enumerate(poly_sol)]
            )
        )

    if not sols and poly_sol is None:
        print("No expression found that approximates %r well enough." % args.decimal)

import argparse

parser = argparse.ArgumentParser(description="My first argparse")

parser.add_argument("--a", type=int, default=10, help="Left operand of summ")
parser.add_argument("--b", type=int, help="right operand of summ")


args = parser.parse_args()
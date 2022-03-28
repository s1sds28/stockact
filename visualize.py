import pandas
import matplotlib.pyplot as plt

def graph(output: str):

    df = pandas.read_csv(output)

    df = df[df["transaction_type"] == "P"]

    df = df.groupby("ticker").sum("amount_max")[["amount_max"]]

    df.plot(kind="bar")
    plt.show()

if __name__ == "__main__":
    graph("output_pelosi.csv")

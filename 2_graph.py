import pandas as pd
import matplotlib.pyplot as plt


def main() -> None:
    # CSV 불러오기
    df = pd.read_csv("financial_regression.csv")

    # 날짜 변환 및 정렬
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df = df.sort_values("date")

    # 추이를 볼 주요 컬럼 선택 (종가 기준)
    columns = ["sp500 close", "nasdaq close", "gold close"]

    # 숫자형 변환 및 결측 제거
    for col in columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    plot_df = df[["date"] + columns].dropna(subset=["date"]).set_index("date")

    # 그래프 출력
    plt.figure(figsize=(12, 6))
    for col in columns:
        plt.plot(plot_df.index, plot_df[col], label=col)

    plt.title("Financial Trend Over Time")
    plt.xlabel("Date")
    plt.ylabel("Value")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()

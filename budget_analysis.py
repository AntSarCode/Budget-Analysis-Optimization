# budget_analysis.py

import pandas as pd

# –– Adjust these to taste ––
# Keys must match your exact category names in the joint section.
TARGETS = {
    'Home Mortgage & Insurance': 0.30,
    'Personal Care & Household Items': 0.05,
    'Misc. + bridal shower': 0.05,
    'random house things & plants': 0.05,
    'Car Payment': 0.10,
    'KU & WMU': 0.05,
    'Spectrum & ADT': 0.05,
    'Storage Unit': 0.02,
    'Groceries': 0.12,
    'Dine-in & Takeout (Mobile Orders)': 0.05,
    'Butcher Box': 0.02,
    'Prime Video': 0.01,
    'Hulu': 0.01,
    'Netflix': 0.01,
    'HBO Max': 0.01,
    'Apple TV+': 0.01,
    'YouTube TV': 0.01,
    'DoorDash Pass': 0.01,
    'Misc. Joint Purchases & Repairs': 0.05,
}


def analyze_joint_budget(file_path: str, sheet_name: str):
    # 1) read raw, no header
    df = pd.read_excel(file_path, sheet_name=sheet_name, header=None)

    # 2) locate the joint‐vs‐individual boundary
    #    find first row that *contains* "Monthly Individual"
    indiv_mask = df[0].astype(str).str.contains('Monthly Individual', case=False, na=False)
    if not indiv_mask.any():
        raise RuntimeError("Could not find a 'Monthly Individual' row to mark the end of joint expenses.")
    end_idx = indiv_mask.idxmax()

    # 3) locate the joint total row: has NaN in col 0 but a number in col 4
    total_mask = df[0].isna() & df[4].notna()
    if not total_mask.any():
        raise RuntimeError("Could not find the built‐in joint‐total row (col E).")
    total_idx = total_mask.idxmax()
    joint_total = float(df.at[total_idx, 4])

    # 4) slice out the lines just under "Monthly Joint Expenses" up to the total row
    #    the title "Monthly Joint Expenses" itself is row 0, so we start at row 1
    block = df.iloc[1:total_idx]

    # 5) drop any rows where column 4 is NaN or zero
    block = block[pd.to_numeric(block[4], errors='coerce').fillna(0) > 0]

    # 6) build a DataFrame of Category / Total
    summary = block[[0, 4]].copy()
    summary.columns = ['Category', 'Total']
    summary['Total'] = summary['Total'].astype(float)

    # 7) compute each category’s share
    summary['Pct'] = summary['Total'] / joint_total

    return summary, joint_total


def print_insights(summary: pd.DataFrame, total: float):
    print(f"\nTotal Joint Expenses: ${total:,.2f}\n")
    print("=== Joint Spending by Category ===")
    print(
        summary.to_string(
            index=False,
            formatters={
                'Total': lambda v: f"${v:,.2f}",
                'Pct': lambda v: f"{v:.1%}"
            }
        )
    )

    print("\n=== Recommended Cuts ===")
    over = []
    for cat, targ in TARGETS.items():
        row = summary[summary['Category'] == cat]
        if not row.empty:
            actual = (row['Pct']).iloc[0]
            if actual > targ:
                over_amt = actual - targ
                over.append((cat, actual, targ, over_amt))
    if not over:
        print("All tracked categories are within target ranges ✔️")
    else:
        for cat, act, targ, over_amt in over:
            print(f" • {cat}: {act:.1%} vs target {targ:.1%} → reduce by at least {over_amt:.1%}")


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description="Analyze only your Monthly Joint Expenses block and suggest savings."
    )
    parser.add_argument('excel_file', help="Path to your .xlsx file")
    parser.add_argument('--sheet', help="Tab name, e.g. 'May 2025'", required=True)
    args = parser.parse_args()

    summary, joint_total = analyze_joint_budget(args.excel_file, args.sheet)
    print_insights(summary, joint_total)


if __name__ == '__main__':
    main()


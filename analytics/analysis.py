import pandas as pd


def load_data():
    data = pd.read_csv("data/program_data.csv")
    return data


def compute_metrics(data):

    data["cost_per_person"] = data["cost"] / data["people_helped"]
    data["volunteer_efficiency"] = data["people_helped"] / data["volunteers"]
    data["impact_score"] = data["people_helped"] / data["cost"]

    return data


def generate_summary(data):

    summary = {
        "total_programs": len(data),
        "total_people_helped": int(data["people_helped"].sum()),
        "total_cost": int(data["cost"].sum()),
        "total_volunteers": int(data["volunteers"].sum())
    }

    return summary


def generate_insights(data):

    highest_impact = data.loc[data["impact_score"].idxmax()]
    most_cost_efficient = data.loc[data["cost_per_person"].idxmin()]

    insights = {
        "highest_impact_program": highest_impact["program_name"],
        "most_cost_efficient_program": most_cost_efficient["program_name"]
    }

    return insights


if __name__ == "__main__":

    data = load_data()

    data = compute_metrics(data)

    summary = generate_summary(data)

    insights = generate_insights(data)

    print("SUMMARY")
    print(summary)

    print("\nINSIGHTS")
    print(insights)
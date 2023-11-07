
import matplotlib.pyplot as plt

# Define your project tasks with multiple time intervals for each task
tasks = [
    {
        "task": "P2",
        "attributes": [
            {"start": 8, "end": 10}
        ]
    },
    {
        "task": "P3",
        "attributes": [
            {"start": 0, "end": 1},
            {"start": 5, "end": 7}
        ]
    },
    {
        "task": "P4",
        "attributes": [
            {"start": 2, "end": 4}
        ]
    },
    # Add more tasks with multiple time intervals
]

def plot_gantt_chart(tasks):
    fig, ax = plt.subplots(figsize=(10, 5))

    for i, task in enumerate(tasks):
        task_name = task["task"]
        attributes = task.get("attributes", [])

        for interval in attributes:
            start_date = interval["start"]
            end_date = interval["end"]
            duration = end_date - start_date

            ax.barh(task_name, width=duration, left=start_date, height=0.4, align='center', color=f"C{i}")

            # Display additional attributes as labels
            attribute_labels = "\n".join([f"Start: {start_date}", f"End: {end_date}"])
            ax.text(start_date + duration / 2, i, attribute_labels, va='center', ha='center')

    ax.set_xlabel("Timeline")
    ax.set_ylabel("Tasks")
    ax.set_title("Gantt Chart")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

plot_gantt_chart(tasks)

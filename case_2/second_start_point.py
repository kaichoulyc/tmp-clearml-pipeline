from allegroai import Task
import yaml
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--config",
        type=str,
        required=True,
        help="Path to the config file",
    )
    parser.add_argument(
        "--start_as_task",
        action="store_true",
        help="Start as ClearML task",
    )
    return parser.parse_args()


def main(config: dict, start_as_task):
    task = None
    if start_as_task:
        task = Task.init(
            project_name="Test",
            task_name="test_2",
        )
        task.connect(config)

    print(config["sm_1"] + sum(config["sm_2"]))


if __name__ == "__main__":
    args = get_args()

    with open(args.config, "r") as f:
        config = yaml.safe_load(f)

    main(config=config, start_as_task=args.start_as_task)

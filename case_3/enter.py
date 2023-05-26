from allegroai import Task
from jsonargparse import ActionConfigFile, ArgumentParser
from typing import List


def get_args():
    parser = ArgumentParser()
    arg = parser.add_argument
    arg(
        "-t",
        "--train_task_id",
        type=str,
        help="The clearml task ID of the model",
        required=False,
    )
    arg(
        "-di",
        "--dataset_ids",
        type=List[str],
        help="A list of IDs of datasets",
        required=False,
    )
    arg("--config", action=ActionConfigFile)
    return parser.parse_args()


def main(args):
    print(args.dataset_ids)


if __name__ == "__main__":
    task = Task.init(
        project_name="case_3",
        task_name="enter",
        task_type=Task.TaskTypes.inference,
    )
    args = get_args()
    main(args)

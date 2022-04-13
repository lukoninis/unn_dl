import os
import argparse
import pathlib


DOCKER_NAME = "lukoninis/unn_dl:latest"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--tests', type=pathlib.Path)
    parser.add_argument('--out', type=pathlib.Path)

    args = parser.parse_args()

    tests_path = args.tests
    out_path = args.out or pathlib.Path(".").resolve()

    if not out_path.exists():
        raise Exception("out path should be exists")

    if tests_path is not None and not tests_path.exists():
        raise Exception("tests path should be exists")

    dirs = []
    dirs.append(f"-v {out_path.resolve()}:/opt/out")

    if tests_path:
        dirs.append(f"-v {tests_path.resolve()}:/opt/examples")

    dirs_str = " ".join(dirs)

    os.system(f"docker run -it {dirs_str} --rm {DOCKER_NAME}")


if __name__ == "__main__":
    main()

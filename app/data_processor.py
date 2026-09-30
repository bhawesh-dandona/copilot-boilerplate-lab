from pathlib import Path

from app.utils import read_csv_rows


def resolve_allowed_data_file(file_path):
    allowed_directory = Path(__file__).resolve().parent
    candidate_path = Path(file_path).expanduser()

    if not candidate_path.is_absolute():
        candidate_path = (allowed_directory / candidate_path).resolve()
    else:
        candidate_path = candidate_path.resolve()

    if candidate_path != allowed_directory and allowed_directory not in candidate_path.parents:
        raise ValueError(f"File path is outside the allowed data directory: {file_path}")

    return candidate_path


def filter_rows_by_second_column(file_path, match_value):
    secure_file_path = resolve_allowed_data_file(file_path)
    matching_rows = []

    for csv_row in read_csv_rows(secure_file_path):
        if len(csv_row) > 1 and csv_row[1] == match_value:
            matching_rows.append(csv_row)

    return matching_rows


if __name__ == "__main__":
    data_file = Path(__file__).with_name("data.csv")
    print(filter_rows_by_second_column(data_file, "active"))
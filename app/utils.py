import csv


def read_csv_rows(file_path):
	"""Read all rows from a CSV file.

	Args:
		file_path (str or os.PathLike): Path to the CSV file to read.

	Returns:
		list[list[str]]: Rows from the CSV file, with each row represented as
		a list of field values.

	Raises:
		FileNotFoundError: If the file at `file_path` does not exist.
	"""
	with open(file_path, "r", newline="") as csv_file:
		return list(csv.reader(csv_file))

def test_read_csv_rows_returns_rows(tmp_path):
	from app.utils import read_csv_rows

	csv_file = tmp_path / "data.csv"
	csv_file.write_text("name,status\nAlice,active\nBob,inactive\n", encoding="utf-8")

	assert read_csv_rows(csv_file) == [
		["name", "status"],
		["Alice", "active"],
		["Bob", "inactive"],
	]


def test_read_csv_rows_raises_for_missing_file(tmp_path):
	import pytest

	from app.utils import read_csv_rows

	missing_file = tmp_path / "missing.csv"

	with pytest.raises(FileNotFoundError):
		read_csv_rows(missing_file)

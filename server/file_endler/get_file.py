from fastapi import UploadFile
import csv
import io
from server.file_endler.file_endler1 import seve_data, load_data



def upload_csv(file: UploadFile):
    if file.content_type != "text/csv":
         return {"error": "File must be a CSV"}

    content = file.file.read().decode("utf-8")
    reader = csv.reader(io.StringIO(content))
    header = next(reader)
    rows = list(reader)
    seve_data(rows)

    for line in rows:
        print(line)

    return {
        "filename": file.filename,
        "content_type": file.content_type,
        "total_rows": len(rows),
        "columns": header,
        "data": rows[0:5],
        "message": f"Successfully processed CSV with {len(rows)} rows"
    }
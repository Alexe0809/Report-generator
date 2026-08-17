from fastapi import FastAPI, File, HTTPException, UploadFile
from fastapi.responses import FileResponse
from analytics import (
    get_total_revenue, get_order_count, get_average_check,
    get_sales_by_product, get_sales_by_customer, get_sales_by_day,
)
from main import run_pipline
from pathlib import Path

app = FastAPI()

@app.get('/')
def read_root():
    return {'status': 'OK'}

@app.get('/metrics')
def metrics():
    return {"revenue": get_total_revenue(),
        "orders": get_order_count(),
        "average_check": get_average_check(),
        "by_product": get_sales_by_product(),
        "by_customer": get_sales_by_customer(),
        "by_day": get_sales_by_day(),}

@app.post('/upload')
def upload(file: UploadFile = File(...)):
    if not file.filename.endswith('.csv'):
        raise HTTPException(status_code=400, detail="Required CSV-file")
    contents = file.file.read()
    with open(f'data/input{file.filename}', 'wb') as f:
        f.write(contents)
    run_pipline()
    return {'filename':file.filename, 'size':len(contents)}

@app.get('/download')
def download():
    if not Path('reports/report.xlsx').exists():
        raise HTTPException(status_code=404, detail="Nothing was uploadded")
    return FileResponse('reports/report.xlsx',
                        filename='report.xlsx',
                        media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
                        )
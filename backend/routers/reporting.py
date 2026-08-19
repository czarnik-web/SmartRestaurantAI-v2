from fastapi import APIRouter, Depends

import schemas

from database import get_db
from services import reporting_service


router = APIRouter(
    prefix="/reports",
    tags=["Reporting"]
)

@router.get("/daily", response_model=schemas.DailyReportResponse)
def get_daily_report(db=Depends(get_db)):
    return reporting_service.get_daily_report(db)

@router.get("/sales", response_model=schemas.SalesReportResponse)
def get_sales_report(db=Depends(get_db)):
    return reporting_service.get_sales_report(db)

@router.get("/refunds", response_model=schemas.RefundReportResponse)
def get_refund_report(db=Depends(get_db)):
    return reporting_service.get_refund_report(db)
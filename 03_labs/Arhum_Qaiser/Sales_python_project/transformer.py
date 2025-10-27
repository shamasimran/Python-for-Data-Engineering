from logger_config import setup_logger

class transformer:
    def __init__(self):
        self.logger = setup_logger()
    
    def clean_data(self, data):
        transformed_data = []
        for record in data:
            try:
                report_id = str(record["ReportID"])
                sales_person_id = str(record["SalesPersonID"])
                product_id = str(record["ProductID"])
                quantity = str(record["Quantity"])
                total_sales = float(record["TotalSalesValue"])

                transformed_data.append({
                    "ReportID": report_id,
                    "SalesPersonID": sales_person_id,
                    "ProductID": product_id,
                    "Quantity": quantity,
                    "TotalSalesValue": total_sales
                })

            except Exception as e:
                self.logger.warning(f"Skipping transforming record {record}: {e}")
        
        self.logger.info(f"Successfully transformed {len(transformed_data)} records.")
        return transformed_data


def company_serial(company) -> dict:
    return {
        "id":str(company["_id"]),
        "name": company.name,
        "email": company.email,
        "website": company.website,
        "description": company.description,
        "registration_date": company.registration_date,
        "job_opportunities_posted": company.job_opportunities_posted,
        "candidates_hired": company.candidates_hired
    }


def company_list_serial(companies) -> list:
    return [company_serial(company) for company in companies]
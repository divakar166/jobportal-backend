from .companies import company_serial


def job_serial(job) -> dict:
    return {
        "title": job.title,
        "company": company_serial(job.company),
        "posted_on": job.posted_on,
        "work_type": job.work_type,
        "description": job.description,
        "job_type": job.job_type,
        "start_date": job.start_date,
        "duration": job.duration,
        "salary_or_stipend": job.salary_or_stipend,
        "apply_by": job.apply_by,
        "applicants_count": job.applicants_count,
        "skills_required": job.skills_required,
        "openings": job.openings,
        "perks": job.perks,
        "conditions": job.conditions,
        "application_link": job.application_link
    }


def job_list_serial(jobs) -> list:
    return [job_serial(job) for job in jobs]

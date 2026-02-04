from flask import Blueprint, render_template, request
from app.services.jsearch import JSearchService

bp = Blueprint("jobs", __name__)
jsearch = JSearchService()


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/search")
def search():
    query = request.args.get("query", "")
    location = request.args.get("location", "")
    page = request.args.get("page", 1, type=int)
    date_posted = request.args.get("date_posted", "all")
    remote_only = request.args.get("remote_only", "false") == "true"
    employment_type = request.args.get("employment_type", "")
    
    if not query:
        return render_template("search.html", jobs=[], query="", error="Please enter a search query")
    
    result = jsearch.search_jobs(
        query=query,
        location=location if location else None,
        page=page,
        date_posted=date_posted,
        remote_jobs_only=remote_only,
        employment_types=employment_type if employment_type else None
    )
    
    jobs = result.get("data", [])
    error = result.get("error")
    
    return render_template(
        "search.html",
        jobs=jobs,
        query=query,
        location=location,
        page=page,
        date_posted=date_posted,
        remote_only=remote_only,
        employment_type=employment_type,
        error=error
    )


@bp.route("/job/<path:job_id>")
def job_details(job_id):
    result = jsearch.get_job_details(job_id)
    
    job = None
    if result.get("data"):
        job = result["data"][0]
    
    error = result.get("error")
    
    return render_template("job_details.html", job=job, error=error)


@bp.route("/salary")
def salary_estimate():
    job_title = request.args.get("job_title", "")
    location = request.args.get("location", "")
    
    if not job_title or not location:
        return render_template("salary.html", salary_data=None, job_title=job_title, location=location)
    
    result = jsearch.get_estimated_salary(job_title, location)
    
    salary_data = result.get("data", [])
    error = result.get("error")
    
    return render_template(
        "salary.html",
        salary_data=salary_data,
        job_title=job_title,
        location=location,
        error=error
    )

from worker.queue import Job


def handle_fintech(job: Job) -> None:
    if job.payload.get("fail"):
        raise RuntimeError("forced failure")
    if "id" not in job.payload:
        raise ValueError("missing id")

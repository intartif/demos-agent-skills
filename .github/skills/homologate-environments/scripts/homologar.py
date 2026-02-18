import yaml
from typing import List, Dict

PROHIBITED_JOBS = [
    'lint', 'test', 'snyk', 'sonar', 'fortify', 'prettier', 'coverage', 'scan', 'semgrep'
]

def load_workflow(path: str) -> Dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)

def filter_jobs(jobs: Dict) -> Dict:
    return {k: v for k, v in jobs.items() if k not in PROHIBITED_JOBS}

def compare_workflows(dev_path: str, prod_path: str) -> Dict:
    dev = load_workflow(dev_path)
    prod = load_workflow(prod_path)
    dev_jobs = filter_jobs(dev.get('jobs', {}))
    prod_jobs = prod.get('jobs', {})
    differences = []
    # Compare jobs
    for job in dev_jobs:
        if job not in prod_jobs:
            differences.append(f"Job '{job}' missing in production workflow.")
        elif dev_jobs[job] != prod_jobs[job]:
            differences.append(f"Job '{job}' differs between dev and prod.")
    for job in prod_jobs:
        if job not in dev_jobs:
            differences.append(f"Job '{job}' should not exist in production workflow.")
    # Compare top-level keys except jobs
    for key in dev:
        if key != 'jobs' and dev[key] != prod.get(key):
            differences.append(f"Key '{key}' differs between dev and prod.")
    return {
        'differences': differences,
        'suggestions': [
            "Remove prohibited jobs from production workflow.",
            "Ensure all other configuration matches development workflow."
        ]
    }

if __name__ == '__main__':
    import sys
    if len(sys.argv) != 3:
        print("Usage: python homologar.py <dev_workflow.yml> <prod_workflow.yml>")
        sys.exit(1)
    result = compare_workflows(sys.argv[1], sys.argv[2])
    print("Diferencias:")
    for diff in result['differences']:
        print(f"- {diff}")
    print("\nSugerencias:")
    for sug in result['suggestions']:
        print(f"- {sug}")
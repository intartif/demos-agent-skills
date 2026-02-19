import os
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

def list_dev_workflows(directory: str) -> List[str]:
    return [f for f in os.listdir(directory) if f.endswith('-dev.yml')]

def main():
    import sys
    if len(sys.argv) != 2:
        print("Usage: python homologar.py <workflows_directory>")
        sys.exit(1)

    workflows_dir = sys.argv[1]
    dev_workflows = list_dev_workflows(workflows_dir)

    if not dev_workflows:
        print("No se encontraron workflows de desarrollo en el directorio especificado.")
        sys.exit(1)

    print("Workflows de desarrollo encontrados:")
    for i, wf in enumerate(dev_workflows, 1):
        print(f"{i}. {wf}")

    selected = input("Seleccione los números de los workflows a analizar (separados por coma): ")
    selected_indices = [int(x.strip()) - 1 for x in selected.split(",") if x.strip().isdigit()]

    for idx in selected_indices:
        dev_workflow = dev_workflows[idx]
        prod_workflow = dev_workflow.replace('-dev.yml', '-prod.yml')
        dev_path = os.path.join(workflows_dir, dev_workflow)
        prod_path = os.path.join(workflows_dir, prod_workflow)

        if not os.path.exists(prod_path):
            print(f"El workflow de producción correspondiente a {dev_workflow} no existe. Sugerencia: crear {prod_workflow} basado en el de desarrollo.")
            continue

        result = compare_workflows(dev_path, prod_path)
        print(f"\nResultados para {dev_workflow} -> {prod_workflow}:")
        print("Diferencias:")
        for diff in result['differences']:
            print(f"- {diff}")
        print("\nSugerencias:")
        for sug in result['suggestions']:
            print(f"- {sug}")

if __name__ == '__main__':
    main()
import json
import os
from pathlib import Path

import _jsonnet as jsonnet
import yaml
from slugify import slugify

with open("schedule.yaml", 'r') as f:
	schedule = yaml.safe_load(f)

workflows_dir = Path(".github/workflows")
workflows_dir.mkdir(exist_ok=True)

for task in schedule:
	run_path = Path(task["run_path"])
	cron = task["cron"]

	try:
		name = task["name"]
	except KeyError:
		name = run_path.stem

	if not run_path.exists():
		raise ValueError(f"File {run_path} not found")
	if not os.access(run_path, os.X_OK):
		raise ValueError(f"File {run_path} is not executable")

	workflow_content = jsonnet.evaluate_file("src/task.jsonnet", ext_vars={
		"cron_expr": cron, "run_path": str(run_path), "name": name
	})
	workflow_content = json.loads(workflow_content)

	workflow_filename = run_path.relative_to(".").with_suffix("")

	# GitHub forces all workflow files to be in the root of `.github/workflows`
	workflow_filename = slugify(str(workflow_filename))
	with open(f"{workflows_dir}/{workflow_filename}.yaml", "w") as workflow_file:
		yaml.dump(workflow_content, workflow_file)

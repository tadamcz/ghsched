Write a single `schedule.yaml` file:

```yaml
# schedule.yaml

- run_path: example.sh
  cron: '0 6 * * 1'  # Mondays 6am

- run_path: example_dir/example.sh
  cron: '0 6 * * *'  # Every day at 6am
  name: 'Hello!'
```

Generate files like this:

```yaml
# .github/workflows/example-dir-example.yaml

jobs:
  scheduled_task:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@v3
    - run: ./example_dir/example.sh
    timeout-minutes: 5
name: Hello!
on:
  schedule:
  - cron: 0 6 * * *
  workflow_dispatch: null  # Allows for manual triggering
```

# Usage
1. Run `poetry install`
2. Create your scripts and edit `schedule.yaml` as appropriate
3. Run `make`
4. Push to GitHub
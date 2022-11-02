{
  name: std.extVar("name"),
  on: {
    schedule: [
      {
        cron: std.extVar("cron_expr"),
      },
    ],
    workflow_dispatch: null,  // allows manual triggering
  },
  jobs: {
    scheduled_task: {
      'runs-on': 'ubuntu-latest',
      steps: [
        {
          name: 'Checkout',
          uses: 'actions/checkout@v3',
        },
        {
          run: './' + std.extVar("run_path"),
        },
      ],
    },
  },
}

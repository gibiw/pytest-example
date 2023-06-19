# pytest-example

This project shows how you can submit your Pytest tests to Test IT.

We will look at two options for submitting test results: [Test IT CLI](#test-it-cli) and [Test IT Pytest Adapter](#test-it-pytest-adapter).

## Test IT CLI

This tool helps to submit a JunitXML report to TMS.     
You can see full documentation on [official site](https://docs.testit.software/user-guide/integrations/cli.html)

### Steps:

1. Use this command to run tests:

```sh
pytest --junit-xml=reports/results.xml
```

2. Install the Test IT CLI using the command:

```sh
pip install testit-cli
```

3. Use this command to submit results:

```sh
export TMS_TOKEN=<YOUR_TOKEN>
testit \
  --url <YOUR_INSTANCE_URL> \
  --project-id 5236eb3f-7c05-46f9-a609-dc0278896464 \
  --configuration-id 15dbb164-c1aa-4cbf-830c-8c01ae14f4fb \
  --testrun-name "Pytest test run" \
  --results reports
```


## Test IT Pytest Adapter

The adapter helps to make more flexible integration with Test IT. 
You can upload not only basic information about autotests, but also other metadata. For example, steps, attachments, messages, etc.

### Steps

1. Install the adapter using the command:

```shell
pip install testit-adapter-pytest
```

2. Create `connection_config.ini` file in project root folder:

```ini
[testit]
URL = <YOUR_INSTANCE_URL>
privateToken = <YOUR_TOKEN>
projectId = 9cc7c239-63d7-47b7-af0c-a307488b08b3
configurationId = 2a7e3e25-9afa-4d52-8eea-54d80e4f7444
testRunName = TestRunPytest
adapterMode = 2
```

3. Use this command to submit results:

```shell
pytest --testit
```
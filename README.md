# Serverless Framework - AWS SSM Parameters

> This repo contains a Serverless Framework project to showcase AWS SSM service parameter retrieve

### Setup
> Add Secret to AWS SSM Parameter Store. You need the AWS CLI Configured for this.

```shell
$ aws ssm put-parameter --name mysecretkey --type String --value mySecretKeyValue
```

> To Update a parameter

```shell
$ aws ssm put-parameter --name mysecretkey --type String --value mySecretKeyValueChanged --overwrite
```

> To delete a parameter

```shell
$ aws ssm delete-parameter --name mysecretkey
```

> To Get a parameter value

```shell
$ aws ssm get-parameter --name supermanToken
```

> Install Serverless Framework globally

```shell
$ npm install -g serverless@1.48.2
```

> Deploy into AWS

```shell
$ serverless deploy --stage dev
```